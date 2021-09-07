#!/usr/bin/env python

import argparse
import logging
import pandas as pd
import yaml

import extractpeople

from pathlib import Path


def get_person_ids(names, people):
    '''Extract list of id in people.yaml from a string with names

    :param names: string with names
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    '''
    ids = []
    if names is not None:
        names = names.replace(' and ', ', ').split(', ')
        for n in names:
            if n not in people:
                logging.warning("'%s' for not found in people " % n)
            else:
                ids.append(people[n])
    return ids
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add projects')
    parser.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)")
    parser.add_argument('-p', '--projects', help="Path to project sheet file")
    parser.add_argument('-i', '--information', help="Path to information sheet file")
    parser.add_argument('-l', '--log', help="Path to log output file")
    args = parser.parse_args()

    logging.basicConfig(filename=args.log, level=logging.DEBUG)

    # add people to people.yaml
    info_fp = Path(args.information)
    info_df = pd.read_csv(info_fp)
    added_people = extractpeople.extract_people(info_df)

    people_fp = Path('_data') / Path('people.yaml')
    # load people.yaml file into a dictionary
    with open(people_fp, 'r') as people_f:
        people = yaml.load(people_f, Loader=yaml.FullLoader)
    
    # reorder people as a dictionary with key being First name - Last name
    # and value being the people id
    reorder_people = {}
    for p in people:
        name = '%s %s' % (people[p]['first-name'], people[p]['last-name'])
        reorder_people[name] = p

    # load people information from sheet file
    # parse it
    # add information to people dictionary
    project_fp = Path('_data') / Path('ols-%s-projects.yaml' % args.cohort )
    project_info_fp = Path(args.projects)
    df = pd.read_csv(project_info_fp)
    df = df.where(pd.notnull(df), None)
    projects = {}
    logging.info('Add new projects')
    for index, row in df.iterrows():
        if row['Comment regarding review'] == 'rejected':
            continue
        logging.info(row['Title'])
        # get title
        p = {
            'name': row['Title'].rstrip().lstrip(),
            'description': row['Project-description'].rstrip().lstrip(),
            'participants': [],
            'mentors': [],
            'keywords': []
        }
        # extract participants
        p['participants'] = get_person_ids(row['Authors'], reorder_people)
        # extract mentors
        p['mentors'] = get_person_ids(row['Mentor 1'], reorder_people)
        if row['Mentor 2'] != '':
            p['mentors'] += get_person_ids(row['Mentor 2'], reorder_people)
        if len(p['mentors']) == 0:
            logging.warning('No mentor')
        # 
        if row['Keywords'] is not None:
            p['keywords'] = row['Keywords'].split(',\n')
        projects[p['name']] = p
        logging.info('')

    # check if everybody are correctly added to projects from participant file
    logging.info('Check project participants')
    # 1. get projects and people from participant registration
    df = info_df.where(pd.notnull(info_df), None)
    projects_people = {}
    for index, row in df.iterrows():
        projects_people.setdefault(row['OLS-%s Project title' % args.cohort ], [])
        name = "%s %s" % (row['First name'].rstrip(), row['Last name'].rstrip())
        projects_people[row['OLS-%s Project title' % args.cohort]].append(name.title())
    # 2. check each project
    for pr in projects_people:
        logging.warning("%s" % pr)
        if pr not in projects:
            logging.warning("Not found in project list")
            continue
        for pa in projects_people[pr]:
            if pa not in reorder_people:
                logging.warning("'%s' not found in people" % pa)
                continue
            pa_id = reorder_people[pa]
            if pa_id not in projects[pr]['participants']:
                projects[pr]['participants'].append(pa_id)
                logging.warning("'%s' added to project" % pa)
        logging.info('')

    # transform project dictionary to list
    project_list = [projects[p] for p in projects]

    # dump project dictionary into project file
    with project_fp.open("w") as project_f:
        project_f.write('# List of projects for OLS-3\n')
        project_f.write('#\n')
        project_f.write('# Check previous OLS for examples\n')
        project_f.write('---\n')
        project_f.write(yaml.dump(project_list, allow_unicode=True))
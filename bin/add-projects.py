#!/usr/bin/env python

import argparse
import pandas as pd
import yaml
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
                print("'%s' for not found in people " % n)
            else:
                ids.append(people[n])
    return ids
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add projects')
    parser.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)")
    parser.add_argument('-p', '--projects', help="Path to project sheet file")
    args = parser.parse_args()

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

    project_fp = Path('_data') / Path('ols-%s-projects.yaml' % args.cohort )
    projects = []
    
    # load people information from sheet file
    # parse it
    # add information to people dictionary
    project_info_fp = Path(args.projects)
    df = pd.read_csv(project_info_fp)
    df = df.where(pd.notnull(df), None)
    for index, row in df.iterrows():
        if row['Comment regarding review'] == 'rejected':
            continue
        print(row['Title'])
        # get title
        p = {
            'name': row['Title'].rstrip().lstrip(),
            'description': row['Project-description'].rstrip().lstrip(),
            'participants': [],
            'mentors': []
        }
        # extract participants
        p['participants'] = get_person_ids(row['Authors'], reorder_people)
        # extract mentors
        p['mentors'] = get_person_ids(row['Mentor 1'], reorder_people)
        # 
        projects.append(p)
        print()

    # dump project dictionary into project file
    with project_fp.open("w") as project_f:
        project_f.write('# List of projects for OLS-3\n')
        project_f.write('#\n')
        project_f.write('# Check previous OLS for examples\n')
        project_f.write('---\n')
        project_f.write(yaml.dump(projects, allow_unicode=True))
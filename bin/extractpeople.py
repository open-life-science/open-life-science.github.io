#!/usr/bin/env python

import argparse
import logging
import pandas as pd
import yaml
from pathlib import Path


optional_info = ['twitter', 'website', 'orcid', 'affiliation', 'city', 'country', 'pronouns', 'expertise', 'bio']
to_capitalize_info = ['affiliation', 'city', 'country', 'first-name', 'last-name']


def extract_people_info(row, people):
    '''Extract people information from a row of the csv
    and return them as a key and a dictionary

    :param row: df row
    :param people: dictionary with people information
    '''
    info = {
        'first-name': row['First name'].rstrip(),
        'last-name': row['Last name'].rstrip(),
        'twitter': row['Twitter username'],
        'website': row['Website'],
        'orcid': row['ORCID'],
        'affiliation': row['Affiliation'],
        'city': row['City'],
        'country': row['Country'],
        'pronouns': row['Pronouns'],
        'expertise': row['Areas of expertise'],
        'bio': row['Bio']
    }
    # get id
    github = row['Github username']
    if github is None:
        # check if person exists from first and last name
        for p in people:
            if people[p]['first-name'] == info['first-name'] and people[p]['last-name'] == info['last-name']:
                github = p
        # create username
        if github is None:
            github = '%s-%s' % (
                info['first-name'],
                info['last-name'])
            info['github'] = False
    github = github.replace('https://github.com/', '')
    github = github.rstrip()
    github = github.lower().replace(' ', '-').replace('@', '')
    # format ORCID
    if info['orcid'] is not None:
        info['orcid'] = info['orcid'].replace('https://orcid.org/', '')
    # format Twitter 
    if info['twitter'] is not None:
        info['twitter'] = info['twitter'].replace('@', '')
    # format expertise
    if info['expertise'] is not None:
        info['expertise'] = info['expertise'].rstrip().split("; ")
        info['expertise'] = [x.capitalize() for x in info['expertise']]
    # format website
    if info['website'] is not None and not info['website'].startswith('https'):
        info['website'] = 'https://%s' % info['website']
    # check info and remove optional empty info
    info_k = list(info.keys())
    for i in info_k:
        if info[i] is None:
            if github in people and i in people[github]:
                info[i] = people[github][i]
            elif i in optional_info:
                del info[i]
        else:
            if i != 'expertise' and i != 'github':
                info[i] = info[i].rstrip()
            if i in to_capitalize_info:
                info[i] = info[i].title()
    return github, info


def extract_people(df):
    '''Extract people information from a sheet and add them to people.yaml

    :param df: Path to information sheet file
    '''
    people_fp = Path('_data') / Path('people.yaml')

    # load people.yaml file into a dictionary
    with open(people_fp, 'r') as people_f:
        people = yaml.load(people_f, Loader=yaml.FullLoader)
    
    # load people information from sheet file
    # parse it
    # add information to people dictionary
    df = df.where(pd.notnull(df), None)
    people_l = []
    for index, row in df.iterrows():
        github, info = extract_people_info(row, people)
        if github not in people:
            logging.info("Add info for %s" % github)
            people[github] = info
        else:
            logging.info("Update info for %s" % github)
            people[github] = info
        people_l.append(github)
    logging.info("Full list")
    people_l.sort()
    logging.info('- %s' % '\n- '.join(people_l))

    # dump people dictionary into people.yaml file
    with people_fp.open("w") as people_f:
        people_f.write('# List of people (alphabetical order)\n')
        people_f.write('#\n')
        people_f.write('# Collection names should be equal to github username,\n')
        people_f.write('# if not, add github: false tag and\n')
        people_f.write('# use firstname-lastname as collection name\n')
        people_f.write('#\n')
        people_f.write('# List of tags for people\n')
        people_f.write('#\n')
        people_f.write('# first-name:\n')
        people_f.write('# last-name:\n')
        people_f.write('# twitter:\n')
        people_f.write('# website:\n')
        people_f.write('# gitter:\n')
        people_f.write('# orcid:\n')
        people_f.write('# affiliation:\n')
        people_f.write('# country:\n')
        people_f.write('# pronouns:\n')
        people_f.write('# expertise:\n')
        people_f.write('#    -\n')
        people_f.write('# bio:\n')
        people_f.write('#\n')
        people_f.write('# Mandatory: first-name, last-name, country\n')
        people_f.write('---\n')
        people_f.write(yaml.dump(people, allow_unicode=True))

    return people_l


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract people information from a sheet and add them to people.yaml')
    parser.add_argument('-i', '--information', help="Path to information sheet file")
    parser.add_argument('-u', '--url', help="URL to information sheet file")
    parser.add_argument('-l', '--log', help="Path to log output file")
    args = parser.parse_args()

    logging.basicConfig(filename=args.log, level=logging.DEBUG)

    if not args.information:
        if not args.url:
            raise ValueError("Provide either path or URL to information sheet file")
        else:
            extract_people(pd.read_csv(args.url))
    else:
        information_fp = Path(args.information)
        extract_people(pd.read_csv(information_fp))

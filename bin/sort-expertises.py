#!/usr/bin/env python

import argparse
import pandas as pd
import yaml
from pathlib import Path

def extract_expertise(people_list, people):
    '''Extract expertise for interesting people
    and return them as a key and a dictionary

    :param people_list: list of username for which extracting expertise
    :param people: dictionary with people information

    :return: dictionary with key being expertise and values 
    list of people with expertise
    '''
    no_expertise = 'No listed expertise'
    p_expertise = {no_expertise: []}
    for p in people_list:
        if 'expertise' in people[p]:
            for e in people[p]['expertise']:
                p_expertise.setdefault(e, [])
                p_expertise[e].append(p)
        else:
            p_expertise[no_expertise].append(p)
    if len(p_expertise[no_expertise]) == 0:
        p_expertise.pop(no_expertise)
    return p_expertise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract expert/mentor expertise from metadata file and order expert/mentor given that information')
    parser.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)")
    args = parser.parse_args()

    people_fp = Path('_data') / Path('people.yaml')
    # load people.yaml file into a dictionary
    with open(people_fp, 'r') as people_f:
        people = yaml.load(people_f, Loader=yaml.FullLoader)

    metadata_fp = Path('_data') / Path('ols-%s-metadata.yaml' % args.cohort )
    # load metadata cohort file into a dictionary
    with open(metadata_fp, 'r') as metadata_f:
        metadata = yaml.load(metadata_f, Loader=yaml.FullLoader)

    # add expertise:people for possible mentors in a dictionary to metadata
    metadata['possible-mentors-with-expertise'] = extract_expertise(
        metadata['possible-mentors'],
        people
    )

    # add expertise:people for possible mentors in a dictionary to metadata
    metadata['experts-with-expertise'] = extract_expertise(
        metadata['experts'],
        people
    )
    
    # dump expertise dictionary into metadata file
    with metadata_fp.open("w") as metadata_f:
        metadata_f.write('# List of experts, possible mentors and organizers for OLS-%s\n' % args.cohort)
        metadata_f.write('#\n')
        metadata_f.write('#\n')
        metadata_f.write('# People should be also in people.yaml file and linked using their GitHub username\n')
        metadata_f.write('# Ordering by expertise should be done by running the bin/sort-expertises.py script\n')
        metadata_f.write('---\n')
        metadata_f.write(yaml.dump(metadata))
        
    

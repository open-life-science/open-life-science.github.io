#!/usr/bin/env python

import argparse
import pandas as pd
import yaml

from pathlib import Path

optional_info = ['twitter', 'website', 'orcid', 'affiliation', 'city', 'country', 'pronouns', 'expertise', 'bio']
to_capitalize_info = ['affiliation', 'city', 'country', 'first-name', 'last-name']



### GENERAL METHODS

### https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data/15423007#15423007
def should_use_block(value):
    for c in u"\u000a\u000d\u001c\u001d\u001e\u0085\u2028\u2029":
        if c in value:
            return True
    return False


def represent_scalar(self, tag, value, style=None):
    if style is None:
        if should_use_block(value):
            style='|'
        else:
            style = self.default_style

    node = yaml.representer.ScalarNode(tag, value, style=style)
    if self.alias_key is not None:
        self.represented_objects[self.alias_key] = node
    return node


def read_yaml(fp):
    '''
    Read content of a YAML file

    :param fp: Path to YAML file
    '''
    with open(fp, 'r') as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
    return content


### METHODS TO INTERACT WITH people.yaml FILE AND DATA

def load_people():
    '''
    Load people.yaml file into a dictionary
    '''
    people_fp = Path('_data') / Path('people.yaml')
    # load people.yaml file into a dictionary
    with open(people_fp, 'r') as people_f:
        people = yaml.load(people_f, Loader=yaml.FullLoader)
    return people


def load_reordered_people():
    '''
    Load people.yaml file and reorder people as a dictionary with 
    key being First name - Last name and value being the people id
    '''
    people = load_people()
    reorder_people = {}
    for p in people:
        name = '%s %s' % (people[p]['first-name'], people[p]['last-name'])
        reorder_people[name] = p
    return reorder_people


def get_people_id(name, people):
    '''Extract id in people.yaml from a string with a name

    :param name: string with the name
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    '''
    if name not in people:
        print("'%s' for not found in people " % name)
        return ''
    else:
        return people[name]


def get_people_ids(names, people):
    '''Extract list of id in people.yaml from a string with names

    :param names: string with names
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    '''
    ids = []
    if not pd.isnull(names):
        names = names.replace(' and ', ', ').split(', ')
        for n in names:
            ids.append(get_people_id(n, people))
            
    return ids


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
            print("Add info for %s" % github)
            people[github] = info
        else:
            print("Update info for %s" % github)
            people[github] = info
        people_l.append(github)
    print("Full list")
    people_l.sort()
    print('- %s' % '\n- '.join(people_l))

    # dump people dictionary into people.yaml file
    with people_fp.open("w") as people_f:
        people_f.write('# List of people (alphabetical order)\n')
        people_f.write('#\n')
        people_f.write('# Collection names should be equal to github username,\n')
        people_f.write('# if not, add github: false tag and\n')
        people_f.write('# use firstname-lastname as collection name\n')
        people_f.write('#\n')
        people_f.write('# Mandatory: first-name, last-name, country\n')
        people_f.write('---\n')
        people_f.write(yaml.dump(people, allow_unicode=True))

    return people_l


### METHODS TO INTERACT WITH COHORT SCHEDULE FILES

def load_schedule(c):
    '''
    Load cohort schedule

    :param c: cohort number
    '''
    fp = Path('_data') / Path('ols-%s-schedule.yaml' % c )
    schedule = read_yaml(fp)
    for w in schedule['weeks']:
        for c in schedule['weeks'][w]['calls']:
            if 'content' in c:
                c['content'] = '%s' % c['content']
            if 'before' in c:
                c['before'] = '%s' % c['before']
            if 'after' in c:
                c['after'] = '%s' % c['after']
    return schedule, fp


def dump_schedule(schedule, cohort, fp):
    '''
    Dump schedule to YAML file

    :param schedule: dictionary with schedule details
    :param cohort: cohort number
    :param fp: Path to YAML file
    '''
    yaml.representer.BaseRepresenter.represent_scalar = represent_scalar
    with fp.open("w") as schedule_f:
        schedule_f.write("# Schedule for the OLS-%s\n" % cohort)
        schedule_f.write("---\n")
        schedule_f.write(yaml.dump(schedule,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False))


def update_call(call, row, people):
    '''
    Update call details

    :param call: dictionary with call details
    :param row: row from dataframe with call details
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    '''
    if not pd.isnull(row['date']):
        call['date'] = row['date'].strftime('%B %d, %Y')
    if not pd.isnull(row['time']):
        call['time'] = row['time'].strftime('%H:%M')
    if not pd.isnull(row['duration']):
        call['duration'] = "%s min" % int(int(row['duration'].seconds)/60)
    if not pd.isnull(row['Note link']):
        call['notes'] = row['Note link']
    if not pd.isnull(row['Learning objectives']):
        call['content'] = 'In this call, participants will:\n%s' % row['Learning objectives']
    if not pd.isnull(row['Title']):
        call['title'] = row['Title']
    if not pd.isnull(row['Recording']):
        call['recording'] = row['Recording']
    if not pd.isnull(row['Hosts']):
        call['hosts'] = get_people_ids(row['Hosts'], people)
    if not pd.isnull(row['Facilitators']):
        call['facilitators'] = get_people_ids(row['Facilitators'], people)
    if not pd.isnull(row['Type']):
        call['type'] = row['Type']
    if not pd.isnull(row['Before']):
        call['before'] = row['Before']
    if not pd.isnull(row['After']):
        call['after'] = row['After']
    return call


def check_same_event(call, row):
    '''
    Compare call information from YAML and CSV
    
    :param call: call information from YAML
    :param row: call information from CSV
    '''
    same = (call['type'] == row['Type'])
    if 'date' in call and pd.notna(row['date']):
        same = same and (call['date'] == row['date'].strftime('%B %d, %Y'))
    if 'title' in call:
        same = same and (call['title'] == row['Title'])
    return same


def update_resource(res, row, people):
    ''''
    Update resource details

    :param res: dictionary with resource details
    :param row: row from dataframe with resource details
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    '''
    if not pd.isnull(row['Slides']):
        res['link'] = row['Slides']
    if not pd.isnull(row['Confirmed speaker']):
        name = row['Confirmed speaker']
        res['speaker'] = get_people_id(name, people)
    res['type'] = 'slides'
    if not pd.isnull(row['Title']):
        res['title'] = row['Title']
    return res


def add_event_information(schedule, event_df, people):
    '''
    Load event file as data frame and add information into schedule

    :param schedule: dictionary with schedule details
    :param event_df: Path to event CSV file
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    '''
    df = (event_df
        .rename(columns = {'Start Date': 'date',
            'Start Time': 'time',
            'Duration': 'duration'})
        .assign(
            date=lambda x: pd.to_datetime(x['date'], dayfirst=True),
            time=lambda x: pd.to_datetime(x['time']),
            duration=lambda x: pd.to_timedelta(x['duration'])))

    call_types = ['Mentor-Mentee', 'Mentor', 'Cohort', 'Skill-up', 'Q&A']

    # format date and time columns, add event information
    last_call = {}
    for index, row in df.iterrows():
        w = "{:02d}".format(row['Week'])

        if not w in schedule['weeks']:
            print("Adding week %s too the schedule")
            schedule['weeks'][w] = {'start': '', 'calls': []}

        if row['Type'] == "Week":
            if schedule['weeks'][w]['start'] != '':
                if schedule['weeks'][w]['start'] != row['date'].strftime('%B %d, %Y'):
                    print("Different start date for week %s" % w)
                    print("In schedule file: %s" % schedule['weeks'][w]['start'])
                    print("In event file: %s" % row['date'].strftime('%B %d, %Y'))
            else:
                schedule['weeks'][w]['start'] = row['date'].strftime('%B %d, %Y')
        elif row['Type'] in call_types:
            found = False
            for call in schedule['weeks'][w]['calls']:
                if check_same_event(call, row):
                    call = update_call(call, row, people)
                    found = True
                    last_call = call

            if not found:
                call = update_call({}, row, people)
                schedule['weeks'][w]['calls'].append(call)
                last_call = call

        elif row['Type'] == 'Presentation':
            found = False
            if 'resources' not in last_call:
                last_call['resources'] = []
            else:
                for res in last_call['resources']:
                    if 'title' in res and row['Title'] == res['title']:
                        res = update_resource(res, row, people)
                        found = True
            
            if not found:
                res = update_resource({}, row, people)
                last_call['resources'].append(res)

    return schedule


def add_projects(cohort, project_info_fp, info_fp):
    '''
    Add projects

    :param cohort: cohort id
    :param project_info_fp: Path to project sheet file
    :param information_fp: Path to information sheet file
    '''
    # add people to people.yaml
    info_fp = Path(info_fp)
    info_df = pd.read_csv(info_fp)
    added_people = extract_people(info_df)
    
    # reorder people as a dictionary with key being First name - Last name
    # and value being the people id
    reorder_people = load_reordered_people()

    # load people information from sheet file
    # parse it
    # add information to people dictionary
    project_fp = Path('_data') / Path('ols-%s-projects.yaml' % args.cohort )
    project_info_fp = Path(project_info_fp)
    df = pd.read_csv(project_info_fp)
    df = df.where(pd.notnull(df), None)
    projects = {}
    print('Add new projects')
    for index, row in df.iterrows():
        if row['Comment regarding review'] == 'rejected':
            continue
        print(row['Title'])
        # get title
        p = {
            'name': row['Title'].rstrip().lstrip(),
            'description': row['Project-description'].rstrip().lstrip(),
            'participants': [],
            'mentors': [],
            'keywords': []
        }
        # extract participants
        p['participants'] = methods.get_people_ids(row['Authors'], reorder_people)
        # extract mentors
        p['mentors'] = methods.get_people_ids(row['Mentor 1'], reorder_people)
        if row['Mentor 2'] != '':
            p['mentors'] += methods.get_people_ids(row['Mentor 2'], reorder_people)
        if len(p['mentors']) == 0:
            print('No mentor')
        # 
        if row['Keywords'] is not None:
            p['keywords'] = row['Keywords'].split(',\n')
        projects[p['name']] = p
        print('')

    # check if everybody are correctly added to projects from participant file
    print('Check project participants')
    # 1. get projects and people from participant registration
    df = info_df.where(pd.notnull(info_df), None)
    projects_people = {}
    for index, row in df.iterrows():
        projects_people.setdefault(row['OLS-%s Project title' % args.cohort ], [])
        name = "%s %s" % (row['First name'].rstrip(), row['Last name'].rstrip())
        projects_people[row['OLS-%s Project title' % args.cohort]].append(name.title())
    # 2. check each project
    for pr in projects_people:
        print("%s" % pr)
        if pr not in projects:
            print("Not found in project list")
            continue
        for pa in projects_people[pr]:
            if pa not in reorder_people:
                print("'%s' not found in people" % pa)
                continue
            pa_id = reorder_people[pa]
            if pa_id not in projects[pr]['participants']:
                projects[pr]['participants'].append(pa_id)
                print("'%s' added to project" % pa)
        print('')

    # transform project dictionary to list
    project_list = [projects[p] for p in projects]

    # dump project dictionary into project file
    with project_fp.open("w") as project_f:
        project_f.write('# List of projects for OLS-3\n')
        project_f.write('#\n')
        project_f.write('# Check previous OLS for examples\n')
        project_f.write('---\n')
        project_f.write(yaml.dump(project_list, allow_unicode=True))


def create_cohort(cohort):
    '''
    Create files for a new cohort

    :param cohort: cohort id
    '''
    print("new cohort")


def get_expertises(cohort):
    '''
    Extract expert/mentor expertise from metadata file and order expert/mentor given that information

    :param cohort: cohort id
    '''
    people = load_people()

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


def update_schedule(cohort, event_df):
    '''
    Update schedule from a sheet

    :param cohort: cohort id
    :param event_df: data frame with schedule
    '''
    # load people information
    reorder_people = load_reordered_people()

    # load schedule
    schedule, schedule_fp = load_schedule(args.cohort)

    # add event information to schedule
    schedule = add_event_information(schedule, event_df, reorder_people)    

    # dump schedule dictionary into schedule file
    dump_schedule(schedule, args.cohort, schedule_fp)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Interact and prepare OLS website data')
    subparser = parser.add_subparsers(dest='command')
    # Add projects
    addprojects = subparser.add_parser('addprojects', help="Add projects")
    addprojects.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)", required=True)
    addprojects.add_argument('-p', '--projects', help="Path to project sheet file", required=True)
    addprojects.add_argument('-i', '--information', help="Path to information sheet file", required=True) 
    # Create cohort
    createcohort = subparser.add_parser('createcohort', help="Create files for a new cohort")
    createcohort.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)", required=True)
    # Extract people
    extractpeople = subparser.add_parser('extractpeople', help='Extract people information from a sheet and add them to people.yaml')
    group = extractpeople.add_mutually_exclusive_group()
    group.add_argument('-i', '--information', help="Path to information sheet file", action='store_true')
    group.add_argument('-u', '--url', help="URL to information sheet file", action='store_true')
    # Get expertises
    getexpertises = subparser.add_parser('getexpertises', help='Extract expert/mentor expertise from metadata file and order expert/mentor given that information')
    getexpertises.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)", required=True)
    # Update schedule
    updateschedule = subparser.add_parser('updateschedule', help='Update schedule from a sheet')
    updateschedule.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)", required=True)
    group = updateschedule.add_mutually_exclusive_group()
    group.add_argument('-e', '--events', help="Path to event CSV file", action='store_true')
    group.add_argument('-u', '--url', help="URL to event sheet file", action='store_true')
    
    
    args = parser.parse_args()

    if args.command == 'addprojects':
        add_projects(args.cohort, args.projects, args.information)
    elif args.command == 'createcohort':
        create_cohort(args.cohort)
    elif args.command == 'extractpeople':
        if args.url:
            extract_people(pd.read_csv(args.url))
        else:
            information_fp = Path(args.information)
            extract_people(pd.read_csv(information_fp))
    elif args.command == 'getexpertises':
        get_expertises(args.cohort)
    elif args.command == 'updateschedule':
        if args.url:
            event_df = pd.read_csv(args.url)
        else:
            event_df = pd.read_csv(Path(args.events))
        update_schedule(args.cohort, event_df)

#!/usr/bin/env python

import argparse
import pandas as pd
import yaml

from pathlib import Path


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


def load_schedule(c):
    '''
    Load cohort schedule

    :param c: cohort number
    '''
    fp = Path('_data') / Path('ols-%s-schedule.yaml' % c )
    schedule = read_yaml(fp)
    for w in schedule:
        for c in schedule[w]['calls']:
            if 'content' in c:
                c['content'] = '%s' % c['content']
            if 'before' in c:
                c['before'] = '%s' % c['before']
            if 'after' in c:
                c['after'] = '%s' % c['after']
    return schedule, fp


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
    if 'date' in call:
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
            date=lambda x: pd.to_datetime(x['date']),
            time=lambda x: pd.to_datetime(x['time']),
            duration=lambda x: pd.to_timedelta(x['duration'])))

    call_types = ['Mentor-Mentee', 'Mentor', 'Cohort', 'Skill-up', 'Q&A']

    # format date and time columns, add event information
    last_call = {}
    for index, row in df.iterrows():
        w = "{:02d}".format(row['Week'])

        if row['Type'] in call_types:
            found = False
            for call in schedule[w]['calls']:
                if check_same_event(call, row):
                    call = update_call(call, row, people)
                    found = True
                    last_call = call

            if not found:
                call = update_call({}, row, people)
                schedule[w]['calls'].append(call)
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


def dump_schedule(schedule, fp):
    '''
    Dump schedule to YAML file

    :param schedule: dictionary with schedule details
    :param fp: Path to YAML file
    '''
    yaml.representer.BaseRepresenter.represent_scalar = represent_scalar
    with schedule_fp.open("w") as schedule_f:
        schedule_f.write("# Schedule for OLS-1\n")
        schedule_f.write("#\n")
        schedule_f.write("# 'weeknb':\n")
        schedule_f.write("#   timeframe:\n")
        schedule_f.write("#   calls:\n")
        schedule_f.write("#     -\n")
        schedule_f.write("#       type: Mentor-Mentee/Cohort/Mentors\n")
        schedule_f.write("#       duration: .. min\n")
        schedule_f.write("#       title:\n")
        schedule_f.write("#       date: Month Day, Year\n")
        schedule_f.write("#       time: '14:00'\n")
        schedule_f.write("#       calendar-event: link to calendar event\n")
        schedule_f.write("#       notes: link to notes\n")
        schedule_f.write("#       recording: link to recording\n")
        schedule_f.write("#       hosts: ids of hosts\n")
        schedule_f.write("#       facilitators: ids of facilitators\n")
        schedule_f.write("#       content: |\n")
        schedule_f.write("#         Details of the content written in Markdown\n")
        schedule_f.write("#       resources:\n")
        schedule_f.write("#         -\n")
        schedule_f.write("#           type: slides/document/external-link\n")
        schedule_f.write("#           title:\n")
        schedule_f.write("#           speaker: username in people.yaml, if slides\n")
        schedule_f.write("#           link:\n")
        schedule_f.write("---\n")
        schedule_f.write(yaml.dump(schedule,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add projects')
    parser.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)")
    parser.add_argument('-e', '--events', help="Path to event CSV file")
    parser.add_argument('-u', '--url', help="URL to event sheet file")
    args = parser.parse_args()

    # check / load event information
    if not args.events:
        if not args.url:
            raise ValueError("Provide either path or URL to event file")
        else:
            event_df = pd.read_csv(args.url)
    else:
        event_df = Path(args.events)

    # load people information
    people_fp = Path('_data') / Path('people.yaml')
    with open(people_fp, 'r') as people_f:
        people = yaml.load(people_f, Loader=yaml.FullLoader)
    reorder_people = {}
    for p in people:
        name = '%s %s' % (people[p]['first-name'], people[p]['last-name'])
        reorder_people[name] = p

    # load schedule
    schedule, schedule_fp = load_schedule(args.cohort)

    # add event information to schedule
    schedule = add_event_information(schedule, event_df, reorder_people)    

    # dump schedule dictionary into schedule file
    dump_schedule(schedule, schedule_fp)
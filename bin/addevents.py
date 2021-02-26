#!/usr/bin/env python

import argparse
import logging
import pandas as pd
import yaml

from pathlib import Path


### https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data/15423007#15423007
def should_use_block(value):
    for c in u"\u000a\u000d\u001c\u001d\u001e\u0085\u2028\u2029":
        if c in value:
            return True
    return False

def my_represent_scalar(self, tag, value, style=None):
    if style is None:
        if should_use_block(value):
             style='|'
        else:
            style = self.default_style

    node = yaml.representer.ScalarNode(tag, value, style=style)
    if self.alias_key is not None:
        self.represented_objects[self.alias_key] = node
    return node


def updatecall(call, row):
    '''
    Update dictionary with call details

    :param call: dictionary with call details
    :param row: row from dataframe with call details

    :return: dictionary with call details
    '''
    call['date'] = row['Start Date'].strftime('%B %d, %Y')
    call['time'] = row['Start Time'].strftime('%H:%M')
    call['duration'] = "%s min" % row['Duration']
    call['notes'] = row['Note link']
    return call


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add projects')
    parser.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)")
    parser.add_argument('-e', '--events', help="Path to event CSV file")
    parser.add_argument('-l', '--log', help="Path to log output file")
    args = parser.parse_args()

    logging.basicConfig(filename=args.log, level=logging.DEBUG)

    # load schedule
    schedule_fp = Path('_data') / Path('ols-%s-schedule.yaml' % args.cohort )
    with open(schedule_fp, 'r') as schedule_f:
        schedule = yaml.load(schedule_f, Loader=yaml.FullLoader)

    # 
    for w in schedule:
        for c in schedule[w]['calls']:
            if 'content' in c:
                c['content'] = '%s' % c['content']
            if 'before' in c:
                c['before'] = '%s' % c['before']
            if 'after' in c:
                c['after'] = '%s' % c['after']

    # 
    event_fp = Path(args.events)
    df = pd.read_csv(event_fp)
    df['Start Date']= pd.to_datetime(df['Start Date'])
    df['Start Time']= pd.to_datetime(df['Start Time'])

    # format date and time columns
    for index, row in df.iterrows():
        w = "{:02d}".format(row['Week'])
        if row['Type'] == 'Cohort':
            for c in schedule[w]['calls']:
                if c['type'] == 'Cohort':
                    c = updatecall(c, row)
        elif row['Type'] == 'Q&A':
            c = updatecall({}, row)
            c['type'] = 'Q&A'
            c['title'] = 'Q&A call on week %s cohort call' % (row['Week']-1)
            schedule[w]['calls'].append(c)


    # dump schedule dictionary into schedule file
    yaml.representer.BaseRepresenter.represent_scalar = my_represent_scalar
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
        schedule_f.write("#       agenda: tldr\n")
        schedule_f.write("#       notes: link to notes\n")
        schedule_f.write("#       recording: link to recording\n")
        schedule_f.write("#       content: |\n")
        schedule_f.write("#         Details of the content written in Markdown\n")
        schedule_f.write("#       before: |\n")
        schedule_f.write("#         Tasks to do before as a list written in Markdown\n")
        schedule_f.write("#       after: |\n")
        schedule_f.write("#         Tasks to do after as a list written in Markdown\n")
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
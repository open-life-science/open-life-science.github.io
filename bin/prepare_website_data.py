#!/usr/bin/env python

import argparse
import copy
import pandas as pd
import pycountry

from geopy.geocoders import Nominatim
from pathlib import Path
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as DQS

ROLES = ['role', 'participant', 'mentor', 'expert', 'speaker', 'facilitator', 'organizer']
CALL_TYPES = ['Mentor-Mentee', 'Mentor', 'Cohort', 'Skill-up', 'Q&A', 'Cafeteria']

# copied from https://github.com/jefftune/pycountry-convert/blob/master/pycountry_convert/country_alpha2_to_continent.py
COUNTRY_ALPHA2_TO_CONTINENT = {
    'AB': 'Asia',
    'AD': 'Europe',
    'AE': 'Asia',
    'AF': 'Asia',
    'AG': 'North America',
    'AI': 'North America',
    'AL': 'Europe',
    'AM': 'Asia',
    'AO': 'Africa',
    'AR': 'South America',
    'AS': 'Oceania',
    'AT': 'Europe',
    'AU': 'Oceania',
    'AW': 'North America',
    'AX': 'Europe',
    'AZ': 'Asia',
    'BA': 'Europe',
    'BB': 'North America',
    'BD': 'Asia',
    'BE': 'Europe',
    'BF': 'Africa',
    'BG': 'Europe',
    'BH': 'Asia',
    'BI': 'Africa',
    'BJ': 'Africa',
    'BL': 'North America',
    'BM': 'North America',
    'BN': 'Asia',
    'BO': 'South America',
    'BQ': 'North America',
    'BR': 'South America',
    'BS': 'North America',
    'BT': 'Asia',
    'BV': 'Antarctica',
    'BW': 'Africa',
    'BY': 'Europe',
    'BZ': 'North America',
    'CA': 'North America',
    'CC': 'Asia',
    'CD': 'Africa',
    'CF': 'Africa',
    'CG': 'Africa',
    'CH': 'Europe',
    'CI': 'Africa',
    'CK': 'Oceania',
    'CL': 'South America',
    'CM': 'Africa',
    'CN': 'Asia',
    'CO': 'South America',
    'CR': 'North America',
    'CU': 'North America',
    'CV': 'Africa',
    'CW': 'North America',
    'CX': 'Asia',
    'CY': 'Asia',
    'CZ': 'Europe',
    'DE': 'Europe',
    'DJ': 'Africa',
    'DK': 'Europe',
    'DM': 'North America',
    'DO': 'North America',
    'DZ': 'Africa',
    'EC': 'South America',
    'EE': 'Europe',
    'EG': 'Africa',
    'ER': 'Africa',
    'ES': 'Europe',
    'ET': 'Africa',
    'FI': 'Europe',
    'FJ': 'Oceania',
    'FK': 'South America',
    'FM': 'Oceania',
    'FO': 'Europe',
    'FR': 'Europe',
    'GA': 'Africa',
    'GB': 'Europe',
    'GD': 'North America',
    'GE': 'Asia',
    'GF': 'South America',
    'GG': 'Europe',
    'GH': 'Africa',
    'GI': 'Europe',
    'GL': 'North America',
    'GM': 'Africa',
    'GN': 'Africa',
    'GP': 'North America',
    'GQ': 'Africa',
    'GR': 'Europe',
    'GS': 'South America',
    'GT': 'North America',
    'GU': 'Oceania',
    'GW': 'Africa',
    'GY': 'South America',
    'HK': 'Asia',
    'HM': 'Antarctica',
    'HN': 'North America',
    'HR': 'Europe',
    'HT': 'North America',
    'HU': 'Europe',
    'ID': 'Asia',
    'IE': 'Europe',
    'IL': 'Asia',
    'IM': 'Europe',
    'IN': 'Asia',
    'IO': 'Asia',
    'IQ': 'Asia',
    'IR': 'Asia',
    'IS': 'Europe',
    'IT': 'Europe',
    'JE': 'Europe',
    'JM': 'North America',
    'JO': 'Asia',
    'JP': 'Asia',
    'KE': 'Africa',
    'KG': 'Asia',
    'KH': 'Asia',
    'KI': 'Oceania',
    'KM': 'Africa',
    'KN': 'North America',
    'KP': 'Asia',
    'KR': 'Asia',
    'KW': 'Asia',
    'KY': 'North America',
    'KZ': 'Asia',
    'LA': 'Asia',
    'LB': 'Asia',
    'LC': 'North America',
    'LI': 'Europe',
    'LK': 'Asia',
    'LR': 'Africa',
    'LS': 'Africa',
    'LT': 'Europe',
    'LU': 'Europe',
    'LV': 'Europe',
    'LY': 'Africa',
    'MA': 'Africa',
    'MC': 'Europe',
    'MD': 'Europe',
    'ME': 'Europe',
    'MF': 'North America',
    'MG': 'Africa',
    'MH': 'Oceania',
    'MK': 'Europe',
    'ML': 'Africa',
    'MM': 'Asia',
    'MN': 'Asia',
    'MO': 'Asia',
    'MP': 'Oceania',
    'MQ': 'North America',
    'MR': 'Africa',
    'MS': 'North America',
    'MT': 'Europe',
    'MU': 'Africa',
    'MV': 'Asia',
    'MW': 'Africa',
    'MX': 'North America',
    'MY': 'Asia',
    'MZ': 'Africa',
    'NA': 'Africa',
    'NC': 'Oceania',
    'NE': 'Africa',
    'NF': 'Oceania',
    'NG': 'Africa',
    'NI': 'North America',
    'NL': 'Europe',
    'NO': 'Europe',
    'NP': 'Asia',
    'NR': 'Oceania',
    'NU': 'Oceania',
    'NZ': 'Oceania',
    'OM': 'Asia',
    'OS': 'Asia',
    'PA': 'North America',
    'PE': 'South America',
    'PF': 'Oceania',
    'PG': 'Oceania',
    'PH': 'Asia',
    'PK': 'Asia',
    'PL': 'Europe',
    'PM': 'North America',
    'PR': 'North America',
    'PS': 'Asia',
    'PT': 'Europe',
    'PW': 'Oceania',
    'PY': 'South America',
    'QA': 'Asia',
    'RE': 'Africa',
    'RO': 'Europe',
    'RS': 'Europe',
    'RU': 'Europe',
    'RW': 'Africa',
    'SA': 'Asia',
    'SB': 'Oceania',
    'SC': 'Africa',
    'SD': 'Africa',
    'SE': 'Europe',
    'SG': 'Asia',
    'SH': 'Africa',
    'SI': 'Europe',
    'SJ': 'Europe',
    'SK': 'Europe',
    'SL': 'Africa',
    'SM': 'Europe',
    'SN': 'Africa',
    'SO': 'Africa',
    'SR': 'South America',
    'SS': 'Africa',
    'ST': 'Africa',
    'SV': 'North America',
    'SY': 'Asia',
    'SZ': 'Africa',
    'TC': 'North America',
    'TD': 'Africa',
    'TG': 'Africa',
    'TH': 'Asia',
    'TJ': 'Asia',
    'TK': 'Oceania',
    'TM': 'Asia',
    'TN': 'Africa',
    'TO': 'Oceania',
    'TP': 'Asia',
    'TR': 'Asia',
    'TT': 'North America',
    'TV': 'Oceania',
    'TW': 'Asia',
    'TZ': 'Africa',
    'UA': 'Europe',
    'UG': 'Africa',
    'US': 'North America',
    'UY': 'South America',
    'UZ': 'Asia',
    'VC': 'North America',
    'VE': 'South America',
    'VG': 'North America',
    'VI': 'North America',
    'VN': 'Asia',
    'VU': 'Oceania',
    'WF': 'Oceania',
    'WS': 'Oceania',
    'XK': 'Europe',
    'YE': 'Asia',
    'YT': 'Africa',
    'ZA': 'Africa',
    'ZM': 'Africa',
    'ZW': 'Africa',
}

optional_info = ['twitter', 'website', 'orcid', 'affiliation', 'city', 'country', 'pronouns', 'expertise', 'bio']
to_capitalize_info = ['affiliation', 'city', 'country']
people_fp = Path('_data/people.yaml')
geolocator = Nominatim(user_agent="MyApp")
artifact_dp = Path('_data/artifacts/')

### GENERAL METHODS

yaml = YAML()
yaml.preserve_quotes = True

def read_yaml(fp):
    '''
    Read content of a YAML file

    :param fp: Path to YAML file
    '''
    with open(fp, 'r') as f:
        content = yaml.load(f)
    return content


def get_list_from_string(s, title=True):
    '''
    Transform a string into a list
    '''
    if title:
        return s.rstrip().replace(' and ', ', ').replace('|', ', ').title().split(', ')
    else:
        return s.rstrip().replace(' and ', ', ').replace('|', ', ').split(', ')


### METHODS TO INTERACT WITH people.yaml FILE AND DATA

def load_people():
    '''
    Load people.yaml file into a dictionary
    '''
    return read_yaml(people_fp)


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


def dump_people(people):
    '''
    Dump people dictionary in people file

    :param people: dictionary with people information
    '''
    with people_fp.open("w") as people_f:
        people_f.write('# List of people (alphabetical order)\n')
        people_f.write('#\n')
        people_f.write('# Collection names should be equal to github username,\n')
        people_f.write('# if not, add github: false tag and\n')
        people_f.write('# use firstname-lastname as collection name\n')
        people_f.write('#\n')
        people_f.write('# Mandatory: first-name, last-name, country\n')
        people_f.write('---\n')
        yaml.dump(dict(sorted(people.items())), people_f)


def get_people_id(name, people):
    '''Extract id in people.yaml from a string with a name

    :param name: string with the name
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    '''
    if name not in people:
        print(f"'{name}' not found in people ")
        return None
    else:
        return people[name]


def get_people_ids(names, people):
    '''Extract list of id in people.yaml from a string with names

    :param names: string with names
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    '''
    ids = []
    if not pd.isnull(names):
        names = get_list_from_string(names, title=False)
        for n in names:
            id = get_people_id(n.rstrip(), people)
            if id is not None:
                ids.append(id)

    return ids


def get_people_names(p_list, people):
    '''Get names of peoke

    :param p_list: list of people id
    :param people: dictionary with people information
    '''
    names = []
    for p in p_list:
        if p is None:
            names.append(None)
        elif p not in people:
            print(f"{p} not found in people")
            names.append(None)
        else:
            names.append(f"{people[p]['first-name']} {people[p]['last-name']}")
    return names


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


def get_country_extra_information(country):
    '''
    Get country code and continent

    :param country: name of the country
    '''
    country_code = None
    continent = None
    py_country = pycountry.countries.get(name=country)
    if py_country is None:
        py_country = pycountry.countries.get(common_name=country)
        if py_country is None:
            print(f"{country} not found")
    else:
        country_code = py_country.alpha_3
        if py_country.alpha_2 not in COUNTRY_ALPHA2_TO_CONTINENT:
            print(f"No continent found for {country} / {py_country.alpha_2}")
        else:
            continent = COUNTRY_ALPHA2_TO_CONTINENT[py_country.alpha_2]
    return country_code, continent


def get_city_location(city):
    '''
    Get city longitude and latitude

    :param city: city name
    '''
    longitude = None
    latitude = None
    location = geolocator.geocode(city)
    if location is None:
        print(f"{city} not found")
    else:
        longitude = location.longitude
        latitude = location.latitude
    return longitude, latitude


def extract_people_info(row, people):
    '''Extract people information from a row of the csv
    and return them as a key and a dictionary

    :param row: df row
    :param people: dictionary with people information
    '''
    info = {
        'first-name': row['First name'].rstrip(),
        'last-name': row['Last name'].rstrip(),
        'twitter': row['Twitter'] if 'Twitter' in row else None,
        'website': row['Website'] if 'Website' in row else None,
        'orcid': row['ORCID'] if 'ORCID' in row else None,
        'affiliation': row['Affiliation'] if 'Affiliation' in row else None,
        'city': row['City'] if 'City' in row else None,
        'country': row['Country'] if 'Country' in row else None,
        'pronouns': row['Pronouns'] if 'Pronouns' in row else None,
        'expertise': row['Areas of expertise'] if 'Areas of expertise' in row else None,
        'bio': row['Bio'] if 'Bio' in row else None
    }
    # get id
    id = row['GitHub']
    if id is None:
        # check if person exists from first and last name
        for p in people:
            if people[p]['first-name'] == info['first-name'] and people[p]['last-name'] == info['last-name']:
                id = p
        # create username
        if id is None:
            id = f"{info['first-name']}-{info['last-name']}"
            info['github'] = False
    id = id.replace('https://github.com/', '').rstrip()
    id = id.lower().replace(' ', '-').replace('@', '')
    # format country
    if info['country'] is not None:
        country = info['country']
        country = country.replace('UK', 'United Kingdom')
        country = country.replace('US', 'United States')
        country = country.replace('USA', 'United States')
        country_3, continent = get_country_extra_information(info['country'])
        if country_3 is not None:
            info['country_3'] = country_3
        if continent is not None:
            info['continent'] = continent
    # format city
    if info['city'] is not None:
        longitude, latitude = get_city_location(info['city'])
        if longitude is not None:
            info['longitude'] = longitude
            info['latitude'] = latitude
    # format ORCID
    if info['orcid'] is not None:
        info['orcid'] = info['orcid'].replace('https://orcid.org/', '')
    # format Twitter
    if info['twitter'] is not None:
        info['twitter'] = info['twitter'].replace('@', '')
    # format expertise
    if info['expertise'] is not None:
        info['expertise'] = get_list_from_string(info['expertise'])
        info['expertise'] = [x.capitalize() for x in info['expertise']]
    # format website
    if info['website'] is not None and not info['website'].startswith('https'):
        info['website'] = 'https://%s' % info['website']
    # check info and remove optional empty info
    info_k = list(info.keys())
    for i in info_k:
        if info[i] is None:
            if id in people and i in people[id]:
                info[i] = people[id][i]
            elif i in optional_info:
                del info[i]
        else:
            if i not in ['expertise', 'github', 'longitude', 'latitude']:
                info[i] = info[i].rstrip()
            if i in to_capitalize_info:
                info[i] = info[i].title()
    return id, info


def extract_people(df):
    '''Extract people information from a sheet and add them to people.yaml

    :param df: Path to information sheet file
    '''
    # get people information
    people = load_people()

    # load people information from sheet file
    # parse it
    # add information to people dictionary
    df = (df.where(pd.notnull(df), None)
        .rename(columns={
            'First Name': 'First name',
            'Last Name': 'Last name',
    }))

    people_l = []
    for index, row in df.iterrows():
        id, info = extract_people_info(row, people)
        if id not in people:
            print(f"Add info for {id}")
            people[id] = info
        else:
            print(f"Update info for {id}")
            for i in info:
                people[id][i] = info[i]
        people_l.append(id)
    print("Full list")
    people_l.sort()
    s = '\n- '.join(people_l)
    print(f"- {s}")

    # dump people dictionary into people.yaml file
    dump_people(people)

    return people_l


def extract_people_df(ids, people, fp):
    '''
    Create a dataframe with people information from a list of ids
    and write in a file

    :param ids: list of people ids
    :param people: people information
    '''
    col = ['affiliation', 'bio', 'city', 'country', 'expertise', 'first-name', 'github', 'last-name', 'orcid', 'pronouns', 'twitter', 'website']
    info = {}
    for i in ids:
        if i not in people:
            print(f"{i} not in people")
            continue
        info[i] = {}
        if 'github' not in people[i]:
            info[i]['github'] = i
        for c in col:
            if c in people[i]:
                if c == 'expertise':
                    info[i][c] = ','.join(people[i][c])
                elif c == 'bio':
                    info[i][c] = people[i][c].replace("\n", '')
                else:
                    info[i][c] = people[i][c]
            else:
                info[i][c] = None
    df = pd.DataFrame.from_dict(info, orient='index', columns=col)
    df.to_csv(fp, sep="\t")


def get_people(cohort, participant_fp, mentor_fp, expert_fp, speaker_fp, host_fp):
    '''
    Extract people information of a specific cohort from website to spreadsheets

    :param cohort: cohort id
    :param participant_fp: path to output sheet with participants details
    :param mentor_fp: path to output sheet with mentor details
    :param expert_fp: path to output sheet with expert details
    :param speaker_fp: path to output sheet with speaker details
    :param host_fp: path to output sheet with call host details
    '''
    # load people information
    people = load_people()

    # extract participants and mentors
    participants = []
    mentors = []
    # load projects
    fp = Path(f'_data/openseeds/ols-{cohort}/projects.yaml' )
    projects = read_yaml(fp)
    for p in projects:
        participants += p['participants']
        mentors += p['mentors']
    extract_people_df(participants, people, participant_fp)
    extract_people_df(mentors, people, mentor_fp)

    # extract experts and organizers
    # load metadata
    fp = Path(f'_data/openseeds/ols-{cohort}/metadata.yaml' )
    metadata = read_yaml(fp)
    experts = metadata['experts']
    extract_people_df(experts, people, expert_fp)

    # extract speakers and call hosts
    speakers = []
    hosts = []
    # load schedule
    schedule = load_schedule(args.cohort)
    for k, week in schedule['weeks'].items():
        for call in week['calls']:
            if call['type'] == 'cohort':
                for r in call['talks']:
                    if 'speakers' in r:
                        speakers += r['speakers']
            if 'hosts' in call:
                hosts += call['hosts']
    extract_people_df(speakers, people, speaker_fp)
    extract_people_df(hosts, people, host_fp)


### METHODS TO INTERACT WITH COHORT SCHEDULE FILES

def create_empty_schedule():
    '''
    Create empty schedule
    '''
    schedule = {
        'timeline': [
            {
                'date': None,
                'description': 'Call for Application opens',
                'details': 'See the [guidelines and templates](https://github.com/open-life-science/application-forms)'
            },{
                'date': None,
                'description': 'Application webinar',
                'type': ['Talk', 'Q&A'],
                'notes': None,
                'recording': None,
                'details': 'Watch recordings from previous webinars on [**YouTube**](https://www.youtube.com/playlist?list=PL1CvC6Ez54KBsPT0fhPtkHmBaXR4f8Dqt)'
            },{
                'date': None,
                'description': 'Application Clinic Call',
                'type': ['Q&A'],
                'notes': None,
                'details': 'At this call, OLS team will be available to provide help if you have any question related to your application'
            },{
                'date': None,
                'description': 'Call for applications closed'
            },{
                'date': None,
                'description': 'Successful applicants announced'
            }],
        'weeks': {}
    }
    for i in range(16):
        schedule['weeks']['%02d' % (i+1)] = {
            'start': None,
            'calls': []
        }
    return schedule


def load_schedule(cohort):
    '''
    Load cohort schedule

    :param cohort: cohort number
    '''
    fp = Path(f'_data/openseeds/ols-{cohort}/schedule.yaml' )
    schedule = read_yaml(fp)
    for w in schedule['weeks']:
        for c in schedule['weeks'][w]['calls']:
            if 'content' in c:
                c['content'] = '%s' % c['content']
            if 'before' in c:
                c['before'] = '%s' % c['before']
            if 'after' in c:
                c['after'] = '%s' % c['after']
    return schedule


def dump_schedule(schedule, cohort):
    '''
    Dump schedule to YAML file

    :param schedule: dictionary with schedule details
    :param cohort: cohort number
    '''
    fp = Path(f'_data/openseeds/ols-{cohort}/schedule.yaml')
    with fp.open("w") as schedule_f:
        schedule_f.write(f"# Schedule for the OLS-{cohort}\n")
        schedule_f.write("---\n")
        yaml.dump(schedule, schedule_f)


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
        call['time'] = DQS(row['time'].strftime('%H:%M'))
    if not pd.isnull(row['duration']):
        call['duration'] = "%s min" % int(int(row['duration'].seconds)/60)
    if not pd.isnull(row['Note link']):
        call['notes'] = row['Note link']
    if 'Learning objectives' in row and not pd.isnull(row['Learning objectives']):
        call['content'] = 'In this call, participants will:\n%s' % row['Learning objectives']
    if not pd.isnull(row['Title']):
        call['title'] = row['Title']
    if not pd.isnull(row['Recording']):
        call['recording'] = row['Recording']
    if 'Hosts' in row and not pd.isnull(row['Hosts']):
        call['hosts'] = get_people_ids(row['Hosts'], people)
    elif 'Call lead' in row and not pd.isnull(row['Call lead']):
        call['hosts'] = get_people_ids(row['Call lead'], people)
    if 'Facilitators' in row and not pd.isnull(row['Facilitators']):
        call['facilitators'] = get_people_ids(row['Facilitators'], people)
    if not pd.isnull(row['Type']):
        call['type'] = row['Type']
    if 'Learning objectives' in row and not pd.isnull(row['Learning objectives']):
        call['learning_objectives'] = row['Learning objectives']
    if 'Before' in row and not pd.isnull(row['Before']):
        call['before'] = row['Before']
    if 'After' in row and not pd.isnull(row['After']):
        call['after'] = row['After']
    elif 'Assignments' in row and not pd.isnull(row['Assignments']):
        call['after'] = row['Assignments']
    call['talks'] = []
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


def update_talks(talks, row, people):
    ''''
    Update resource details

    :param talks: dictionary with talk details
    :param row: row from dataframe with talk details
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    '''
    if not pd.isnull(row['Slides']):
        talks['slides'] = row['Slides']
    if not pd.isnull(row['Confirmed speaker']):
        names = row['Confirmed speaker'].split(', ')
        talks['speakers'] = [get_people_id(n, people) for n in names]
    if not pd.isnull(row['Title']):
        talks['title'] = row['Title']
    if not pd.isnull(row['Recording']):
        talks['recording'] = row['Recording']
    if not pd.isnull(row['Tag']):
        talks['tag'] = row['Tag']
    return talks


def prepare_schedule_df(schedule_df):
    '''
    Prepare data frame with schedule

    :param schedule_df: data frame with schedule
    '''
    df = (schedule_df
        .rename(columns = {'Start Date': 'date',
            'Start Time': 'time',
            'Duration': 'duration'})
        .assign(
            date=lambda x: pd.to_datetime(x['date'], dayfirst=True, errors='coerce'),
            time=lambda x: pd.to_datetime(x['time'], format='%H:%M:%S', errors='coerce'),
            duration=lambda x: pd.to_timedelta(x['duration'])))
    return df


def add_event_information(schedule, schedule_df, people):
    '''
    Load event file as data frame and add information into schedule

    :param schedule: dictionary with schedule details
    :param schedule_df: data frame with schedule
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    '''
    df = prepare_schedule_df(schedule_df)

    # format date and time columns, add event information
    last_call = {}
    for index, row in df.iterrows():
        w = "{:02d}".format(int(row['Week']))

        if not w in schedule['weeks']:
            print(f"Adding week {w} to the schedule")
            schedule['weeks'][w] = {'start': '', 'calls': []}

        if row['Type'] == "Week":
            if schedule['weeks'][w]['start'] != '':
                if schedule['weeks'][w]['start'] != row['date'].strftime('%B %d, %Y'):
                    if schedule['weeks'][w]['start'] is None:
                        schedule['weeks'][w]['start'] = row['date'].strftime('%B %d, %Y')
                    else:
                        print(f"Different start date for week {w}")
                        print(f"In schedule file: {schedule['weeks'][w]['start']}")
                        print(f"In event file: {row['date'].strftime('%B %d, %Y')}")
            else:
                schedule['weeks'][w]['start'] = row['date'].strftime('%B %d, %Y')
        elif row['Type'] in CALL_TYPES:
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
            last_call['talks'].append(update_talks({}, row, people))

    return schedule

### METHODS TO INTERACT WITH COHORT PROJECT FILES

def dump_projects(projects, cohort):
    '''
    Dump projects to YAML file

    :param projects: dictionary with project details
    :param cohort: cohort number
    '''
    project_fp = Path(f'_data/openseeds/ols-{cohort}/projects.yaml')
    with project_fp.open("w") as project_f:
        project_f.write(f'# List of projects for OLS-{cohort}\n')
        project_f.write('#\n')
        project_f.write('# Check previous OLS for examples\n')
        project_f.write('---\n')
        yaml.dump(projects, project_f)


### METHODS TO INTERACT WITH COHORT METADATA FILE

def create_empty_metadata():
    '''
    Create empty metadata
    '''
    metadata = {
        'experts': [],
        'organizers': ['bebatut', 'emmyft', 'malvikasharan', 'yochannah'],
        'possible-mentors': []
    }
    return metadata


def load_metadata(cohort):
    '''
    Laod metadata from YAML file

    :param cohort: cohort number
    '''
    metadata_fp = Path(f'_data/openseeds/ols-{cohort}/metadata.yaml' )
    # load metadata cohort file into a dictionary
    with open(metadata_fp, 'r') as metadata_f:
        metadata = yaml.load(metadata_f)
    return metadata


def dump_metadata(metadata, cohort):
    '''
    Dump metadata to YAML file

    :param metadata: dictionary with metadata details
    :param cohort: cohort number
    '''
    metadata_fp = Path(f'_data/openseeds/ols-{cohort}/metadata.yaml' )
    with metadata_fp.open("w") as metadata_f:
        metadata_f.write(f'# List of experts, possible mentors and organizers for OLS-{cohort}\n')
        metadata_f.write('#\n')
        metadata_f.write('#\n')
        metadata_f.write('# People should be also in people.yaml file and linked using their GitHub username\n')
        metadata_f.write('# Ordering by expertise should be done by running the bin/sort-expertises.py script\n')
        metadata_f.write('---\n')
        yaml.dump(metadata, metadata_f)


### METHODS TO BUILD THE LIBRARY

def extract_talks():
    '''
    Extract talks from all cohort
    '''
    talks = []
    for c in Path('_data/openseeds').iterdir():
        # get cohort schedule
        cohort = c.name.split("-")[1]
        schedule = load_schedule(cohort)
        # extract talks
        for w, week in schedule['weeks'].items():
            if 'calls' not in week:
                continue
            for c, call in enumerate(week['calls']):
                if 'talks' in call:
                    for talk in call['talks']:
                        talk = dict(talk)
                        talk['date'] = call['date']
                        talk['cohort'] = f'ols-{cohort}'
                        talks.append(talk)
    return talks


def aggregate_talks(talks):
    '''
    Aggregate talks by tag

    :param talks: list with talks
    '''
    talks_by_tag = {}
    for talk in talks:
        if 'tag' in talk:
            tag = talk['tag']
            del talk['tag']
        else:
            tag = 'Not tagged'
        talks_by_tag.setdefault(tag, [])
        talks_by_tag[tag].append(dict(talk))
    return talks_by_tag


def combine_tags(talks_by_tag):
    '''
    Combine tags by topic to build library

    :param talks_by_tag: dictionary with talks grouped by tags
    '''
    # get tag to topic mapping
    tag_topic_mapping = pd.read_csv("https://docs.google.com/spreadsheets/d/1sDJLG8RuoShWUQN78lvx_mghBbGfusdzlb1WwYrCbjk/export?format=csv&gid=0")
    # build library
    library = {}
    for tag, talks in talks_by_tag.items():
        if tag in tag_topic_mapping.Tag.values:
            tag_row = tag_topic_mapping[tag_topic_mapping.Tag == tag]
            topic = tag_row.Topic.tolist()[0]
            description = tag_row.Description.tolist()[0]
        else:
            print(f'No topic found for {tag}')
            continue
        # add talks to library
        library.setdefault(topic, {})
        library[topic][tag] = {
            'description': description,
            'talks': talks
        } 
    # reorder library
    ordered_library = {}
    for t in tag_topic_mapping.Topic.unique():
        if t in library:
            ordered_library[t] = library[t]
    return ordered_library


### METHODS TO EXTRACT DATA TO CSV

def update_people_info(p_list, p_dict, cohort, role, value):
    '''
    Update people attribute for a cohort

    :param p_list: list of people id to update
    :param p_dict: dictionary with people information
    :param role: status to add
    :param cohort: concerned cohort
    '''
    for p in p_list:
        if p is None:
            continue
        if p not in p_dict:
            print(f"{p} not found in people")
            continue
        p_dict[p][f'{cohort}-role'].append(role)
        if role == 'participant' or role == 'mentor':
            p_dict[p][f'{cohort}-{role}'].append(value)
        else:
            p_dict[p][f'{cohort}-{role}'] = value


def format_people_per_cohort(people, projects):
    '''
    Format to get people with their location and cohort and role
    (1 entry per person, per cohort, per role)

    :param people: dictionary with people information
    :param projects: 
    '''
    people_per_cohort = []
    for key, value in people.items():
        info = {'id': key}
        # get localisation information
        for e in ['country', 'country_3', 'city', 'longitude', 'latitude']:
            info[e] = value[e] if e in value else None
        # get cohort participation
        for c in Path('_data/openseeds').iterdir():
            cohort = get_cohort_name(c)
            el = f'{cohort}-role'
            if el in value and len( value[el]) > 0:
                for r in value[el]:
                    t_info = copy.copy(info)
                    t_info['cohort'] = cohort.split('-')[-1]
                    t_info['role'] = r
                    people_per_cohort.append(t_info)
    return people_per_cohort


def export_people_per_roles(people_df, out_dp):
    '''
    Export people per role

    :param people_df: dataframe with people information
    :param out_dp: Path object to output directory
    '''
    people_info_df = people_df[[
        'city',
        'country',
        'first-name',
        'last-name',
        'pronouns',
        'country_3',
        'continent',
        'longitude',
        'latitude']]
    out_dp = out_dp / Path("roles")
    out_dp.mkdir(parents=True, exist_ok=True)
    for r in ROLES:
        role_df = people_df.filter(regex = r)
        role_df = role_df[role_df.filter(regex = r).notna().any(axis=1)]
        for c in Path('_data/openseeds').iterdir():
            i = c.name.split("-")[1]
            role_df.rename(columns={f"ols-{i}-{r}": f"ols-{i}"}, inplace=True)
        df = pd.merge(
            people_info_df,
            role_df,
            left_index=True,
            right_index=True,
            how="inner")
        fp = Path(out_dp) / Path(f"{r}.csv")
        df.to_csv(fp)


def get_cohort_name(c):
    '''Get cohort name from cohort data path
    
    :param c: Path object to cohort data
    '''
    i = c.name.split("-")[1]
    return f'ols-{i}'


### METHODS TO PREPARE CALL TEMPLATES

def extract_calls(schedule_df):
    '''
    Extract calls

    :param schedule_df: data frame with schedule
    '''
    calls = {}
    for index, row in schedule_df.iterrows():
        w = "{:02d}".format(int(row['Week']))
        
        if row['Type'] == 'Cohort' or row['Type'] == 'Skill-up':
            calls[w] = {
                'date': '',
                'time': '',
                'duration': '',
                'title': '',
                'lead': '',
                'facilitator': '',
                'learning_objectives': '',
                'before': '',
                'after': '',
                'icebreaker': '',
            }
            if not pd.isnull(row['date']):
                calls[w]['date'] = row['date'].strftime('%B %d, %Y')
            if not pd.isnull(row['time']):
                calls[w]['time'] = DQS(row['time'].strftime('%H:%M'))
            if not pd.isnull(row['duration']):
                calls[w]['duration'] = "%s min" % int(int(row['duration'].seconds)/60)
            if not pd.isnull(row['Title']):
                calls[w]['title'] = row['Title']
            if 'Hosts' in row and not pd.isnull(row['Hosts']):
                calls[w]['lead'] = row['Hosts']
            elif 'Call lead' in row and not pd.isnull(row['Call lead']):
                calls[w]['lead'] = row['Call lead']
            if 'Facilitators' in row and not pd.isnull(row['Facilitators']):
                calls[w]['facilitator'] = row['Facilitators']
            if 'Learning objectives' in row and not pd.isnull(row['Learning objectives']):
                calls[w]['learning_objectives'] = row['Learning objectives'].replace('* ', '   * ').replace('- ', '   - ')
            if 'Before' in row and not pd.isnull(row['Before']):
                calls[w]['before'] = row['Before'].replace('* ', '   * ').replace('- ', '   - ')
            if 'After' in row and not pd.isnull(row['After']):
                calls[w]['after'] = row['After'].replace('* ', '   * ').replace('- ', '   - ')
            elif 'Assignments' in row and not pd.isnull(row['Assignments']):
                calls[w]['after'] = row['Assignments'].replace('* ', '   * ').replace('- ', '   - ')
            if 'Icebreaker' in row and not pd.isnull(row['Icebreaker']):
                calls[w]['icebreaker'] = row['Icebreaker']
            calls[w]['content'] = []
            
        elif row['Type'] == 'Presentation':
            talk = {
                'type': 'presentation',
                'duration': 0,
                'title': '',
                'speakers': 'PRESENTER',
                'slides': 'SLIDES'
            }
            if not pd.isnull(row['duration']):
                talk['duration'] = int(int(row['duration'].seconds)/60)
            if not pd.isnull(row['Slides']):
                talk['slides'] = row['Slides']
            if not pd.isnull(row['Confirmed speaker']):
                talk['speakers'] = row['Confirmed speaker']
            if not pd.isnull(row['Title']):
                talk['title'] = row['Title']
            elif 'Tag' in row and not pd.isnull(row['Tag']):
                talk['title'] = row['Tag']
            if 'Before' in row and not pd.isnull(row['Before']):
                talk['before'] = row['Before'].replace('* ', '   * ').replace('- ', '   - ')
            if 'After' in row and not pd.isnull(row['After']):
                talk['after'] = row['After'].replace('* ', '   * ').replace('- ', '   - ')
            calls[w]['content'].append(talk)

        elif row['Type'] == 'Welcome':
            content = {
                'type': 'welcome',
                'duration': 0,
            }
            if not pd.isnull(row['duration']):
                content['duration'] = int(int(row['duration'].seconds)/60)
            if 'Before' in row and not pd.isnull(row['Before']):
                content['before'] = row['Before'].replace('* ', '   * ').replace('- ', '   - ')
            if 'After' in row and not pd.isnull(row['After']):
                content['after'] = row['After'].replace('* ', '   * ').replace('- ', '   - ')
            calls[w]['content'].append(content)

        elif row['Type'] == 'Breakout' or row['Type'] == 'Silent reflections':
            content = {
                'type': 'breakout' if row['Type'] == 'Breakout' else 'silent',
                'duration': 0,
                'title': 'Breakout' if row['Type'] == 'Breakout' else 'Silent reflections',
                'instructions': '' if row['Type'] == 'Breakout' else [],
            }
            if not pd.isnull(row['Title']):
                content['title'] = row['Title']
            if not pd.isnull(row['duration']):
                content['duration'] = int(int(row['duration'].seconds)/60)
            if not pd.isnull(row['People per room']):
                content['people'] = row['People per room']
            else:
                content['people'] = 3
            if 'Instructions' in row and not pd.isnull(row['Instructions']):
                if row['Type'] == 'Breakout':
                    content['instructions'] = row['Instructions'].replace('* ', '   * ').replace('- ', '   - ')
                else:
                    content['instructions'] = row['Instructions'].replace('* ', '').replace('- ', '').split('\n')
            if 'Before' in row and not pd.isnull(row['Before']):
                content['before'] = row['Before'].replace('* ', '   * ').replace('- ', '   - ')
            if 'After' in row and not pd.isnull(row['After']):
                content['after'] = row['After'].replace('* ', '   * ').replace('- ', '   - ')
            calls[w]['content'].append(content)
        

    print("Add time after each content")
    return calls


def add_empty_line(out_f):
    '''
    Add emptry list elements

    :param out_f: file object
    '''
    out_f.write(f"\n")


def add_empty_list_elements(out_f, level = 1):
    '''
    Add emptry list elements

    :param out_f: file object 
    :param level: list level
    '''
    sep = "   "
    out_f.write(f"{ sep * level}*  \n")
    out_f.write(f"{ sep * level}*  \n\n")


def create_templates(calls, output_dp):
    '''
    Create templates for calls in a cohort

    :param schedule_df: dictionary with cohort calls
    :param output_dp: Path object to output directory
    '''
    for w, call in calls.items():
        week_dp = output_dp / Path(f'week-{w}')
        week_dp.mkdir(parents=True, exist_ok=True)
        with open(week_dp / Path(f'week-{w}-template.md'), 'w') as out_f:
            out_f.write(f"# Week {w} - { call['title'] }\n\n")
            
            out_f.write(f"**Date**: { call['date'] }\n\n")
            out_f.write(f"**Time**: { call['time'] } UTC\n\n")
            out_f.write(f"**Duration**: { call['duration'] }\n\n")
            out_f.write(f"**Call lead**: { call['lead'] }\n\n")
            out_f.write(f"**Facilitator**: { call['facilitator'] }\n\n")
            add_empty_line(out_f)
            
            out_f.write(f"## Join the Cohort Room\n\n")
            out_f.write(f"**Join the Zoom call**:\n\n")
            add_empty_line(out_f)
            out_f.write(f"**Are you an Open Seeds participant but can't attend this call? The recording from this call will be updated on YouTube**: [https://www.youtube.com/c/OpenLifeSci/playlists](**https://www.youtube.com/c/OpenLifeSci/playlists**)\n\n")
            add_empty_line(out_f)
            out_f.write(f"**This call is being recorded and transcribed!**\n\n")
            out_f.write(f"   * The video will be available on the YouTube channel ([https://www.youtube.com/c/OpenLifeSci))](https://www.youtube.com/c/OpenLifeSci))) in the next days\n")
            out_f.write(f"   * Turn on your webcam if you don't mind sharing your face (or off if you do!)\n\n")
            add_empty_line(out_f)
            out_f.write(f"**Breakout room**: Speaking and Writing:\n\n")
            out_f.write(f"   * Please edit your Zoom name (click on the three dots on the top right of your video) and add one of the following letters in front of your name:\n")
            out_f.write(f"      * W for written reflection-based exercise in the main room\n")
            out_f.write(f"      * S for Spoken Discussion Breakout Room This will help us assign you to the breakout room with the format of your choice\n")
            out_f.write(f"   * If you are ok with both, please choose one for this week so that the hosts can assign you to a breakout room during the cohort call\n\n")
            add_empty_line(out_f)
            out_f.write(f"## During this week's cohort call, we will:\n\n")
            add_empty_line(out_f)
            out_f.write(f"{ call['learning_objectives'] }\n\n")
            add_empty_line(out_f)
            
            out_f.write(f"## 🌍 Roll call\n\n")
            add_empty_line(out_f)
            out_f.write(f"### Introducing yourself\n\n")
            out_f.write(f"Name / Project / social handles (twitter, GitHub, etc.) / \_emoji mood \_\n\n")
            add_empty_list_elements(out_f)
            add_empty_line(out_f)
            out_f.write(f"### Icebreaker question\n\n")
            out_f.write(f"*{ call['icebreaker'] }*\n\n")
            add_empty_list_elements(out_f)
            add_empty_line(out_f)

            timing = 0
            for content in call['content']:
                if content['type'] == 'welcome':
                    out_f.write(f"## 🗣️ Welcome!\n\n")
                    timing += content['duration']
                    out_f.write(f"[HOST] ({ content['duration'] } min)[⏰ {timing}]\n\n")
                    add_empty_line(out_f)
                    out_f.write(f"**Code of conduct and community participation guidelines** [https://openlifesci.org/code-of-conduct](https://openlifesci.org/code-of-conduct)\n\n")
                    out_f.write(f"   * If you experience or witness unacceptable behaviour, or have any other concerns, please report it by contacting the organisers - Bérénice, Malvika, Yo, Paz and Emmy. (team@openlifesci.org).\n")
                    out_f.write(f"   * To report an issue involving one of the organisers, please email one of the members individually (berenice@we-are-ols.org, malvika@we-are-ols.org, yo@we-are-ols.org, emmy@we-are-ols.org, paz@we-are-ols.org).\n\n")
                    add_empty_line(out_f)
                    out_f.write(f"**This call is being recorded and transcribed!**\n\n")
                    out_f.write(f"   * Please turn your video off if you would prefer to be off video\n")
                    out_f.write(f"   * You can follow the transcriptions following the link on the top of the Zoom screen\n\n")
                    add_empty_line(out_f)
                    out_f.write(f"**Breakout room**: Speaking and Writing:\n\n")
                    out_f.write(f"   * Indicate by editing your name on Zoom and add \n")
                    out_f.write(f"       * W for written reflection-based exercise in based breakout room\n")
                    out_f.write(f"       * S for Spoken Discussion Breakout Room \n")
                    out_f.write(f"   * This will help us assign you to the breakout room with the format of your choice\n")
                    out_f.write(f"   * Even if you are ok with both, please choose one option for this call to help us assign you easily to one group.\n\n")
                    add_empty_line(out_f)
                elif content['type'] == 'presentation':
                    out_f.write(f"## 🖥 { content['title'] }!\n\n")
                    timing += content['duration']
                    out_f.write(f"[HOST] ({ content['duration'] } min)[⏰ {timing}]\n\n")
                    out_f.write(f"**Presenter**: { content['speakers'] }\n\n")
                    out_f.write(f"   * Contact / social: \n")
                    out_f.write(f"   * Slides: { content['slides'] }\n\n")
                    out_f.write(f"**Notes**:\n\n")
                    add_empty_list_elements(out_f)
                    out_f.write(f"**Questions**\n\n")
                    add_empty_list_elements(out_f)
                    add_empty_line(out_f)
                elif content['type'] == 'breakout':
                    out_f.write(f"## 👥 { content['title'] }!\n\n")
                    timing += content['duration']
                    out_f.write(f"[HOST] introduces, [HOST] makes breakouts ({ content['duration']} min) [⏰ {timing}]\n\n")
                    out_f.write(f"{ content['duration']} minutes, ~{ content['people']} ppl per room\n\n")
                    out_f.write(f"### Instructions for the room\n\n")
                    add_empty_line(out_f)
                    out_f.write(f"{ content ['instructions']}\n\n")
                    add_empty_line(out_f)
                    out_f.write(f"### Notes from breakout discussions\n\n")
                    add_empty_line(out_f)
                    out_f.write(f"Breakout Room 1 - Written/Spoken\n\n")
                    out_f.write(f"   * Names\n\n")
                    add_empty_list_elements(out_f, level=2)
                    out_f.write(f"   * Notes\n\n")
                    add_empty_list_elements(out_f, level=2)
                    out_f.write(f"Breakout Room 2 - Written/Spoken\n\n")
                    out_f.write(f"   * Names\n\n")
                    add_empty_list_elements(out_f, level=2)
                    out_f.write(f"   * Notes\n\n")
                    add_empty_list_elements(out_f, level=2)
                    add_empty_line(out_f)
                    out_f.write(f"### **Any insights/thoughts/comments to share from your breakout room?**\n\n")
                    add_empty_list_elements(out_f)
                    add_empty_line(out_f)
                elif content['type'] == 'silent': 
                    out_f.write(f"## 👥 { content['title'] }!\n\n")
                    timing += content['duration']
                    out_f.write(f"### Questions\n\n")
                    add_empty_line(out_f)
                    for q in content ['instructions']:
                        out_f.write(f"{ q }\n\n")
                        add_empty_list_elements(out_f)
                        add_empty_line(out_f)

                if 'after' in content:
                    out_f.write(f"{content['after']}\n\n")
                    add_empty_line(out_f)

            out_f.write(f"## 🗣️ Closing\n\n")
            out_f.write(f"[HOST] (5 min) [⏰ 90]\n\n")
            out_f.write(f"### Assignments\n\n")
            out_f.write(f"{ call['after']}\n\n")
            out_f.write(f"### Have any questions? \n\n")
            out_f.write(f"Add them below. We will respond to these on Slack and also share them via an email\n\n")
            add_empty_list_elements(out_f)
            out_f.write(f"### Feedback about this call:\n\n")
            out_f.write(f"What worked?\n\n")
            add_empty_list_elements(out_f)
            add_empty_line(out_f)
            out_f.write(f"What didn't work?\n\n")
            add_empty_list_elements(out_f)
            add_empty_line(out_f)
            out_f.write(f"What would you change?\n\n")
            add_empty_list_elements(out_f)
            add_empty_line(out_f)
            out_f.write(f"What surprised you?\n\n")
            add_empty_list_elements(out_f)
            add_empty_line(out_f)
            out_f.write(f"**Reference**: Mozilla Open leadership Framework, Open Life Science\n\n")
            out_f.write(f"**Licence**: CC BY 4.0, Open Life Science (OLS), 2023\n\n")



### COMMANDS

def add_projects(cohort, project_df, people_df):
    '''
    Add projects

    :param cohort: cohort id
    :param project_df: dataframe with project details
    :param people_df: dataframe with people details
    '''
    # add people to people.yaml
    added_people = extract_people(people_df)

    # reorder people as a dictionary with key being First name - Last name
    # and value being the people id
    reorder_people = load_reordered_people()

    # load people information from sheet file
    # parse it
    # add information to people dictionary
    project_df = project_df.where(pd.notnull(project_df), None)
    projects = {}
    print('Add new projects')
    for index, row in project_df.iterrows():
        if 'Comment regarding review' in row and row['Comment regarding review'] == 'rejected':
            continue
        print(row['Title'])
        # get title
        p = {
            'name': row['Title'].rstrip().lstrip(),
            'description': '',
            'participants': [],
            'mentors': [],
            'keywords': []
        }
        # extract participants
        p['participants'] = get_people_ids(row['Authors'], reorder_people)
        # extract mentors
        p['mentors'] = get_people_ids(row['Mentor 1'], reorder_people)
        if len(p['mentors']) == 0:
            print('No mentor')
        # extract description
        if row['Project-description'] is not None:
            p['description'] = row['Project-description'].rstrip().lstrip()
        # extract keywords
        if row['Keywords'] is not None:
            p['keywords'] = get_list_from_string(row['Keywords'])
        projects[p['name']] = p
        # 
        if 'Collaboration' in row and row['Collaboration'] is not None:
            p['collaboration'] = get_list_from_string(row['Collaboration'], title=False)
        # 

        print('')

    # transform project dictionary to list
    project_list = [projects[p] for p in projects]

    # dump project dictionary into project file
    dump_projects(project_list, cohort)


def replace_cohort_names(s, cohort):
    '''
    Replace cohort name in string

    :param s: string
    :param cohort: cohort id
    '''
    new_s = s.replace('ols-4', 'ols-%s' % cohort)
    new_s = new_s.replace('OLS-4', 'OLS-%s' % cohort)
    new_s = new_s.replace('4th', '%sth' % cohort)
    new_s = new_s.replace('fourth', '%sth' % cohort)
    return new_s


def write_new_cohort_file(new_cohort_fp, ex_cohort_fp, cohort):
    '''
    Write new cohort files

    :param new_cohort_fp: Path to new cohort file
    :param ex_cohort_fp: Path to example cohort file
    :param cohort: cohort id
    '''
    with ex_cohort_fp.open('r') as ex_cohort_page_f:
        with new_cohort_fp.open('w') as cohort_page_f:
            s = replace_cohort_names(ex_cohort_page_f.read(), cohort)
            cohort_page_f.write(s)


def create_cohort(cohort):
    '''
    Create files for a new cohort

    :param cohort: cohort id
    '''
    # create schedule skeleton
    schedule = create_empty_schedule()
    dump_schedule(schedule, cohort)
    # create project skeleton
    dump_projects([], cohort)
    # create metadata skeleton
    metadata = create_empty_metadata()
    dump_metadata(metadata, cohort)
    # create cohort page
    write_new_cohort_file(
        Path('ols-%s.md' % cohort ),
        Path('ols-4.md'),
        cohort)
    # create cohort folder
    cohort_dp = Path('_ols-%s' % cohort )
    cohort_dp.mkdir(parents=True, exist_ok=True)
    ex_cohort_dp = Path('_ols-4')
    write_new_cohort_file(
        cohort_dp / Path('projects-participants.md'),
        ex_cohort_dp / Path('projects-participants.md'),
        cohort)
    write_new_cohort_file(
        cohort_dp / Path('schedule.md'),
        ex_cohort_dp / Path('schedule.md'),
        cohort)
    write_new_cohort_file(
        cohort_dp / Path('speaker-guide.md'),
        ex_cohort_dp / Path('speaker-guide.md'),
        cohort)


def get_expertises(cohort):
    '''
    Extract expert/mentor expertise from metadata file and order expert/mentor given that information

    :param cohort: cohort id
    '''
    people = load_people()

    metadata = load_metadata(cohort)
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
    dump_metadata(metadata, cohort)


def add_mentors_experts(type, people_df, cohort):
    '''
    Add mentor/experts details to people.yaml, add them to the metadata file for the cohort and extract expertises

    :param type: mentor or expert
    :param people_df: dataframe with people details
    :param cohort: cohort id
    '''
    # add people to people.yaml
    added_people = extract_people(people_df)

    # add mentors/experts to the metadata file
    metadata = load_metadata(cohort)
    print(metadata)
    if type == "mentor":
        metadata['possible-mentors'] = added_people
    else:
        metadata['experts'] = added_people
    print(metadata)
    dump_metadata(metadata, cohort)

    # extract expertises
    get_expertises(cohort)


def update_schedule(cohort, schedule_df):
    '''
    Update schedule from a sheet

    :param cohort: cohort id
    :param schedule_df: data frame with schedule
    '''
    # load people information
    reorder_people = load_reordered_people()
    # load schedule
    schedule = load_schedule(args.cohort)
    # add event information to schedule
    schedule = add_event_information(schedule, schedule_df, reorder_people)
    # dump schedule dictionary into schedule file
    dump_schedule(schedule, args.cohort)


def build_library():
    '''
    Extract talks from all cohort schedule to build library
    '''
    # extract talks
    talks = extract_talks()
    # aggregate talks by tags
    talks_by_tag = aggregate_talks(talks)
    # combine tags by topic to build library
    library = combine_tags(talks_by_tag)
    # write library to file
    fp = Path('_data/library.yaml')
    with fp.open("w") as cat_f:
        cat_f.write("# Library of expert talks in cohort calls\n")
        cat_f.write("---\n")
        yaml.dump(library, cat_f)


def reformate_people():
    '''
    Reformate people information
    '''
    # get people information
    people = load_people()
    # update people information
    for key, value in people.items():
        # get location information
        if 'country' in value:
            country_3, continent = get_country_extra_information(value['country'])
            if country_3 is not None:
                value['country_3'] = country_3
            if continent is not None:
                value['continent'] = continent
        if 'city' in value:
            longitude, latitude = get_city_location(value['city'])
            if longitude is not None:
                value['longitude'] = longitude
                value['latitude'] = latitude
    # save people information
    dump_people(people)


def extract_library(out_fp):
    '''
    Extract library data to a CSV file

    :param out_fp: Path to CSV file
    '''
    library = read_yaml('_data/library.yaml')
    # flatten the library
    flat_library = []
    for tag, t_v in library.items():
        for subtag, st_v in t_v.items():
            for v in st_v['talks']:
                v['tag'] = tag
                v['subtag'] = subtag
                flat_library.append(v)
    # transform to data frame to export it to csv
    library_df = pd.DataFrame(flat_library)
    library_df.to_csv(out_fp)


def extract_full_people_data(out_dp):
    '''
    Extract full people data from website into CSV files

    :param out_dp: Path object to output folder
    '''
    # prepare output folder
    out_dp = Path('_data/artifacts/')
    out_dp.mkdir(parents=True, exist_ok=True)

    # get people information
    people = load_people()
    # format information
    for key, value in people.items():
        # remove some keys
        value.pop('affiliation', None)
        value.pop('bio', None)
        value.pop('orcid', None)
        value.pop('twitter', None)
        value.pop('website', None)
        value.pop('github', None)
        value.pop('title', None)
        value.pop('expertise', None)
        # add space for openseeds cohorts
        for c in Path('_data/openseeds').iterdir():
            cohort = get_cohort_name(c)
            value[f'{cohort}-role'] = []
            value[f'{cohort}-participant'] = []
            value[f'{cohort}-mentor'] = []
            value[f'{cohort}-expert'] = None
            value[f'{cohort}-speaker'] = None
            value[f'{cohort}-facilitator'] =  None
            value[f'{cohort}-organizer'] =  None

    # get cohort and project informations
    projects = []
    for c in Path('_data/openseeds').iterdir():
        cohort = get_cohort_name(c)
        # extract experts, facilitators, organizers from metadata
        metadata = read_yaml(f"{c}/metadata.yaml")
        update_people_info(metadata['experts'], people, cohort, 'expert', 'expert')
        if 'facilitators' in metadata:
            update_people_info(metadata['facilitators'], people, cohort, 'facilitator', 'facilitator')
        update_people_info(metadata['organizers'], people, cohort, 'organizer',  'organizer')
        # extract participants, mentors from projects
        # extract project details
        cohort_projects = read_yaml(f"{c}/projects.yaml")
        for p in cohort_projects:
            # update participant and mentor information
            update_people_info(p['participants'], people, cohort, 'participant', p['name'])
            update_people_info(p['mentors'], people, cohort, 'mentor', p['name'])
            # get project details
            pr = copy.copy(p)
            pr['participants'] = get_people_names(p['participants'], people)
            pr['mentors'] = get_people_names(p['mentors'], people)
            pr['cohort'] = cohort.split("-")[-1]
            pr['keywords'] = p['keywords'] if 'keywords' in p else []
            projects.append(pr)
        # extract speakers from schedule
        schedule = read_yaml(f"{c}/schedule.yaml")
        for w, week in schedule['weeks'].items():
            for c in week['calls']:
                if c['type'] == 'Cohort' and 'resources' in c and c['resources'] is not None:
                    for r in c['resources']:
                        if r['type'] == 'slides' and 'speaker' in r and r['speaker'] is not None:
                            update_people_info([r['speaker']], people, cohort,'speaker', 'speaker')
    
    # format people / project information per cohort
    people_per_cohort = format_people_per_cohort(people, projects)
    
    # export people information to CSV file
    people_df = pd.DataFrame.from_dict(people, orient='index')
    for c in Path('_data/openseeds').iterdir():
        cohort = get_cohort_name(c)
        people_df[f'{cohort}-role'] = people_df[f'{cohort}-role'].apply(lambda x: ', '.join([str(i) for i in x]) if len(x)>0 else None)
        people_df[f'{cohort}-participant'] = people_df[f'{cohort}-participant'].apply(lambda x: ', '.join([str(i) for i in x]) if len(x)>0 else None)
        people_df[f'{cohort}-mentor'] = people_df[f'{cohort}-mentor'].apply(lambda x: ', '.join([str(i) for i in x]) if len(x)>0 else None)
    people_fp = out_dp / Path('people.csv')
    people_df.to_csv(people_fp)

    # export project information to CSV file
    project_df = pd.DataFrame(projects)
    project_df['participants'] = project_df['participants'].apply(lambda x: ', '.join([str(i) for i in x]))
    project_df['mentors'] = project_df['mentors'].apply(lambda x: ', '.join([str(i) for i in x]))
    project_df['keywords'] = project_df['keywords'].apply(lambda x: ', '.join([str(i) for i in x]))
    project_fp = out_dp / Path('projects.csv')
    project_df.to_csv(project_fp)

    # export people per cohort
    people_per_cohort_df = pd.DataFrame(people_per_cohort)
    people_per_cohort_fp = out_dp / Path('people_per_cohort.csv')
    people_per_cohort_df.to_csv(people_per_cohort_fp)

    # export people per role
    export_people_per_roles(people_df, out_dp)


def create_call_template(schedule_df, output_dp):
    '''
    Create call templates for a cohort

    :param schedule_df: data frame with schedule
    :param output_dp: Path object to output directory
    '''
    # load schedule
    schedule_df = prepare_schedule_df(schedule_df)
    # extract calls
    calls = extract_calls(schedule_df)
    # create templates
    create_templates(calls, output_dp)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Interact and prepare OLS website data')
    subparser = parser.add_subparsers(dest='command')
    # Add projects
    addprojects = subparser.add_parser('addprojects', help="Add projects")
    addprojects.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)", required=True)
    projectgroup = addprojects.add_mutually_exclusive_group()
    projectgroup.add_argument('-pf', '--project_fp', help="Path to project sheet file")
    projectgroup.add_argument('-pu', '--project_url', help="URL to project sheet file")
    peoplegroup = addprojects.add_mutually_exclusive_group()
    peoplegroup.add_argument('-df', '--people_fp', help="Path to people details sheet file")
    peoplegroup.add_argument('-du', '--people_url', help="URL to people details sheet file")
    # Create cohort
    createcohort = subparser.add_parser('createcohort', help="Create files for a new cohort")
    createcohort.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)", required=True)
    # Extract people
    extractpeople = subparser.add_parser('extractpeople', help='Extract people details from a sheet and add them to people.yaml')
    group = extractpeople.add_mutually_exclusive_group()
    group.add_argument('-df', '--people_fp', help="Path to people details sheet file")
    group.add_argument('-du', '--people_url', help="URL to people details sheet file")
    # Get expertises
    getexpertises = subparser.add_parser('getexpertises', help='Extract expert/mentor expertise from metadata file and order expert/mentor given that information')
    getexpertises.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)", required=True)
    # Add mentors / experts
    addmentorexperts = subparser.add_parser('addmentorsexperts', help='Add mentor/experts details to people.yaml, add them to the metadata file for the cohort and extract expertises')
    addmentorexperts.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)", required=True)
    addmentorexperts.add_argument('-t', '--type', choices=['mentor', 'expert'], help="Mentors or experts to add", required=True)
    group = addmentorexperts.add_mutually_exclusive_group()
    group.add_argument('-df', '--people_fp', help="Path to people details sheet file")
    group.add_argument('-du', '--people_url', help="URL to people details sheet file")
    # Update schedule
    updateschedule = subparser.add_parser('updateschedule', help='Update schedule from a sheet')
    updateschedule.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)", required=True)
    group = updateschedule.add_mutually_exclusive_group()
    group.add_argument('-sf', '--schedule_fp', help="Path to schedule CSV file")
    group.add_argument('-su', '--schedule_url', help="URL to schedule sheet file")
    # Extract people information of a specific cohort to spreadsheets
    getpeople = subparser.add_parser('getpeople', help='Extract people information of a specific cohort to spreadsheets')
    getpeople.add_argument('-c', '--cohort', help="Cohort id (3, 4, etc)", required=True)
    getpeople.add_argument('-pf', '--participants', help="Path to output sheet with participants details", required=True)
    getpeople.add_argument('-mf', '--mentors', help="Path to output sheet with mentor details", required=True)
    getpeople.add_argument('-ef', '--experts', help="Path to output sheet with expert details", required=True)
    getpeople.add_argument('-sf', '--speakers', help="Path to output sheet with speaker details", required=True)
    getpeople.add_argument('-hf', '--hosts', help="Path to output sheet with call host details", required=True)
    # Extract talks to build library
    buildlibrary = subparser.add_parser('buildlibrary', help='Extract talks to build library')
    # Reformate people data
    reformatepeople = subparser.add_parser('reformatepeople', help='Reformate people information')
    # Extract library data to CSV
    extractlibrary = subparser.add_parser('extractlibrary', help='Extract library data to CSV file stored in _data folder')
    # Extract full people data to CSV
    extractfullpeopledata = subparser.add_parser('extractfullpeopledata', help='Extract full people data (location, participation, etc) into CSV files stored in _data folder')
    # Create cohort call template
    createcalltemplate = subparser.add_parser('createcalltemplate', help='Create cohort call template')
    group = createcalltemplate.add_mutually_exclusive_group()
    group.add_argument('-sf', '--schedule_fp', help="Path to schedule CSV file")
    group.add_argument('-su', '--schedule_url', help="URL to schedule sheet file")
    createcalltemplate.add_argument('-o', '--output', help="Output directory", required=True)
    
    args = parser.parse_args()

    # prepare artifact folder
    artifact_dp.mkdir(parents=True, exist_ok=True)

    if args.command == 'addprojects':
        if args.project_fp:
            project_df = pd.read_csv(Path(args.project_fp))
        else:
            project_df = pd.read_csv(args.project_url)
        if args.people_fp:
            people_df = pd.read_csv(Path(args.people_fp))
        else:
            people_df = pd.read_csv(args.people_url)
        add_projects(args.cohort, project_df, people_df)
    elif args.command == 'createcohort':
        create_cohort(args.cohort)
    elif args.command == 'extractpeople':
        if args.people_url:
            extract_people(pd.read_csv(args.people_url))
        else:
            extract_people(pd.read_csv(Path(args.people_fp)))
    elif args.command == 'getexpertises':
        get_expertises(args.cohort)
    elif args.command == 'addmentorsexperts':
        if args.people_url:
            people_df = pd.read_csv(args.people_url)
        else:
            people_df = pd.read_csv(Path(args.people_fp))
        add_mentors_experts(args.type, people_df, args.cohort)
    elif args.command == 'updateschedule':
        if args.schedule_url:
            schedule_df = pd.read_csv(args.schedule_url)
        else:
            schedule_df = pd.read_csv(Path(args.schedule_fp))
        update_schedule(args.cohort, schedule_df)
    elif args.command == 'getpeople':
        get_people(
            args.cohort,
            Path(args.participants),
            Path(args.mentors),
            Path(args.experts),
            Path(args.speakers),
            Path(args.hosts))
    elif args.command == 'buildlibrary':
        build_library()
    elif args.command == 'reformatepeople':
        reformate_people()
    elif args.command == 'extractlibrary':
        extract_library(artifact_dp / Path('library.csv'))
    elif args.command == 'extractfullpeopledata':
        extract_full_people_data(artifact_dp)
    elif args.command == 'createcalltemplate':
        if args.schedule_url:
            schedule_df = pd.read_csv(args.schedule_url)
        else:
            schedule_df = pd.read_csv(Path(args.schedule_fp))
        create_call_template(schedule_df, Path(args.output))
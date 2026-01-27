#!/usr/bin/env python

import argparse
import copy
from pathlib import Path

import bibtexparser
import pandas as pd
import pycountry
from geopy.geocoders import Nominatim
from jinja2 import (
    Environment,
    FileSystemLoader,
)
from pyzotero import zotero
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as DQS

ROLES = ["role", "participant", "mentor", "expert", "speaker", "facilitator", "organizer"]
CALL_TYPES = ["Mentor-Mentee", "Mentor", "Cohort", "Skill-up", "Q&A", "Cafeteria"]

# copied from https://github.com/jefftune/pycountry-convert/blob/master/pycountry_convert/country_alpha2_to_continent.py
COUNTRY_ALPHA2_TO_CONTINENT = {
    "AB": "Asia",
    "AD": "Europe",
    "AE": "Asia",
    "AF": "Asia",
    "AG": "North America",
    "AI": "North America",
    "AL": "Europe",
    "AM": "Asia",
    "AO": "Africa",
    "AR": "South America",
    "AS": "Oceania",
    "AT": "Europe",
    "AU": "Oceania",
    "AW": "North America",
    "AX": "Europe",
    "AZ": "Asia",
    "BA": "Europe",
    "BB": "North America",
    "BD": "Asia",
    "BE": "Europe",
    "BF": "Africa",
    "BG": "Europe",
    "BH": "Asia",
    "BI": "Africa",
    "BJ": "Africa",
    "BL": "North America",
    "BM": "North America",
    "BN": "Asia",
    "BO": "South America",
    "BQ": "North America",
    "BR": "South America",
    "BS": "North America",
    "BT": "Asia",
    "BV": "Antarctica",
    "BW": "Africa",
    "BY": "Europe",
    "BZ": "North America",
    "CA": "North America",
    "CC": "Asia",
    "CD": "Africa",
    "CF": "Africa",
    "CG": "Africa",
    "CH": "Europe",
    "CI": "Africa",
    "CK": "Oceania",
    "CL": "South America",
    "CM": "Africa",
    "CN": "Asia",
    "CO": "South America",
    "CR": "North America",
    "CU": "North America",
    "CV": "Africa",
    "CW": "North America",
    "CX": "Asia",
    "CY": "Asia",
    "CZ": "Europe",
    "DE": "Europe",
    "DJ": "Africa",
    "DK": "Europe",
    "DM": "North America",
    "DO": "North America",
    "DZ": "Africa",
    "EC": "South America",
    "EE": "Europe",
    "EG": "Africa",
    "ER": "Africa",
    "ES": "Europe",
    "ET": "Africa",
    "FI": "Europe",
    "FJ": "Oceania",
    "FK": "South America",
    "FM": "Oceania",
    "FO": "Europe",
    "FR": "Europe",
    "GA": "Africa",
    "GB": "Europe",
    "GD": "North America",
    "GE": "Asia",
    "GF": "South America",
    "GG": "Europe",
    "GH": "Africa",
    "GI": "Europe",
    "GL": "North America",
    "GM": "Africa",
    "GN": "Africa",
    "GP": "North America",
    "GQ": "Africa",
    "GR": "Europe",
    "GS": "South America",
    "GT": "North America",
    "GU": "Oceania",
    "GW": "Africa",
    "GY": "South America",
    "HK": "Asia",
    "HM": "Antarctica",
    "HN": "North America",
    "HR": "Europe",
    "HT": "North America",
    "HU": "Europe",
    "ID": "Asia",
    "IE": "Europe",
    "IL": "Asia",
    "IM": "Europe",
    "IN": "Asia",
    "IO": "Asia",
    "IQ": "Asia",
    "IR": "Asia",
    "IS": "Europe",
    "IT": "Europe",
    "JE": "Europe",
    "JM": "North America",
    "JO": "Asia",
    "JP": "Asia",
    "KE": "Africa",
    "KG": "Asia",
    "KH": "Asia",
    "KI": "Oceania",
    "KM": "Africa",
    "KN": "North America",
    "KP": "Asia",
    "KR": "Asia",
    "KW": "Asia",
    "KY": "North America",
    "KZ": "Asia",
    "LA": "Asia",
    "LB": "Asia",
    "LC": "North America",
    "LI": "Europe",
    "LK": "Asia",
    "LR": "Africa",
    "LS": "Africa",
    "LT": "Europe",
    "LU": "Europe",
    "LV": "Europe",
    "LY": "Africa",
    "MA": "Africa",
    "MC": "Europe",
    "MD": "Europe",
    "ME": "Europe",
    "MF": "North America",
    "MG": "Africa",
    "MH": "Oceania",
    "MK": "Europe",
    "ML": "Africa",
    "MM": "Asia",
    "MN": "Asia",
    "MO": "Asia",
    "MP": "Oceania",
    "MQ": "North America",
    "MR": "Africa",
    "MS": "North America",
    "MT": "Europe",
    "MU": "Africa",
    "MV": "Asia",
    "MW": "Africa",
    "MX": "North America",
    "MY": "Asia",
    "MZ": "Africa",
    "NA": "Africa",
    "NC": "Oceania",
    "NE": "Africa",
    "NF": "Oceania",
    "NG": "Africa",
    "NI": "North America",
    "NL": "Europe",
    "NO": "Europe",
    "NP": "Asia",
    "NR": "Oceania",
    "NU": "Oceania",
    "NZ": "Oceania",
    "OM": "Asia",
    "OS": "Asia",
    "PA": "North America",
    "PE": "South America",
    "PF": "Oceania",
    "PG": "Oceania",
    "PH": "Asia",
    "PK": "Asia",
    "PL": "Europe",
    "PM": "North America",
    "PR": "North America",
    "PS": "Asia",
    "PT": "Europe",
    "PW": "Oceania",
    "PY": "South America",
    "QA": "Asia",
    "RE": "Africa",
    "RO": "Europe",
    "RS": "Europe",
    "RU": "Europe",
    "RW": "Africa",
    "SA": "Asia",
    "SB": "Oceania",
    "SC": "Africa",
    "SD": "Africa",
    "SE": "Europe",
    "SG": "Asia",
    "SH": "Africa",
    "SI": "Europe",
    "SJ": "Europe",
    "SK": "Europe",
    "SL": "Africa",
    "SM": "Europe",
    "SN": "Africa",
    "SO": "Africa",
    "SR": "South America",
    "SS": "Africa",
    "ST": "Africa",
    "SV": "North America",
    "SY": "Asia",
    "SZ": "Africa",
    "TC": "North America",
    "TD": "Africa",
    "TG": "Africa",
    "TH": "Asia",
    "TJ": "Asia",
    "TK": "Oceania",
    "TM": "Asia",
    "TN": "Africa",
    "TO": "Oceania",
    "TP": "Asia",
    "TR": "Asia",
    "TT": "North America",
    "TV": "Oceania",
    "TW": "Asia",
    "TZ": "Africa",
    "UA": "Europe",
    "UG": "Africa",
    "US": "North America",
    "UY": "South America",
    "UZ": "Asia",
    "VC": "North America",
    "VE": "South America",
    "VG": "North America",
    "VI": "North America",
    "VN": "Asia",
    "VU": "Oceania",
    "WF": "Oceania",
    "WS": "Oceania",
    "XK": "Europe",
    "YE": "Asia",
    "YT": "Africa",
    "ZA": "Africa",
    "ZM": "Africa",
    "ZW": "Africa",
}

optional_info = ["twitter", "website", "orcid", "affiliation", "city", "country", "pronouns", "expertise", "bio"]
to_capitalize_info = ["affiliation", "city", "country"]
people_fp = Path("_data/people.yaml")
geolocator = Nominatim(user_agent="MyApp")
artifact_dp = {
    "all": Path("_data/artifacts/"),
    "openseeds": Path("_data/artifacts/openseeds"),
}
cohort_names = {
    "openseeds": "ols-",
    "nebula": "neb-",
}

### GENERAL METHODS

yaml = YAML()
yaml.preserve_quotes = True


def read_yaml(fp):
    """
    Read content of a YAML file

    :param fp: Path to YAML file
    """
    with open(fp) as f:
        content = yaml.load(f)
    return content


def get_list_from_string(s, title=True):
    """
    Transform a string into a list
    """
    if title:
        return s.rstrip().replace(" and ", ", ").replace("|", ", ").title().split(", ")
    else:
        return s.rstrip().replace(" and ", ", ").replace("|", ", ").split(", ")


### METHODS TO INTERACT WITH people.yaml FILE AND DATA


def load_people():
    """
    Load people.yaml file into a dictionary
    """
    return read_yaml(people_fp)


def load_reordered_people():
    """
    Load people.yaml file and reorder people as a dictionary with
    key being First name - Last name and value being the people id
    """
    people = load_people()
    reorder_people = {}
    for p in people:
        name = f"{people[p]['first-name']} {people[p]['last-name']}"
        reorder_people[name] = p
    return reorder_people


def dump_people(people):
    """
    Dump people dictionary in people file

    :param people: dictionary with people information
    """
    with people_fp.open("w") as people_f:
        people_f.write("# List of people (alphabetical order)\n")
        people_f.write("#\n")
        people_f.write("# Collection names should be equal to github username,\n")
        people_f.write("# if not, add github: false tag and\n")
        people_f.write("# use firstname-lastname as collection name\n")
        people_f.write("#\n")
        people_f.write("# Mandatory: first-name, last-name, country\n")
        people_f.write("---\n")
        yaml.dump(dict(sorted(people.items())), people_f)


def get_people_id(name, people):
    """Extract id in people.yaml from a string with a name

    :param name: string with the name
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    """
    if name not in people:
        print(f"{name} not found in people (get_people_id)")
        return None
    else:
        return people[name]


def get_people_ids(names, people):
    """Extract list of id in people.yaml from a string with names

    :param names: string with names
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    """
    ids = []
    if not pd.isnull(names):
        names = get_list_from_string(names, title=False)
        for n in names:
            id = get_people_id(n.rstrip(), people)
            if id is not None:
                ids.append(id)

    return ids


def get_people_names(p_list, people):
    """Get names of people

    :param p_list: list of people id
    :param people: dictionary with people information
    """
    names = []
    for p in p_list:
        if p is None:
            names.append(None)
        elif p not in people:
            print(f"{p} not found in people (get_people_names)")
            names.append(None)
        else:
            names.append(f"{people[p]['first-name']} {people[p]['last-name']}")
    return names


def extract_expertise(people_list, people):
    """Extract expertise for interesting people
    and return them as a key and a dictionary

    :param people_list: list of username for which extracting expertise
    :param people: dictionary with people information

    :return: dictionary with key being expertise and values
    list of people with expertise
    """
    no_expertise = "No listed expertise"
    p_expertise = {no_expertise: []}
    for p in people_list:
        if "expertise" in people[p]:
            for e in people[p]["expertise"]:
                p_expertise.setdefault(e, [])
                p_expertise[e].append(p)
        else:
            p_expertise[no_expertise].append(p)
    if len(p_expertise[no_expertise]) == 0:
        p_expertise.pop(no_expertise)
    return p_expertise


def get_country_extra_information(country):
    """
    Get country code and continent

    :param country: name of the country
    """
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
    """
    Get city longitude and latitude

    :param city: city name
    """
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
    """Extract people information from a row of the csv
    and return them as a key and a dictionary

    :param row: df row
    :param people: dictionary with people information
    """
    info = {
        "first-name": row["First name"].rstrip().title(),
        "last-name": row["Last name"].rstrip().title(),
        "twitter": row["Twitter"] if "Twitter" in row else None,
        "website": row["Website"] if "Website" in row else None,
        "orcid": row["ORCID"] if "ORCID" in row else None,
        "affiliation": row["Affiliation"] if "Affiliation" in row else None,
        "city": row["City"] if "City" in row else None,
        "country": row["Country"] if "Country" in row else None,
        "pronouns": row["Pronouns"] if "Pronouns" in row else None,
        "expertise": row["Areas of expertise"] if "Areas of expertise" in row else None,
        "bio": row["Bio"] if "Bio" in row else None,
    }
    # get id
    id = row["GitHub"]
    if id is None:
        # check if person exists from first and last name
        for p in people:
            if people[p]["first-name"] == info["first-name"] and people[p]["last-name"] == info["last-name"]:
                id = p
        # create username
        if id is None:
            id = f"{info['first-name']}-{info['last-name']}"
            info["github"] = False
    id = id.replace("https://github.com/", "").rstrip()
    id = id.lower().replace(" ", "-").replace("@", "")
    # format country
    if info["country"] is not None:
        country = info["country"]
        country = country.replace("UK", "United Kingdom")
        country = country.replace("US", "United States")
        country = country.replace("USA", "United States")
        country_3, continent = get_country_extra_information(info["country"])
        if country_3 is not None:
            info["country_3"] = country_3
        if continent is not None:
            info["continent"] = continent
    # format city
    if info["city"] is not None:
        longitude, latitude = get_city_location(info["city"])
        if longitude is not None:
            info["longitude"] = longitude
            info["latitude"] = latitude
    # format ORCID
    if info["orcid"] is not None:
        info["orcid"] = info["orcid"].replace("https://orcid.org/", "")
    # format Twitter
    if info["twitter"] is not None:
        info["twitter"] = info["twitter"].replace("@", "")
    # format expertise
    if info["expertise"] is not None:
        info["expertise"] = get_list_from_string(info["expertise"])
        info["expertise"] = [x.capitalize() for x in info["expertise"]]
    # format website
    if info["website"] is not None and not info["website"].startswith("https"):
        info["website"] = f"https://{info['website']}"
    # check info and remove optional empty info
    info_k = list(info.keys())
    for i in info_k:
        if info[i] is None:
            if id in people and i in people[id]:
                info[i] = people[id][i]
            elif i in optional_info:
                del info[i]
        else:
            if i not in ["expertise", "github", "longitude", "latitude"]:
                info[i] = info[i].rstrip()
            if i in to_capitalize_info:
                info[i] = info[i].title()
    return id, info


def extract_people(df):
    """Extract people information from a sheet and add them to people.yaml

    :param df: Path to information sheet file
    """
    # get people information
    people = load_people()

    # load people information from sheet file
    # parse it
    # add information to people dictionary
    df = df.where(pd.notnull(df), None).rename(
        columns={
            "First Name": "First name",
            "Last Name": "Last name",
        }
    )

    people_l = []
    for _, row in df.iterrows():
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
    s = "\n- ".join(people_l)
    print(f"- {s}")

    # dump people dictionary into people.yaml file
    dump_people(people)

    return people_l


def extract_people_df(ids, people, fp):
    """
    Create a dataframe with people information from a list of ids
    and write in a file

    :param ids: list of people ids
    :param people: people information
    """
    col = [
        "affiliation",
        "bio",
        "city",
        "country",
        "expertise",
        "first-name",
        "github",
        "last-name",
        "orcid",
        "pronouns",
        "twitter",
        "website",
    ]
    info = {}
    for i in ids:
        if i not in people:
            print(f"{i} not in people")
            continue
        info[i] = {}
        if "github" not in people[i]:
            info[i]["github"] = i
        for c in col:
            if c in people[i]:
                if c == "expertise":
                    info[i][c] = ",".join(people[i][c])
                elif c == "bio":
                    info[i][c] = people[i][c].replace("\n", "")
                else:
                    info[i][c] = people[i][c]
            else:
                info[i][c] = None
    df = pd.DataFrame.from_dict(info, orient="index", columns=col)
    df.to_csv(fp, sep="\t")


### METHODS TO INTERACT WITH COHORT SCHEDULE FILES


def create_empty_schedule():
    """
    Create empty schedule
    """
    schedule = {
        "timeline": [
            {
                "date": None,
                "description": "Call for Application opens",
                "details": "See the [guidelines and templates](https://github.com/open-life-science/application-forms)",
            },
            {
                "date": None,
                "description": "Application webinar",
                "type": ["Talk", "Q&A"],
                "notes": None,
                "recording": None,
                "details": "Watch recordings from previous webinars on [**YouTube**](https://www.youtube.com/playlist?list=PL1CvC6Ez54KBsPT0fhPtkHmBaXR4f8Dqt)",
            },
            {
                "date": None,
                "description": "Application Clinic Call",
                "type": ["Q&A"],
                "notes": None,
                "details": "At this call, OLS team will be available to provide help if you have any question related to your application",
            },
            {
                "date": None,
                "description": "Call for applications closed",
            },
            {
                "date": None,
                "description": "Successful applicants announced",
            },
        ],
        "weeks": {},
    }
    for i in range(16):
        schedule["weeks"][f"{(i + 1):02d}"] = {"start": None, "calls": []}
    return schedule


def load_schedule(program, cohort):
    """
    Load cohort schedule

    :param program: Training program
    :param cohort: cohort number
    """
    fp = Path(f"_data/{program}/{cohort}/schedule.yaml")
    schedule = read_yaml(fp)
    for w in schedule["weeks"]:
        for c in schedule["weeks"][w]["calls"]:
            if "content" in c:
                c["content"] = f"{c['content']}"
            if "before" in c:
                c["before"] = f"{c['before']}"
            if "after" in c:
                c["after"] = f"{c['after']}"
    return schedule


def dump_schedule(schedule, program, cohort):
    """
    Dump schedule to YAML file

    :param program: Training program
    :param schedule: dictionary with schedule details
    :param cohort: cohort number
    """
    fp = Path(f"_data/{program}/{cohort}/schedule.yaml")
    with fp.open("w") as schedule_f:
        schedule_f.write(f"# Schedule for the {program} {cohort}\n")
        schedule_f.write("---\n")
        yaml.dump(schedule, schedule_f)


def format_into_list(s):
    """
    Format a Markdown based list into a Python list

    :param s: string representing a list in Markdown
    """
    return s.replace("* ", "- ", 1).replace("- ", "", 1).split("\n- ")


def update_call(call, row, people):
    """
    Update call details

    :param call: dictionary with call details
    :param row: row from dataframe with call details
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    """
    if not pd.isnull(row["date"]):
        call["date"] = row["date"].strftime("%B %d, %Y")
    if not pd.isnull(row["time"]):
        call["time"] = DQS(row["time"].strftime("%H:%M"))
    if not pd.isnull(row["duration"]):
        call["duration"] = f"{format_duration(row['duration'])} min"
    if not pd.isnull(row["Note link"]):
        call["notes"] = row["Note link"]
    if "Title" in row and not pd.isnull(row["Title"]):
        call["title"] = row["Title"]
    if "Module" in row and not pd.isnull(row["Module"]):
        call["title"] = row["Module"]
    if not pd.isnull(row["Recording"]):
        call["recording"] = row["Recording"]
    if "Hosts" in row and not pd.isnull(row["Hosts"]):
        call["hosts"] = get_people_ids(row["Hosts"], people)
    if "Expert" in row and not pd.isnull(row["Expert"]):
        call["expert"] = get_people_ids(row["Expert"], people)
    elif "Call lead" in row and not pd.isnull(row["Call lead"]):
        call["hosts"] = get_people_ids(row["Call lead"], people)
    if "Facilitators" in row and not pd.isnull(row["Facilitators"]):
        call["facilitators"] = get_people_ids(row["Facilitators"], people)
    if "Type" in row and not pd.isnull(row["Type"]):
        call["type"] = row["Type"]
    if "Learning objectives" in row and not pd.isnull(row["Learning objectives"]):
        call["learning_objectives"] = format_into_list(row["Learning objectives"])
    if "Syllabus" in row and not pd.isnull(row["Syllabus"]):
        call["syllabus"] = format_into_list(row["Syllabus"])
    if "Before" in row and not pd.isnull(row["Before"]):
        call["before"] = format_into_list(row["Before"])
    if "After" in row and not pd.isnull(row["After"]):
        call["after"] = format_into_list(row["After"])
    elif "Assignments" in row and not pd.isnull(row["Assignments"]):
        call["after"] = format_into_list(row["Assignments"])
    call["talks"] = []
    return call


def check_same_event(call, row):
    """
    Compare call information from YAML and CSV

    :param call: call information from YAML
    :param row: call information from CSV
    """
    if "type" in call and "type" in row:
        same = call["type"] == row["Type"]
    else:
        same = True
    if "date" in call and pd.notna(row["date"]):
        same = same and (call["date"] == row["date"].strftime("%B %d, %Y"))
    if "title" in call:
        if "Title" in row:
            same = same and (call["title"] == row["Title"])
        elif "Module" in row:
            same = same and (call["title"] == row["Module"])
    return same


def update_talks(talks, row, people):
    """
    Update resource details

    :param talks: dictionary with talk details
    :param row: row from dataframe with talk details
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    """
    if not pd.isnull(row["Slides"]):
        talks["slides"] = row["Slides"]
    if not pd.isnull(row["Confirmed speaker"]):
        names = row["Confirmed speaker"].split(", ")
        talks["speakers"] = [get_people_id(n, people) for n in names]
    if not pd.isnull(row["Title"]):
        talks["title"] = row["Title"]
    if not pd.isnull(row["Recording"]):
        talks["recording"] = row["Recording"]
    if not pd.isnull(row["Tag"]):
        talks["tag"] = row["Tag"]
    return talks


def prepare_schedule_df(schedule_df):
    """
    Prepare data frame with schedule

    :param schedule_df: data frame with schedule
    """
    if "date" in schedule_df.columns and "time" in schedule_df.columns:
        # If standard column names are found
        df = schedule_df.rename(columns={"date": "date", "time": "time", "duration": "duration"}).assign(
            date=lambda x: pd.to_datetime(x["date"], dayfirst=True, errors="coerce"),
            time=lambda x: pd.to_datetime(x["time"], format="%H:%M:%S", errors="coerce"),
            duration=lambda x: pd.to_timedelta(x["duration"]),
        )
    elif "Start Date" in schedule_df.columns and "Start Time" in schedule_df.columns:
        # Handling for programs like openseeds
        df = schedule_df.rename(columns={"Start Date": "date", "Start Time": "time", "Duration": "duration"}).assign(
            date=lambda x: pd.to_datetime(x["date"], dayfirst=True, errors="coerce"),
            time=lambda x: pd.to_datetime(x["time"], format="%H:%M:%S", errors="coerce"),
            duration=lambda x: pd.to_timedelta(x["duration"]),
        )
    elif "Date" in schedule_df.columns and "Start Time (UTC)" in schedule_df.columns:
        # For Nebula-specific column names
        df = schedule_df.rename(
            columns={"Date": "date", "Start Time (UTC)": "time", "End Time (UTC)": "duration"}
        ).assign(
            date=lambda x: pd.to_datetime(x["date"], dayfirst=True, errors="coerce"),
            time=lambda x: x["time"].apply(lambda t: pd.to_datetime(t)),
            duration=lambda x: x["duration"].apply(lambda t: pd.to_datetime(t)),
        )
        df["duration"] = df["duration"] - df["time"]
        df.assign(
            time=lambda x: x["time"].apply(lambda t: t.time()),
        )
    else:
        raise KeyError("The expected columns for date and time are not found in the spreadsheet")
    return df


def add_call(row, week_calls, people):
    """
    Add call

    :param row:
    :param schedule:
    :param people:
    """
    found = False
    for call in week_calls:
        if check_same_event(call, row):
            call = update_call(call, row, people)
            found = True
            last_call = call

    if not found:
        call = update_call({}, row, people)
        week_calls.append(call)
        last_call = call

    return last_call


def add_event_information(schedule, schedule_df, people, program):
    """
    Load event file as data frame and add information into schedule

    :param schedule: dictionary with schedule details
    :param schedule_df: data frame with schedule
    :param people: dictionary with people information (key: name, value: id in people.yaml)
    :param program: Training program
    """
    df = prepare_schedule_df(schedule_df)

    # format date and time columns, add event information
    last_call = {}
    for _, row in df.iterrows():
        w = "{:02d}".format(int(row["Week"]))

        if w not in schedule["weeks"]:
            print(f"Adding week {w} to the schedule")
            schedule["weeks"][w] = {"start": "", "calls": []}

        if program == "openseeds":
            if row["Type"] == "Week":
                if schedule["weeks"][w]["start"] != "":
                    if schedule["weeks"][w]["start"] != row["date"].strftime("%B %d, %Y"):
                        if schedule["weeks"][w]["start"] is None:
                            schedule["weeks"][w]["start"] = row["date"].strftime("%B %d, %Y")
                        else:
                            print(f"Different start date for week {w}")
                            print(f"In schedule file: {schedule['weeks'][w]['start']}")
                            print(f"In event file: {row['date'].strftime('%B %d, %Y')}")
                else:
                    schedule["weeks"][w]["start"] = row["date"].strftime("%B %d, %Y")
            elif row["Type"] in CALL_TYPES:
                last_call = add_call(row, schedule["weeks"][w]["calls"], people)
            elif row["Type"] == "Presentation":
                last_call["talks"].append(update_talks({}, row, people))
        elif program == "nebula":
            add_call(row, schedule["weeks"][w]["calls"], people)

    return schedule


### METHODS TO INTERACT WITH COHORT PROJECT FILES


def dump_projects(projects, program, cohort):
    """
    Dump projects to YAML file

    :param projects: dictionary with project details
    :param program: Training program
    :param cohort: cohort number
    """
    project_fp = Path(f"_data/{program}/{cohort}/projects.yaml")
    with project_fp.open("w") as project_f:
        project_f.write(f"# List of projects for {program} {cohort}\n")
        project_f.write("---\n")
        yaml.dump(projects, project_f)


### METHODS TO INTERACT WITH COHORT METADATA FILE


def create_empty_metadata():
    """
    Create empty metadata
    """
    metadata = {
        "experts": [],
        "organizers": ["bebatut", "malvikasharan", "yochannah"],
        "possible-mentors": [],
    }
    return metadata


def load_metadata(program, cohort):
    """
    Laod metadata from YAML file

    :param program: Training program
    :param cohort: cohort name
    """
    metadata_fp = Path(f"_data/{program}/{cohort}/metadata.yaml")
    # load metadata cohort file into a dictionary
    with open(metadata_fp) as metadata_f:
        metadata = yaml.load(metadata_f)
    return metadata


def dump_metadata(metadata, program, cohort):
    """
    Dump metadata to YAML file

    :param metadata: dictionary with metadata details
    :param program: Training program
    :param cohort: cohort name
    """
    metadata_fp = Path(f"_data/{program}/{cohort}/metadata.yaml")
    with metadata_fp.open("w") as metadata_f:
        metadata_f.write(f"# List of experts, possible mentors and organizers for {program} {cohort}\n")
        metadata_f.write("#\n")
        metadata_f.write("#\n")
        metadata_f.write("# People should be also in people.yaml file and linked using their GitHub username\n")
        metadata_f.write("# Ordering by expertise should be done by running the bin/sort-expertises.py script\n")
        metadata_f.write("---\n")
        yaml.dump(metadata, metadata_f)


def format_duration(duration):
    """
    Format duration in minutes

    :param duration: timedelta
    """
    return int(int(duration.seconds) / 60)


def build_cohort_name(cohort, program):
    """
    Build cohort name

    :param program: Training program
    :param cohort: cohort number
    """
    return f"{cohort_names[program]}{cohort}"


### METHODS TO INTERACT WITH COHORT PAGES


def replace_cohort_names(s, cohort):
    """
    Replace cohort name in string

    :param s: string
    :param cohort: cohort id
    """
    new_s = s.replace("ols-8", cohort)
    new_s = new_s.replace("OLS-8", cohort.upper())
    new_s = new_s.replace("8th", "xth")
    new_s = new_s.replace("eighth", "xth")
    return new_s


def write_new_cohort_file(new_cohort_fp, ex_cohort_fp, cohort):
    """
    Write new cohort files

    :param new_cohort_fp: Path to new cohort file
    :param ex_cohort_fp: Path to example cohort file
    :param cohort: cohort name
    """
    with ex_cohort_fp.open("r") as ex_cohort_page_f:
        with new_cohort_fp.open("w") as cohort_page_f:
            s = replace_cohort_names(ex_cohort_page_f.read(), cohort)
            cohort_page_f.write(s)


### METHODS TO INTERACT WITH COHORT LIBRARY


def extract_talks(program):
    """
    Extract talks from all cohort

    :param program: Training program
    """
    talks = []
    for c in sorted(Path(f"_data/{program}").iterdir()):
        if c.is_file():
            continue
        # get cohort schedule
        cohort = get_cohort_name(c, program)
        schedule = load_schedule(program, cohort)
        # extract talks
        for week in schedule["weeks"].values():
            if "calls" not in week:
                continue
            for call in week["calls"]:
                if "talks" in call:
                    for talk in call["talks"]:
                        if talk == {}:
                            continue
                        talk = dict(talk)
                        if "date" in call:
                            talk["date"] = call["date"]
                        talk["cohort"] = f"{cohort}"
                        if "title" not in talk:
                            talk["title"] = talk["tag"]
                        if "speakers" not in talk:
                            talk["speakers"] = []
                        talks.append(talk)
    return talks


def aggregate_talks(talks):
    """
    Aggregate talks by tag

    :param talks: list with talks
    """
    talks_by_tag = {}
    for talk in talks:
        if "tag" in talk:
            tag = talk["tag"]
            del talk["tag"]
        else:
            tag = "Not tagged"
        talks_by_tag.setdefault(tag, [])
        talks_by_tag[tag].append(dict(talk))
    return talks_by_tag


def combine_tags(talks_by_tag):
    """
    Combine tags by topic to build library

    :param talks_by_tag: dictionary with talks grouped by tags
    """
    # get tag to topic mapping
    tag_topic_mapping = pd.read_csv(
        "https://docs.google.com/spreadsheets/d/1sDJLG8RuoShWUQN78lvx_mghBbGfusdzlb1WwYrCbjk/export?format=csv&gid=0"
    )
    # build library
    library = {}
    for tag, talks in talks_by_tag.items():
        if tag in tag_topic_mapping.Tag.values:
            tag_row = tag_topic_mapping[tag_topic_mapping.Tag == tag]
            topic = tag_row.Topic.tolist()[0]
            description = tag_row.Description.tolist()[0]
        else:
            print(f"No topic found for {tag}")
            continue
        # add talks to library
        library.setdefault(topic, {})
        library[topic][tag] = {"description": description, "talks": talks}
    # reorder library
    ordered_library = {}
    for t in tag_topic_mapping.Topic.unique():
        if t in library:
            ordered_library[t] = library[t]
    return ordered_library


### METHODS TO EXTRACT DATA TO CSV


def update_people_info(p_list, p_dict, cohort, role, value):
    """
    Update people attribute for a cohort

    :param p_list: list of people id to update
    :param p_dict: dictionary with people information
    :param role: status to add
    :param cohort: concerned cohort
    """
    for p in p_list:
        if p is None:
            continue
        if p not in p_dict:
            print(f"{p} not found in people (update_people_info)")
            continue
        p_dict[p][f"{cohort}-role"].append(role)
        if role == "participant" or role == "mentor":
            p_dict[p][f"{cohort}-{role}"].append(value)
        else:
            p_dict[p][f"{cohort}-{role}"] = value


def format_people_per_cohort(people, program):
    """
    Format to get people with their location and cohort and role
    (1 entry per person, per cohort, per role)

    :param people: dictionary with people information
    :param program: Training program
    """
    people_per_cohort = []
    for key, value in people.items():
        info = {"id": key}
        # get localisation information
        for e in ["country", "country_3", "city", "longitude", "latitude"]:
            info[e] = value[e] if e in value else None
        # get cohort participation
        for c in sorted(Path(f"_data/{program}").iterdir()):
            if c.is_file():
                continue
            cohort = get_cohort_name(c, program)
            el = f"{cohort}-role"
            if el in value and len(value[el]) > 0:
                for r in value[el]:
                    t_info = copy.copy(info)
                    t_info["cohort"] = cohort.split("-")[-1]
                    t_info["role"] = r
                    people_per_cohort.append(t_info)
    return people_per_cohort


def export_people_per_roles(people_df, program, out_dp):
    """
    Export people per role

    :param people_df: dataframe with people information
    :param program: Training program
    :param out_dp: Path object to output directory
    """
    people_info_df = people_df[
        ["city", "country", "first-name", "last-name", "pronouns", "country_3", "continent", "longitude", "latitude"]
    ]
    out_dp = out_dp / Path("roles")
    out_dp.mkdir(parents=True, exist_ok=True)
    for r in ROLES:
        role_df = people_df.filter(regex=r)
        role_df = role_df[role_df.filter(regex=r).notna().any(axis=1)]
        for c in sorted(Path(f"_data/{program}").iterdir()):
            if c.is_file():
                continue
            i = get_cohort_name(c, program)
            role_df.rename(columns={f"{i}-{r}": f"{i}"}, inplace=True)
        df = pd.merge(people_info_df, role_df, left_index=True, right_index=True, how="inner")
        fp = Path(out_dp) / Path(f"{r}.csv")
        df.to_csv(fp)


def get_cohort_name(c, program):
    """
    Get cohort name from cohort data path

    :param c: Path object to cohort data
    :param program: Training program
    """
    split_name = c.name.split("-")
    i = split_name[1]
    ext = split_name[-1]
    if i != ext:
        i = f"{i}-{ext}"
    return build_cohort_name(i, program)


### METHODS TO PREPARE CALL TEMPLATES


def extract_calls(schedule_df):
    """
    Extract calls

    :param schedule_df: data frame with schedule
    """
    calls = {}
    for _, row in schedule_df.iterrows():
        w = "{:02d}".format(int(row["Week"]))
        if row["Type"] == "Cohort" or row["Type"] == "Skill-up":
            calls[w] = {
                "date": "",
                "time": "",
                "duration": "",
                "title": "",
                "lead": "",
                "facilitator": "",
                "learning_objectives": "",
                "before": "",
                "after": "",
                "icebreaker": "",
            }
            if not pd.isnull(row["date"]):
                calls[w]["date"] = row["date"].strftime("%B %d, %Y")
            if not pd.isnull(row["time"]):
                calls[w]["time"] = DQS(row["time"].strftime("%H:%M"))
            if not pd.isnull(row["duration"]):
                duration = format_duration(row["duration"])
                calls[w]["duration"] = f"{duration} min"
            if not pd.isnull(row["Title"]):
                calls[w]["title"] = row["Title"]
            if "Hosts" in row and not pd.isnull(row["Hosts"]):
                calls[w]["lead"] = row["Hosts"]
            elif "Call lead" in row and not pd.isnull(row["Call lead"]):
                calls[w]["lead"] = row["Call lead"]
            if "Facilitators" in row and not pd.isnull(row["Facilitators"]):
                calls[w]["facilitator"] = row["Facilitators"]
            if "Learning objectives" in row and not pd.isnull(row["Learning objectives"]):
                calls[w]["learning_objectives"] = (
                    row["Learning objectives"].replace("* ", "   * ").replace("- ", "   - ")
                )
            if "Before" in row and not pd.isnull(row["Before"]):
                calls[w]["before"] = row["Before"].replace("* ", "   * ").replace("- ", "   - ")
            if "After" in row and not pd.isnull(row["After"]):
                calls[w]["after"] = row["After"].replace("* ", "   * ").replace("- ", "   - ")
            elif "Assignments" in row and not pd.isnull(row["Assignments"]):
                calls[w]["after"] = row["Assignments"].replace("* ", "   * ").replace("- ", "   - ")
            if "Icebreaker" in row and not pd.isnull(row["Icebreaker"]):
                calls[w]["icebreaker"] = row["Icebreaker"]
            calls[w]["content"] = []
        elif row["Type"] == "Presentation":
            talk = {"type": "presentation", "duration": 0, "title": "", "speakers": "PRESENTER", "slides": "SLIDES"}
            if not pd.isnull(row["duration"]):
                talk["duration"] = format_duration(row["duration"])
            if not pd.isnull(row["Slides"]):
                talk["slides"] = row["Slides"]
            if not pd.isnull(row["Confirmed speaker"]):
                talk["speakers"] = row["Confirmed speaker"]
            if not pd.isnull(row["Title"]):
                talk["title"] = row["Title"]
            elif "Tag" in row and not pd.isnull(row["Tag"]):
                talk["title"] = row["Tag"]
            if "Before" in row and not pd.isnull(row["Before"]):
                talk["before"] = row["Before"].replace("* ", "   * ").replace("- ", "   - ")
            if "After" in row and not pd.isnull(row["After"]):
                talk["after"] = row["After"].replace("* ", "   * ").replace("- ", "   - ")
            calls[w]["content"].append(talk)
        elif row["Type"] == "Welcome":
            content = {
                "type": "welcome",
                "duration": 0,
            }
            if not pd.isnull(row["duration"]):
                content["duration"] = format_duration(row["duration"])
            if "Before" in row and not pd.isnull(row["Before"]):
                content["before"] = row["Before"].replace("* ", "   * ").replace("- ", "   - ")
            if "After" in row and not pd.isnull(row["After"]):
                content["after"] = row["After"].replace("* ", "   * ").replace("- ", "   - ")
            calls[w]["content"].append(content)
        elif row["Type"] == "Breakout" or row["Type"] == "Silent reflections":
            content = {
                "type": "breakout" if row["Type"] == "Breakout" else "silent",
                "duration": 0,
                "title": "Breakout" if row["Type"] == "Breakout" else "Silent reflections",
                "instructions": "" if row["Type"] == "Breakout" else [],
            }
            if not pd.isnull(row["Title"]):
                content["title"] = row["Title"]
            if not pd.isnull(row["duration"]):
                content["duration"] = format_duration(row["duration"])
            if not pd.isnull(row["People per room"]):
                content["people"] = row["People per room"]
            else:
                content["people"] = 3
            if "Instructions" in row and not pd.isnull(row["Instructions"]):
                if row["Type"] == "Breakout":
                    content["instructions"] = row["Instructions"].replace("* ", "   * ").replace("- ", "   - ")
                else:
                    content["instructions"] = row["Instructions"].replace("* ", "").replace("- ", "").split("\n")
            if "Before" in row and not pd.isnull(row["Before"]):
                content["before"] = row["Before"].replace("* ", "   * ").replace("- ", "   - ")
            if "After" in row and not pd.isnull(row["After"]):
                content["after"] = row["After"].replace("* ", "   * ").replace("- ", "   - ")
            calls[w]["content"].append(content)
        elif row["Type"] == "Panel":
            content = {
                "type": "panel",
                "duration": 0,
            }
            if not pd.isnull(row["duration"]):
                content["duration"] = format_duration(row["duration"])
            calls[w]["content"].append(content)
    return calls


def create_template_env(template_dir):
    """
    Create and return a Jinja2 environment

    :param template_dir: Path to template directory
    """
    return Environment(loader=FileSystemLoader(template_dir))


def render_template(env, template_name, context):
    """
    Render a Jinja2 template with the given context

    :param env: Jinja2 environment
    :param template_name: name of the template file
    :param context: dictionary with template variables
    """
    template = env.get_template(template_name)
    return template.render(**context)


def create_templates(calls, output_dp):
    """
    Create templates for calls in a cohort

    :param calls: dictionary with cohort calls
    :param output_dp: Path object to output directory
    """
    template_dp = Path("bin/templates")
    env = create_template_env(template_dp)
    for w, call in calls.items():
        week_dp = output_dp / Path(f"week-{w}")
        week_dp.mkdir(parents=True, exist_ok=True)
        with open(week_dp / Path(f"week-{w}-template.md"), "w") as out_f:
            context = {
                "week_nb": w,
                "title": call["title"],
                "date": call["date"],
                "time": call["time"],
                "duration": call["duration"],
                "lead": call["lead"],
                "facilitator": call["facilitator"],
                "learning_objectives": call["learning_objectives"],
                "icebreaker": call["icebreaker"],
            }
            out_f.write(render_template(env, "header.md", context))
            timing = 0
            for content in call["content"]:
                if content["type"] == "welcome":
                    timing += content["duration"]
                    context = {
                        "duration": content["duration"],
                        "timing": timing,
                    }
                    out_f.write(render_template(env, "welcome.md", context))
                elif content["type"] == "presentation":
                    timing += content["duration"]
                    context = {
                        "duration": content["duration"],
                        "timing": timing,
                        "title": content["title"],
                        "speaker": content["speakers"],
                        "slides": content["slides"],
                    }
                    out_f.write(render_template(env, "presentation.md", context))
                elif content["type"] == "breakout":
                    timing += content["duration"]
                    context = {
                        "duration": content["duration"],
                        "timing": timing,
                        "title": content["title"],
                        "people": content["people"],
                        "instructions": content["instructions"],
                    }
                    out_f.write(render_template(env, "breakout.md", context))
                elif content["type"] == "silent":
                    timing += content["duration"]
                    questions = ""
                    for q in content["instructions"]:
                        questions += f"* { q }\n\n"
                        questions += "   *\n"
                        questions += "   *\n\n"
                    context = {
                        "duration": content["duration"],
                        "timing": timing,
                        "title": content["title"],
                        "questions": questions,
                    }
                    out_f.write(render_template(env, "silent.md", context))
                elif content["type"] == "panel":
                    timing += content["duration"]
                    context = {
                        "duration": content["duration"],
                        "timing": timing,
                    }
                    out_f.write(render_template(env, "panel.md", context))

                if "after" in content:
                    out_f.write(f"{content['after']}\n\n")
                    out_f.write("\n")

            timing += 5
            context = {
                "assignments": content["after"] if "after" in content else "",
                "year": call["date"].split()[-1] if call["date"] else "",
                "duration": 5,
                "timing": timing,
            }
            out_f.write(render_template(env, "closing.md", context))


### COMMANDS


def add_projects(program, cohort, project_df, people_df):
    """
    Add projects for a cohort

    :param program: Training program
    :param cohort: cohort id
    :param project_df: dataframe with project details
    :param people_df: dataframe with people details
    """
    # add people to people.yaml
    extract_people(people_df)

    # reorder people as a dictionary with key being First name - Last name
    # and value being the people id
    reorder_people = load_reordered_people()

    # load people information from sheet file
    # parse it
    # add information to people dictionary
    project_df = project_df.where(pd.notnull(project_df), None)
    projects = {}
    print("Add new projects")
    for _, row in project_df.iterrows():
        if "Comment regarding review" in row and row["Comment regarding review"] == "rejected":
            continue
        print(row["Title"])
        # get title
        p = {
            "name": row["Title"].rstrip().lstrip(),
            "description": "",
            "participants": [],
            "mentors": [],
            "keywords": [],
        }
        # extract participants
        p["participants"] = get_people_ids(row["Authors"], reorder_people)
        # extract mentors
        p["mentors"] = get_people_ids(row["Mentor 1"], reorder_people)
        if len(p["mentors"]) == 0:
            print("No mentor")
        # extract description
        if row["Project-description"] is not None:
            p["description"] = row["Project-description"].rstrip().lstrip()
        # extract keywords
        if row["Keywords"] is not None:
            p["keywords"] = get_list_from_string(row["Keywords"])
        projects[p["name"]] = p
        #
        if "Collaboration" in row and row["Collaboration"] is not None:
            p["collaboration"] = get_list_from_string(row["Collaboration"], title=False)
        print("")

    # transform project dictionary to list
    project_list = [projects[p] for p in projects]

    # dump project dictionary into project file
    dump_projects(project_list, program, cohort)


def create_cohort(program, cohort):
    """
    Create files for a new cohort

    :param program: Training program
    :param cohort: Cohort name
    """
    program_dp = Path(f"_data/{program}")
    program_dp.mkdir(parents=True, exist_ok=True)
    # create schedule skeleton
    schedule = create_empty_schedule()
    dump_schedule(schedule, program, cohort)
    # create project skeleton
    dump_projects([], program, cohort)
    # create metadata skeleton
    metadata = create_empty_metadata()
    dump_metadata(metadata, program, cohort)
    # create cohort folder
    cohort_dp = program_dp / Path(cohort)
    cohort_dp.mkdir(parents=True, exist_ok=True)
    ex_cohort_dp = Path("_data/openseeds/ols-8")
    write_new_cohort_file(cohort_dp / Path("index.md"), ex_cohort_dp / Path("index.md"), cohort)
    write_new_cohort_file(
        cohort_dp / Path("projects-participants.md"), ex_cohort_dp / Path("projects-participants.md"), cohort
    )
    write_new_cohort_file(cohort_dp / Path("schedule.md"), ex_cohort_dp / Path("schedule.md"), cohort)
    write_new_cohort_file(cohort_dp / Path("speaker-guide.md"), ex_cohort_dp / Path("speaker-guide.md"), cohort)


def get_expertises(program, cohort):
    """
    Extract expert/mentor expertise from metadata file and order expert/mentor given that information

    :param program: Training program
    :param cohort: cohort name
    """
    people = load_people()

    metadata = load_metadata(program, cohort)
    # add expertise:people for possible mentors in a dictionary to metadata
    metadata["possible-mentors-with-expertise"] = extract_expertise(metadata["possible-mentors"], people)
    # add expertise:people for possible mentors in a dictionary to metadata
    metadata["experts-with-expertise"] = extract_expertise(metadata["experts"], people)
    # dump expertise dictionary into metadata file
    dump_metadata(metadata, program, cohort)


def add_mentors_experts(type, people_df, program, cohort):
    """
    Add mentor/experts details to people.yaml, add them to the metadata file for the cohort and extract expertises

    :param type: mentor or expert
    :param people_df: dataframe with people details
    :param program: Training program
    :param cohort: cohort name
    """
    # add people to people.yaml
    added_people = extract_people(people_df)

    # add mentors/experts to the metadata file
    metadata = load_metadata(program, cohort)
    print(metadata)
    if type == "mentor":
        metadata["possible-mentors"] = added_people
    else:
        metadata["experts"] = added_people
    print(metadata)
    dump_metadata(metadata, program, cohort)

    # extract expertises
    get_expertises(program, cohort)


def update_schedule(program, cohort, schedule_df):
    """
    Update schedule from a sheet

    :param program: Training program
    :param cohort: cohort name
    :param schedule_df: data frame with schedule
    """
    # load people information
    reorder_people = load_reordered_people()
    # load schedule
    schedule = load_schedule(program, cohort)
    # add event information to schedule
    schedule = add_event_information(schedule, schedule_df, reorder_people, program)
    # dump schedule dictionary into schedule file
    dump_schedule(schedule, program, cohort)


def get_people(program, cohort, participant_fp, mentor_fp, expert_fp, speaker_fp, host_fp):
    """
    Extract people information of a specific cohort from website to spreadsheets

    :param program: Training program
    :param cohort: cohort id
    :param participant_fp: path to output sheet with participants details
    :param mentor_fp: path to output sheet with mentor details
    :param expert_fp: path to output sheet with expert details
    :param speaker_fp: path to output sheet with speaker details
    :param host_fp: path to output sheet with call host details
    """
    # load people information
    people = load_people()

    # extract participants and mentors
    participants = []
    mentors = []
    # load projects
    fp = Path(f"_data/{program}/{cohort}/projects.yaml")
    projects = read_yaml(fp)
    for p in projects:
        participants += p["participants"]
        mentors += p["mentors"]
    extract_people_df(participants, people, participant_fp)
    extract_people_df(mentors, people, mentor_fp)

    # extract experts and organizers
    # load metadata
    fp = Path(f"_data/{program}/{cohort}/metadata.yaml")
    metadata = read_yaml(fp)
    experts = metadata["experts"]
    extract_people_df(experts, people, expert_fp)

    # extract speakers and call hosts
    speakers = []
    hosts = []
    # load schedule
    schedule = load_schedule(cohort)
    for week in schedule["weeks"].values():
        for call in week["calls"]:
            if call["type"] == "cohort":
                for r in call["talks"]:
                    if "speakers" in r:
                        speakers += r["speakers"]
            if "hosts" in call:
                hosts += call["hosts"]
    extract_people_df(speakers, people, speaker_fp)
    extract_people_df(hosts, people, host_fp)


def build_library(program):
    """
    Extract talks from all cohort schedule to build library

    :param program: Training program
    """
    # extract talks
    talks = extract_talks(program)
    # aggregate talks by tags
    talks_by_tag = aggregate_talks(talks)
    # combine tags by topic to build library
    library = combine_tags(talks_by_tag)
    # write library to file
    fp = Path(f"_data/{program}/library.yaml")
    with fp.open("w") as cat_f:
        cat_f.write("# Library of expert talks in cohort calls\n")
        cat_f.write("---\n")
        yaml.dump(library, cat_f)


def reformate_people():
    """
    Reformate people information
    """
    # get people information
    people = load_people()
    # update people information
    for value in people.values():
        # get location information
        if "country" in value:
            country_3, continent = get_country_extra_information(value["country"])
            if country_3 is not None:
                value["country_3"] = country_3
            if continent is not None:
                value["continent"] = continent
        if "city" in value:
            longitude, latitude = get_city_location(value["city"])
            if longitude is not None:
                value["longitude"] = longitude
                value["latitude"] = latitude
    # save people information
    dump_people(people)


def extract_library(program, out_fp):
    """
    Extract library data to a CSV file

    :param program: Training program
    :param out_fp: Path to CSV file
    """
    # get people information
    people = load_people()
    library = read_yaml(f"_data/{program}/library.yaml")
    # flatten the library
    flat_library = []
    for tag, t_v in library.items():
        for subtag, st_v in t_v.items():
            for v in st_v["talks"]:
                v["tag"] = tag
                v["subtag"] = subtag
                if "speakers" in v:
                    v["speakers"] = get_people_names(v["speakers"], people)
                flat_library.append(v)
    # transform to data frame to export it to csv
    library_df = pd.DataFrame(flat_library)
    library_df["speakers"] = library_df["speakers"].apply(
        lambda x: ", ".join([str(i) for i in x]) if len(x) > 0 else None
    )
    library_df.to_csv(out_fp)


def extract_full_people_data(artifact_dp):
    """
    Extract full people data from website into CSV files

    :param artifact_dp: dictionary with Path object to artifact folders
    """
    # get people information
    people = load_people()

    for value in people.values():
        # remove some keys
        value.pop("affiliation", None)
        value.pop("bio", None)
        value.pop("orcid", None)
        value.pop("twitter", None)
        value.pop("website", None)
        value.pop("github", None)
        value.pop("title", None)
        value.pop("expertise", None)

    # export people information to CSV file
    people_df = pd.DataFrame.from_dict(people, orient="index")
    people_fp = artifact_dp["all"] / Path("people.csv")
    people_df.to_csv(people_fp)

    for program in ["openseeds"]:
        progr_people = copy.copy(people)

        for value in people.values():
            # add space for openseeds cohorts
            for c in sorted(Path(f"_data/{program}").iterdir()):
                if c.is_file():
                    continue
                cohort = get_cohort_name(c, program)
                value[f"{cohort}-role"] = []
                value[f"{cohort}-participant"] = []
                value[f"{cohort}-mentor"] = []
                value[f"{cohort}-expert"] = None
                value[f"{cohort}-speaker"] = None
                value[f"{cohort}-facilitator"] = None
                value[f"{cohort}-organizer"] = None

        # get cohort and project informations
        projects = []
        for c in sorted(Path(f"_data/{program}").iterdir()):
            if c.is_file():
                continue
            cohort = get_cohort_name(c, program)
            # extract experts, facilitators, organizers from metadata
            metadata = read_yaml(f"{c}/metadata.yaml")
            update_people_info(metadata["experts"], progr_people, cohort, "expert", "expert")
            if "facilitators" in metadata:
                update_people_info(metadata["facilitators"], progr_people, cohort, "facilitator", "facilitator")
            update_people_info(metadata["organizers"], progr_people, cohort, "organizer", "organizer")
            # extract participants, mentors from projects
            # extract project details
            cohort_projects = read_yaml(f"{c}/projects.yaml")
            for p in cohort_projects:
                # update participant and mentor information
                update_people_info(p["participants"], progr_people, cohort, "participant", p["name"])
                update_people_info(p["mentors"], progr_people, cohort, "mentor", p["name"])
                # get project details
                pr = copy.copy(p)
                pr["participants"] = get_people_names(p["participants"], progr_people)
                pr["mentors"] = get_people_names(p["mentors"], progr_people)
                pr["cohort"] = cohort.split("-")[-1]
                pr["keywords"] = p["keywords"] if "keywords" in p else []
                projects.append(pr)
            # extract speakers from schedule
            schedule = read_yaml(f"{c}/schedule.yaml")
            for week in schedule["weeks"].values():
                for c in week["calls"]:
                    if c["type"] == "Cohort" and "talks" in c:
                        for t in c["talks"]:
                            if "speakers" in t:
                                update_people_info(t["speakers"], progr_people, cohort, "speaker", "speaker")

        # format people / project information per cohort
        people_per_cohort = format_people_per_cohort(progr_people, program)

        # export people information to CSV file
        people_df = pd.DataFrame.from_dict(progr_people, orient="index")
        for c in sorted(Path(f"_data/{program}").iterdir()):
            if c.is_file():
                continue
            cohort = get_cohort_name(c, program)
            people_df[f"{cohort}-role"] = people_df[f"{cohort}-role"].apply(
                lambda x: ", ".join([str(i) for i in x]) if len(x) > 0 else None
            )
            people_df[f"{cohort}-participant"] = people_df[f"{cohort}-participant"].apply(
                lambda x: ", ".join([str(i) for i in x]) if len(x) > 0 else None
            )
            people_df[f"{cohort}-mentor"] = people_df[f"{cohort}-mentor"].apply(
                lambda x: ", ".join([str(i) for i in x]) if len(x) > 0 else None
            )
        people_fp = artifact_dp[program] / Path("people.csv")
        people_df.to_csv(people_fp)

        # export project information to CSV file
        project_df = pd.DataFrame(projects).fillna("")
        project_df["participants"] = project_df["participants"].apply(lambda x: ", ".join([str(i) for i in x]))
        project_df["mentors"] = project_df["mentors"].apply(lambda x: ", ".join([str(i) for i in x]))
        project_df["keywords"] = project_df["keywords"].apply(lambda x: ", ".join([str(i) for i in x]))
        project_df["collaboration"] = project_df["collaboration"].apply(lambda x: ", ".join([str(i) for i in x]))
        project_fp = artifact_dp[program] / Path("projects.csv")
        project_df.to_csv(project_fp)

        # export people per cohort
        people_per_cohort_df = pd.DataFrame(people_per_cohort)
        people_per_cohort_fp = artifact_dp[program] / Path("people_per_cohort.csv")
        people_per_cohort_df.to_csv(people_per_cohort_fp)

        # export people per role
        export_people_per_roles(people_df, program, artifact_dp[program])


def create_call_template(schedule_df, output_dp):
    """
    Create call templates for a cohort

    :param program: Training program
    :param schedule_df: data frame with schedule
    :param output_dp: Path object to output directory
    """
    # load schedule
    schedule_df = prepare_schedule_df(schedule_df)
    # extract calls
    calls = extract_calls(schedule_df)
    # create templates
    create_templates(calls, output_dp)


def update_bibliography(api):
    """
    Update bibliography file from Zotero group

    :param api: Zotero API key
    """
    zot = zotero.Zotero("5292095", "group", api)
    zot.add_parameters(format="bibtex")
    library = zot.everything(zot.top())
    bibtex_fp = Path("_bibliography/team.bib")
    with bibtex_fp.open("w") as bib_f:
        bibtexparser.dump(library, bib_f)


def create_project_table(program):
    """
    Create interactive table for openseeds projects

    :param program: Training program
    """
    columns = ["", "Name", "Participants", "Keywords", "Mentors", "Description", "Cohort", "Status", "Collaboration"]
    df = (
        pd.read_csv(artifact_dp[program] / Path("projects.csv"), index_col=False)
        .rename(columns=str.title)
        .reindex(columns=columns)
        .fillna("")
    )
    df_str = df.to_html(border=0, table_id="dataframe", classes=["display", "nowrap"], index=False)
    with Path(f"_includes/{program}-project.html").open("w") as project_f:
        project_f.write(df_str)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interact and prepare OLS website data")
    subparser = parser.add_subparsers(dest="command")
    # Add projects
    addprojects = subparser.add_parser("addprojects", help="Add projects")
    addprojects.add_argument("-p", "--program", help="Program (e.g. openseeds)", required=True)
    addprojects.add_argument("-c", "--cohort", help="Cohort id (3, 4, etc)", required=True)
    projectgroup = addprojects.add_mutually_exclusive_group()
    projectgroup.add_argument("-pf", "--project_fp", help="Path to project sheet file")
    projectgroup.add_argument("-pu", "--project_url", help="URL to project sheet file")
    peoplegroup = addprojects.add_mutually_exclusive_group()
    peoplegroup.add_argument("-df", "--people_fp", help="Path to people details sheet file")
    peoplegroup.add_argument("-du", "--people_url", help="URL to people details sheet file")
    # Create cohort
    createcohort = subparser.add_parser("createcohort", help="Create files for a new cohort")
    createcohort.add_argument("-p", "--program", help="Program (e.g. openseeds)", required=True)
    createcohort.add_argument("-c", "--cohort", help="Cohort id (3, 4, etc)", required=True)
    # Extract people
    extractpeople = subparser.add_parser(
        "extractpeople", help="Extract people details from a sheet and add them to people.yaml"
    )
    group = extractpeople.add_mutually_exclusive_group()
    group.add_argument("-df", "--people_fp", help="Path to people details sheet file")
    group.add_argument("-du", "--people_url", help="URL to people details sheet file")
    # Get expertises
    getexpertises = subparser.add_parser(
        "getexpertises",
        help="Extract expert/mentor expertise from metadata file and order expert/mentor given that information",
    )
    getexpertises.add_argument("-p", "--program", help="Program (e.g. openseeds)", required=True)
    getexpertises.add_argument("-c", "--cohort", help="Cohort id (3, 4, etc)", required=True)
    # Add mentors / experts
    addmentorexperts = subparser.add_parser(
        "addmentorsexperts",
        help="Add mentor/experts details to people.yaml, add them to the metadata file for the cohort and extract expertises",
    )
    addmentorexperts.add_argument("-p", "--program", help="Program (e.g. openseeds)", required=True)
    addmentorexperts.add_argument("-c", "--cohort", help="Cohort id (3, 4, etc)", required=True)
    addmentorexperts.add_argument(
        "-t", "--type", choices=["mentor", "expert"], help="Mentors or experts to add", required=True
    )
    group = addmentorexperts.add_mutually_exclusive_group()
    group.add_argument("-df", "--people_fp", help="Path to people details sheet file")
    group.add_argument("-du", "--people_url", help="URL to people details sheet file")
    # Update schedule
    updateschedule = subparser.add_parser("updateschedule", help="Update schedule from a sheet")
    updateschedule.add_argument("-p", "--program", help="Program (e.g. openseeds)", required=True)
    updateschedule.add_argument("-c", "--cohort", help="Cohort id (3, 4, etc)", required=True)
    group = updateschedule.add_mutually_exclusive_group()
    group.add_argument("-sf", "--schedule_fp", help="Path to schedule CSV file")
    group.add_argument("-su", "--schedule_url", help="URL to schedule sheet file")
    # Extract people information of a specific cohort to spreadsheets
    getpeople = subparser.add_parser(
        "getpeople", help="Extract people information of a specific cohort to spreadsheets"
    )
    getpeople.add_argument("-p", "--program", help="Program (e.g. openseeds)", required=True)
    getpeople.add_argument("-c", "--cohort", help="Cohort id (3, 4, etc)", required=True)
    getpeople.add_argument(
        "-pf", "--participants", help="Path to output sheet with participants details", required=True
    )
    getpeople.add_argument("-mf", "--mentors", help="Path to output sheet with mentor details", required=True)
    getpeople.add_argument("-ef", "--experts", help="Path to output sheet with expert details", required=True)
    getpeople.add_argument("-sf", "--speakers", help="Path to output sheet with speaker details", required=True)
    getpeople.add_argument("-hf", "--hosts", help="Path to output sheet with call host details", required=True)
    # Extract talks to build library
    buildlibrary = subparser.add_parser("buildlibrary", help="Extract talks to build library")
    buildlibrary.add_argument("-p", "--program", help="Program (e.g. openseeds)", required=True)
    # Reformate people data
    reformatepeople = subparser.add_parser("reformatepeople", help="Reformate people information")
    # Extract library data to CSV
    extractlibrary = subparser.add_parser(
        "extractlibrary", help="Extract library data to CSV file stored in _data folder"
    )
    extractlibrary.add_argument("-p", "--program", help="Program (e.g. openseeds)", required=True)
    # Extract full people data to CSV
    extractfullpeopledata = subparser.add_parser(
        "extractfullpeopledata",
        help="Extract full people data (location, participation, etc) into CSV files stored in _data folder",
    )
    # Create cohort call template
    createcalltemplate = subparser.add_parser("createcalltemplate", help="Create cohort call template")
    # createcalltemplate.add_argument("-p", "--program", help="Program (e.g. openseeds)", required=True)
    group = createcalltemplate.add_mutually_exclusive_group()
    group.add_argument("-sf", "--schedule_fp", help="Path to schedule CSV file")
    group.add_argument("-su", "--schedule_url", help="URL to schedule sheet file")
    createcalltemplate.add_argument("-o", "--output", help="Output directory", required=True)
    # Update bibliography
    updatebibliography = subparser.add_parser("updatebibliography", help="Get the bibliography file from Zotero")
    updatebibliography.add_argument("-a", "--api", help="Zotero API key", required=True)
    # Create project interactive table
    createprojecttable = subparser.add_parser("createprojecttable", help="Create project interactive table")
    createprojecttable.add_argument("-p", "--program", help="Program (e.g. openseeds)", required=True)

    args = parser.parse_args()

    # prepare artifact folder
    for dp in artifact_dp.values():
        dp.mkdir(parents=True, exist_ok=True)

    if args.command == "addprojects":
        if args.project_fp:
            project_df = pd.read_csv(Path(args.project_fp))
        else:
            project_df = pd.read_csv(args.project_url)
        if args.people_fp:
            people_df = pd.read_csv(Path(args.people_fp))
        else:
            people_df = pd.read_csv(args.people_url)
        add_projects(args.program, build_cohort_name(args.cohort, args.program), project_df, people_df)
    elif args.command == "createcohort":
        create_cohort(args.program, build_cohort_name(args.cohort, args.program))
    elif args.command == "extractpeople":
        if args.people_url:
            extract_people(pd.read_csv(args.people_url))
        else:
            extract_people(pd.read_csv(Path(args.people_fp)))
    elif args.command == "getexpertises":
        get_expertises(args.program, build_cohort_name(args.cohort, args.program))
    elif args.command == "addmentorsexperts":
        if args.people_url:
            people_df = pd.read_csv(args.people_url)
        else:
            people_df = pd.read_csv(Path(args.people_fp))
        add_mentors_experts(args.type, people_df, args.program, build_cohort_name(args.cohort, args.program))
    elif args.command == "updateschedule":
        if args.schedule_url:
            schedule_df = pd.read_csv(args.schedule_url)
        else:
            schedule_df = pd.read_csv(Path(args.schedule_fp))
        try:
            update_schedule(args.program, build_cohort_name(args.cohort, args.program), schedule_df)
        except KeyError as e:
            print(f"Error in {args.program} schedule processing: {e}")
            raise e
    elif args.command == "getpeople":
        get_people(
            args.program,
            build_cohort_name(args.cohort, args.program),
            Path(args.participants),
            Path(args.mentors),
            Path(args.experts),
            Path(args.speakers),
            Path(args.hosts),
        )
    elif args.command == "buildlibrary":
        build_library(args.program)
    elif args.command == "reformatepeople":
        reformate_people()
    elif args.command == "extractlibrary":
        extract_library(args.program, artifact_dp[args.program] / Path("library.csv"))
    elif args.command == "extractfullpeopledata":
        extract_full_people_data(artifact_dp)
    elif args.command == "createcalltemplate":
        if args.schedule_url:
            schedule_df = pd.read_csv(args.schedule_url)
        else:
            schedule_df = pd.read_csv(Path(args.schedule_fp))
        create_call_template(schedule_df, Path(args.output))
    elif args.command == "updatebibliography":
        update_bibliography(args.api)
    elif args.command == "createprojecttable":
        create_project_table(args.program)

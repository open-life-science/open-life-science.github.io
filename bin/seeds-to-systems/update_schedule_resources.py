#!/usr/bin/env python3
"""
Standalone script (not yet integrated into bin/prepare_website_data.py) to read the
Seeds to Systems session-materials spreadsheet and update
_data/seeds-to-systems/schedule.yaml with the real schedule/talks information.

Usage:
    python bin/seeds-to-systems/update_schedule_resources.py --sheet_url "<csv export url>"
"""

import argparse
from pathlib import Path

import pandas as pd
import yaml

SCHEDULE_FP = Path("_data/seeds-to-systems/schedule.yaml")


def slug_session(value):
    """Normalize a spreadsheet Session value to match schedule.yaml's session_number.

    Pure numbers (e.g. "3") become int 3, to match the unquoted ints already in the
    YAML. Anything else (e.g. "Graduation 1") is slugified to "graduation-1".
    """
    value = str(value).strip()
    if value.isdigit():
        return int(value)
    return value.lower().replace(" ", "-")


def split_names(value):
    """Split a "Confirmed speaker" cell into a list of plain names."""
    if pd.isnull(value) or not str(value).strip():
        return []
    return [n.strip() for n in str(value).split(",") if n.strip()]


def clean(value):
    """Return None for empty/NaN cells, else the stripped string."""
    if pd.isnull(value):
        return None
    value = str(value).strip()
    return value or None


def build_sessions(df):
    """Group spreadsheet rows by Session, in first-seen order."""
    sessions = {}
    order = []
    for _, row in df.iterrows():
        session_id = slug_session(row["Session"])
        if session_id not in sessions:
            sessions[session_id] = []
            order.append(session_id)
        sessions[session_id].append(row)
    return order, sessions


def find_call(schedule, session_id):
    """Find the call dict in schedule['weeks'] matching this session_number."""
    for week in schedule["weeks"].values():
        for call in week["calls"]:
            if call.get("session_number") == session_id:
                return call
    return None


def create_call(schedule, session_id, week_value):
    """Create a new call for this session_number under the right week bucket.

    :param week_value: raw "Week" cell from the spreadsheet (e.g. 3 or "3")
    """
    if week_value is None:
        return None
    week_key = f"{int(float(week_value)):02d}"
    if week_key not in schedule["weeks"]:
        schedule["weeks"][week_key] = {"start": None, "calls": []}
    call = {"session_number": session_id}
    schedule["weeks"][week_key]["calls"].append(call)
    return call


def update_schedule(schedule, order, sessions):
    not_found = []
    for session_id in order:
        rows = sessions[session_id]
        main = rows[0]
        call = find_call(schedule, session_id)
        if call is None:
            call = create_call(schedule, session_id, clean(main.get("Week")))
            if call is None:
                not_found.append(session_id)
                continue
        # The sheet is the source of truth: an empty cell clears the field,
        # it doesn't just leave the existing value alone.
        duration = clean(main["Duration"])
        call["date"] = clean(main["Start Date"])
        call["time"] = clean(main["Start Time"])
        call["timezone_link"] = clean(main["Timezone"])
        call["duration"] = f"{int(float(duration))} min" if duration else None
        call["title"] = clean(main["Title"])
        call["notes"] = clean(main["Note link"])
        call["recording"] = clean(main["Recording"])
        call["transcript"] = clean(main["Transcript"])
        call["description"] = clean(main["Description"])

        talks = []
        for row in rows:
            names = split_names(row["Confirmed speaker"])
            slides = clean(row["Slides"])
            other_resources = clean(row["Other resources"])
            if names or slides or other_resources:
                talks.append({"speakers": names, "slides": slides, "other_resources": other_resources})
        call["talks"] = talks

    return not_found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--sheet_url", help="URL to the sheet exported as CSV")
    group.add_argument("--sheet_fp", help="Path to a local CSV file")
    args = parser.parse_args()

    df = pd.read_csv(args.sheet_url if args.sheet_url else args.sheet_fp)

    with SCHEDULE_FP.open() as f:
        schedule = yaml.safe_load(f)

    order, sessions = build_sessions(df)
    not_found = update_schedule(schedule, order, sessions)

    with SCHEDULE_FP.open("w") as f:
        f.write("# Schedule for Seeds to Systems Cohort\n")
        f.write("---\n")
        yaml.dump(schedule, f, sort_keys=False, allow_unicode=True)

    if not_found:
        print(f"Warning: no matching call found in schedule.yaml for session(s): {not_found}")
    print(f"Updated {len(order) - len(not_found)} session(s) in {SCHEDULE_FP}")


if __name__ == "__main__":
    main()

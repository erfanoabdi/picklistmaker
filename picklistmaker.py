#!/usr/bin/env python3
import json

changes_file = open('changes.json', 'r')
changes_data = changes_file.readlines()

projects = set()

for line in changes_data:
    if not line.strip():
        continue

    parsed_line = json.loads(line)
    if "id" in parsed_line:
        projects.add(parsed_line['project'])

changes = dict()
for project in projects:
    change = dict()
    for line in changes_data:
        if not line.strip():
            continue

        parsed_line = json.loads(line)
        if "id" in parsed_line and project == parsed_line['project']:
            change[parsed_line['number']] = parsed_line['subject']

    changes[project] = change

for project in projects:
    print("## Project: {}\n".format(project))

    for change in changes[project]:
        print("repopick {} # {}".format(change, changes[project][change]))

    print("")

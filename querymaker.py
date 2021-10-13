#!/usr/bin/env python3
from lxml import etree
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description='Generate Gerrit query string from manifests, covering organization-forked projects')
parser.add_argument("manifests_path", help="The path containing manifest XMLs")
parser.add_argument("organization", help="The organization name, e.g. LineageOS")
parser.add_argument("branch", help="The branch name, e.g. lineage-19.0")
parser.add_argument("-e", "--exclude", nargs="+", type=int, help="Exclude specified change IDs")
args = parser.parse_args()

query_string = 'status:open branch:' + args.branch + ' '

# Get all XMLs - https://stackoverflow.com/a/18394205/4857393
manifests = list(Path(args.manifests_path).rglob("*.[xX][mM][lL]"))
manifests = [str(p) for p in manifests]

query_string += '('
for m in manifests:
    with open(m, 'r') as f:
        # Remove comments - https://stackoverflow.com/a/10437575/4857393
        tree = etree.parse(f)
        comments = tree.xpath('//comment()')
        for c in comments:
            p = c.getparent()
            p.remove(c)

        # Find organization-forked projects
        projects = tree.xpath('/manifest/project')
        for p in projects:
            if p.attrib['name'].startswith(args.organization) and (
                    'groups' not in p.attrib or (
                    p.attrib['groups'] != 'infra' and p.attrib['groups'] != 'tools')):
                query_string += 'project:' + p.attrib['name'] + ' OR '
query_string = query_string.rstrip(' OR ') + ')'

for id in args.exclude:
    query_string += ' NOT ' + str(id)

print(query_string)

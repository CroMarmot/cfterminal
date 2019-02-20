#!/usr/bin/python3
import argparse
import json
import os.path

CONFIG_FILE = 'config.json'


class argresult():
    def __init__(self):
        self.language = ''
        self.contest = ''


def doparse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--language', '-l', help="The programming language you want to use c++17 / c++11 / Java8")
    parser.add_argument('contest', help="contest id. Example 1114")
    args = parser.parse_args()

    if not os.path.isfile(CONFIG_FILE):
        raise Exception(CONFIG_FILE + " NOT EXIST!")
    with open(CONFIG_FILE) as f:
        cfg_language = json.load(f)['language']

    q = argresult()
    q.contest = args.contest
    q.language = args.language if args.language is not None else cfg_language
    return q


def main():
    r = doparse()
    print(r.contest)
    print(r.language)


if __name__ == '__main__':
    main()

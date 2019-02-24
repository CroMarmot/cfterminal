#!/usr/bin/python3
from urllib.request import urlopen
from html.parser import HTMLParser
import json
import re
import os
import shutil

import languagecontestparse

RED: str = '\033[31m'
GREEN: str = '\033[32m'
BOLD: str = '\033[1m'
RESET: str = '\033[0m'


class CodeforcesProblemParser(HTMLParser):
    def error(self, message):
        print("ERROR in CodeforcesProblemParser", message)

    def __init__(self):
        HTMLParser.__init__(self)
        self.testcase = []  # output

        self.tmp = None
        self.state = False
        self.pre = True
        self.itr = None

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            if attrs == [('class', 'input')]:
                self.tmp = ['', '']
                self.pre = True
                self.itr = 0
            elif attrs == [('class', 'output')]:
                self.pre = True
                self.itr = 1
        elif tag == 'pre' and self.pre:
            self.pre = False
            self.state = True

    def handle_endtag(self, tag):
        if tag == 'br' and self.state and self.tmp is not None and self.tmp[self.itr] != '':
            self.tmp[self.itr] += '\n'
        if tag == 'pre' and self.state:
            self.state = False
            if self.itr == 1:
                self.testcase.append(self.tmp)
                self.tmp = None

    def handle_entityref(self, name):
        if self.state:
            self.tmp[self.itr] += self.unescape(('&%s;' % name)).encode('utf-8')

    def handle_data(self, data):
        if self.state and self.tmp is not None:
            self.tmp[self.itr] += data


class CodeforcesContestParser(HTMLParser):
    def error(self, message):
        print("ERROR in CodeforcesContestParser", message)

    def __init__(self, contest):
        HTMLParser.__init__(self)
        self.contest = contest
        self.start_contest = False
        self.start_problem = False
        self.name = ''
        self.problem_name = ''
        self.problems = []
        self.problem_names = []

    def handle_starttag(self, tag, attrs):
        if self.name == '' and attrs == [('style', 'color: black'), ('href', '/contest/%s' % (self.contest))]:
            self.start_contest = True
        elif tag == 'option':
            if len(attrs) == 1:
                regexp = re.compile(r"'[A-Z]\d?'")  # The attrs will be something like: ('value', 'X')
                string = str(attrs[0])
                search = regexp.search(string)
                if search is not None:
                    self.problems.append(search.group(0).split("'")[-2])
                    self.start_problem = True

    def handle_endtag(self, tag):
        if tag == 'a' and self.start_contest:
            self.start_contest = False
        elif self.start_problem:
            self.problem_names.append(self.problem_name)
            self.problem_name = ''
            self.start_problem = False

    def handle_data(self, data):
        if self.start_contest:
            self.name = data
        elif self.start_problem:
            self.problem_name += data


def parse_problem(contest, problem):
    url = 'http://codeforces.com/contest/%s/problem/%s' % (contest, problem)
    html = urlopen(url).read()
    parser = CodeforcesProblemParser()
    parser.feed(html.decode('utf-8'))
    return parser.testcase


def parse_contest(contest):
    url = 'http://codeforces.com/contest/%s' % (contest)
    html = urlopen(url).read()
    parser = CodeforcesContestParser(contest)
    parser.feed(html.decode('utf-8'))
    return parser

def format_testcase(teststring):
    return teststring.lstrip("\n ").rstrip("\n ")

def main():
    mp_ret = languagecontestparse.doparse()

    contest = mp_ret.contest
    language = mp_ret.language
    with open('language.json') as f:
        language_params = json.load(f)[language]

    # Find contest and problems.
    print('Contest: \t', contest)
    print('Language:\t', language)
    content = parse_contest(contest)
    print(BOLD + GREEN + 'Round name:\t' + content.name + RESET)
    print('%d Problems' % (len(content.problems)))

    # initial
    template_file = language_params["TEMPLATE"]
    suffix = '.' + template_file.split('.')[-1]
    folder = 'dist/%s_%s/' % (contest, language)
    try:
        os.makedirs(folder)
    except:
        print('******* ' + folder + ' GENERATED *******')
    testfile = language_params["TESTFILE"]
    testfile_newname = "test." + testfile.split('.')[-1]
    shutil.copy(testfile, folder + testfile_newname)
    shutil.copy("submit.py", folder + "submit.py")

    # Find problems and test cases.
    # Generate pretest in/out file and template code file
    for index, problem in enumerate(content.problems):
        print('Downloading %s: %s...' % (problem, content.problem_names[index]))
        test_case = parse_problem(contest, problem)
        print("Generate " + problem + suffix)
        shutil.copy(template_file, folder + problem + suffix)
        print('%d sample test(s) found.' % len(test_case))
        for idx, tc in enumerate(test_case):
            with open(folder + problem + '.in.' + str(idx), "w") as inputcase:
                inputcase.write(format_testcase(tc[0]))
                inputcase.close()
            with open(folder + problem + '.out.' + str(idx), "w") as outputcase:
                outputcase.write(format_testcase(tc[1]))
                outputcase.close()
    contest_state = {
        "contestId": mp_ret.contest,
        "language": language_params["value"],
        "suffix": suffix,
    }
    with open(folder + 'state.json', "w") as statejson:
        json.dump(contest_state, statejson)
        statejson.close()

    os.chdir(folder)
    os.system("$SHELL")


if __name__ == '__main__':
    main()

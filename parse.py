#!/usr/bin/python3
from urllib.request import urlopen
from html.parser import HTMLParser
import json
import re
import os
import shutil

import myparse
from color import *

# Problems parser.
class CodeforcesProblemParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.testcase = [] # output

        self.tmp = None
        self.state = False
        self.pre = True
        self.itr = None

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            if attrs == [('class', 'input')]:
                self.tmp = ['','']
                self.pre = True
                self.itr = 0
            elif attrs == [('class', 'output')]:
                self.pre = True
                self.itr = 1
        elif tag == 'pre' and self.pre:
            self.pre = False
            self.state = True

    def handle_endtag(self, tag):
        if tag == 'br' and self.state and self.tmp[self.itr] != '':
            self.tmp[self.itr] += '\n'
        if tag == 'pre' and self.state:
            self.state = False
            if self.itr == 1:
                self.testcase.append(self.tmp)
                self.tmp = None

    def handle_entityref(self, name):
        if self.state :
            self.tmp[self.itr] += self.unescape(('&%s;' % name)).encode('utf-8')

    def handle_data(self, data):
        if self.state :
            self.tmp[self.itr] += data

# Contest parser.
class CodeforcesContestParser(HTMLParser):

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
                regexp = re.compile(r"'[A-Z]'") # The attrs will be something like: ('value', 'X')
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

# Parses each problem page.
def parse_problem(contest, problem):
    url = 'http://codeforces.com/contest/%s/problem/%s' % (contest, problem)
    html = urlopen(url).read()
    parser = CodeforcesProblemParser()
    parser.feed(html.decode('utf-8'))
    return parser.testcase

# Parses the contest page.
def parse_contest(contest):
    url = 'http://codeforces.com/contest/%s' % (contest)
    html = urlopen(url).read()
    parser = CodeforcesContestParser(contest)
    parser.feed(html.decode('utf-8'))
    return parser

# Generates the test script.
def generate_test_script(folder, language, num_tests, problem):

    print("GENERATE ")

# Main function.
def main():
    mp_ret = myparse.doparse()

    contest = mp_ret.contest
    language = mp_ret.language
    with open('language.json') as f:
        language_params = json.load(f)

    # Find contest and problems.
    print ('Contest: \t',contest)
    print ('Language:\t',language)
    content = parse_contest(contest)
    print (BOLD+GREEN_F+'Round name:\t'+content.name+NORM)
    print ('%d Problems' % (len(content.problems)))

    # Find problems and test cases.
    TemplateFile = language_params[language]["TEMPLATE"]
    suffix = '.'+TemplateFile.split('.')[-1]
    folder = 'dist/%s_%s/' % (contest, language)
    try:
        os.makedirs(folder)
    except:
        print('*******'+folder + '*******')
    shutil.copyfile('test.py',folder+'test.py')

    problems = {}
    for index, problem in enumerate(content.problems):
        print ('Downloading %s: %s...' % (problem, content.problem_names[index]))
        testcase = parse_problem(contest, problem)
        print(testcase)
        shutil.copyfile(TemplateFile,folder+problem+suffix)
        print('%d sample test(s) found.' % len(testcase))
        problems[problem] = len(testcase) 
        for idx,tc in enumerate(testcase):
            with open(folder+problem+'.in.'+str(idx),"w") as inputcase:
                inputcase.write(tc[0])
                inputcase.close()
            with open(folder+problem+'.out.'+str(idx),"w") as outputcase:
                outputcase.write(tc[1])
                outputcase.close()
    with open(folder+'pro.json',"w") as projson:
        json.dump(problems,projson)
        projson.close()


if __name__ == '__main__':
    main()

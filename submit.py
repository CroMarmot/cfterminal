#!/usr/bin/python3
import requests
import argparse
import time
import json
from robobrowser import RoboBrowser

RED: str = '\033[31m'
GREEN: str = '\033[32m'
BOLD: str = '\033[1m'
RESET: str = '\033[0m'


def get_latest_verdict(user):
    ret = (requests.get('http://codeforces.com/api/user.status?' +
                        'handle={}&from=1&count=1'.format(user))).json()
    if 'status' not in ret or ret['status'] != 'OK':
        raise ConnectionError('Cannot connect to Codeforces! ' + json.dumps(ret))
    try:
        result = ret['result'][0]
        result_id = result['id']
        result_verdict = result.get('verdict')
        result_time = result['timeConsumedMillis']
        result_memory = result['memoryConsumedBytes']
        passed_test_count = result['passedTestCount']
    except Exception:
        raise ConnectionError('Cannot get latest submission, error')
    return result_id, result_verdict, result_time, result_memory, passed_test_count


def cli():
    # problem_id
    parser = argparse.ArgumentParser()
    parser.add_argument('problem_id', help="problem ID. Example: A")
    parser.add_argument('--username', '-u')
    parser.add_argument('--password', '-p')
    args = parser.parse_args()
    problem_id = args.problem_id

    # username password
    try:
        with open('../../config.json') as f:
            user_config = json.load(f)
        username = args.username if args.username is not None else user_config['username']
        password = args.password if args.password is not None else user_config['password']
    except Exception:
        raise Exception("config.json ERROR")

    # contest_id language_value suffix
    try:
        with open('state.json') as f:
            contest_state = json.load(f)
        contest_id = contest_state['contestId']
        language_value = contest_state['language']
        suffix = contest_state['suffix']
    except Exception:
        raise Exception("state.json ERROR")

    filename = problem_id + suffix
    # get latest submission id, so when submitting should have not equal id
    last_id, _, _, _, _ = get_latest_verdict(username)

    # Browse to Codeforces and Login
    browser = RoboBrowser(parser='html.parser')
    browser.open('http://codeforces.com/enter')
    enter_form = browser.get_form('enterForm')
    enter_form['handleOrEmail'] = username
    enter_form['password'] = password
    browser.submit_form(enter_form)
    try:
        checks = list(map(lambda x: x.getText()[1:].strip(),
                          browser.select('div.caption.titled')))
        if username not in checks:
            print(RED + 'Login Failed.. Wrong password.' + RESET)
            return
    except Exception:
        print(RED + 'Login Failed.. Maybe wrong id/password.' + RESET)
        return

    # select language and submit file
    print(GREEN + '[{0}] login successful! '.format(username) + RESET)
    print('Submitting [{0}] for problem [{1}]'.format(filename, problem_id))
    browser.open('https://codeforces.com/contest/' + contest_id + '/problem/' + problem_id)
    submit_form = browser.get_form(class_='submitForm')
    try:
        submit_form['programTypeId'].value = language_value
    except Exception as e:
        print('language select Error')
        raise(e)
        return
    try:
        submit_form['sourceFile'] = filename
    except Exception:
        print('File {0} not found in current directory'.format(filename))
        return
    browser.submit_form(submit_form)
    # check submit success
    if browser.url[-3:] != '/my':
        print(RED + 'Failed submission, probably you have submit : strthe same file before' + RESET)
        return
    print('[{0}] submitted ...'.format(filename))

    has_started = True
    while True:
        submit_id, verdict, used_time, used_memory, passed_test_count = get_latest_verdict(username)
        if submit_id != last_id:
            if verdict == 'OK':
                print(GREEN + 'OK - Passed {} tests'.format(passed_test_count) + RESET)
            elif verdict == 'TESTING':
                if not has_started:
                    print("Judgment has begun")
                    has_started = True
                time.sleep(0.5)
                continue
            elif verdict is not None:
                print(RED + "{} on test {}".format(verdict, passed_test_count + 1) + RESET)
            print((GREEN if verdict == 'OK' else RED) + '{} MS | {} KB'.format(used_time, used_memory / 1000) + RESET)
            return
        print("Refreshing...")
        time.sleep(0.5)


if __name__ == '__main__':
    cli()

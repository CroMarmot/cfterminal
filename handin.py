import argparse


def getconfig():
    ret = {
            'username':'',
            'password':'',
            'contestId':'',
            'problem':'',
            }
    parser = argparse.ArgumentParser()
    parser.add_argument('problem', help="The problem you want to hanin"
            "A"
            "B"
            "...")
    args = parser.parse_args()
    ret.problem = args.problem
    with open('cfg.json') as cfg:
        ret.username = cfg.username
        ret.password = cfg.password
        ret.contest = cfg.contest
        ret.language = cfg.language

    return ret

# Main function.
def doparse():
    cfg = getconfig()
    return q

def main():
    r = doparse()

if __name__ == '__main__':
    main()

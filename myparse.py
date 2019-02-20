import argparse


class argresult():
    def __init__(self):
        self.language = ''
        self.contest = ''
        self.user = {
            "name": '',
            "password": ''}


# Main function.
def doparse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--language', '-l', default="c++17", help="The programming language you want to use "
                                                  "(c++17)"
                                                  "(c++11)"
                                                  "Java8")
    parser.add_argument('contest', help="")
    args = parser.parse_args()

    q = argresult();
    q.contest = args.contest
    q.language = args.language
    return q


def main():
    r = doparse()
    print(r.contest)
    print(r.language)


if __name__ == '__main__':
    main()

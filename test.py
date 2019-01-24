import argparse
import os
import shutil

def getconfig():
    ret = {
            'problem':'',
            'language':'',
            }
    parser = argparse.ArgumentParser()
    parser.add_argument('problem', help="The problem you want to hanin"
            "A"
            "B"
            "...")
    args = parser.parse_args()
    ret.problem = args.problem
    return ret

def main():
    cfg = getconfig()
    folder = 'tmp_test/'
    os.mkdir(testfolder)
    
    # move to test folder
    shutil.copyfile(cfg.problem+suffix,folder+cfg.problem+suffix)
    # TODO
    # A.in.* 

    # 1. complete
    # g++ -o '' 
    
    # 2. excute && kill
    # which time` -o .....

    # 3. diff & time check
    # diff -- .out

    # 4. clean dir
    os.remove
    # report
    


    r = doparse()

if __name__ == '__main__':
    main()

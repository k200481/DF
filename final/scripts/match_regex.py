import re
import os
import argparse

def parse_file(file_path, rule):
    print(file_path + ':')
    print('--------------------------')
    for line in open(file_path):
        res = rule.search(line)
        if res:
            print(res.string.strip())
    print()
    return

def parse_dir(dir_path, rule):
    for entry_name in os.listdir(dir_path):
        entry_path = dir_path + "/" + entry_name
        if os.path.isdir(entry_path):
            parse_dir(entry_path, rule)
        elif os.path.isfile(entry_path):
            parse_file(entry_path, rule)
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_path')
    parser.add_argument('-r')
    args = parser.parse_args()

    dir_path = args.dir_path
    rule = args.r

    if os.path.isdir(dir_path):
        parse_dir(dir_path, re.compile(rule))
    else:
        print('Not a directory')

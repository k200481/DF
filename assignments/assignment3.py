import yara
import os
import argparse

def parse_file(file_path, rule):
    res = rule.match(file_path)
    if res:
        print(res, ': ' + file_path)
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
    rulefile_path = args.r

    if os.path.isdir(dir_path):
        parse_dir(dir_path, yara.compile(rulefile_path))
    else:
        print('Not a directory')

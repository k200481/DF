import argparse
import sys

def dump(pid):
    print(pid)
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('ps_out_file')
    args = parser.parse_args()

    f = open(args.ps_out_file)
    for line in f.readlines():
        pid = line.split()[1]
        dump(pid)

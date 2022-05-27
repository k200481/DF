import os
import argparse
import hashlib

def item_is_in_list(search_item, list):
    for item in list:
        if item == search_item:
            return True
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('dir1')
    parser.add_argument('dir2')
    args = parser.parse_args()
    dir1 = args.dir1
    dir2 = args.dir2

    list1 = os.listdir(dir1)
    list2 = os.listdir(dir2)

    for filename in list1:
        if not item_is_in_list(filename, list2):
            print(filename + ' is not in ' + dir2)
            continue
        path1 = dir1 + '/' + filename
        path2 = dir2 + '/' + filename
        hash1 = hashlib.md5(open(path1).read().encode()).digest()
        hash2 = hashlib.md5(open(path2).read().encode()).digest()
        if not hash1 == hash2:
            print(path1 + ' =/= ' + path2)

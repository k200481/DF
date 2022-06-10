import os
import json
import argparse

def SCP(ip, port, username, password, dir_list, localpath):
    os.system(f'mkdir {localpath}')
    for dir in dir_list:
        name = dir.split('/')
        name.reverse()
        os.system(f'sshpass -p {password} scp -P {port} -r {username}@{ip}:{dir} {localpath}/')

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('ip')
    parser.add_argument('instance_file')
    parser.add_argument('dest_dir')
    parser.add_argument('-d', nargs="+")
    args = parser.parse_args()

    ip = args.ip
    instances = json.load(open(args.instance_file))
    dir_list = args.d
    dest_dir = args.dest_dir

    for instance in instances:
        print(instance)
        print('---------------------------------')
        port = instances[instance]['ssh']['port']
        username = instances[instance]['ssh']['username']
        password = instances[instance]['ssh']['password']

        SCP(ip, port, username, password, dir_list, f"{dest_dir}/{instance}")

        print('')

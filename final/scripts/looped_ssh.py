#import paramiko
import argparse
import json
import os

#def print_res(command, stdin, stdout, stderr):
#    print(command)
#    print("\tstdout:")
#    for line in stdout.readlines():
#        print('\t\t', line.strip())
#    print('\tstderr:')
#    for line in stderr.readlines():
#        print('\t\t', line.strip())

#def exec_commands(client, command_list):
#    for command in command_list:
#        command = command.strip()
#        if not command:
#            continue
#        stdin, stdout, stderr = client.exec_command(command)
#        print_res(command, stdin, stdout, stderr)

def run_script(ip, port, username, password, script_dir):
    os.system(f'sshpass -p {password} ssh -p {port} {username}@{ip} "mkdir k200481"')
    os.system(f'sshpass -p {password} scp -P {port} -r {script_dir} {username}@{ip}:~/k200481/scripts')
    os.system(f'sshpass -p {password} ssh -p {port} {username}@{ip} "bash ~/k200481/scripts/commands.sh"')
    os.system(f'sshpass -p {password} ssh -p {port} {username}@{ip} "rm -rf ~/k200481/scripts"')

def run_command(ip, port, username, password, command):
    os.system(f'sshpass -p {password} ssh -p {port} {username}@{ip} {command}')

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('ip')
    parser.add_argument('instance_file')
    parser.add_argument('-c')
    parser.add_argument('-s')
    args = parser.parse_args()

    if args.c and args.s:
        print('no')
        exit(0)
    elif not (args.c or args.s):
        print('no2')
        exit(0)

    ip = args.ip
    instances = json.load(open(args.instance_file))

    for instance in instances:
        port = instances[instance]['ssh']['port']
        username = instances[instance]['ssh']['username']
        password = instances[instance]['ssh']['password']

        print(instance)
        print('---------------------------------')
        if args.c:
            run_command(ip, port, username, password, args.c)
        else:
            run_script(ip, port, username, password, args.s)
        print('')

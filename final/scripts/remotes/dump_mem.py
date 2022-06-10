import argparse
import sys

def dump(pid, out_path):
	map_file = open(f"/proc/{pid}/maps", 'r')
	mem_file = open(f"/proc/{pid}/mem", 'rb')
	out_file = open(out_path + f"{pid}", 'wb')
	
	for line in map_file.readlines():
		section = line.split(' ')
		if section[1][0] != 'r':
			continue
		addresses = section[0].split('-')
		start = int(addresses[0],16)
		end = int(addresses[1],16)
		mem_file.seek(int(addresses[0],16))
		try:
			out_file.write(mem_file.read(end-start))
		except OSError:
			print(hex(start), '-', hex(end), '[error,skipped]', file=sys.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('ps_out_file')
    parser.add_argument('dest_dir')
    args = parser.parse_args()

    outpath = args.dest_dir
    if not outpath.endswith('/'):
        outpath += '/'

    f = open(args.ps_out_file)
    for line in f.readlines():
        pid = line.split()[1]
        dump(pid, outpath)

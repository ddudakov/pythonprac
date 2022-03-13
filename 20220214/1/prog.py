import zlib
import sys
from glob import iglob
from os.path import basename, dirname

if len(sys.argv) == 1:
	for dr in iglob('.git/refs/heads/*'):
		print(basename(dr))
else:
	branch = sys.argv[1]
	commit_name = ''
	with open(f'.git/refs/heads/{branch}/') as bp:
		commit_name = bp.readline().strip()
	commit_dir, commit_file = commit_name[:2], commit_name[2:]
	obj = ''
	with open(f'.git/objects/{commit_dir}/{commit_name_file}/', 'rb') as cf:
		obj = zlib.decompress(cf.read())
	print(obj.decode())


import zlib
import sys
from glob import iglob
from os.path import basename, dirname

SHIFT = ' '

def viewtree(tid, shtcnt):
	nametree_dir, nametree_file = tid[:2], tid[2:]
	obj = ''
	with open(f'.git/objects/{nametree_dir}/{nametree_file}/', 'rb') as nf:
		obj = zlib.decompress(nf.read())
	header, _, tail = obj.partition(b'\x00')
	kind, _ = header.split()
	if kind == b'tree':
		while tail:
			treeobj, _, tail = tail.partition(b'\x00')
			_, tname = treeobj.split()
			num, tail = tail[:20], tail[20:]
			num = num.hex()
			print(SHIFT * shtcnt + f"{tname.decode()}")
			viewtree(num, shtcnt + 1)


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
	objtext = obj.decode()
	print(objtext)
	_, objtxt = objtext.split('tree ')

	if 'parent' in objtext:
		nametree, _ = objtxt.split('\nparent')
	else:
		nametree, _ = objtxt.split('\nauthor')
	print('tree', nametree)
	viewtree(nametree, 1)


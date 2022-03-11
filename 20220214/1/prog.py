import sys
import zlib
from glob import iglob
from os.path import basename, dirname


def viewindeep(iden, sh):
    for store in iglob("../../.git/objects/??/*"):
        Id = basename(dirname(store)) + basename(store)
        if Id == iden:
            with open(store, "rb") as f:
                obj = zlib.decompress(f.read())
                header, _, body = obj.partition(b'\x00')
                kind, size = header.split()
            if kind == b'tree':
                tail = body
                while tail:
                    treeobj, _, tail = tail.partition(b'\x00')
                    tmode, tname = treeobj.split()
                    num, tail = tail[:20], tail[20:]
                    print(f"{sh}{tname.decode()} {tmode.decode()} {num.hex()}")
                    viewindeep(num.hex(), sh + "  ")


def commithist(comm):
    LastCommitId = comm
    SHIFT = "  "
    for store in iglob("../../.git/objects/??/*"):
        Id = basename(dirname(store)) + basename(store)
        if Id == LastCommitId:
            with open(store, "rb") as f:
                obj = zlib.decompress(f.read())
                header, _, body = obj.partition(b'\x00')
                kind, size = header.split()
            print(Id, kind.decode())
            out = body.decode().replace('\n', '\n' + SHIFT)
            print(f"{SHIFT}{out}")
            treeId = out.split('\n')[0][5:]
    viewindeep(treeId, SHIFT)
    parentId = out.split('\n')[1][9:]
    commithist(parentId)


mytree = sys.argv
if len(mytree) == 1:
    for store in iglob("../../.git/refs/heads/*"):
        branchname = basename(store)
        print(branchname)
else:
    LastCommitId = 0
    for store in iglob("../../.git/refs/heads/*"):
        Id = basename(store)
        if Id == mytree[1]:
            with open(store, "rb") as f:
                LastCommitId = f.read()
                LastCommitId = LastCommitId[:-1].decode()
            break
    commithist(LastCommitId)

    """for store in iglob("../../.git/objects/??/*"):
        Id = basename(dirname(store)) + basename(store)

        with open(store, "rb") as f:
            obj = zlib.decompress(f.read())
            header, _, body = obj.partition(b'\x00')
            kind, size = header.split()
        print(Id, kind.decode())
        if kind == b'tree':
            tail = body
            while tail:
                treeobj, _, tail = tail.partition(b'\x00')
                tmode, tname = treeobj.split()
                num, tail = tail[:20], tail[20:]
                print(f"{SHIFT}{tname.decode()} {tmode.decode()} {num.hex()}")
        elif kind == b'commit':
            out = body.decode().replace('\n', '\n' + SHIFT)
            print(f"{SHIFT}{out}")"""

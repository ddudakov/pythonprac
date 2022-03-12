import sys
import os
from ipsedixit import Generator

n, source = int(sys.argv[1]), sys.argv[2]
if source != 'caesar' and source != 'tacitus':
	with open(source, encoding = 'utf-8') as f:
		source = f.read()
g = Generator(source)
print(*g.paragraphs(n), sep ='\n\n')

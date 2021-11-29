import sys

br = sys.stdin.buffer.read()
sys.stdout.buffer.write(br.decode().encode('latin1','replace').decode('cp1251').encode('utf-8'))

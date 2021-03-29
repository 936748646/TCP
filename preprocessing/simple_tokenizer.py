import sys

for line in sys.stdin:
    line = line.replace('\n','')
    line = line.replace('\r','')
    tokens = line.split()
    for t in tokens:
        print(t)
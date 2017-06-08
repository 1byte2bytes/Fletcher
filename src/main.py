import sys

import markdown.headers

print(sys.argv[1])

with open(sys.argv[1]) as f:
    for line in f.readlines():
        print(line.strip())

        header = markdown.headers.detectHeader(line)

        if header != None:
            print(header.level)

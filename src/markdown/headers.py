def detectHeader(line):
    isHeader = False
    headerCount = 0
    headerSpacePrefix = False

    if line.startswith("#"):
        isHeader = True
        for letter in line:
            if letter == '#':
                headerCount += 1
            else:
                if letter == ' ':
                    headerSpacePrefix = True
                break
        print(headerCount, headerSpacePrefix)
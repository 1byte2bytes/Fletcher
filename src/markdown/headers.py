class header():
    level = 0
    contentSpacePrefixed = False

def detectHeader(line):
    isHeader = False
    newHeader = header()

    if line.startswith("#"):
        isHeader = True
        for letter in line:
            if letter == '#':
                newHeader.level += 1
            else:
                if letter == ' ':
                    newHeader.contentSpacePrefixed = True
                else:
                    isHeader = False
                break
        print(newHeader.level, newHeader.contentSpacePrefixed)
    
    if isHeader == True:
        return newHeader
    else:
        return None
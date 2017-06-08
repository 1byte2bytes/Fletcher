class header():
    level = 0
    content = ""

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
                    pass
                else:
                    isHeader = False
                break
    
    if isHeader == True:
        return newHeader
    else:
        return None
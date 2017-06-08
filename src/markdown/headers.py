class header():
    def __init__(self):
        self.level = 0
        self.content = ""
        self.rawline = ""

def detectHeader(line):
    isHeader = False
    newHeader = header()
    header.rawline = line

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
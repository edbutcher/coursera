name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

def startsWith():
    sw = raw_input("Enter line prefix to consider: ")
    if len(sw) < 1 : sw = "From"
    return sw

counts = dict()

def makedict()
    for line in handle:
        words = line.split()
        for word in words:
            wrd = word.lowwer()
            counts = counts.get(wrd, 0) + 1
print counts.items()
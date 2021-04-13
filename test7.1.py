fname = input("Enter file name:")
fh = open(fname)
for ls in fh:
    ly = ls.rstrip()
    print(ly.upper())
fname = input("Enter file name:")
fh = open(fname)
time = []
counts={}
lst = []
for line in fh:
    if line.startswith("From "):
        l = line.split()
        t = l[5].split(":")
        time.append(t[0])
for hour in time:
    counts[hour] = counts.get(hour,0)+1
lst = sorted(counts.items())
for hour,count in lst:
    print(hour,count)
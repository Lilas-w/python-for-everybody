# Use the file name mbox-short.txt as the file name
fname = input("Enter file name:")
fh = open(fname)
count = 0
total = 0
for lx in fh:
    if lx.startswith("X-DSPAM-Confidence:"):
        num = lx[20:]
        total = total + float(num)
        count = count + 1
average = total / count
print("Average spam confidence:",average)

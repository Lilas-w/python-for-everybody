file = input("Enter file name:")
fh = open(file)
# lst = list() 
counts = dict()
for line in fh:
    if line.startswith("From "):
        words = line.split()
        mail = words[1]
        counts[mail] = counts.get(mail,0)+1

        # lst.append(mail)
# for mail in counts.keys():
    # counts[mail] = counts.get(mail,0)+1
bigcount = None
bigkey = None
for mail,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigkey = mail
print(bigkey,bigcount) 
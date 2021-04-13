import re
file = open("regex_sum_1116434.txt")
lst = []
for line in file:
    line = line.rstrip()
    num = re.findall("[0-9]+",line)
    for i in num:
        lst.append(i)
value = 0
for n in lst:
    n = int(n)
    value = value + n
print(value)
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
url = address
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
lst = []
for item in results:
    lst.append(int(item.find("count").text))
i = sum(lst,0)
print(i)

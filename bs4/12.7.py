# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input("Enter count:")
position = input("Enter position:")

for i in range(int(count)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    lst = []

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        lst.append(tag.get('href', None))
    url = lst[int(position)-1]
u = url.split(".")
name = u[2].split("_")[-1]
print(name)
from random import choice
from string import digits
from string import ascii_lowercase
from bs4 import BeautifulSoup
import requests
import urllib.request

headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.3'
'(KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.142'}

def gen():
    nd_part = (''.join(choice(ascii_lowercase) for i in range(4) )) # Generating 4 characters for first part of link

    nd_part += (''.join(choice(digits) for i in range(2) )) # Generating 2 digits for last part of link

    url = 'https://prnt.sc/' + nd_part # Assembling into working link



    global page
    page = requests.get(url, headers=headers)

list = [] # Empty list - will be used as storage for URL's

for i in range(111): # range(Amount of links you want to generate)
    gen()
    soup = BeautifulSoup(page.content, 'html.parser')
    for img in soup.findAll('img'):
        temp = img.get('src')
        if 'image.' in temp:
            list.append(temp)
counter = '0' # Counter is a string because I will use it in filename, then change type to int -> increment -> change to string again

for i in list:
    filename = 'photo' + counter + '.jpg'
    tmp = int(counter)
    tmp += 1
    counter = str(tmp)
    r = requests.get(i, allow_redirects = True)
    open(filename, 'wb').write(r.content)

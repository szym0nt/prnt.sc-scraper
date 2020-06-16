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
    nd_part = (''.join(choice(ascii_lowercase) for i in range(4) )) # generowanie 4 liter do linku

    nd_part += (''.join(choice(digits) for i in range(2) )) # generowanie 2 cyfr do linku

    url = 'https://prnt.sc/' + nd_part # tworzenie działającego linku



    global page
    page = requests.get(url, headers=headers)

    #print(url)



#print(soup)
list = [] # pusta lista - magazyn na url z obrazkami

for i in range(111): # range(liczba linkow, ktore maja zostac wygenerowane)
    gen()
    soup = BeautifulSoup(page.content, 'html.parser')
    for img in soup.findAll('img'):
        temp = img.get('src')
        if 'image.' in temp:
            list.append(temp)
#print(list)
counter = '0'

for i in list:
    filename = 'zdjęcie' + counter + '.jpg'
    tmp = int(counter)
    tmp += 1
    counter = str(tmp)
    #print(i)
    r = requests.get(i, allow_redirects = True)
    open(filename, 'wb').write(r.content)

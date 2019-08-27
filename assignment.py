#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 20:23:27 2019

@author: manzars
"""

import requests
from bs4 import BeautifulSoup

url = "http://www.abmec.org.uk/memberslist/about-abmec-members/"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')
divs = soup.findAll('div', {'class': 'row listmembers'})
links = []
for div in divs:
    links.append(div.a.attrs['href'])

file = open('assignment.csv', 'w')
header = 'Company Name, Email, Telephone, Website\n'
file.write(header)
for link in links:
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'lxml')
    tel_p = soup.findAll('p', {'class': 'tel'})
    email_p = soup.findAll('p', {'class': 'email'})
    web_p = soup.findAll('p', {'class': 'web'})
    tel = tel_p[0].text.replace('\xa0', '').lstrip()
    email = email_p[0].a.attrs['href'].replace('mailto:', '')
    web = web_p[0].a.attrs['href']
    name = soup.findAll('h2')[0].text
    print(name)
    file.write(name.replace(',', '') + ', ' + email + ', ' + tel + ', ' + web + '\n')
file.close()
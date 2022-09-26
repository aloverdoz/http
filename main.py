import requests
from bs4 import BeautifulSoup

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
name = []
intelligence = []
for i in soup:
    for ii in i:
        na = str(ii).split('\n')
        for i2 in na:
            if '"name":' in i2:
                na = i2[13:].replace('",', '')
                name.append(na)
            if '"intelligence":' in i2:
                inte = i2[22:].replace(',', '')
                intelligence.append(int(inte))

hero = ['Hulk', 'Captain America', 'Thanos']
hero_intel = []
count = 0
while count < len(hero):
    hero_intel.append(intelligence[name.index(hero[count])])
    count += 1

print(f'Среди Hulk, Captain America и Thanos самым умным является '
      f'{hero[hero_intel.index(max(hero_intel))]} с интелектом {max(hero_intel)}')

vvod = input('Введите имя персонажа чтобы узнать уровень его интелекта:')
for i in name:
    if vvod in i:
        index_char = name.index(i)
        print(f'Интелект персонажа {i} = {intelligence[index_char]}')
        break
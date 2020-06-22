"""
 get first names for boys from :https://www.familyeducation.com/baby-names/popular-names/boys
 get first names for girls from :https://www.familyeducation.com/baby-names/popular-names/girls
 get last names from: https://www.thoughtco.com/most-common-us-surnames-1422656
 generate a random number value between 1 and 10 000
 generate a random birthDate
 set gender based on the name
"""

import random
import requests


from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from Objects_Blueprints import Human

print('Loading...')

male_names = []
female_names = []
last_names = []
birth_dates = []
money100 = []
males = []
females = []
all_humans = []

# creates 100 male names
url = requests.get("https://www.familyeducation.com/baby-names/popular-names/boys").text
male_names_scraper = BeautifulSoup(url, 'lxml')

for name1, name2 in zip(male_names_scraper.find('ul', class_='part1').find_all('a'),
                        male_names_scraper.find('ul', class_='part2').find_all('a')):
    male_names.append(name1.text)
    male_names.append(name2.text)

# creates 100 female names
url = requests.get("https://www.familyeducation.com/baby-names/popular-names/girls").text
female_names_scraper = BeautifulSoup(url, 'lxml')

for name1, name2 in zip(female_names_scraper.find('ul', class_='part1').find_all('a'),
                        female_names_scraper.find('ul', class_='part2').find_all('a')):
    female_names.append(name1.text)
    female_names.append(name2.text)

# creates 100 last names
url = requests.get("https://www.thoughtco.com/most-common-us-surnames-1422656").text
last_names_scraper = BeautifulSoup(url, 'lxml')

for i in last_names_scraper.find('table', class_='mntl-sc-block-table__table').find_all('a'):
    last_names.append(i.text)

# creates 100 money values
for i in range(100):
    money100.append(random.randint(0, 15000))

# creates 100 birthDates
for i in range(100):
    birth_dates.append((datetime(1920, 1, 1) + timedelta(days=random.randrange(0, 100*365))))

# creates 100 male and female values
for i in range(100):
    males.append('Male')
    females.append('Female')

# creates 100 Human objects

female_objects = []
male_objects = []

for first_name, last_name, money, birth, gender in zip(female_names, last_names, money100, birth_dates, females):
    female_objects.append(Human(f'{first_name} {last_name}', money, birth, gender))

for first_name, last_name, money, birth, gender in zip(male_names, last_names, money100, birth_dates, males):
    male_objects.append(Human(f'{first_name} {last_name}', money, birth, gender))

male_objects.extend(female_objects)
all_humans = male_objects
random.shuffle(all_humans)

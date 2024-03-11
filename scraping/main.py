import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import json

base_url = "https://www.gazeta.uz/oz/ramadan"
driver = webdriver.Chrome()


def get_page(url : str) -> str:
    driver.get(url)
    return driver.page_source


def get_cites():
    base_page_html = get_page("https://www.gazeta.uz/oz/ramadan")
    base_page_soup = BeautifulSoup(base_page_html, 'html.parser')

    cites = base_page_soup.find('td', class_ = 'city')

    data = {}
    for city in cites.find_all('option'):
        name = city.get_text()
        url_name = city.get('value')
        data[name] = url_name
    
    return data

def get_date(date : str):
    if re.search('mart', date):
        return f"2024-3-{date[:2]}"
    elif re.search('aprel', date):
        return f"2024-4-{date[:2]}"

def get_week_order(day : int) -> int:
    if day / 7 <= 1:
        return 1
    elif day / 7 <= 2:
        return 2
    elif day / 7 <= 3:
        return 3
    elif day / 7 <= 4:
        return 4
    elif day / 7 <= 5:
        return 5
    

def get_region_data(city : str):
    region_page = get_page(f"https://www.gazeta.uz/oz/ramadan/{city}")
    region_page_soup = BeautifulSoup(region_page, 'html.parser')

    data = {}
    table = region_page_soup.find('table', class_ = 'ramadan-month')
    for row in table.find_all('tr'):
        row_data = [box.get_text() for box in row.find_all('td')]
        if row_data:
            n = int(row_data[0])
            row_data[1] = get_date(row_data[1])
            row_data[1] = row_data[1].strip()
            week_order = get_week_order(n)
        
            data[int(row_data[0])] = {'week_order' : week_order, 'date' : row_data[1], 'week' : row_data[2], 'start' : row_data[3], 'end' : row_data[4]}
        

    return data


cites = get_cites()
meta_data = {}
for city, key in cites.items():
    print(city)
    city_data = get_region_data(key)
    meta_data[city] = city_data
    

with open("data/ramadan.json", 'w') as file:
    json.dump(meta_data, file)

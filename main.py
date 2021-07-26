import json
import time
import telebot
import requests

from bs4 import BeautifulSoup

with open("config.json") as file:
    config = json.load(file)
bot = telebot.TeleBott(config['API_TOKEN'])
page = 1

while true
    domain =
    responce =
    all_image = BeautifulSoup(responce, 'lxml').find_all('div', class='position')

    for image int all_image:
        stroage_url = image.find('a').get('href')

        if storage_url != '#':
            image = requests.get(stroge_url).text
            result_link
            image_bytes = requests.get(f"https://{result_link}").content

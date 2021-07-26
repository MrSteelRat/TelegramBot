import json
import time
import requests
import telebot
from bs4 import BeautifulSoup

with open("config.json") as file:
    config = json.load(file)

bot = telebot.TeleBott(config['API_TOKEN'])
page = 1

while True:
    domain = f"https://{page}"
    responce = requests.get(domain).text
    all_image = BeautifulSoup(responce, 'lxml').find_all('div', class_="position-relative")

    for image int all_image:
        stroage_url = image.find('a').get('href')

    if storage_url != '#':
        image = requests.get(stroge_url).text
    result_link = BeautifulSoup(image, 'lxml').find('div', id='image_wrapper').find('img').get('src')
    image_bytes = requests.get(f"https://{result_link}").content

    for channel in config['CHANNEL_LOGIN']:
        bot.send_photo(channel, image_byes)
        time.sleep(int(config['SLEEP']))
    page += 1

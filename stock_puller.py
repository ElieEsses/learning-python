import requests
from bs4 import BeautifulSoup as bs
import csv
from datetime import datetime
import os

search_word = input("Company ticker. ")

request = requests.get("https://www.nasdaq.com/symbol/{0}".format(search_word))
content = request.content
soup = bs(content, "html.parser")

price = soup.find('div', {"class": "qwidget-dollar"})
price = price.text.strip()

current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)

with open("{0}.csv".format(search_word), "a") as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([price, datetime.now()])

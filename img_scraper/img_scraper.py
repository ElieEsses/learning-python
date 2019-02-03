import requests
from bs4 import BeautifulSoup as bs
import os


# asks user for search information
search = input("What image are you looking for? ")

# create image folder with name of search

current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)

if os.path.exists(search):
    print("Sorry, but that folder already exists.")

else:
    os.makedirs(search)
    os.chdir(search)

    # site with imgs' url
    url = "https://www.pexels.com/search/" + search + "/"

    # gets page's content
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')

    # locate all elements with "img" tag
    image_tags = soup.findAll('img')

    # adds images
    x = 0

    for image in image_tags:
        try:
            url = image['src']
            response = requests.get(url)
            if response.status_code == 200:
                with open(search + "-" + str(x) + ".jpg", "wb") as f:
                    f.write(requests.get(url).content)
                    f.close()
                    x += 1
        except:
            pass
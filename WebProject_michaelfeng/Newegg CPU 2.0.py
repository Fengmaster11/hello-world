import requests
import datetime
from bs4 import BeautifulSoup
import json

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

# Parse NewEgg CPU
# 'position' marks the beginning of the grid where all the products are found on the page
# 'product' marks the position of the grid in where a product is found
# All other data is found in its relationship to 'position'
# Scrape Newegg CPUs with requests
url = 'https://www.newegg.com/Processors-Desktops/SubCategory/ID-343'
page = requests.get(url)

# Prepare for parsing NeweggCPU with BeautifulSoup
soup = BeautifulSoup(page.content, 'lxml')

for position in soup.find_all('div', class_='item-container'):
    #if(position.find('li', class_="price-current").find('strong') != None):
    if (position.get('class')[1] != 'is-feature-item'):
        productLink = position.find('a').get('href')
        productPage = requests.get(productLink)
        productSoup = BeautifulSoup(productPage.content, 'lxml')
        productPosition = productSoup.find('div', class_= "objOption")
        brand = productPosition.find('img').get('alt')

        response.append({"Brand": brand})


# Write response to JSON file
postingsFile = today + 'NeweggCPU_2.json'

#Write response to JSON file in another location
with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)
outfile.close()
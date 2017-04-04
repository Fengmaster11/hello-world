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
url = 'https://www.newegg.com/Product/Product.aspx?Item=N82E16819117726'
page = requests.get(url)

# Prepare for parsing NeweggCPU with BeautifulSoup
soup = BeautifulSoup(page.content, 'lxml')


#position = soup.find('div', id="Specs")
#productModel = position.find('h3', class_="specTitle")
#print(productModel)
for position in soup.find_all('d1'):
    #if(position.dt.a.string == "Operating Frequency"):
    print(position)
    #if(position.find('dt').string == "Brand"):
     #   brand = position.find('dd')
      #  print(brand)

#for modelDetails in soup.find_all('d1'):
    #brand = productModel.get('dt')
    #print(brand)
#for position in soup.find('div', id="Specs"):

    #if position.string == "Operating Frequency":
     #   speed = position.get('dd')
      #  print(speed)
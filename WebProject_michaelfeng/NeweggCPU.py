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

i = 1
parse = True

while parse == True and i < 6:
    page = requests.get(url)
    # Prepare for parsing NeweggCPU with BeautifulSoup
    soup = BeautifulSoup(page.content, 'lxml')
    for position in soup.find_all('div', class_='item-container'):
        #if conditional to scrape the product that is not repeated as the feature item on every page
        if position.get('class')[1] != 'is-feature-item':
            if position.find('li', class_="price-current").find('strong'):
                # price of the CPU by combining the strings of the strong and sup
                dollarPrice = position.find('li', class_="price-current").find('strong').string
                centPrice = position.find('li', class_="price-current").find('sup').string
                price = "$" + dollarPrice + centPrice
            else:
                price = "Not Included"
            #if conditional to provide price if it is available
            if position.find('span', class_="item-rating-num"):
                numRating = position.find('span', class_="item-rating-num").string.split('(')[1].split(')')[0]
                avgRatingPre = position.find('div', class_="item-branding")
                avgRatingString = avgRatingPre.find('i').get('class')[1]
                avgRating = avgRatingString.split('-')[1]
            else:
                numRating = "Not Included"
                avgRating = "Not Included"
            #if conditional to find the number of offers if it is available
            if position.find('li', class_="price-current").find('a', class_="price-current-num") != None:
                numOffersStr = position.find('li', class_="price-current").find('a', class_="price-current-num").string
                numOffersPre = numOffersStr.split('(')[1]
                numOffers = numOffersPre.split(' O')[0]
            else:
                numOffers = "Not Included"
            #product name
            productName = position.find('img').get('alt')
            # variables to split the processor speed
            performanceFirstSplit = productName.split(' GHz ')[0]
            performanceArray = performanceFirstSplit.split(' ')
            performance = performanceArray[len(performanceArray) - 1] + " GHz"
            #brand of the CPU
            brand = productName.split(' ')[0]
            #product link by using findall and getting the 2nd link
            productPosition = position.find('div', class_="item-info")
            #productArray = productPosition.find_all('a')
            #productLink = "https:" + productArray[1].get('href')
            productLink = position.find('a').get('href')
            #shipping
            shippingLine = position.find('li', class_="price-ship").string.split(' S')[0]
            shippingTrim = shippingLine.replace(' ', '')
            shipping = shippingTrim.split('\n')[1] + " Shipping"
            response.append({'CPU Name': productName, 'Performance': performance, 'Price': price, 'Brand': brand, 'Link': productLink,
                         'Shipping': shipping, 'Number of Ratings': numRating, 'Average Rating': avgRating, 'Number of Offers': numOffers})
    parse = False
    if (soup.find('button', title="Next")):
        i += 1
        url = "https://www.newegg.com/Processors-Desktops/SubCategory/ID-343/Page-" + str(i) + "?PageSize=36&order=BESTMATCH"
        parse = True
#comet

# Write response to JSON file
postingsFile = today + '.NeweggCPU.json'

#Write response to JSON file in another location
with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)
outfile.close()
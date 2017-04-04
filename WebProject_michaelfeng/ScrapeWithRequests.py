import requests
import datetime


today = str(datetime.datetime.now().date())

sites = {'Newegg CPUs': 'https://www.newegg.com/Processors-Desktops/SubCategory/ID-343',
         'Newegg Mobo':'https://www.newegg.com/Motherboards/Category/ID-20',
         'Newegg PSU': 'https://www.newegg.com/Power-Supplies/Category/ID-32',
         'Newegg HD':'https://www.newegg.com/Hard-Drives/Category/ID-15',
         'Newegg SSD':'https://www.newegg.com/SSDs/Category/ID-119',
         'i7 processor': 'https://www.newegg.com/Product/Product.aspx?Item=N82E16819117726'}

for name, link in sites.items():
    response = requests.get(link)
    html = response.content

    fileName = today + '.' + name + '.html'
    outfile = open(fileName, "wb")
    outfile.write(html)
    outfile.close()
from scraper import Scraper
import json

#site to scrap
page_url = "https://theporndude.com/"

#call class scraper to extract data and create a dictionary
data = Scraper.extract_data(page_url)

#Create json file with data
with open('site_data.json', 'w') as fp:
    json.dump(data, fp,indent=4)







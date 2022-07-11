import requests
from bs4 import BeautifulSoup
import re

class Scraper:
    url : str
    meta = str
    title = str
    photo_url = str
    page_text = str

    def extract_data(url_f):
        data = requests.get(url_f)
        soup = BeautifulSoup(data.content, "html.parser")
        links = []
        page_text = []
        for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
            links.append(link)
        # getting all the paragraphs
        for para in soup.find_all("p"):
            page_text.append(para.get_text())
        data = {
            "url" : str(url_f),
            "page_meta_tag" : str(soup.find("meta")),
            "page_title" :str(soup.find("title")),
            "page_links": str(links),
            "page_text" : str(page_text)
        }
        return data
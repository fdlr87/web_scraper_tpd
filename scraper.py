import requests
from bs4 import BeautifulSoup

class Scraper:
    url : str
    meta = str
    title = str
    photo_url = str
    page_text = str

    def extract_data(url_f):
        data = requests.get(url_f)
        soup = BeautifulSoup(data.content, "html.parser")
        photo_url = ""
        page_text = ""
        data = [
            url_f,
            soup.find("meta"),
            soup.find("title"),
            soup.find("tittle"),

        ]
        links = soup.find('img')
        print([i.find('img')['src'] for i in links])
        print([i.find('img')['title'] for i in links])
        return data

    def create_json(data):
        return data
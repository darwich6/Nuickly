import requests
from bs4 import BeautifulSoup


def get_content(url):
    page = requests.get(url)
    page_soup = BeautifulSoup(page.content, 'html.parser')
    # print(page_soup)

    # depending on what news agencies to parse, the container will hold different items
    content = []
    links = []
    if(url == "https://www.aljazeera.com/news/"):
        for i in page_soup.find_all('a', {"class": "u-clickable-card__link"}):
            content.append(i.get('href'))
        # print(content)
        # so content holds all the paths to the links after "https://www.aljazeera.com/news"
        # so lets append that to the beginning of them
        prefix = "https://www.aljazeera.com/news/"
        for j in content:
            links.append(prefix + j)
        # looks like it worked
        # print(links)

get_content("https://www.aljazeera.com/news/")



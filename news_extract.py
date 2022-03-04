import requests
from bs4 import BeautifulSoup


def get_content(user_topic):
    # determine the correct url for the given agency and topic
    url_alj = ""
    # url_bbc = ""
    url_usa = ""
    if(user_topic.lower() == "News".lower()):
        url_alj = "https://www.aljazeera.com/news/"
        # url_bbc = "https://www.bbc.com/news"
        url_usa = "https://www.usatoday.com/news/"
    elif(user_topic.lower() == "Sports".lower()):
        url_alj = "https://www.aljazeera.com/sports/"
        # url_bbc = "https://www.bbc.com/sport"
        url_usa = "https://www.usatoday.com/sports/"
    elif(user_topic.lower() == "Economy".lower()):
        url_alj = "https://www.aljazeera.com/economy/"
        # url_bbc = "https://www.bbc.com/news/business/economy"
        url_usa = "https://www.usatoday.com/money/"

    page_alj = requests.get(url_alj)
    # page_bbc = requests.get(url_bbc)
    page_usa = requests.get(url_usa)
    page_alj_soup = BeautifulSoup(page_alj.content, 'html.parser')
    # page_bbc_soup = BeautifulSoup(page_bbc.content, 'html.parser')
    page_usa_soup = BeautifulSoup(page_usa.content, 'html.parser')
    # print(page_soup)

    # depending on what news agencies to parse, the container will hold different items
    content_alj = []
    # content_bbc = []
    content_usa = []
    links_alj = []
    # links_bbc = []
    links_usa = []

    if(url_alj == "https://www.aljazeera.com/news/"):
        for i in page_alj_soup.find_all('a', {"class": "u-clickable-card__link"}):
            content_alj.append(i.get('href'))
        # print(content)
        # so content holds all the paths to the links after "https://www.aljazeera.com/news"
        # so lets append that to the beginning of them
        prefix = "https://www.aljazeera.com"
        for j in content_alj:
            links_alj.append(prefix + j)
        # looks like it worked
        # print(links)

    if (url_alj == "https://www.aljazeera.com/sports/"):
        for i in page_alj_soup.find_all('a', {"class": "u-clickable-card__link"}):
            content_alj.append(i.get('href'))
        # print(content)
        # so content holds all the paths to the links after "https://www.aljazeera.com"
        # so lets append that to the beginning of them
        prefix = "https://www.aljazeera.com"
        for j in content_alj:
            links_alj.append(prefix + j)
        # looks like it worked
        # print(links)

    if (url_alj == "https://www.aljazeera.com/economy/"):
        for i in page_alj_soup.find_all('a', {"class": "u-clickable-card__link"}):
            content_alj.append(i.get('href'))
        # print(content)
        # so content holds all the paths to the links after "https://www.aljazeera.com"
        # so lets append that to the beginning of them
        prefix = "https://www.aljazeera.com"
        for j in content_alj:
            links_alj.append(prefix + j)
        # looks like it worked
        # print(links)
    """
    if (url_bbc == "https://www.bbc.com/news"):
        for i in page_bbc_soup.find_all('a', {"class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"}):
            content_bbc.append(i.get('href'))
        # print(content)
        # so content holds all the paths to the links after "https://www.bbc.com"
        #so append that to the beginning of them
        prefix = "https://www.bbc.com"
        for j in content_bbc:
            links_bbc.append(prefix + j)
        # print(links)

    if (url_bbc == "https://www.bbc.com/sport"):
        for i in page_bbc_soup.find_all('a', {"class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link sp-o-link-split__anchor gel-double-pica-bold"}):
            content_bbc.append(i.get('href'))
        # print(content)
        # so content holds all the paths to the links after "https://www.bbc.com"
        #so append that to the beginning of them
        prefix = "https://www.bbc.com"
        for j in content_bbc:
            links_bbc.append(prefix + j)
        #print(links)

    if (url_bbc == "https://www.bbc.com/news/business/economy"):
        for i in page_bbc_soup.find_all('a', {"class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"}):
            content_bbc.append(i.get('href'))
        # print(content)
        # so content holds all the paths to the links after "https://www.bbc.com"
        #so append that to the beginning of them
        prefix = "https://www.bbc.com"
        for j in content_bbc:
            links_bbc.append(prefix + j)
        # print(links) 
    """

    if (url_usa == "https://www.usatoday.com/news/"):
        for i in page_usa_soup.find_all('a', {"class": "gnt_m_flm_a gnt_lbl_pm gnt_m_flm_a__pm"}):
            content_usa.append(i.get('href'))
        # print(content)
        # so content holds all the paths to the links after "https://www.usatoday.com"
        prefix = "https://www.usatoday.com"
        for j in content_usa:
            links_usa.append(prefix + j)
        # print(links)

    if (url_usa == "https://www.usatoday.com/money/"):
        for i in page_usa_soup.find_all('a', {"class": "gnt_m_flm_a"}):
            content_usa.append(i.get('href'))
        # print(content)
        # we see that the first index is actually link to the "the Daily money"
        # delete the first index
        del content_usa[0]
        # we also see that some empty strings have been found, remove them
        finalized_content = list(filter(None, content_usa))
        # so finalized content holds all the paths to the links after "https://www.usatoday.com"
        prefix = "https://www.usatoday.com"
        for j in finalized_content:
            links_usa.append(prefix + j)
        # print(links)

    if (url_usa == "https://www.usatoday.com/sports/"):
        for i in page_usa_soup.find_all('a', {"class": "gnt_m_flm_a"}):
            content_usa.append(i.get('href'))
        # print(content)
        # we can see that some empty strings have been found, remove them
        finalized_content = list(filter(None, content_usa))
        # so content holds all the paths to the links after "https://www.usatoday.com"
        prefix = "https://www.usatoday.com"
        for j in finalized_content:
            links_usa.append(prefix + j)
        # print(links)

    return links_alj, links_usa

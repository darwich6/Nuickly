import requests
from bs4 import BeautifulSoup


def get_content(user_agency, user_topic):
    # determine the correct url for the given agency and topic
    url = ""
    if(user_agency.lower() == "Al Jazeera".lower()):
        if(user_topic.lower() == "News".lower()):
            url = "https://www.aljazeera.com/news/"
        elif(user_topic.lower() == "Sports".lower()):
            url = "https://www.aljazeera.com/sports/"
        elif(user_topic.lower() == "Economy".lower()):
            url = "https://www.aljazeera.com/economy/"
    elif(user_agency.lower() == "BBC".lower()):
        if (user_topic.lower() == "News".lower()):
            url = "https://www.bbc.com/news"
        elif (user_topic.lower() == "Sports".lower()):
            url = "https://www.bbc.com/sport"
        elif (user_topic.lower() == "Economy".lower()):
            url = "https://www.bbc.com/news/business/economy"
    elif (user_agency.lower() == "USA Today".lower()):
        if (user_topic.lower() == "News".lower()):
            url = "https://www.usatoday.com/news/"
        elif (user_topic.lower() == "Sports".lower()):
            url = "https://www.usatoday.com/sports/"
        elif (user_topic.lower() == "Money".lower()):
            url = "https://www.usatoday.com/money/"

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
        prefix = "https://www.aljazeera.com"
        for j in content:
            links.append(prefix + j)
        # looks like it worked
        # print(links)

    if (url == "https://www.aljazeera.com/sports/"):
        for i in page_soup.find_all('a', {"class": "u-clickable-card__link"}):
            content.append(i.get('href'))
        # print(content)
        # so content holds all the paths to the links after "https://www.aljazeera.com"
        # so lets append that to the beginning of them
        prefix = "https://www.aljazeera.com"
        for j in content:
            links.append(prefix + j)
        # looks like it worked
        # print(links)

    if (url == "https://www.aljazeera.com/economy/"):
        for i in page_soup.find_all('a', {"class": "u-clickable-card__link"}):
            content.append(i.get('href'))
        # print(content)
        # so content holds all the paths to the links after "https://www.aljazeera.com"
        # so lets append that to the beginning of them
        prefix = "https://www.aljazeera.com"
        for j in content:
            links.append(prefix + j)
        # looks like it worked
        # print(links)

    if (url == "https://www.bbc.com/news"):
        for i in page_soup.find_all('a', {"class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"}):
            content.append(i.get('href'))
        # print(content)
        # so content holds all the paths to the links after "https://www.bbc.com"
        #so append that to the beginning of them
        prefix = "https://www.bbc.com"
        for j in content:
            links.append(prefix + j)
        # print(links)

    if (url == "https://www.bbc.com/sport"):
        for i in page_soup.find_all('a', {"class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link sp-o-link-split__anchor gel-double-pica-bold"}):
            content.append(i.get('href'))
        # print(content)
        # so content holds all the paths to the links after "https://www.bbc.com"
        #so append that to the beginning of them
        prefix = "https://www.bbc.com"
        for j in content:
            links.append(prefix + j)
        #print(links)

    if (url == "https://www.bbc.com/news/business/economy"):
        for i in page_soup.find_all('a', {"class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"}):
            content.append(i.get('href'))
        # print(content)
        # so content holds all the paths to the links after "https://www.bbc.com"
        #so append that to the beginning of them
        prefix = "https://www.bbc.com"
        for j in content:
            links.append(prefix + j)
        # print(links)

    if (url == "https://www.usatoday.com/news/"):
        for i in page_soup.find_all('a', {"class": "gnt_m_flm_a gnt_lbl_pm gnt_m_flm_a__pm"}):
            content.append(i.get('href'))
        # print(content)
        # so content holds all the paths to the links after "https://www.usatoday.com"
        prefix = "https://www.usatoday.com"
        for j in content:
            links.append(prefix + j)
        # print(links)

    if (url == "https://www.usatoday.com/money/"):
        for i in page_soup.find_all('a', {"class": "gnt_m_flm_a"}):
            content.append(i.get('href'))
        # print(content)
        # we see that the first index is actually link to the "the Daily money"
        # delete the first index
        del content[0]
        # we also see that some empty strings have been found, remove them
        finalized_content = list(filter(None, content))
        # so finalized content holds all the paths to the links after "https://www.usatoday.com"
        prefix = "https://www.usatoday.com"
        for j in finalized_content:
            links.append(prefix + j)
        # print(links)

    if (url == "https://www.usatoday.com/sports/"):
        for i in page_soup.find_all('a', {"class": "gnt_m_flm_a"}):
            content.append(i.get('href'))
        # print(content)
        # we can see that some empty strings have been found, remove them
        finalized_content = list(filter(None, content))
        # so content holds all the paths to the links after "https://www.usatoday.com"
        prefix = "https://www.usatoday.com"
        for j in finalized_content:
            links.append(prefix + j)
        # print(links)

    return links

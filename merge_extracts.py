from article_scrape import *
from news_extract import*


# create function that will merge lists into an dataframe
def merge(input_links_alj, input_links_usa):

    # grab all the information from Al Jazeera
    authors_alj = []
    formatted_dates_alj = []
    top_images_alj = []
    article_summaries_alj = []
    links_alj = []
    for i in input_links_alj:
        author, formatted_date, top_images, article_summary = summarize_article(i)
        authors_alj.append(author)
        formatted_dates_alj.append(formatted_date)
        top_images_alj.append(top_images)
        article_summaries_alj.append(article_summary)
        links_alj.append(i)

    # grab all the information from BBC
    # authors_bbc = []
    # formatted_dates_bbc = []
    # top_images_bbc = []
    # article_summaries_bbc = []
    # links_bbc = []
    # for i in input_links_bbc:
    #    author, formatted_date, top_images, article_summary = summarize_article(i)
    #    authors_bbc.append(author)
    #    formatted_dates_bbc.append(formatted_date)
    #    top_images_bbc.append(top_images)
    #    article_summaries_bbc.append(article_summary)
    #    links_bbc.append(i)

    # grab all the information from USA Today
    authors_usa = []
    formatted_dates_usa = []
    top_images_usa = []
    article_summaries_usa = []
    links_usa = []
    for i in input_links_usa:
        author, formatted_date, top_images, article_summary = summarize_article(i)
        authors_usa.append(author)
        formatted_dates_usa.append(formatted_date)
        top_images_usa.append(top_images)
        article_summaries_usa.append(article_summary)
        links_usa.append(i)

    total_authors = authors_alj + authors_usa
    total_dates = formatted_dates_alj + formatted_dates_usa
    total_top_images = top_images_alj + top_images_usa
    total_article_summaries = article_summaries_alj + article_summaries_usa
    total_links = links_alj + links_usa

    return total_authors, total_dates, total_top_images, total_article_summaries, total_links


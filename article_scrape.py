import newspaper.article
from newspaper import Article
import nltk
import time


# create a function that will summarize the article based on inputted url
def summarize_article(url):
    # create an article object based off the url given
    article = Article(url)

    # download the article and parse it
    article.download()
    article.parse()

    # punkt is a tokenizer which helps extract text
    nltk.download('punkt', quiet=True)
    article.nlp()

    # grab the articles authors
    print("Author: " + str(article.authors))
    author = str(article.authors)

    # get the publishing date of the article and format according to M-D-Y
    unf_date = article.publish_date
    formatted_date = ""
    if unf_date:
        formatted_date = str(unf_date.strftime("%m-%d-%Y"))
    else:
        formatted_date = "No Date Available"
    print("Publish Date: " + formatted_date)

    # grab the top image of the article
    print("Top Image Url: " + str(article.top_image))
    top_image = str(article.top_image)

    # grab all the images within the article
    # image_string = "All Images: "
    # for image in article.images:
    #    image_string += "\n\t" + image
    # print(image_string)

    print("A Quick Article Summary")
    print("----------------------------")
    print(article.summary)

    print("Link to Original Article")
    print("----------------------------")
    print(url)
    print()

    # grab the article summary
    article_summary = article.summary

    return author, formatted_date, top_image, article_summary

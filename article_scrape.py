from newspaper import Article
import nltk


# create a function that will summarize the article based on inputted url
def summarize_article(url):
    # create an article object based off the url given
    article = Article(url)

    # download the article and parse it
    article.download()
    article.parse()

    # punkt is a tokenizer which helps extract text
    nltk.download('punkt')
    article.nlp()

    # grab the articles authors
    # print("Author: " + str(article.authors))
    author = str(article.authors)

    # get the publishing date of the article and format according to M-D-Y
    # print("Publish Date: " + str(date.strftime("%m-%d-%Y")))
    unf_date = article.publish_date
    formatted_date = str(unf_date.strftime("%m-%d-%Y"))

    # grab the top image of the article
    # print("Top Image Url: " + str(article.top_image))
    top_image = str(article.top_image)

    # grab all the images within the article
    image_string = "All Images: "
    for image in article.images:
        image_string += "\n\t" + image
    # print(image_string)

    # print("A Quick Article Summary")
    # print("----------------------------")
    # print(article.summary)

    # grab the article summary
    article_summary = article.summary

    # return
    return author, formatted_date, top_image, article_summary

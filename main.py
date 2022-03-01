from article_scrape import *
from news_extract import *
import time

print("Hi, welcome to Nuickly a fully functional news aggregator! \n"
      "This is simply a prototype for what will be an awesome \n"
      "application that will allow users to quickly search through \n"
      "their favorite news, be provided with links to the actual article, \n"
      "and be shown a quick summary what the article is about. ")
print("------------------------------------------------------------------------------------------------------")
print("To get started, please input a news agency you would to view! \n Al Jazeera \t BBC \t USA Today")
user_agency = input("Type here: ")
user_topic = ""
if(user_agency.lower() == "Al Jazeera".lower()):
      print("Which topic space would you like to view? \n News \t Sports \t Economy")
      user_topic = input("Type here: ")
elif(user_agency.lower() == "BBC".lower()):
      print("Which topic space would you like to view? \n News \t Sports \t Economy")
      user_topic = input("Type here: ")
elif(user_agency.lower() == "USA Today".lower()):
      print("Which topic space would you like to view? \n News \t Sports \t Money")
      user_topic = input("Type here: ")

print("------------------------------------------------------------------------------------------------------")
print("Scraping articles...")
links = get_content(user_agency, user_topic)
time.sleep(2)
print()

print("Preparing summaries...")
time.sleep(2)
author = ""
formatted_date = ""
top_image = ""
article_summary = ""
for i in links:
      summarize_article(i)
      print("Link to article: " + i)

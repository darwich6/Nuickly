from news_extract import *
from merge_extracts import *
import time

print("Hi, welcome to Nuickly a fully functional news aggregator! \n"
      "This is simply a prototype for what will be an awesome \n"
      "application that will allow users to quickly search through \n"
      "their favorite news, be provided with links to the actual article, \n"
      "and be shown a quick summary what the article is about. ")
print("------------------------------------------------------------------------------------------------------")
print("To get started, please input a topic space you would to view! \n News \t Sports \t Economy")
user_agency = input("Type here: ")

print("------------------------------------------------------------------------------------------------------")
print("Scraping articles...")
input_links_alj, input_links_usa = get_content(user_agency)
time.sleep(2)
print()

for i in input_links_alj:
      summarize_article(i)

for j in input_links_usa:
      summarize_article(j)
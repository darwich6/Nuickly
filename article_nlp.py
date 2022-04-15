from textblob import TextBlob


def find_sentiment(news_story):
    # Create a textblob object for every news article summary
    news = TextBlob(news_story)
    sentiments = []

    # store each sentiment (polarity, subjectivity) in an array
    for sentence in news.sentences:
        sentiment = sentence.sentiment
        for metric in sentiment:
            sentiments.append(metric)

    # seperate the polarity from the subjectivity into different arrays
    polarity_data = []
    subjectivity_data = []
    for i in range(len(sentiments)):
        if i % 2 == 0:
            polarity_data.append(sentiments[i])
        else:
            subjectivity_data.append(sentiments[i])

    # calculate the total average of polarity and sentiment for the news summary
    polarity_average = calculate_average(polarity_data)
    subjectivity_average = calculate_average(subjectivity_data)

    # categorize the polarity and subjectivity to strings
    polarity_category = calculate_sentiment(polarity_average, "polarity")
    subjectivity_category = calculate_sentiment(subjectivity_average, "subjectivity")

    # print results
    print("Sentiment Analysis")
    print("----------------------------")
    print("Polarity: " + polarity_category)
    print("Subjectivity: " + subjectivity_category)


# Calculates a lists average
def calculate_average(list):
    return sum(list) / len(list)


# Categorizes inputted sentiments according to user defined categories
def calculate_sentiment(sentiment, type):
    sentiment_category = ""
    # Range for polarity is [-1,1]
    if type == "polarity":
        if sentiment > 0.75:
            sentiment_category = "Extremely Positive"
        elif sentiment > 0.5:
            sentiment_category = "Significantly Positive"
        elif sentiment > 0.25:
            sentiment_category = "Fairly Positive"
        elif sentiment > 0.1:
            sentiment_category = "Slightly Positive"
        elif sentiment < -0.1:
            sentiment_category = "Slightly Negative"
        elif sentiment < -0.25:
            sentiment_category = "Fairly Negative"
        elif sentiment < -0.5:
            sentiment_category = "Significantly Negative"
        elif sentiment < -0.75:
            sentiment_category = "Extremely Negative"
        else:
            sentiment_category = "Neutral"
    elif type == "subjectivity":
        # range of subjectivity is [0,1]
        if sentiment > 0.75:
            sentiment_category = "Extremely Subjective"
        elif sentiment > 0.5:
            sentiment_category = "Fairly Subjective"
        elif sentiment > 0.25:
            sentiment_category = "Fairly Objective"
        elif sentiment > 0.1:
            sentiment_category = "Extremely Objective"
    else:
        print("Invalid Input")

    return sentiment_category

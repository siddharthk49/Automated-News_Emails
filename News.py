import requests
import pprint
class NewsFeed:
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "f9622ffc608246adb4475f995c38ad6f"
    def __init__(self, interest, from_date, to_date, language= 'en'):
        self.interest= interest
        self.from_date = from_date
        self.to_date = to_date
        self.language= language

    def get(self):
        url = f"{self.base_url}q={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              "sortBy=publishedAt&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        email_body = ""
        # x= content['articles'][5]['title']

        # get all the titles and URLs
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n \n"
            # print(f"{article['title']} : {article['url']}")

        return email_body


"""url = "https://newsapi.org/v2/everything?q=arsenal&" \
      "from=2023-09-29&" \
      "sortBy=publishedAt&" \
      "language = en&" \
      "apiKey=f9622ffc608246adb4475f995c38ad6f"
response = requests.get(url)
content = response.json()
articles = content['articles']
email_body = ""
#x= content['articles'][5]['title']

#get all the titles and URLs
for article in articles:
    email_body = email_body + article['title'] + "\n"  + article['url'] + "\n \n"
    #print(f"{article['title']} : {article['url']}")

print(email_body)"""

"""
nf = NewsFeed(interest = "Football", from_date = "2023-09-29", to_date = "2023-09-29", language = "en")
nf.get()
"""
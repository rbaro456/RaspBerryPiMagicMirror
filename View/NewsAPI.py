from newsapi import NewsApiClient
import requests
import json

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=694b9bb634cc49df9a294a7b16cc74a7')

response = requests.get(url)


print(type(response))

my_json = response.json()


def article_titles():

    title_list = []

    for i in range(5):
        title_list.append(my_json['articles'][i]['title'])

    return title_list


list_title = article_titles()

for i in list_title:
    print(i)


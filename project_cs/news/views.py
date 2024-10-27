
from decouple import config
from django.shortcuts import render
from newsapi import NewsApiClient



API_KEY = config('NEWS_API_KEY', default='')

# Initialize the News API client
newsapi = NewsApiClient(api_key=API_KEY)

def news(request):
    # Fetch top headlines in the 'technology' category without restricting to a country
    tech_headlines = newsapi.get_top_headlines(category='technology',
                                               language='en')

    # Send the articles to the template
    articles = tech_headlines.get('articles', [])

    return render(request, 'news/tech_news.html', {'articles': articles})


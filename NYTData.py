#!/usr/bin/env python
"""
Module to scrape news articles from the NYT article search api.
"""

import requests
import json

class NewYorkTimes:
  def __init__(self, api_key):
    self.url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    self.api_key = api_key

  def get_text(self, search_term):
    """ Get the lead paragraph from the NYT articles matching this 
    search term. 
    """
    i = 0
    text = []
    payload = {'q' : search_term, 'fl' : 'headline', 
      'api_key' : self.api_key, 'page' : str(i)} 
    r = requests.get(self.url, payload)
    while (i < 2):
      if r.status_code != requests.codes.ok:
        r.raise_for_status()
      data = r.json()
      docs = data['response']['docs']
      for x in docs:
        for y in x.values():
          text.append(y['main'])
      i = i + 1
      payload = {'q' : search_term, 'fl' : 'headline', 
        'api_key' : self.api_key, 'page' : str(i)} 
      r = requests.get(self.url, payload)
    return text


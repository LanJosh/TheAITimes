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
    payload = {'q' : search_term, 'fl' : 'lead_paragraph', 
        'api_key' : self.api_key}
    r = requests.get(self.url, payload)
    if (r.status_code != requests.codes.ok):
      r.raise_for_status()
    data = r.json()
    docs = data['response']['docs']
    text = []
    for x in docs:
      text.extend(list(x.values())) 
    return text


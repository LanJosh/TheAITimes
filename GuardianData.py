#!/usr/bin/env python
"""
Module to scrape news articles from the Guardian article search api.
"""

import requests
import json

class Guardian:
  def __init__(self, api_key):
    self.url = "https://content.guardianapis.com/search"
    self.api_key = api_key

  def get_text(self, search_term):
    """
    Get the lead paragraph from the Guardian articles matching this 
    search term. 
    """
    payload = {'q' : search_term, 'format' : 'json', 
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

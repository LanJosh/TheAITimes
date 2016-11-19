#!/usr/bin/env python
"""
Module to get news feeds from NewsAPI.com
"""

import requests
import json

class NewsAPI :
    def __init__(self, api_key):
        self.atkurl = "https://newsapi.org/v1/articles"
        self.srcurl = "https://newsapi.org/v1/sources"
        self.apikey = api_key

        def get_text(self, category = None, lang = None, country = None, sortBy = None) :
            """
            First get the available news sources, then loop through the
            news sources to get article titles
            """
            # category : business, entertainment, gaming, general, music, science-and-nature, sport, technology
            # lang   : en, de, fr
            # country: au, de, gb, in, it, us
            # sortBy : top, latest, popular

            # get the news sources
            websites = []
            payload = dict()
            
            if category is not None :
                payload['category'] = category

            if lang is not None :
                payload['language'] = lang

            if country is not None :
                payload['country'] = country

            if len(payload) == 0 :
                r = requests.get(self.srcurl)
            else :
                r = requests.get(self.srcurl, payload)

            if r.status_code != requests.codes.ok:
                r.raise_for_status()

            data = r.json()
            for i in data['sources'] :
                websites.append(i['id'])

            # loop through the websites to get article titles
            titles = []
            for source in websites :
                pld = dict()

                pld['source'] = source
                pld['apiKey'] = self.apikey

                if sortBy is not None :
                    pld['sortBy'] = sortBy

                time.sleep(2)

                r = requests.get(self.atkurl, pld)
                if r.status_code != requests.codes.ok:
                    r.raise_for_status()
                data = r.json()
                for j in data['articles'] :
                    titles.append( j['title'] )

            return titles

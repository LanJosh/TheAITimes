#!/usr/bin/env python
"""
Module to get all the titles in the RSS feeds of CNN
"""

import urllib.request as u
from bs4 import BeautifulSoup

class CNNRSS :
    def __init__(self) :
        # 'http://rss.cnn.com/services/podcasting/studentnews/rss.xml', \
        self.cnn_rss_list = ['http://rss.cnn.com/rss/cnn_topstories.rss', \
                             'http://rss.cnn.com/rss/cnn_world.rss', \
                             'http://rss.cnn.com/rss/cnn_us.rss', \
                             'http://rss.cnn.com/rss/money_latest.rss', \
                             'http://rss.cnn.com/rss/cnn_allpolitics.rss', \
                             'http://rss.cnn.com/rss/cnn_tech.rss', \
                             'http://rss.cnn.com/rss/cnn_health.rss', \
                             'http://rss.cnn.com/rss/cnn_showbiz.rss', \
                             'http://rss.cnn.com/rss/cnn_travel.rss', \
                             'http://rss.cnn.com/rss/cnn_living.rss', \
                             'http://rss.cnn.com/rss/cnn_freevideo.rss', \
                             'http://rss.cnn.com/rss/cnn_latest.rss']

         def get_titles(self) :
            """
            Get the title of the news articles in the RSS feed
            """

            all_titles = list()
            file_save = open('/home/yp/Documents/2016-11-19 Dummy/CNNRSS.txt','w')
            for rss in self.cnn_rss_list :
                some = u.urlopen(rss).read()
                ss = BeautifulSoup(some, "lxml")
                
                #f = open('/home/yp/Documents/2016-11-19 Dummy/dummy', 'w')
                #f.write(str(ss.prettify()))
                #f.close()
                
                for ll in ss.find_all('item') :
                    newurl = ll.guid.string
                    #print(newurl)
                    
                    some = u.urlopen(newurl).read()
                    ss = BeautifulSoup(some)
                    
                    #f = open('/home/yp/Documents/2016-11-19 Dummy/dummy', 'w')
                    #f.write(str(ss.prettify()))
                    #f.close()
                    
                    all_titles.append( ss.h1.string )

                    file_save(write( ss.h1.string + '\n' ))
                    file_save.close()
                    
            return all_titles

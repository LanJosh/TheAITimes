#!/usr/bin/env python

from MarkovII import Markov
import os

"""
The world's worst p(ai)r programmer.

Takes your valid program as input, adds it to the AI training set, then 
generates another valid (but totally wrong) program to run.
"""

class CoreScraper:
  def __init__(self, directory):
    self.directory = directory

  def get_data(self):
    data = []
    for filename in os.listdir(self.directory):
      with open(self.directory + filename) as f:
        data.append(f.read())
    return data

def main():
  x = CoreScraper('./core-programs/')
  data = x.get_data()
  y = Markov(1)
  y.generate_model(data)
  count = input('Enter the number of programs to generate: ')
  for _ in range(int(count)):
    print(y.generate_text(50, 'end', seed='program'))

if __name__ == '__main__':
  main()

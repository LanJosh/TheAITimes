#!/usr/bin/env python
"""
A Markov model 
"""

import random

class Markov:
  def __init__(self, size):
    self.model = {}
    self.size = size

  def generate_model(self, data):
    """
    Generates a Markov model.
    ```data``` is a list of headlines to generate the model from
    ```size``` is the number of words to look back at
    """
    for headline in data:
      vocab = headline.split()
      if (self.size > len(vocab)):
        print("State size is too large for corpus") 
      for i in range(len(vocab) - self.size):
        key = ()
        for j in range(self.size):
          key += (vocab[i+j],) 
        if key in self.model:
          self.model[key].append(vocab[i+self.size])
        else:
          self.model[key] = [vocab[i+self.size]] 
  
  def generate_word(self, key):
    if key in self.model:
      return random.choice(self.model[key])
    else:
      return "ERROR"

  def generate_text(self, count):
    """
    Uses the Markov model to generate text
    ```count``` is the number of words to generate
    """
    key = random.choice(self.model.keys())
    print("Run started at: {}".format(key))
    i = 0
    text = ""
    for word in list(key):
      text += " " + word
    while (i < count - self.size):
      word = self.generate_word(key)
      if word == "ERROR":
        return text
      text += " " + word
      key = ((list(key))[1:]) 
      key.append(word)
      key = tuple(key)
      print("Run is at {}".format(key))
      i += 1 
    return text.strip('*')


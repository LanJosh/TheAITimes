#!/usr/bin/env python

from Markov import Markov

with open("data") as f:
  text = f.read()
data = text.split('\n')
x = Markov(2)
x.generate_model(data)
result = x.generate_text(10)
print(result.strip('*')) 


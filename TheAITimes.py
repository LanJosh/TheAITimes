from NYTData import NewYorkTimes
"""
Script develops news headlines for a subject using a Markov model
"""

def main():
  api_key = input('API key for the NYT article search API')
  NYT_scraper = NewYorkTimes(api_key)
  subject = input('Enter the subject to generate headlines for')
  data = NYT_scraper.get_text(subject)


if __name__ == '__main__':
  main()

import requests
import sched
import time
import logging

logging.basicConfig(filename = 'sys.log', level=logging.DEBUG, format='%(asctime)s :: %(levelname)s :: %(message)s')

def news_API_request(covid_terms = 'Covid COVID-19 coronavirus'):
  """
  Accesses current news articles that contain the terms 'covid', 'covid-19, 'coronavirus
  
  Parameters:
  covid_terms(str): a list of terms that must be contained in the news articles

  Returns:
  title_list(list): a list that contains the titles of the news articles
  content_list(list): a list that contains the contents of the news articles.

  """
  global title_list
  global content_list
  title_list = []
  content_list = []
  covid_terms = ["covid" or "covid-19" or "coronavirus"]
  news_url = ('https://newsapi.org/v2/top-headlines?q=' + ','.join(covid_terms)) + '&language=en' + '&apiKey=' + 'b824cd621c344562825f86336b79c3f0'
  response = requests.get(news_url)
  for article in response.json()['articles']:
    title = (article['title'])
    content = (article['content'])
    title_list.append(title)
    content_list.append(content)
  print(title_list)
  print(content_list)
  logging.info("Current news articles were accessed")
  logging.debug("covid terms: {}".format(covid_terms))
news_API_request()

response = requests.get("https://api.coronavirus.data.gov.uk/v1/data")
json_data = response.json()
print(json_data)

def update_news(update_interval, update_name, args=(), priority=1):
  """
  Updates the news articles every 24 hours

  Parameters:
  update_interval: the interval between each news update
  update_name: the name of the function that is going to be updated
  args: the argument from the function
  priority: the order of priority if several events are scheduled for the same time.

  """
  s = sched.scheduler(time.time, time.sleep)
  periodic_task(s, update_interval, update_name, args, priority)
  s.run()

def periodic_task(scheduler, update_interval, update_name, args, priority):
  update_name(*args)
  scheduler.enter(update_interval, priority, periodic_task, (scheduler, update_interval, update_name, args, priority))
  logging.info("News is scheduled to update in 24 hours")
update_news(86400,news_API_request)
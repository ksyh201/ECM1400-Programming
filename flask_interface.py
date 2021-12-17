from flask import Flask
from flask import render_template
from flask import request

import sched
import time
import requests
import logging
import csv

app = Flask(__name__)
news = []


s = sched.scheduler(time.time, time.sleep)
logging.basicConfig(filename = 'sys.log', level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

def news_API_request(covid_terms = 'Covid COVID-19 coronavirus'):
  """Accesses current news articles that contain the terms 'covid', 'covid-19, 'coronavirus"""
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
news_API_request()

def add_news_article():
    """A function that adds news articles to the flask interface."""
    try:
        global news
        for i in range(len(title_list)):
            news.append({
                "title" : title_list[i],
                "content" : content_list[i]
            })
        logging.info("Title and content were appended onto flask interface")
    except:
        logging.exception("Adding news articles failed")

def schedule_add_news(update):
    e1 = s.enter(update,1,add_news_article)

def minutes_to_seconds( minutes: str ) -> int:
    """Converts minutes to seconds."""
    return int(minutes)*60

def hours_to_minutes( hours: str ) -> int:
    """Converts hours to minutes."""
    return int(hours)*60

def hhmm_to_seconds( hhmm: str ) -> int:
    if len(hhmm.split(':')) != 2:
        print('Incorrect format. Argument must be formatted as HH:MM')
        return None
    return minutes_to_seconds(hours_to_minutes(hhmm.split(':')[0])) + \
        minutes_to_seconds(hhmm.split(':')[1])

@app.route('/index')
def hello():
    with open('nation_2021-10-28.csv') as csvfile:
        covid_csv_data = csv.reader(csvfile, delimiter=',')
        number_of_cases = []
        current_hospital = []
        number_of_deaths = []
        for row in covid_csv_data:
            number_cases = row[6]
            hospital_cases = row[5]
            number_deaths = row[4]

            number_of_cases.append(number_cases)
            current_hospital.append(hospital_cases)
            number_of_deaths.append(number_deaths)

        last7days_cases = number_of_cases[2:9]
        #figure out how to do total sum
        current_hospital_cases = current_hospital[1]
        total_deaths = number_of_deaths[14]

    logging.info("Flask interface has loaded")
    s.run(blocking=False)
    text_field = request.args.get('two')
    print(text_field)
    if text_field:
        update_time = request.args.get('update')
        print(update_time)
        update_time_sec = hhmm_to_seconds(update_time)
        schedule_add_news(update_time_sec)
    return render_template('index.html', 
        title='COVID-19 dashboard',
        location = 'Exeter',
        nation_location = 'England',
        hospital_cases = 'Current number of hospital cases nationally: ' + current_hospital_cases,
        deaths_total = 'Total number of deaths nationally: ' + total_deaths,
        news_articles=news)
    
if __name__ == '__main__':
    app.run()
import csv
import json
import requests
import sched
import time
import logging
from uk_covid19 import Cov19API

logging.basicConfig(filename = 'sys.log', level=logging.DEBUG, format='%(asctime)s :: %(levelname)s :: %(message)s')

def parse_csv_data(csv_filename: str):
    """
    A function that returns a list of strings for the rows in the file

    Parameters:
    csv_filename(str): the name of the CSV file that we are going to be reading from

    Returns:
    lists: a list of strings for the rows in the file.

    """
    file_name = open("nation_2021-10-28.csv", 'r', newline='')
    csv_reader = csv.reader(file_name) 
    lists = [] #empty list which will contain the data from the csv file
    for row in csv_reader: # for each row in the file, we will append it to a list
        lists.append(row)
    print(lists)
    logging.info("A list of strings was created from a CSV file")
parse_csv_data('nation_2021-10-28.csv')

def process_covid_csv_data(covid_csv_data: list):
    """
    A function that takes a list of data and returns three variables
    
    Parameters:
    covid_csv_data(list): a list of data from a CSV file 

    Returns:
    cases_last_7days: the sum of the number of COVID-19 cases in the last 7 days
    current_number_hospital_cases: the current number of hospital cases
    cum_number_deaths: the cumulative number of deaths.

    """
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

        print('The number of cases is', last7days_cases)
        print('The current number of hospital cases is', current_hospital_cases)
        print('The cumulative number of deaths is', total_deaths)
        logging.info("A list of data was taken and three variables were returned")
        logging.debug("The number of cases in the last 7 days: {}".format(last7days_cases))
        logging.debug("The current number of hospital cases is: {}".format(current_hospital_cases))
        logging.debug("The cumulative number of deaths is: {}".format(total_deaths))
process_covid_csv_data()


def covid_API_request(location="Exeter", location_type="ltla"):
    """
    A function that returns up to date COVID-19 data as a dictionary
    
    Parameters:
    location(str): the location of where the data is from
    location_type(str): the type of location

    Returns:
    data(dict): a dictionary that contains up to date COVID-19 data.

    """
    location_filter = ["areaType="+(location_type), "areaName="+(location)]
    data_structure = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "cumDailyNsoDeathsByDeathDate": "cumDailyNsoDeathsByDeathDate",
        "hospitalCases": "hospitalCases",
        "newCasesBySpecimenDate": "newCasesBySpecimenDate"
        }
    api = Cov19API(filters = location_filter, structure = data_structure)
    data = api.get_json()
    print(data)
    logging.info("COVID-19 data was returned as a dictionary")

def schedule_covid_updates(update_interval, update_name, args=(), priority=1):
    """
    Updates the news articles every hour

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
    schedule_covid_updates(3600,covid_API_request)
    logging.info("The news articles will update in an hour")
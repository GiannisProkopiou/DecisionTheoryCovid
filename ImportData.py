import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings("ignore")
from datetime import date, timedelta


def ImportData():

    yesterday = date.today() - timedelta(days=1)

    confirmed_cases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    confirmed_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    confirmed_recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    latest_data_daily = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + str(yesterday.strftime('%m-%d-%Y')) + '.csv')
    confirmed_cases_US = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
    confirmed_deaths_US = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')
    apple_mobility_data = pd.read_csv('applemobilitytrends-2020-12-20.csv')

    print(confirmed_cases.head())
    print(confirmed_deaths.head())
    print(confirmed_recovered.head())
    print(latest_data_daily.head())
    print(confirmed_cases_US.head())
    print(confirmed_deaths_US.head())
    print(apple_mobility_data.head())

    return confirmed_cases, confirmed_deaths, confirmed_recovered, latest_data_daily, confirmed_cases_US, confirmed_deaths_US, apple_mobility_data

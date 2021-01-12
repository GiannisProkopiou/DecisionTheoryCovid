import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import random
import math
import time
from sklearn.linear_model import LinearRegression, BayesianRidge
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error
import datetime
import operator
plt.style.use('fivethirtyeight')
#matplotlib inline
from IPython.display import set_matplotlib_formats
#set_matplotlib_formats('retina')
import warnings
warnings.filterwarnings("ignore")
from datetime import date, timedelta

from ImportData import *
from GetDates import *
from GetDaily import *
from MovingAverage import *
from Forecasting import *
from PredictingConfirmed import *
from Flatten import *
from country_plot import *



# 1. Import CSV data from John Hopkins University and Apple Mobility Data (2)
print(  '1. Import CSV data from John Hopkins University and Apple Mobility Data (2)')
confirmed_cases, confirmed_deaths, confirmed_recovered, latest_data_daily, confirmed_cases_US, confirmed_deaths_US, apple_mobility_data = ImportData()
print('----- 1 FINISHED SUCCESSFULLY ----- ')

# 2. Get all the dates for the ongoing coronavirus pandemic (3)
print('2. Get all the dates for the ongoing coronavirus pandemic (3)')
dates, world_cases, total_deaths, total_recovered, total_active, mortality_rate, recovery_rate = GetDates(confirmed_cases, confirmed_deaths, confirmed_recovered, latest_data_daily, confirmed_cases_US, confirmed_deaths_US, apple_mobility_data)
print('----- 2 FINISHED SUCCESSFULLY -----')

# 3. Getting daily increases and moving averages
print('3. Getting daily increases and moving averages')
daily_case_increases, daily_case_increase_avgs, daily_case_moving_avgs, daily_deaths_increases, daily_deaths_increase_avgs, daily_deaths_moving_avgs, daily_recovered_increases, daily_recovered_increase_avgs, daily_recovered_moving_avgs,  daily_active_increases, daily_active_increase_avgs, daily_active_moving_avgs = GetDaily(dates, world_cases, total_deaths, total_recovered, total_active)
MovingAverage(daily_case_moving_avgs, daily_deaths_moving_avgs, daily_recovered_moving_avgs, daily_active_moving_avgs, window_size=7)
print('----- 3 FINISHED SUCCESSFULLY -----')

# 4. Future forecasting and Convert integer into daytime for better visualization (5,6)
print('4. Future Forecasting and Convert integer into daytime for better visualization')
future_forcast_dates, X_train_confirmed, X_test_confirmed, y_train_confirmed, y_test_confirmed, future_forcast, adjusted_dates = Forecasting(dates, world_cases, total_deaths, total_recovered)
print('----- 4 FINISHED SUCCESSFULLY -----')

# 5. Model for predicting # of confirmed cases. (7)
print('5. Model for predicting # of confirmed cases.')
world_daily_increase, world_confirmed_avg, world_daily_increase_avg, world_daily_death, world_death_avg, world_daily_death_avg, world_daily_recovery, world_recovery_avg, world_daily_recovery_avg, world_active_avg, window = PredictingConfirmed(future_forcast_dates, X_train_confirmed, X_test_confirmed, y_train_confirmed, y_test_confirmed, future_forcast, world_cases, total_deaths, total_recovered, total_active)
print('----- 5 FINISHED SUCCESSFULLY -----')
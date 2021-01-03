import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import RandomizedSearchCV, train_test_split
import datetime
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings("ignore")
from datetime import date, timedelta

def Forecasting(dates, world_cases, total_deaths, total_recovered):

    days_since_1_22 = np.array([i for i in range(len(dates))]).reshape(-1, 1)
    world_cases = np.array(world_cases).reshape(-1, 1)
    total_deaths = np.array(total_deaths).reshape(-1, 1)
    total_recovered = np.array(total_recovered).reshape(-1, 1)

    # future forecasting
    days_in_future = 10
    future_forcast = np.array([i for i in range(len(dates)+days_in_future)]).reshape(-1, 1)
    adjusted_dates = future_forcast[:-10]
    start = '1/22/2020'
    start_date = datetime.datetime.strptime(start, '%m/%d/%Y')
    future_forcast_dates = []

    for i in range(len(future_forcast)):

        future_forcast_dates.append((start_date + datetime.timedelta(days=i)).strftime('%m/%d/%Y'))

    # slightly modify the data to fit the model better (regression models cannot pick the pattern)
    X_train_confirmed, X_test_confirmed, y_train_confirmed, y_test_confirmed = train_test_split(days_since_1_22,
                                                                                                world_cases,
                                                                                                test_size=0.05,
                                                                                                shuffle=False)

    print("future_forcast_dates: ", future_forcast_dates)
    print("-----------------------------------------------")
    print("X_train_confirmed: ", X_train_confirmed)
    print("-----------------------------------------------")
    print("X_test_confirmed: ", X_test_confirmed)
    print("-----------------------------------------------")
    print("y_train_confirmed: ", y_train_confirmed)
    print("-----------------------------------------------")
    print("y_test_confirmed: ", y_test_confirmed)
    print("-----------------------------------------------")

    return future_forcast_dates, X_train_confirmed, X_test_confirmed, y_train_confirmed, y_test_confirmed, future_forcast



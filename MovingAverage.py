import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings("ignore")

from ImportData import *
from GetDates import *
from GetDaily import *

def MovingAverage(daily_case_moving_avgs, daily_deaths_moving_avgs, daily_recovered_moving_avgs, daily_active_moving_avgs, window_size):

    for i in range(window_size):

        print('Case: ', daily_case_moving_avgs[i])
        print('Deaths: ', daily_deaths_moving_avgs[i])
        print('Recovered: ' , daily_recovered_moving_avgs[i])
        print('Active: ', daily_active_moving_avgs[i])
        print('------------')

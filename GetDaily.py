import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings("ignore")

from ImportData import *
from GetDates import *

def GetDaily(dates, world_cases, total_deaths, total_recovered, total_active):

    daily_case_increases = []
    daily_case_increase_avgs = []
    daily_case_moving_avgs = []

    daily_deaths_increases = []
    daily_deaths_increase_avgs = []
    daily_deaths_moving_avgs = []

    daily_recovered_increases = []
    daily_recovered_increase_avgs = []
    daily_recovered_moving_avgs = []

    daily_active_increases = []
    daily_active_increase_avgs = []
    daily_active_moving_avgs = []

    for date in range(len(dates) - 1):

        # date_obj = datetime.datetime.strptime(date, '%m/%d/%y')
        # yesterday = date_obj.date() - datetime.timedelta(days=1)

        # daily_case_increase = world_cases[date_obj.strftime('%m/%d/%y')] - world_cases[yesterday.strftime('%m/%d/%y')]
        daily_case_increase = world_cases[date + 1] - world_cases[date]
        daily_case_increases.append(daily_case_increase)

        daily_case_increase_avg = daily_case_increase / 2
        daily_case_increase_avgs.append(daily_case_increase_avg)

        daily_case_moving_avg = sum(daily_case_increase_avgs) / len(daily_case_increase_avgs)
        daily_case_moving_avgs.append(daily_case_moving_avg)

        #-------------------------------------------------------------------------------------------

        daily_deaths_increase = total_deaths[date + 1] - total_deaths[date]
        daily_deaths_increases.append(daily_deaths_increase)

        daily_deaths_increase_avg = daily_deaths_increase / 2
        daily_deaths_increase_avgs.append(daily_deaths_increase_avg)

        daily_deaths_moving_avg = sum(daily_deaths_increase_avgs) / len(daily_deaths_increase_avgs)
        daily_deaths_moving_avgs.append(daily_deaths_moving_avg)

        #-------------------------------------------------------------------------------------------

        daily_recovered_increase = total_recovered[date + 1] - total_recovered[date]
        daily_recovered_increases.append(daily_recovered_increase)

        daily_recovered_increase_avg = daily_recovered_increase / 2
        daily_recovered_increase_avgs.append(daily_recovered_increase_avg)

        daily_recovered_moving_avg = sum(daily_recovered_increase_avgs) / len(daily_recovered_increase_avgs)
        daily_recovered_moving_avgs.append(daily_recovered_moving_avg)

        #--------------------------------------------------------------------------------------------

        daily_active_increase = total_active[date + 1] - total_active[date]
        daily_active_increases.append(daily_active_increase)

        daily_active_increase_avg = daily_active_increase / 2
        daily_active_increase_avgs.append(daily_active_increase_avg)

        daily_active_moving_avg = sum(daily_active_increase_avgs) / len(daily_active_increase_avgs)
        daily_active_moving_avgs.append(daily_active_moving_avg)

    return daily_case_increases, daily_case_increase_avgs, daily_case_moving_avgs, daily_deaths_increases, daily_deaths_increase_avgs, daily_deaths_moving_avgs, daily_recovered_increases, daily_recovered_increase_avgs, daily_recovered_moving_avgs,  daily_active_increases, daily_active_increase_avgs, daily_active_moving_avgs



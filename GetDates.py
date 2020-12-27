import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
#matplotlib inline
import warnings
warnings.filterwarnings("ignore")

from ImportData import *

def GetDates(confirmed_cases, confirmed_deaths, confirmed_recovered, latest_data_daily, confirmed_cases_US, confirmed_deaths_US, apple_mobility_data):

    confirrmed_cases_keys = confirmed_cases.keys()
    confirmed_deaths_keys = confirmed_deaths.keys()
    confirmed_recovered_keys = confirmed_recovered.keys()
    latest_data_daily_keys = latest_data_daily.keys()
    confirmed_cases_US_keys = confirmed_cases_US.keys()
    confirmed_deaths_US_keys = confirmed_deaths_US.keys()
    apple_mobility_data_keys = apple_mobility_data.keys()

    confirmed = confirmed_cases.iloc[:, 4:-1]
    deaths = confirmed_deaths.iloc[:, 4:-1]
    recoveries = confirmed_recovered.iloc[:, 4:-1]

    dates = confirmed.keys()

    world_cases = []
    total_deaths = []
    mortality_rate = []
    recovery_rate = []
    total_recovered = []
    total_active = []

    for date in dates:

        confirmed_sum = confirmed[date].sum()
        death_sum = deaths[date].sum()
        recovered_sum = recoveries[date].sum()

        # confirmed, deaths, recovered, and active
        # optimal: world_cases.append(confirmed[i].sum())
        world_cases.append(confirmed_sum)
        total_deaths.append(death_sum)
        total_recovered.append(recovered_sum)
        total_active.append(confirmed_sum - death_sum - recovered_sum)

        # calculate rates
        mortality_rate.append(death_sum / confirmed_sum)
        recovery_rate.append(recovered_sum / confirmed_sum)

    print(world_cases)
    print(total_deaths)
    print(total_recovered)
    print(total_active)
    print(mortality_rate)
    print(recovery_rate)

    return dates, world_cases, total_deaths, total_recovered, total_active, mortality_rate, recovery_rate
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
#matplotlib inline
from IPython.display import set_matplotlib_formats
#set_matplotlib_formats('retina')
import warnings
warnings.filterwarnings("ignore")
from datetime import date, timedelta

def Flatten(world_cases, adjusted_dates, world_confirmed_avg, total_deaths, world_death_avg, total_recovered, total_active, world_active_avg, world_recovery_avg, world_daily_increase, world_daily_increase_avg, world_daily_death, world_daily_death_avg, world_daily_recovery, world_daily_recovery_avg, window):

    adjusted_dates = adjusted_dates.reshape(1, -1)[0]
    plt.figure(figsize=(16, 10))
    plt.plot(adjusted_dates, world_cases)
    plt.plot(adjusted_dates, world_confirmed_avg, linestyle='dashed', color='orange')
    plt.title('# of Coronavirus Cases Over Time', size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.legend(['Worldwide Coronavirus Cases', 'Moving Average {} Days'.format(window)], prop={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.plot(adjusted_dates, total_deaths)
    plt.plot(adjusted_dates, world_death_avg, linestyle='dashed', color='orange')
    plt.title('# of Coronavirus Deaths Over Time', size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.legend(['Worldwide Coronavirus Deaths', 'Moving Average {} Days'.format(window)], prop={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.plot(adjusted_dates, total_recovered)
    plt.plot(adjusted_dates, world_recovery_avg, linestyle='dashed', color='orange')
    plt.title('# of Coronavirus Recoveries Over Time', size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.legend(['Worldwide Coronavirus Recoveries', 'Moving Average {} Days'.format(window)], prop={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.plot(adjusted_dates, total_active)
    plt.plot(adjusted_dates, world_active_avg, linestyle='dashed', color='orange')
    plt.title('# of Coronavirus Active Cases Over Time', size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Active Cases', size=30)
    plt.legend(['Worldwide Coronavirus Active Cases', 'Moving Average {} Days'.format(window)], prop={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.bar(adjusted_dates, world_daily_increase)
    plt.plot(adjusted_dates, world_daily_increase_avg, color='orange', linestyle='dashed')
    plt.title('World Daily Increases in Confirmed Cases', size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.legend(['Moving Average {} Days'.format(window), 'World Daily Increase in COVID-19 Cases'], prop={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.bar(adjusted_dates, world_daily_death)
    plt.plot(adjusted_dates, world_daily_death_avg, color='orange', linestyle='dashed')
    plt.title('World Daily Increases in Confirmed Deaths', size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.legend(['Moving Average {} Days'.format(window), 'World Daily Increase in COVID-19 Deaths'], prop={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.bar(adjusted_dates, world_daily_recovery)
    plt.plot(adjusted_dates, world_daily_recovery_avg, color='orange', linestyle='dashed')
    plt.title('World Daily Increases in Confirmed Recoveries', size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.legend(['Moving Average {} Days'.format(window), 'World Daily Increase in COVID-19 Recoveries'], prop={'size': 20})
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.plot(adjusted_dates, np.log10(world_cases))
    plt.title('Log of # of Coronavirus Cases Over Time', size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.plot(adjusted_dates, np.log10(total_deaths))
    plt.title('Log of # of Coronavirus Deaths Over Time', size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.plot(adjusted_dates, np.log10(total_recovered))
    plt.title('Log of # of Coronavirus Recoveries Over Time', size=30)
    plt.xlabel('Days Since 1/22/2020', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

 # def flatten(arr):
 #        a = []
 #        arr = arr.tolist()
 #        for i in arr:
 #            a.append(i[0])
 #        return a

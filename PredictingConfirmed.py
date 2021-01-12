import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, BayesianRidge
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings("ignore")
import numpy as np

from daily_increase2 import *

def PredictingConfirmed(future_forcast_dates, X_train_confirmed, X_test_confirmed, y_train_confirmed, y_test_confirmed, future_forcast, world_cases, total_deaths, total_recovered, total_active):

    # kernel = ['poly', 'sigmoid', 'rbf']
    # c = [0.01, 0.1, 1, 10]
    # gamma = [0.01, 0.1, 1]
    # epsilon = [0.01, 0.1, 1]
    # shrinking = [True, False]
    # svm_grid = {'kernel': kernel, 'C': c, 'gamma': gamma, 'epsilon': epsilon, 'shrinking': shrinking}
    # svm = SVR(kernel='poly', degree=3)

    # svm_search = RandomizedSearchCV(svm, svm_grid, scoring='neg_mean_squared_error', cv=3, return_train_score=True, n_jobs=-1, n_iter=30, verbose=1)
    #
    # svm_search.fit(X_train_confirmed, y_train_confirmed.ravel()) # this is where the error is
    #GridSearchCV

    #svm_search.best_params_

    #svm_confirmed = svm_search.best_estimator_

    svm_confirmed = SVR(shrinking=True, kernel='poly', gamma=0.01, epsilon=1, degree=4, C=0.1)
    svm_confirmed.fit(X_train_confirmed, y_train_confirmed)
    svm_pred = svm_confirmed.predict(future_forcast)

    # check against testing data
    svm_test_pred = svm_confirmed.predict(X_test_confirmed)
    plt.plot(y_test_confirmed)
    plt.plot(svm_test_pred)
    plt.legend(['Test Data', 'SVM Predictions'])
    print('MAE:', mean_absolute_error(svm_test_pred, y_test_confirmed))
    print('MSE:', mean_squared_error(svm_test_pred, y_test_confirmed))
    plt.show()

    # Transform our data for polynomial regression
    poly = PolynomialFeatures(degree=4)
    poly_X_train_confirmed = poly.fit_transform(X_train_confirmed)
    poly_X_test_confirmed = poly.fit_transform(X_test_confirmed)
    poly_future_forcast = poly.fit_transform(future_forcast)

    bayesian_poly = PolynomialFeatures(degree=5)
    bayesian_poly_X_train_confirmed = bayesian_poly.fit_transform(X_train_confirmed)
    bayesian_poly_X_test_confirmed = bayesian_poly.fit_transform(X_test_confirmed)
    bayesian_poly_future_forcast = bayesian_poly.fit_transform(future_forcast)

    # Polynomial regression
    linear_model = LinearRegression(normalize=True, fit_intercept=False)
    linear_model.fit(poly_X_train_confirmed, y_train_confirmed.ravel())
    test_linear_pred = linear_model.predict(poly_X_test_confirmed)
    linear_pred = linear_model.predict(poly_future_forcast)
    print('MAE:', mean_absolute_error(test_linear_pred, y_test_confirmed))
    print('MSE:', mean_squared_error(test_linear_pred, y_test_confirmed))

    print(linear_model.coef_)

    plt.plot(y_test_confirmed)
    plt.plot(test_linear_pred)
    plt.legend(['Test Data', 'Polynomial Regression Predictions'])
    plt.show()

    # Bayesian ridge polynomial regression
    tol = [1e-6, 1e-5, 1e-4, 1e-3, 1e-2]
    alpha_1 = [1e-7, 1e-6, 1e-5, 1e-4, 1e-3]
    alpha_2 = [1e-7, 1e-6, 1e-5, 1e-4, 1e-3]
    lambda_1 = [1e-7, 1e-6, 1e-5, 1e-4, 1e-3]
    lambda_2 = [1e-7, 1e-6, 1e-5, 1e-4, 1e-3]
    normalize = [True, False]

    bayesian_grid = {'tol': tol, 'alpha_1': alpha_1, 'alpha_2': alpha_2, 'lambda_1': lambda_1, 'lambda_2': lambda_2,
                     'normalize': normalize}

    bayesian = BayesianRidge(fit_intercept=False)
    bayesian_search = RandomizedSearchCV(bayesian, bayesian_grid, scoring='neg_mean_squared_error', cv=3,
                                         return_train_score=True, n_jobs=-1, n_iter=40, verbose=1)
    bayesian_search.fit(bayesian_poly_X_train_confirmed, y_train_confirmed.ravel())
    bayesian_search.best_params_
    bayesian_confirmed = bayesian_search.best_estimator_
    test_bayesian_pred = bayesian_confirmed.predict(bayesian_poly_X_test_confirmed)
    bayesian_pred = bayesian_confirmed.predict(bayesian_poly_future_forcast)
    print('MAE:', mean_absolute_error(test_bayesian_pred, y_test_confirmed))
    print('MSE:', mean_squared_error(test_bayesian_pred, y_test_confirmed))

    plt.plot(y_test_confirmed)
    plt.plot(test_bayesian_pred)
    plt.legend(['Test Data', 'Bayesian Ridge Polynomial Predictions'])
    plt.show()

    # window size
    window = 7

    # confirmed cases
    world_daily_increase = daily_increase(world_cases)
    world_confirmed_avg = moving_average(world_cases, window)
    world_daily_increase_avg = moving_average(world_daily_increase, window)
    # deaths
    world_daily_death = daily_increase(total_deaths)
    world_death_avg = moving_average(total_deaths, window)
    world_daily_death_avg = moving_average(world_daily_death, window)

    # recoveries
    world_daily_recovery = daily_increase(total_recovered)
    world_recovery_avg = moving_average(total_recovered, window)
    world_daily_recovery_avg = moving_average(world_daily_recovery, window)

    # active
    world_active_avg = moving_average(total_active, window)

    return world_daily_increase, world_confirmed_avg, world_daily_increase_avg, world_daily_death, world_death_avg, world_daily_death_avg, world_daily_recovery, world_recovery_avg, world_daily_recovery_avg, world_active_avg, window


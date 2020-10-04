#import matplotlib.pyplot as plt
#import requests
#import numpy as np
#import pandas as pd
#import sys


def profit(revenue, cost):
    return revenue - cost


def weather():
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=Toronto&cnt=16&appid=0f184978c3e7dc795bc05fbd70fd110d'
    r = requests.get(url)

    forecast = {

    }

    # return if cold or nah

    return r.text


def data():
    df = pd.read_csv('C:/Users/Hudson Yuen/OneDrive/School/Other/AmpHacks/retail_trans/retail_data_sum3.csv')

    df['new_date'] = pd.to_datetime(df['new_date'])
    df['diff'] = abs(df['new_amount'].diff())
    df['period'] = 1

    for i in range(len(df) - 1):
        # if abs(df.loc[i + 1, 'diff'] / df.loc[i, 'new_amount']) > 0.4:
        if df.loc[i + 1, 'diff'] > 5000:
            df.loc[i + 1:, 'period'] += 1

    # print(df[1220:1230])

    curr_period = df['period'].iloc[-1]
    df_forecast = df.loc[df['period'] == curr_period, ['new_date', 'new_amount']]

    return df_forecast


def moving_avg(values, window):
    weights = np.repeat(1.0, window) / window
    sma = np.convolve(values, weights, 'valid')

    return sma


def predict_rev(revenue, date):
    df2 = pd.DataFrame({'new_date': [date], 'new_amount': [revenue]})

    df_forecast = data()
    df_forecast = df_forecast.append(df2, ignore_index=True)

    prediction = moving_avg(df_forecast['new_amount'], 20)[-1]
    #
    # weather_forecast = weather()
    #
    # if weather_forecast == 'cold':
    #     prediction = prediction * 0.66
    # elif weather_forecast == 'hot':
    #     prediction = prediction * 1.15

    return prediction


def fixed_costs(rent, rent_freq, utilities, util_freq):
    month_tag = "m"
    year_tag = "y"

    if rent_freq == month_tag:
        day_rent = rent / 30
    elif rent_freq == year_tag:
        day_rent = rent / 365
    else:
        day_rent = 0

    if util_freq == month_tag:
        day_util = utilities / 30
    elif util_freq == year_tag:
        day_util = utilities / 365
    else:
        day_rent = 0

    return {'daily_rent': day_rent, 'daily_util': day_util}


def staff_costs(num_staff, hours, salary):
    # assume weekly hours per person, salary per hour
    week_salary = hours * salary
    week_cost = num_staff * week_salary
    day_cost = week_cost / 7

    return day_cost


def product_costs(order_cost, num_orders, sell_cost, num_sold):
    order_month_cost = order_cost * num_orders  # num orders per month
    order_day_cost = order_month_cost / 30

    sell_day_cost = sell_cost * num_sold

    return order_day_cost + sell_day_cost


if __name__ == "__main__":
    # rev = int(input())
    # cost = int(input())
    # funds = int(input())
    #
    # prof = profit(rev, cost)
    # if prof < 0:
    #     print(abs(funds / prof))
    # else:
    #     print(prof, "you good")

    # window = 30
    #
    # x = df_forecast['new_date']
    # y = df_forecast['new_amount']
    # plt.plot(x, y, 'o', color='violet')
    # plt.plot(x[window - 1:], moving_avg(df_forecast['new_amount'], window))
    # plt.show()

    rev = predict_rev(2600, pd.to_datetime('10/5/2020'))
    print("Predicted Revenue:", rev)

    costs_fixed = fixed_costs(5000, "m", 12000, "y")
    costs_staff = staff_costs(5, 40, 15)
    costs_product = product_costs(1000, 2, 2, 500)

    print("Fixed Costs:", costs_fixed, "Staff Costs:", costs_staff, "Product Costs:", costs_product)

    print(profit(rev, costs_fixed['daily_rent'] + costs_fixed['daily_util'] + costs_staff + costs_product))

    print(weather())

    exit(0)

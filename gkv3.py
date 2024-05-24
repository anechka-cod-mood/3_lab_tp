# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def load_data(file_path):
    return pd.read_csv(file_path, parse_dates=['Date'])

def display_data(data):
    print(data)

def plot_data(data, forecast_days):
    plt.figure(figsize=(14, 7))

    plt.subplot(2, 1, 1)
    plt.plot(data['Date'], data['Currency1'], label='Currency 1')
    plt.title('Курс рубля к первой валюте')
    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(data['Date'], data['Currency2'], label='Currency 2')
    plt.title('Курс рубля ко второй валюте')
    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.legend()

    plt.tight_layout()
    plt.show()

    forecast_data(data, forecast_days)

def calculate_max_changes(data):
    data['Currency1_Change'] = data['Currency1'].diff()
    data['Currency2_Change'] = data['Currency2'].diff()

    max_gain_currency1 = data['Currency1_Change'].max()
    max_loss_currency1 = data['Currency1_Change'].min()
    max_gain_date_currency1 = data.loc[data['Currency1_Change'].idxmax(), 'Date']
    max_loss_date_currency1 = data.loc[data['Currency1_Change'].idxmin(), 'Date']

    max_gain_currency2 = data['Currency2_Change'].max()
    max_loss_currency2 = data['Currency2_Change'].min()
    max_gain_date_currency2 = data.loc[data['Currency2_Change'].idxmax(), 'Date']
    max_loss_date_currency2 = data.loc[data['Currency2_Change'].idxmin(), 'Date']

    print(f"Максимальное увеличение курса первой валюты: {max_gain_currency1} на {max_gain_date_currency1}")
    print(f"Максимальное уменьшение курса первой валюты: {max_loss_currency1} на {max_loss_date_currency1}")
    print(f"Максимальное увеличение курса второй валюты: {max_gain_currency2} на {max_gain_date_currency2}")
    print(f"Максимальное уменьшение курса второй валюты: {max_loss_currency2} на {max_loss_date_currency2}")

def forecast_data(data, forecast_days):
    data['Currency1_SMA'] = data['Currency1'].rolling(window=5).mean()
    data['Currency2_SMA'] = data['Currency2'].rolling(window=5).mean()

    forecast_dates = [data['Date'].iloc[-1] + timedelta(days=i) for i in range(1, forecast_days + 1)]
    forecast_currency1 = [data['Currency1_SMA'].iloc[-1]] * forecast_days
    forecast_currency2 = [data['Currency2_SMA'].iloc[-1]] * forecast_days

    plt.figure(figsize=(14, 7))

    plt.subplot(2, 1, 1)
    plt.plot(data['Date'], data['Currency1'], label='Currency 1')
    plt.plot(data['Date'], data['Currency1_SMA'], label='SMA (Currency 1)', linestyle='--')
    plt.plot(forecast_dates, forecast_currency1, label='Forecast (Currency 1)', linestyle=':', color='red')
    plt.title('Курс рубля к первой валюте с прогнозом')
    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(data['Date'], data['Currency2'], label='Currency 2')
    plt.plot(data['Date'], data['Currency2_SMA'], label='SMA (Currency 2)', linestyle='--')
    plt.plot(forecast_dates, forecast_currency2, label='Forecast (Currency 2)', linestyle=':', color='red')
    plt.title('Курс рубля ко второй валюте с прогнозом')
    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    file_path = 'exchange_rates.csv' 
    data = load_data(file_path)
    display_data(data)
    calculate_max_changes(data)
    forecast_days = 7 
    plot_data(data, forecast_days)

if __name__ == "__main__":
    main()


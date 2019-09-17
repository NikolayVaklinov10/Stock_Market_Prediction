import pandas as pd
import numpy as np
import matplotlib as plt
import tensorflow as tf


GOLD_TRAIN_DATA = 'CSV_Files/Gold Data Last Year.csv'
GOLD_TEST_DATA = 'CSV_Files/Gold Data Last Month.csv'

current_train_data = GOLD_TRAIN_DATA
current_test_data = GOLD_TEST_DATA

NUM_TRAIN_DATA_POINTS = 266
NUM_TEST_DATA_POINTS = 22


def load_stock_data(stock_name, num_data_points):
    data = pd.read_csv(stock_name,
                       skiprows=0,
                       nrows=num_data_points,
                       usecols=['Price', 'Open', 'Vol.'])
    final_prices = data['Price'].astype(str).str.replace(',', '').astype(np.float)
    opening_prices = data['Open'].astype(str).str.replace(',', '').astype(np.float)
    volumes = data['Vol.'].str.strip('MK').astype(np.float)
    return final_prices, opening_prices, volumes


print(load_stock_data(current_test_data, NUM_TEST_DATA_POINTS))
































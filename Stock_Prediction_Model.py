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

LEARNING_RATE = 0.1


def load_stock_data(stock_name, num_data_points):
    data = pd.read_csv(stock_name,
                       skiprows=0,
                       nrows=num_data_points,
                       usecols=['Price', 'Open', 'Vol.'])
    final_prices = data['Price'].astype(str).str.replace(',', '').astype(np.float)
    opening_prices = data['Open'].astype(str).str.replace(',', '').astype(np.float)
    volumes = data['Vol.'].str.strip('MK').astype(np.float)
    return final_prices, opening_prices, volumes


def calculate_price_differences(final_prices, opening_prices):
    price_differences = []
    for d_i in range(len(final_prices) - 1):
        price_difference = opening_prices[d_i + 1] - final_prices[d_i]
        price_differences.append(price_difference)
    return price_differences


# y = Wx + b
x = tf.placeholder(tf.float32, name='')
W = tf.Variable([.1], name='W')
b = tf.Variable([.1], name='b')
y = W * x + b
y_predicted = tf.placeholder(tf.float32, name='y_predicted')

loss = tf.reduce_sum(tf.square(y - y_predicted))
optimizer = tf.train.AdamOptimizer(LEARNING_RATE).minimize(loss)


























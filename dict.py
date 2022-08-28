from random import random
import pandas as pd
import datetime

df = pd.read_csv('/home/kamil/workplace/Tritem/new.csv')

df['elapsed-time'] = df['distance'] / df['wheel_speed'] # in hours
df['elapsed-time2'] = df['distance'] / df['gps_speed'] # in hours
df["initial_time"] = pd.to_datetime(df["initial_time"])

start_time = df.groupby('id')['initial_time'].min().rename('start-time')
end_time = df.groupby('id')['initial_time'].max().rename('finish-time')

time = df.groupby('id')["initial_time"].agg([max, min]).eval('max-min').rename('journey_time')


# c = time[3]




distance_new = 100
speed = distance_new / 2

print(time)



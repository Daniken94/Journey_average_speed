import time
import pandas as pd
import random
from datetime import datetime
import math


df = pd.read_csv('/home/kamil/workplace/Tritem/new.csv')

df['elapsed-time'] = df['distance'] / df['wheel_speed']
df['elapsed-time2'] = df['distance'] / df['gps_speed']
df['elapsed-time3'] = df['distance'] / df['higher_speed']
df["initial_time"] = pd.to_datetime(df["initial_time"])
journey_time = df.groupby('id')["initial_time"].agg([max, min]).eval('max-min').rename('journey_time')
validate = str(journey_time)[19:34]
validate_hour = int(validate[0:2])
validate_minute = int(validate[4:5])
validate_seconds = float(validate[6:])
print(validate_hour)
print(validate_minute)
print(validate_seconds)
print(validate)


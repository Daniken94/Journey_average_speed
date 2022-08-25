import pandas as pd
from io import StringIO


# speed in km / hour; distance in km
data = '''checkpoint    initial-time id  speed distance speed2 distance2
1   2020-09-18T12:03:14.485952Z car_01 72 9 71 9
2   2020-09-18T12:10:14.485952Z car_01 83 8 82 8
3   2020-09-18T12:15:14.485952Z car_01 73 9 73 9
4   2020-09-18T12:25:14.485952Z car_01 74 9 74 9
5   2020-09-18T12:35:14.485952Z car_01 72 9 72 9
6   2020-09-18T12:50:14.485952Z car_01 72 9 71 9
7   2020-09-18T12:59:14.485952Z car_01 72 9 72 9
8   2020-09-18T13:05:14.485952Z car_01 80 9 80 9
9   2020-09-18T13:14:14.485952Z car_01 71 9 71 9
10   2020-09-18T13:19:14.485952Z car_01 70 9 71 9
'''


df = pd.read_csv(StringIO(data), delim_whitespace=True)
df['elapsed-time'] = df['distance'] / df['speed'] # in hours
df['elapsed-time2'] = df['distance2'] / df['speed2']

df["initial-time"] = pd.to_datetime(df["initial-time"])



start_time = df.groupby('id')['initial-time'].min().rename('start-time')
end_time = df.groupby('id')['initial-time'].max().rename('finish-time')

time = df.groupby('id')["initial-time"].agg([max, min]).eval('max-min').rename('journey_time')

ave_speed = ((df.groupby('id')['distance'].sum() / df.groupby('id')['elapsed-time'].sum())
             .rename('ave speed (km/hr)').round(2))
distance = (df.groupby('id')['distance'].sum())
ave_speed2 = ((df.groupby('id')['distance2'].sum() / df.groupby('id')['elapsed-time2'].sum())
             .rename('ave speed2 (km/hr)').round(2))
distance2 = (df.groupby('id')['distance2'].sum())


result = pd.concat([start_time, end_time, time, ave_speed, distance, ave_speed2, distance2], axis=1)

print(result)

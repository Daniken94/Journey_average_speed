import pandas as pd
from datetime import datetime

df = pd.read_csv(r'/home/kamil/workplace/Tritem/car_details.csv', delim_whitespace=True)


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

new_data = {
    "initial-time" : "2022-08-25 20:27:43.225624",
    "id" : "car_01",
    "speed" : "20",
    "distance" : "5",
    "speed2" : "20",
    "distance2" : "5"
}

df = pd.DataFrame(list(new_data))
df.to_csv('car_details.csv', mode='a', index=False, header=False)

result = pd.concat([start_time, end_time, time, ave_speed, distance, ave_speed2, distance2], axis=1)

print(result)

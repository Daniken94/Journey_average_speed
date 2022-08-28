import pandas as pd
from datetime import datetime
import random
import math
import time





starttime = time.time()

def average_speed_during_jurney():
    while True:
        print("Checkpoint!")

        df = pd.read_csv('/home/kamil/workplace/Tritem/new.csv')

        df['elapsed-time'] = df['distance'] / df['wheel_speed']
        df['elapsed-time2'] = df['distance'] / df['gps_speed']
        df['elapsed-time3'] = df['distance'] / df['higher_speed']
        df["initial_time"] = pd.to_datetime(df["initial_time"])

        start_time = df.groupby('id')['initial_time'].min().rename('start-time')
        end_time = df.groupby('id')['initial_time'].max().rename('finish-time')
        journey_time = df.groupby('id')["initial_time"].agg([max, min]).eval('max-min').rename('journey_time')


        ave_wheel_speed = ((df.groupby('id')['distance'].sum() / df.groupby('id')['elapsed-time'].sum())
                    .rename('ave wheel speed (km/hr)').round(2))
        distance = (df.groupby('id')['distance'].sum())
        ave_gps_speed = ((df.groupby('id')['distance'].sum() / df.groupby('id')['elapsed-time2'].sum())
                    .rename('ave gps speed (km/hr)').round(2))
        ave_higher_speed = ((df.groupby('id')['distance'].sum() / df.groupby('id')['elapsed-time3'].sum())
                    .rename('average speed (km/hr)').round(2))



        today = str(datetime.today())
        distance_new = random.uniform(0.00, 0.27)
        speed = random.uniform(0.1, 159.9)
        speed_up = math.ceil(speed)
        speed_down = math.floor(speed)


        random_speed = [speed_up, speed_down]


        new_data = {
            "initial-time" : [f'{today}'],
            "id" : ["car_01"],
            "wheel_speed" : [f'{random.choice(random_speed)}'],
            "distance" : [f'{distance_new}'],
            "gps_speed" : [f'{random.choice(random_speed)}']
        }

        val1 = new_data["wheel_speed"]
        val2 = new_data["gps_speed"]

        new_data_update = {
            "higher_speed" : (val1 if val1 > val2 else val2)
        }

        new_data.update(new_data_update)


        df = pd.DataFrame(new_data)
        df.to_csv('new.csv', mode='a', index=False, header=False)

        result = pd.concat([start_time, end_time, journey_time, distance, ave_higher_speed], axis=1)
        print(result)


        time.sleep(10.0 - ((time.time() - starttime) % 10.0))

average_speed_during_jurney()



import pandas as pd
from datetime import datetime
import random
import math
import time
import timedelta


starttime = time.time()



def average_speed_during_jurney():

    while True:

        df = pd.read_csv("/home/kamil/workplace/Tritem/car_details.csv")

        today = str(datetime.today())
        distance_new = random.uniform(0.00, 0.27)
        speed = random.uniform(0.1, 159.9)
        speed_up = math.ceil(speed)
        speed_down = math.floor(speed)

        random_speed = [speed_up, speed_down]

        new_data = {
            "initial-time": [f"{today}"],
            "id": ["car_01"],
            "wheel_speed": [f"{random.choice(random_speed)}"],
            "distance": [f"{distance_new}"],
            "gps_speed": [f"{random.choice(random_speed)}"],
        }

        val1 = new_data["wheel_speed"]
        val2 = new_data["gps_speed"]

        new_data_update = {"higher_speed": (val1 if val1 > val2 else val2)}

        new_data.update(new_data_update)

        df = pd.DataFrame(new_data)

        if len(df) > 1:

            print("Checkpoint!")

            df["initial_time"] = pd.to_datetime(df["initial_time"])

            journey_time = (
                df.groupby("id")["initial_time"]
                .agg([max, min])
                .eval("max-min")
                .rename("journey_time")
            )
            validate = str(journey_time)[19:34]
            validate_days = int(str(journey_time)[12:13])
            validate_hour = int(str(validate[0:2]))
            validate_minute = int(str(validate[4:5]))
            validate_seconds = float(str(validate[6:]))

            td = timedelta.Timedelta(
                days=validate_days,
                hours=validate_hour,
                minutes=validate_minute,
                seconds=validate_seconds,
            )
            time_result_hour = (td.total.seconds) * 0.000277777778

            start_time = df.groupby("id")["initial_time"].min().rename("start-time")
            end_time = df.groupby("id")["initial_time"].max().rename("finish-time")
            journey_time = (
                df.groupby("id")["initial_time"]
                .agg([max, min])
                .eval("max-min")
                .rename("journey_time")
            )
            distance = df.groupby("id")["distance"].sum()
            ave_higher_speed = (
                (df.groupby("id")["distance"].sum() / time_result_hour)
                .rename("average speed (km/hr)")
                .round(2)
            )

            df.to_csv("car_details.csv", mode="a", index=False, header=False)
            result = pd.concat(
                [start_time, end_time, journey_time, distance, ave_higher_speed], axis=1
            )
            print(result)

        else:
            print("Start new journey")
            df.to_csv("car_details.csv", mode="a", index=False, header=False)

        time.sleep(10.0 - ((time.time() - starttime) % 10.0))


average_speed_during_jurney()

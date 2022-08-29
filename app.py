import pandas as pd
from datetime import datetime
import random
import math
import time
import timedelta


# Variable for running script for every 10 seconds
starttime = time.time()


def average_speed_during_jurney():
    """This func emulate car and calculate
    avarage speed and distance"""
    while True:

        df = pd.read_csv("/home/kamil/workplace/Journey_average_speed/car_details.csv")

        # Create some variables for new car data send by dict
        today = str(datetime.today())
        distance_new = random.uniform(0.00, 0.27)
        speed = random.uniform(0.1, 159.9)
        speed_up = math.ceil(speed)
        speed_down = math.floor(speed)

        random_speed = [speed_up, speed_down]

        # Dict with new car data
        new_data = {
            "initial-time": [f"{today}"],
            "id": ["car_01"],
            "wheel_speed": [f"{random.choice(random_speed)}"],
            "distance": [f"{distance_new}"],
            "gps_speed": [f"{random.choice(random_speed)}"],
        }

        # Catch bigger value from dict and update it in dict
        val1 = new_data["wheel_speed"]
        val2 = new_data["gps_speed"]

        new_data_update = {"higher_speed": (val1 if val1 > val2 else val2)}

        new_data.update(new_data_update)

        """"If" is important to check data in scv file. 
        If file is empty function don't calculate parameters. 
        Only send new values. But if existing some data in file, 
        func do all work"""
        if len(df) > 1:

            print("Checkpoint!")

            # Convert value to data field
            df["initial_time"] = pd.to_datetime(df["initial_time"])

            journey_time = (
                df.groupby("id")["initial_time"]
                .agg([max, min])
                .eval("max-min")
                .rename("journey_time")
            )

            # Catch and convert time from jurney_time
            validate = str(journey_time)[19:34]
            validate_days = int(str(journey_time)[12:13])
            validate_hour = int(str(validate[0:2]))
            validate_minute = int(str(validate[4:5]))
            validate_seconds = float(str(validate[6:]))

            # Convert values to hour number (float)
            td = timedelta.Timedelta(
                days=validate_days,
                hours=validate_hour,
                minutes=validate_minute,
                seconds=validate_seconds,
            )
            time_result_hour = (td.total.seconds) * 0.000277777778

            # Calculating necessary variables like distance, average speed
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

            # Prepare new car data to send to csv file
            df = pd.DataFrame(new_data)

            # Send data to csv file
            df.to_csv("car_details.csv", mode="a", index=False, header=False)

            # Print results in console
            result = pd.concat(
                [start_time, end_time, journey_time, distance, ave_higher_speed], axis=1
            )
            print(result)

        else:
            # Sending data to csv file
            print("Start new journey")

            # Prepare new car data to send to csv file
            df = pd.DataFrame(new_data)
            df.to_csv("car_details.csv", mode="a", index=False, header=False)

        # Parameters for starttime variable
        time.sleep(10.0 - ((time.time() - starttime) % 10.0))


average_speed_during_jurney()

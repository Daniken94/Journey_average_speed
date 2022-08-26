import pandas as pd
from datetime import datetime
import random
import math

today = datetime.today()
id = "car_01"
distance = random.randint(0,10)
speed = distance / 0.112
speed1 = math.ceil(speed)
# speed2 = round(speed)
speed2 = math.floor(speed)


data = [str(today), id, speed1, distance, speed2, distance]

print(data)
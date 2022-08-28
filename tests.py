import pandas as pd
from datetime import datetime
import random
import math

today = datetime.today()
id = "car_01"
distance_new = random.randint(0,10)
speed = distance_new / 0.112
speed1 = math.ceil(speed)
speed2 = math.floor(speed)


new_data = today, id, speed1, distance_new, speed2, distance_new

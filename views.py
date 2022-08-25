import pandas as pd
from io import StringIO


# speed in km / hour; distance in km
data = '''location    initial-time id  speed distance speed2 distance2
1   2020-09-18T12:03:14.485952Z car_uno 72 9 71 9
2   2020-09-18T12:10:14.485952Z car_uno 83 8 82 8
3   2020-09-18T12:15:14.485952Z car_uno 73 9 73 9
4   2020-09-18T12:25:14.485952Z car_uno 74 9 74 9
5   2020-09-18T12:35:14.485952Z car_uno 72 9 72 9
6   2020-09-18T12:50:14.485952Z car_uno 72 9 71 9
7   2020-09-18T12:59:14.485952Z car_uno 72 9 72 9
8   2020-09-18T13:05:14.485952Z car_uno 80 9 80 9
9   2020-09-18T13:14:14.485952Z car_uno 71 9 71 9
10   2020-09-18T13:19:14.485952Z car_uno 70 9 71 9
'''


df = pd.read_csv(StringIO(data), delim_whitespace=True)
df['elapsed-time'] = df['distance'] / df['speed'] # in hours
df['elapsed-time2'] = df['distance2'] / df['speed2']

# utility function
def hours_to_hms(elapsed):
    ''' Convert `elapsed` (in hours) to hh:mm:ss (round to nearest sec)'''
    h, m = divmod(elapsed, 1)
    m *= 60
    _, s = divmod(m, 1)
    s *= 60
    hms = '{:02d}:{:02d}:{:02d}'.format(int(h), int(m), int(round(s, 0)))
    return hms

# perform calculations
start_time = df.groupby('id')['initial-time'].min()
journey_hrs = df.groupby('id')['elapsed-time'].sum().rename('elapsed-hrs')
hms = journey_hrs.apply(lambda x: hours_to_hms(x)).rename('hh:mm:ss')
ave_speed = ((df.groupby('id')['distance'].sum() 
             / df.groupby('id')['elapsed-time'].sum())
             .rename('ave speed (km/hr)')
             .round(2))
ave_speed2 = ((df.groupby('id')['distance2'].sum() 
             / df.groupby('id')['elapsed-time2'].sum())
             .rename('ave speed2 (km/hr)')
             .round(2))

# assemble results
result = pd.concat([start_time, journey_hrs, hms, ave_speed, ave_speed2], axis=1)

print(result)
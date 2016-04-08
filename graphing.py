#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.dates
import pandas as pd
import datetime

# Read the data into a pandas DataFrame
hr_data = pd.read_csv("/home/ivan/Documents/Projects/FitBit/hr_2016-03-25.csv")
intraday_data = pd.read_csv("/home/ivan/Documents/Projects/FitBit/intraday_data_2016-03-25.csv")

# These are the "Tableau 20" colors as RGB.
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

  
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)

data_headers = ['heart-rate']

# Correct time formatting 
badformattime = hr_data.time.values
splittime = badformattime[0].split("-")
year = splittime[0]
month = splittime[1]
splittime = splittime[2].split(" ")
day = splittime[0]
splittime = splittime[1].split(":")
hour = splittime[0]
minute = splittime[1]
second = splittime[2]
t = datetime.time(int(hour), int(minute), int(second))
d = datetime.date(int(year), int(month), int(day))
dt = datetime.datetime.combine(d,t)

fds = matplotlib.dates.date2num(dt)
print dt,fds

#for i, column in enumerate(data_headers):
    # Plot each line separately with its own color, using the Tableau 20
    # color set in order.
#    plt.plot(hr_data.time.values,
#            hr_data[column.replace("\n", " ")].values,
#            lw=2.5, color=tableau20[i])

    # Add a text label to the right end of every line.
    # Adding specific offsets y position because some labels overlapped.
#    y_pos = gender_degree_data[column.replace("\n", " ")].values[-1] - 0.5


# Finally, save the figure as a PNG.
# You can also save it as a PDF, JPEG, etc.
# Just change the file extension in this call.
# bbox_inches="tight" removes all the extra whitespace on the edges of your plot. 

#plt.savefig("heart-rate.png", bbox_inches="tight")

#!/usr/bin/python

# necessary for VNC with no X server
#import matplotlib as mpl
#mpl.use('Agg')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

# Read .csv into pandas dataframe
hrcsv = pd.read_csv("hr_2016-03-25.csv")

# Get raw data as numpy arrays
hr_raw = hrcsv['heart-rate'].values
time_raw = hrcsv['time'].values

# Convert time string to datetime
temp = []
for i in range(0,len(time_raw)):
   temp += [dt.datetime.strptime(time_raw[i], '%Y-%m-%d %H:%M:%S')]

time_np = np.array(temp)

## DELETE ZERO ELEMENTS, NEEDS REVISITTING
zeros_hr = np.where(hr_raw == 0)[0]
hr_final = np.delete(hr_raw, zeros_hr)
time_final = np.delete(time_np, zeros_hr)

##########
# Plotting
##########
# create subplots
fig, ax = plt.subplots()

# set x-axis tick date formatting
timeFmt = mdates.DateFormatter('%I%p')
ax.xaxis.set_major_formatter(timeFmt)

# enable grid
ax.grid(True)

# plot
ax.plot(time_final, hr_final)

# rotates and right aligns the x labels, and moves the bottom of the
# axes up to make room for them
fig.autofmt_xdate()

# show & save
plt.show()
plt.savefig("hr.png")

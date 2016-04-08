#!/usr/bin/python
#!/depot/Python-2.7.6/bin/python2.7

# necessary for VNC with no X server
import matplotlib as mpl
mpl.use('Agg')

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

### Plotting
hours = mdates.HourLocator()
minutes = mdates.MinuteLocator()
timeFmt = mdates.DateFormatter('%I%p')
#timeFmt = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')

## DELETE ZERO ELEMENTS, NEEDS REVISITTING
hr_raw = np.delete(hr_raw, range(72,75))
time_np = np.delete(time_np, range(72,75))

fig, ax = plt.subplots()
ax.plot(time_np, hr_raw)

# format ticks
#ax.xaxis.set_major_locator(hours)
ax.xaxis.set_major_formatter(timeFmt)
#ax.xaxis.set_minor_locator(minutes)
ax.grid(True)

#datemin = dt.date(time_np.min().hour, 1, 1)
#datemax = dt.date(time_np.max().hour + 1, 1, 1)
#ax.set_xlim(datemin, datemax)

# rotates and right aligns the x labels, and moves the bottom of the
# axes up to make room for them
fig.autofmt_xdate()

# ax.plot(time_useful, hr_raw)
# ax.xaxis_date()
# fig = plt.figure()
# plt.plot(hr_raw)


plt.show()
plt.savefig("hr.png")

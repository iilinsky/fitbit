#!/depot/Python-2.7.6/bin/python2.7
#!/usr/bin/python

# necessary for VNC with no X server
import matplotlib as mpl
mpl.use('Agg')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from matplotlib.collections import LineCollection
from matplotlib.colors import BoundaryNorm
from scipy.interpolate import interp1d
import colormaps as cm

################################################################################
# GLOBAL VARIABLES
################################################################################
# Calculate HR zones
age = 25
hrmax = 220 - age    # subtract your age from 220
fatburn = .5 * hrmax # 50% of max
cardio = .7 * hrmax  # 70% of max
peak = .85 * hrmax   # 85% of max

# Set HR limts (used for y-axis and colormap)
limit_hrmin = 40
limit_hrmax = 180

################################################################################
# DATA PREPARATION
################################################################################
# Read .csv into pandas dataframe
hrcsv = pd.read_csv("ivan/hr_2016-04-13.csv")

# Get raw data as numpy arrays
hr_raw = hrcsv['heart-rate'].values
time_raw = hrcsv['time'].values

# Convert time string to datetime
temp = []
for i in range(0,len(time_raw)):
   temp += [dt.datetime.strptime(time_raw[i], '%Y-%m-%d %H:%M:%S')]

time_dt = np.array(temp)

# Convert datetime to float (needed for multi-color line plotting)
time_float = mdates.date2num(time_dt)

# Delete zero elements
zeros_hr = np.where(hr_raw == 0)[0]
hr_nozero = np.delete(hr_raw, zeros_hr)
time_nozero = np.delete(time_float, zeros_hr)

# Raw data comes in at 5 min intervals, making for a very segmented plot.
# Interpolate data to 4 pts/min
f = interp1d(time_nozero, hr_nozero, kind='cubic')
time_final = np.linspace(time_nozero.min(), time_nozero.max(), num=4*60*24, endpoint=True)
hr_final = f(time_final)

################################################################################
# Plotting
################################################################################

# select the colormap
cmap = cm.hr_cmap

# set the color boundaries based on the HR limits and number of colors
boundaries = np.linspace(limit_hrmin,limit_hrmax,cmap.N)
norm = BoundaryNorm(boundaries, cmap.N)

# pair up time & HR points
x = time_final
y = hr_final
points = np.array([x,y]).T.reshape(-1,1,2)

# create segments for line collection
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# create line collection
lc = LineCollection(segments, linewidth=3, cmap=cmap, norm=norm)
lc.set_array(y)

# create subplots
fig, ax = plt.subplots()

# set figure dimensions
fig.set_figheight(5)
fig.set_figwidth(12)

# Remove the plot frame lines. They are unnecessary chartjunk.
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# Remove the ticks except for bottom axis
ax.get_xaxis().set_ticks_position('bottom')
ax.get_yaxis().set_ticks_position('none')

# set limits
plt.xlim(x.min(), x.max())
plt.ylim(limit_hrmin,limit_hrmax)

# Add gray horizonal tick lines
for y in range(limit_hrmin+20, limit_hrmax+20, 20):
    ax.axhline(y, color='black', alpha=0.3)

# Add thick horizonal bottom frame line
ax.axhline(limit_hrmin, color='black', alpha=0.3, lw=3)

# set x-axis tick time formatting + location
timeFmt = mdates.DateFormatter('%I %p')
hours = mdates.HourLocator(range(0,24,2))
ax.get_xaxis().set_major_formatter(timeFmt)
ax.get_xaxis().set_major_locator(hours)

# plot HR collection
ax.add_collection(lc)

# plot horizonal zone lines
ax.axhline(fatburn, color=cmap(.5))
ax.axhline(cardio, color=cmap(.7))
ax.axhline(peak, color=cmap(.85))
ax.annotate(' Fat Burn', xy=(max(x), fatburn-2), color=cmap(.5))
ax.annotate(' Cardio', xy=(max(x), cardio-2), color=cmap(.7))
ax.annotate(' Peak', xy=(max(x), peak-2), color=cmap(.85))

# add labels, title
plt.title("Heart Rate - Ivan - Apr. 13, 2016\n", fontsize=14)
plt.ylabel("BPM", fontsize=10)
plt.xlabel("\nData source: www.fitbit.com | "
           "Author: Ivan Ilinsky", fontsize=8)

# rotates and right aligns the x labels, and moves the bottom of the
# axes up to make room for them
fig.autofmt_xdate()

# show & save
#plt.show()
output = "hr.png"
plt.savefig(output, bbox_inches="tight")
print "Output: %s" % (output)

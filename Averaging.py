import os

import matplotlib
import matplotlib.animation as animation

matplotlib.use('TkAgg') # do this before importing pylab
import matplotlib.pyplot as plt

from scipy import signal

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


# location = open('fileLocation.txt','r').read()
pathForTextFile = ("C:/Users/Elgar/Singapore University of Technology and Design/Siddharth Kumar - Whiskers Array Sensing/191023_wind_tunnel/heavy_tip_22_run3_v8.2_on30off120.txt")
#pathForTextFile =  os.path.join(location, "test.txt")   #making path for the text file

def animate(i):

    graph_data = open(pathForTextFile,'r').read()
    lines = graph_data.split('\n')
    ts = []
    xs = []
    x = 0
    for line in lines:
        if len(line) > 1:
            line = line.split(' ')
            ts.append(float(line[0]))
            xs.append(float(line[1]))
            # if float(line[0]) >= 0.4:
            #     break;

    xs=signal.savgol_filter(xs, 1001, 2)  # window size used for filtering # order of fitted polynomial
    ax1.clear()
    #ax1.plot(ts, xs, '-r', label = '40 Hz at 40 PSI of 15 mm whisker kept at 35 mm from the pressure dispenser source')
    #ax1.plot(ts, xs, '-r', label='Frequency Sweep 1 to 40 Hz at 10PSI kept at middle 20 mm from the pressure dispenser source')
    ax1.plot(ts, xs, '-r',label='Speed 8.2 m/s')
    ax1.legend(loc = 'upper left')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Average Voltage(V)')




ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()

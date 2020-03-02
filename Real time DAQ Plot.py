import nidaqmx
import pandas as pd

i=0
data_array = []
with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    data = task.read(number_of_samples_per_channel=1)
    data_array.append(data)
    print(data)

import os

import matplotlib
import matplotlib.animation as animation

matplotlib.use('TkAgg') # do this before importing pylab
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


location = open('D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/Live Data From DAQ/fileLocation.txt', 'r').read()
pathForTextFile =  os.path.join(location, "test.txt")   #making path for the text file

def animate(i):
    graph_data = open(pathForTextFile,'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    y = 0
    for line in lines:
        if len(line) > 1:
            x = line
            y = y + 0.005
            xs.append(float(x))
            ys.append(float(y))

    MWSD1 = pd.Series(xs)
    # print(xs)
    data1 = MWSD1.rolling(1000).std()
    # xs = xs[-66:]
    # ys = ys[-66:]
    # xs=signal.savgol_filter(xs, 53, 2)  # window size used for filtering # order of fitted polynomial
    ax1.clear()
    ax1.plot(ys, data1, '-b', label = 'Voltage')
    ax1.legend(loc = 'upper left')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Voltage')




ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()




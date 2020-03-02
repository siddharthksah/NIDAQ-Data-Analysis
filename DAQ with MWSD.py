##################################################################
#IMPORT NECESSARY PACKAGES
##################################################################

import os
import nidaqmx
import matplotlib.pyplot as plt
import numpy
import time
import matplotlib
import matplotlib.animation as animation
import pandas as pd
from matplotlib import style
from scipy import signal

matplotlib.use('TkAgg') # do this before importing pylab
import matplotlib.pyplot as plt

matplotlib.use('TkAgg') # do this before importing pylab

##################################################################



##################################################################
#CHOOSE THE STYLE FOR THE PLOTTING
##################################################################
style.use('fivethirtyeight')
##################################################################



##################################################################
#DECLARE FIGS
##################################################################

fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
##################################################################



##################################################################
#GET THE LOCATION WHERE THE DATA FROM SERIAL IS BEING LOGGED
##################################################################
# location = open('fileLocation.txt','r').read()
# pathForTextFile =  os.path.join(location, "test.txt")   #making path for the text file
pathForTextFile = (
    "C:/Users/Elgar/Singapore University of Technology and Design/Siddharth Kumar - Whiskers Array Sensing/191110\2 Dispensers\5 9 13 15 Hz 40 Seconds\[22]/sweep1.txt")
##################################################################



##################################################################
#FUNCTION WHICH IS CALLED TO PLOT
##################################################################
def animatex(i):
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev6/ai0")
        # task.read()
        #start_time = time.time()

        data = task.read(number_of_samples_per_channel=1)
        print(data)
        data_array.append(data)
        plt.scatter(i / 10, data[0])
        # plt.plot(i, data[0])
        # plt.show()
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (V)')
        plt.pause(0.000001)
        # plt.show()
        # i = i + 1

    graph_data = open(pathForTextFile,'r').read()
    lines = graph_data.split('\n')
    ts = []
    xs = []
    x = 0
    for line in lines:
        if len(line) > 0:
            line = line.split(' ')
            if float(line[0]) >= 0:
                #ts.append(float(line[0]))
                ts.append(float(line[0])/2)
                xs.append(float(line[1]))

            if float(line[0]) >= 60:
                break;



    #xs=signal.savgol_filter(xs, 1001, 2)
    MWSD1 = pd.Series(xs)
    data1 = MWSD1.rolling(1000).std()
    #data2 = pd.rolling_mean()#change the number for changing rolling window
    # data1new = []
    # tsnew = []
    # t2 = 1
    # for line in data1:
    #     if len(data1) > 1:
    #         #print(line)
    #         data1new.append(float(line))
    #         tsnew.append(t2 - 1)
    #         t2 = t2 + 0.001


    ax1.clear()
    #ax1.plot(ts, data1, '-b', label = 'Frequency 15Hz 21Hz 24Hz at middle 20 mm from the pressure dispenser source')
    #ax1.plot(ts, data1, '-b', label='Frequency Sweep 1 to 30 Hz at middle 20 mm from the pressure dispenser source')
    ax1.plot(ts, data1, '-b', label='Sweep')
    ax1.legend(loc = 'upper left')
    ax1.set_xlabel('Freq(Hz)')
    #ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('MWSD of Raw Voltage')
    #ax1.plot(ts, data1)
##################################################################



ani1 = animation.FuncAnimation(fig1, animatex, interval = 30)
plt.show()





plt.ion()
i=0
data_array = []
with nidaqmx.Task() as task:
     task.ai_channels.add_ai_voltage_chan("Dev6/ai0")
     #task.read()
     start_time = time.time()
     while i<50000:
         data=task.read(number_of_samples_per_channel=1)
         print(data)
         data_array.append(data)
         plt.scatter(i/10, data[0])
         # plt.plot(i, data[0])
         # plt.show()
         plt.xlabel ('Time (s)')
         plt.ylabel ('Voltage (V)')
         plt.pause(0.000001)
         #plt.show()
         i=i+1


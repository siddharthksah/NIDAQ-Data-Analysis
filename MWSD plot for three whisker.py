##################################################################
#IMPORT NECESSARY PACKAGES
##################################################################

import os

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
pathForTextFile18 = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/20 PSI Sweep_1.txt")

pathForTextFile1 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing with pulse of 2Hz/Tall whisker 10-20-10 50PSI WITH PULSE 2 Hz.txt")

pathForTextFile2 = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/30 PSI Sweep_1.txt")

pathForTextFile3 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 8PSI NO PULSE.txt")

pathForTextFile4 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 10PSI NO PULSE.txt")

pathForTextFile5 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 15PSI NO PULSE.txt")
pathForTextFile6 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 20PSI NO PULSE.txt")
pathForTextFile7 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 25PSI NO PULSE.txt")

pathForTextFile8 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 50PSI NO PULSE.txt")

pathForTextFile9 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 35PSI NO PULSE.txt")
pathForTextFile10 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 40PSI NO PULSE.txt")
pathForTextFile11 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 45PSI NO PULSE.txt")
pathForTextFile12 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 50PSI NO PULSE.txt")
pathForTextFile13 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 60PSI NO PULSE.txt")
pathForTextFile14 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 70PSI NO PULSE.txt")
pathForTextFile15 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 80PSI NO PULSE.txt")
pathForTextFile16 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 90PSI NO PULSE.txt")
pathForTextFile17 = (
    "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/23082019/on off thing no pulse/Tall whisker 10-20-10 100PSI NO PULSE.txt")




##################################################################



##################################################################
#FUNCTION WHICH IS CALLED TO PLOT
##################################################################
def animatex(i):
    graph_data = open(pathForTextFile2,'r').read()
    lines = graph_data.split('\n')
    ts1 = []
    xs1 = []
    x = 0
    for line in lines:
        if len(line) > 1:
            line = line.split(',')
            ts1.append(float(line[0])/2)
            xs1.append(-float(line[1]))
            if float(line[0]) >= 80:
                break;

    #xs=signal.savgol_filter(xs, 1001, 2)
    MWSD1 = pd.Series(xs1)
    data1 = MWSD1.rolling(300).std()

    # graph_data = open(pathForTextFile2,'r').read()
    # lines = graph_data.split('\n')
    # ts2 = []
    # xs2 = []
    # x = 0
    # for line in lines:
    #     if len(line) > 1:
    #         line = line.split(',')
    #         ts2.append(float(line[0]))
    #         xs2.append(-float(line[1]))
    #         if float(line[0]) >= 40:
    #             break;
    #
    # #xs=signal.savgol_filter(xs, 1001, 2)
    # MWSD2 = pd.Series(xs2)
    # data2 = MWSD2.rolling(1000).std()
    #
    #
    # graph_data = open(pathForTextFile3,'r').read()
    # lines = graph_data.split('\n')
    # ts3 = []
    # xs3 = []
    # x = 0
    # for line in lines:
    #     if len(line) > 1:
    #         line = line.split(',')
    #         ts3.append(float(line[0]))
    #         xs3.append(-float(line[1]))
    #         if float(line[0]) >= 40:
    #             break;

    #xs=signal.savgol_filter(xs, 1001, 2)
    # MWSD3 = pd.Series(xs3)
    # data3 = MWSD3.rolling(1000).std()

    graph_data = open(pathForTextFile18,'r').read()
    lines = graph_data.split('\n')
    ts2 = []
    xs2 = []
    x = 0
    for line in lines:
        if len(line) > 1:
            line = line.split(',')
            ts2.append(float(line[0])/2)
            xs2.append(-float(line[1]))
            if float(line[0]) >= 80:
                break;

    #xs2=signal.savgol_filter(xs2, 1001, 2)
    MWSD2 = pd.Series(xs2)
    data2 = MWSD2.rolling(300).std()



    ax1.clear()
    ax1.plot(ts1, data1, '-b', label = 'No pulse')
    ax1.plot(ts2, data2, '-r', label = '2 Hz pulse')
    # ax1.plot(ts3, data3, '-r', label = 'Long Whisker')
    ax1.legend(loc = 'upper left')
    ax1.set_title('Comparison of pulse and no pulse data at 50 PSI Tall Whisker ')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('MWSD of Raw Voltage')
    #ax1.plot(ts, data1)
##################################################################



ani1 = animation.FuncAnimation(fig1, animatex, interval = 30)
plt.show()






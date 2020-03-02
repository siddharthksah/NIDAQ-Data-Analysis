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
pathForTextFile1 = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/10 PSI Sweep_1.txt")

pathForTextFile2 = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/20 PSI Sweep_1.txt")

pathForTextFile3 = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/30 PSI Sweep_1.txt")

pathForTextFile4 = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/40 PSI Sweep_1.txt")

pathForTextFile5 = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/50 PSI Sweep_1.txt")

pathForTextFile6 = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/60 PSI Sweep_1.txt")

pathForTextFile7 = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/70 PSI Sweep_1.txt")

pathForTextFile8 = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/80 PSI Sweep_1.txt")

pathForTextFile9 = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/90 PSI Sweep_1.txt")

pathForTextFile10 = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/100 PSI Sweep_1.txt")



##################################################################



##################################################################
#FUNCTION WHICH IS CALLED TO PLOT
##################################################################
def animatex(i):
    graph_data = open(pathForTextFile1,'r').read()
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

    graph_data = open(pathForTextFile2,'r').read()
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

    graph_data = open(pathForTextFile3, 'r').read()
    lines = graph_data.split('\n')
    ts3 = []
    xs3 = []
    x = 0
    for line in lines:
        if len(line) > 1:
            line = line.split(',')
            ts3.append(float(line[0]) / 2)
            xs3.append(-float(line[1]))
            if float(line[0]) >= 80:
                break;

    # xs2=signal.savgol_filter(xs2, 1001, 2)
    MWSD3 = pd.Series(xs3)
    data3 = MWSD3.rolling(300).std()

    graph_data = open(pathForTextFile4, 'r').read()
    lines = graph_data.split('\n')
    ts4 = []
    xs4 = []
    x = 0
    for line in lines:
        if len(line) > 1:
            line = line.split(',')
            ts4.append(float(line[0]) / 2)
            xs4.append(-float(line[1]))
            if float(line[0]) >= 80:
                break;

    # xs2=signal.savgol_filter(xs2, 1001, 2)
    MWSD4 = pd.Series(xs4)
    data4 = MWSD4.rolling(300).std()

    graph_data = open(pathForTextFile5, 'r').read()
    lines = graph_data.split('\n')
    ts5 = []
    xs5 = []
    x = 0
    for line in lines:
        if len(line) > 1:
            line = line.split(',')
            ts5.append(float(line[0]) / 2)
            xs5.append(-float(line[1]))
            if float(line[0]) >= 80:
                break;

    # xs2=signal.savgol_filter(xs2, 1001, 2)
    MWSD5 = pd.Series(xs5)
    data5 = MWSD5.rolling(300).std()

    graph_data = open(pathForTextFile6, 'r').read()
    lines = graph_data.split('\n')
    ts6 = []
    xs6 = []
    x = 0
    for line in lines:
        if len(line) > 1:
            line = line.split(',')
            ts6.append(float(line[0]) / 2)
            xs6.append(-float(line[1]))
            if float(line[0]) >= 80:
                break;

    # xs2=signal.savgol_filter(xs2, 1001, 2)
    MWSD6 = pd.Series(xs6)
    data6 = MWSD4.rolling(300).std()

    graph_data = open(pathForTextFile7, 'r').read()
    lines = graph_data.split('\n')
    ts7 = []
    xs7 = []
    x = 0
    for line in lines:
        if len(line) > 1:
            line = line.split(',')
            ts7.append(float(line[0]) / 2)
            xs7.append(-float(line[1]))
            if float(line[0]) >= 80:
                break;

    # xs2=signal.savgol_filter(xs2, 1001, 2)
    MWSD7 = pd.Series(xs4)
    data7 = MWSD7.rolling(300).std()

    graph_data = open(pathForTextFile8, 'r').read()
    lines = graph_data.split('\n')
    ts8 = []
    xs8 = []
    x = 0
    for line in lines:
        if len(line) > 1:
            line = line.split(',')
            ts8.append(float(line[0]) / 2)
            xs8.append(-float(line[1]))
            if float(line[0]) >= 80:
                break;

    # xs2=signal.savgol_filter(xs2, 1001, 2)
    MWSD8 = pd.Series(xs8)
    data8 = MWSD8.rolling(300).std()

    graph_data = open(pathForTextFile9, 'r').read()
    lines = graph_data.split('\n')
    ts9 = []
    xs9 = []
    x = 0
    for line in lines:
        if len(line) > 1:
            line = line.split(',')
            ts9.append(float(line[0]) / 2)
            xs9.append(-float(line[1]))
            if float(line[0]) >= 80:
                break;

    # xs2=signal.savgol_filter(xs2, 1001, 2)
    MWSD9 = pd.Series(xs9)
    data9 = MWSD9.rolling(300).std()

    graph_data = open(pathForTextFile10, 'r').read()
    lines = graph_data.split('\n')
    ts10 = []
    xs10 = []
    x = 0
    for line in lines:
        if len(line) > 1:
            line = line.split(',')
            ts10.append(float(line[0]) / 2)
            xs10.append(-float(line[1]))
            if float(line[0]) >= 80:
                break;

    # xs2=signal.savgol_filter(xs2, 1001, 2)
    MWSD10 = pd.Series(xs10)
    data10 = MWSD10.rolling(300).std()





    ax1.clear()
    ax1.plot(ts1, data1, '-b', label = '10 PSI')
    ax1.plot(ts2, data2, '-r', label = '20 PSI')
    ax1.plot(ts3, data3, '-y', label= '30 PSI')
    ax1.plot(ts4, data4, '-g', label='40 PSI')
    ax1.plot(ts5, data5, '-p', label='50 PSI')
    ax1.plot(ts6, data6, '-c', label='60 PSI')
    ax1.plot(ts7, data7, '-m', label='70 PSI')
    ax1.plot(ts8, data8, '-w', label='80 PSI')
    ax1.plot(ts9, data9, '-rs', label='90 PSI')
    ax1.plot(ts10, data10, '-gs', label='100 PSI')
    # ax1.plot(ts3, data3, '-r', label = 'Long Whisker')
    ax1.legend(loc = 'upper left')
    ax1.set_title('Comparison of pulse and no pulse data at 50 PSI Tall Whisker ')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('MWSD of Raw Voltage')
    #ax1.plot(ts, data1)
##################################################################



ani1 = animation.FuncAnimation(fig1, animatex, interval = 30)
plt.show()






##################################################################
# IMPORT NECESSARY PACKAGES
##################################################################

import os

import matplotlib
import matplotlib.animation as animation
import pandas as pd
from matplotlib import style
from scipy import signal
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')  # do this before importing pylab



##################################################################


##################################################################
# CHOOSE THE STYLE FOR THE PLOTTING
##################################################################
style.use('fivethirtyeight')
##################################################################


##################################################################
# DECLARE FIGS
##################################################################

fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)

fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)

fig3 = plt.figure()
ax3 = fig3.add_subplot(1, 1, 1)

fig4 = plt.figure()
ax4 = fig4.add_subplot(1, 1, 1)

fig5 = plt.figure()
ax5 = fig5.add_subplot(1, 1, 1)

fig6 = plt.figure()
ax6 = fig6.add_subplot(1, 1, 1)

fig7 = plt.figure()
ax7 = fig7.add_subplot(1, 1, 1)

fig8 = plt.figure()
ax8 = fig8.add_subplot(1, 1, 1)

fig9 = plt.figure()
ax9 = fig9.add_subplot(1, 1, 1)

fig10 = plt.figure()
ax10 = fig10.add_subplot(1, 1, 1)

fig11 = plt.figure()
ax11 = fig11.add_subplot(1, 1, 1)

fig12 = plt.figure()
ax12 = fig12.add_subplot(1, 1, 1)

fig13 = plt.figure()
ax13 = fig13.add_subplot(1, 1, 1)

fig14 = plt.figure()
ax14 = fig14.add_subplot(1, 1, 1)

fig15 = plt.figure()
ax15 = fig15.add_subplot(1, 1, 1)

fig16 = plt.figure()
ax16 = fig16.add_subplot(1, 1, 1)

##################################################################


##################################################################
# GET THE LOCATION WHERE THE DATA FROM SERIAL IS BEING LOGGED
##################################################################
# location = open('fileLocation.txt','r').read()
# pathForTextFile =  os.path.join(location, "test.txt")   #making path for the text file
pathForTextFile = (
    "D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191212_4X4_Sensor_Array_01/sweep1.txt")


##################################################################


##################################################################
# FUNCTION WHICH IS CALLED TO PLOT
##################################################################
def animatex(i):
    graph_data = open(pathForTextFile, 'r').read()
    lines = graph_data.split('\n')
    ts = []
    xs1 = []
    xs2 = []
    xs3 = []
    xs4 = []
    xs5 = []
    xs6 = []
    xs7 = []
    xs8 = []
    xs9 = []
    xs10 = []
    xs11 = []
    xs12 = []
    xs13 = []
    xs14 = []
    xs15 = []
    xs16 = []

    x = 0
    for line in lines:
        if len(line) > 0:
            # print(line)
            line = line.split()
            ts.append(float(line[0]))
            xs1.append(float("{0:.6f}".format(float(line[1]))))
            xs2.append(float("{0:.6f}".format(float(line[3]))))
            xs3.append(float("{0:.6f}".format(float(line[5]))))
            xs4.append(float("{0:.6f}".format(float(line[7]))))
            xs5.append(float("{0:.6f}".format(float(line[9]))))
            xs6.append(float("{0:.6f}".format(float(line[11]))))
            xs7.append(float("{0:.6f}".format(float(line[13]))))
            xs8.append(float("{0:.6f}".format(float(line[15]))))
            xs9.append(float("{0:.6f}".format(float(line[17]))))
            xs10.append(float("{0:.6f}".format(float(line[19]))))
            xs11.append(float("{0:.6f}".format(float(line[21]))))
            xs12.append(float("{0:.6f}".format(float(line[23]))))
            xs13.append(float("{0:.6f}".format(float(line[25]))))
            xs14.append(float("{0:.6f}".format(float(line[27]))))
            xs15.append(float("{0:.6f}".format(float(line[29]))))
            xs16.append(float("{0:.6f}".format(float(line[31]))))

    rolling_window = 10001

    MWSD1 = pd.Series(xs1)
    data1 = MWSD1.rolling(rolling_window).std()
    MWSD2 = pd.Series(xs2)
    data2 = MWSD2.rolling(rolling_window).std()
    MWSD3 = pd.Series(xs3)
    data3 = MWSD3.rolling(rolling_window).std()
    MWSD4 = pd.Series(xs4)
    data4 = MWSD4.rolling(rolling_window).std()
    MWSD5 = pd.Series(xs5)
    data5 = MWSD5.rolling(rolling_window).std()
    MWSD6 = pd.Series(xs6)
    data6 = MWSD6.rolling(rolling_window).std()
    MWSD7 = pd.Series(xs7)
    data7 = MWSD7.rolling(rolling_window).std()
    MWSD8 = pd.Series(xs8)
    data8 = MWSD8.rolling(rolling_window).std()
    MWSD9 = pd.Series(xs9)
    data9 = MWSD9.rolling(rolling_window).std()
    MWSD10 = pd.Series(xs10)
    data10 = MWSD10.rolling(rolling_window).std()
    MWSD11 = pd.Series(xs11)
    data11 = MWSD11.rolling(rolling_window).std()
    MWSD12 = pd.Series(xs12)
    data12 = MWSD12.rolling(rolling_window).std()
    MWSD13 = pd.Series(xs13)
    data13 = MWSD13.rolling(rolling_window).std()
    MWSD14 = pd.Series(xs14)
    data14 = MWSD14.rolling(rolling_window).std()
    MWSD15 = pd.Series(xs15)
    data15 = MWSD15.rolling(rolling_window).std()
    MWSD16 = pd.Series(xs16)
    data16 = MWSD16.rolling(rolling_window).std()

    ax1.clear()
    ax1.plot(ts, data1, '-b', label='1')
    ax1.legend(loc='upper left')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('MWSD of Raw Voltage')
    fig1.savefig('D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/1.png')

    ax2.clear()
    ax2.plot(ts, data2, '-b', label='2')
    ax2.legend(loc='upper left')
    ax2.set_xlabel('Time(s)')
    ax2.set_ylabel('MWSD of Raw Voltage')
    fig2.savefig('D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/2.png')

    ax3.clear()
    ax3.plot(ts, data3, '-b', label='3')
    ax3.legend(loc='upper left')
    ax3.set_xlabel('Time(s)')
    ax3.set_ylabel('MWSD of Raw Voltage')
    fig3.savefig(
        'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/3.png')


    ax4.clear()
    ax4.plot(ts, data4, '-b', label='4')
    ax4.legend(loc='upper left')
    ax4.set_xlabel('Time(s)')
    ax4.set_ylabel('MWSD of Raw Voltage')
    fig4.savefig(
        'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/4.png')

    ax5.clear()
    ax5.plot(ts, data5, '-b', label='5')
    ax5.legend(loc='upper left')
    ax5.set_xlabel('Time(s)')
    ax5.set_ylabel('MWSD of Raw Voltage')
    fig5.savefig(
        'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/5.png')

    ax6.clear()
    ax6.plot(ts, data6, '-b', label='6')
    ax6.legend(loc='upper left')
    ax6.set_xlabel('Time(s)')
    ax6.set_ylabel('MWSD of Raw Voltage')
    fig6.savefig(
        'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/6.png')

    ax7.clear()
    ax7.plot(ts, data7, '-b', label='7')
    ax7.legend(loc='upper left')
    ax7.set_xlabel('Time(s)')
    ax7.set_ylabel('MWSD of Raw Voltage')
    fig7.savefig(
        'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/7.png')

    ax8.clear()
    ax8.plot(ts, data8, '-b', label='8')
    ax8.legend(loc='upper left')
    ax8.set_xlabel('Time(s)')
    ax8.set_ylabel('MWSD of Raw Voltage')
    fig8.savefig(
        'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/8.png')

    ax9.clear()
    ax9.plot(ts, data9, '-b', label='9')
    ax9.legend(loc='upper left')
    ax9.set_xlabel('Time(s)')
    ax9.set_ylabel('MWSD of Raw Voltage')
    fig9.savefig(
        'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/9.png')

    ax10.clear()
    ax10.plot(ts, data10, '-b', label='10')
    ax10.legend(loc='upper left')
    ax10.set_xlabel('Time(s)')
    ax10.set_ylabel('MWSD of Raw Voltage')
    fig10.savefig(
        'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/10.png')

    ax11.clear()
    ax11.plot(ts, data11, '-b', label='11')
    ax11.legend(loc='upper left')
    ax11.set_xlabel('Time(s)')
    ax11.set_ylabel('MWSD of Raw Voltage')
    fig11.savefig(
        'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/11.png')

    ax12.clear()
    ax12.plot(ts, data12, '-b', label='12')
    ax12.legend(loc='upper left')
    ax12.set_xlabel('Time(s)')
    ax12.set_ylabel('MWSD of Raw Voltage')
    fig12.savefig(
        'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/12.png')

    ax13.clear()
    ax13.plot(ts, data13, '-b', label='13')
    ax13.legend(loc='upper left')
    ax13.set_xlabel('Time(s)')
    ax13.set_ylabel('MWSD of Raw Voltage')
    fig13.savefig(
        'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/13.png')

    ax14.clear()
    ax14.plot(ts, data14, '-b', label='14')
    ax14.legend(loc='upper left')
    ax14.set_xlabel('Time(s)')
    ax14.set_ylabel('MWSD of Raw Voltage')
    fig14.savefig(
        'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/14.png')

    ax15.clear()
    ax15.plot(ts, data15, '-b', label='15')
    ax15.legend(loc='upper left')
    ax15.set_xlabel('Time(s)')
    ax15.set_ylabel('MWSD of Raw Voltage')
    fig15.savefig(
        'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/15.png')

    ax16.clear()
    ax16.plot(ts, data16, '-b', label='16')
    ax16.legend(loc='upper left')
    ax16.set_xlabel('Time(s)')
    ax16.set_ylabel('MWSD of Raw Voltage')
    fig16.savefig(
        'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/16.png')
    #print(xs1)


ani1 = animation.FuncAnimation(fig1, animatex, interval=30)
plt.show()

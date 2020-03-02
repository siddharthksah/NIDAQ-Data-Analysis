import matplotlib
import matplotlib.animation as animation
from matplotlib import style
from scipy import signal
import pandas as pd
matplotlib.use('TkAgg')  # do this before importing pylab
import matplotlib.pyplot as plt

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# location = open('fileLocation.txt','r').read()
pathForTextFile = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/190919_01/Red Base Copper Wire[21] Ball Bearing 20PSI/sweep3.txt")


# pathForTextFile =  os.path.join(location, "test.txt")   #making path for the text file


def animate(i):
    graph_data = open(pathForTextFile, 'r').read()
    lines = graph_data.split('\n')
    ts = []
    xs = []
    x = 0

    for line in lines:
        if len(line) > 1:
            line = line.split(',')
            #ts.append(float(line[0])/10)
            ts.append(float(line[0]))
            xs.append((float(line[1])))
            # if float(line[0]) >= 0.4:
            #     break;
    #xs1=signal.savgol_filter(xs, 1001, 2)
    MWSD1 = pd.Series(xs)
    data1 = MWSD1.rolling(100).std()

    ax1.clear()
    # ax1.plot(ts, xs, '-b', label='40 Hz at 40 PSI of 15 mm whisker kept at 35 mm from the pressure dispenser source')
    ax1.plot(ts, xs, '-b', label='RAW V')
    ax1.plot(ts, data1, '-r', label = 'MWSD(V)')
    ax1.set_title('10 PSI 10 Hz')
    ax1.legend(loc='upper right')
    #ax1.set_xlabel('Frequency(Hz)')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Voltage(V)')


ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()

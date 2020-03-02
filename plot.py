import matplotlib
import matplotlib.animation as animation
from matplotlib import style
from scipy import signal
matplotlib.use('TkAgg')  # do this before importing pylab
import matplotlib.pyplot as plt

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# location = open('fileLocation.txt','r').read()
pathForTextFile = (
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/200130_Ball Bearing Whisker Vortex Gun Underwater/2020-01-30_17-05-18/test.txt")


# pathForTextFile =  os.path.join(location, "test.txt")   #making path for the text file


def animate(i):
    graph_data = open(pathForTextFile, 'r').read()
    lines = graph_data.split('\n')
    ts = []
    xs = []
    x = 0
    y = 0

    for line in lines:
        if len(line) > 1:
            #line = line.split('')
            #ts.append(float(line[0])/10)
            if (len(line)) > 0:
                #ts.append(float(line[0]))
                xs.append(float((float(line))))
                y = y + 0.005
                ts.append(y)
            # if float(line[0]) >= 40:
            #      break;
    #xs=signal.savgol_filter(xs, 5301, 2)
    ax1.clear()
    # ax1.plot(ts, xs, '-b', label='40 Hz at 40 PSI of 15 mm whisker kept at 35 mm from the pressure dispenser source')
    ax1.plot(ts, xs, '-b', label='Pillar')
    ax1.legend(loc='upper left')
    #ax1.set_xlabel('Frequency(Hz)')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Raw Voltage(V)')


ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()

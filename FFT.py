import matplotlib.animation as animation
from matplotlib import style
import time
import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np
from plotly.offline import *
import os


# style.use('fivethirtyeight')

# location = open('fileLocation.txt','r').read()
# pathForTextFile =  os.path.join(location, "test.txt")   #making path for the text file
pathForTextFile = ("C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/14082019/40 PSI/40 Hz/v vs t.txt")

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)



graph_data = open(pathForTextFile,'r').read()
lines = graph_data.split('\n')
ts = []
xs = []
x = 0
for line in lines:
    if len(line) > 1:
        line = line.split()
        ts.append(float(line[0]))
        xs.append(float(line[1]))



Fs = 25000.0;  # sampling rate
n = len(xs) # length of the signal
k = np.arange(n)
T = n/Fs

frq = k/T # two sides frequency range
frq = frq[range(int(n/2))] # one side frequency range

Y = np.fft.fft(xs)/n # fft computing and normalization
Y = Y[range(int(n/2))]

fig, ax = plt.subplots(2, 1)
ax[0].plot(ts,xs)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
plt.show()
#plot_url = py.offline.plot_mpl(fig, filename='mpl-basic-fft')






















fourierTransform = np.fft.fft(xs)


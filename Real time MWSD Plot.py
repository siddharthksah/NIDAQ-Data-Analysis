import time
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import nidaqmx
import pandas as pd

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []


start_time = time.time()

rolling_window = 1000
numberofsamples = 1000
n = 1
def animate(i, xs, ys):

    global n

    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev6/ai0")
        data = task.read(number_of_samples_per_channel = numberofsamples)

    for i in range(numberofsamples):
        xs.append(n/10000)
        n = n + 1

    #print(xs)
    for elements in data:
        ys.append(elements)

    #print(ys)
    MWSD = pd.Series(ys)

    data1 = MWSD.rolling(rolling_window).std()

    # Draw x and y lists
    ax.clear()
    #ax.plot(xs, data1)
    ax.plot(xs, data1)

    plt.ylabel('MWSD')
    plt.xlabel('Time(s)')

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=30)
plt.show()


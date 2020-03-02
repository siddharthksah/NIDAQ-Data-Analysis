
# ##################################################################
# #IMPORT NECESSARY PACKAGES
# ##################################################################

import time
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import nidaqmx


# ##################################################################
# #DECLARE FIGS
# ##################################################################
#
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# ##################################################################

xs = []
ys = []

start_time = time.time()

def animate(i, xs, ys):
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        data = task.read(number_of_samples_per_channel=1)


    xs.append(time.time() - start_time)
    ys.append(data[0])

    ax.clear()
    ax.plot(xs, ys)

    plt.title('Real time Raw Voltage')
    plt.ylabel('Raw Voltage(V)')
    plt.xlabel('Time(s)')


ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=10)
plt.show()

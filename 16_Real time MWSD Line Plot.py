import time
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import nidaqmx
import pandas as pd

# Create figure for plotting
plt.ion()
fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)

# fig2 = plt.figure()
# ax2 = fig2.add_subplot(1, 1, 1)
#
# fig3 = plt.figure()
# ax3 = fig3.add_subplot(1, 1, 1)
#
# fig4 = plt.figure()
# ax4 = fig4.add_subplot(1, 1, 1)

xs = []
ys1 = []
ys2 = []
ys3 = []
ys4 = []


start_time = time.time()

rolling_window = 1000
numberofsamples = 1000
n = 1
def animate(i):

    global n

    with nidaqmx.Task() as task:

        task.ai_channels.add_ai_voltage_chan("Dev6/ai0")
        task.ai_channels.add_ai_voltage_chan("Dev6/ai1")
        task.ai_channels.add_ai_voltage_chan("Dev6/ai2")
        task.ai_channels.add_ai_voltage_chan("Dev6/ai3")
        # task.ai_channels.add_ai_voltage_chan("Dev1/ai4")
        # task.ai_channels.add_ai_voltage_chan("Dev1/ai5")
        # task.ai_channels.add_ai_voltage_chan("Dev1/ai6")
        # task.ai_channels.add_ai_voltage_chan("Dev1/ai7")
        # task.ai_channels.add_ai_voltage_chan("Dev1/ai16")
        # task.ai_channels.add_ai_voltage_chan("Dev1/ai17")
        # task.ai_channels.add_ai_voltage_chan("Dev1/ai18")
        # task.ai_channels.add_ai_voltage_chan("Dev1/ai19")
        # task.ai_channels.add_ai_voltage_chan("Dev1/ai20")
        # task.ai_channels.add_ai_voltage_chan("Dev1/ai21")
        # task.ai_channels.add_ai_voltage_chan("Dev1/ai22")
        # task.ai_channels.add_ai_voltage_chan("Dev1/ai23")
        data = task.read(number_of_samples_per_channel = numberofsamples)

    for i in range(numberofsamples):
        xs.append(n/1000)
        n = n + 1

    #print(xs)
    for elements in data[0]:
        ys1.append(elements)

    # for elements in data[1]:
    #     ys2.append(elements)
    #
    # for elements in data[2]:
    #     ys2.append(elements)
    #
    # for elements in data[3]:
    #     ys2.append(elements)

    #print(ys)
    MWSD1 = pd.Series(ys1)
    data1 = MWSD1.rolling(rolling_window).std()

    # MWSD2 = pd.Series(ys2)
    # data2 = MWSD2.rolling(rolling_window).std()
    #
    # MWSD3 = pd.Series(ys3)
    # data3 = MWSD3.rolling(rolling_window).std()
    #
    # MWSD4 = pd.Series(ys4)
    # data4 = MWSD4.rolling(rolling_window).std()

    # Draw x and y lists
    ax1.clear()
    #ax.plot(xs, data1)
    ax1.plot(xs, data1)

    # ax2.clear()
    # # ax.plot(xs, data1)
    # ax2.plot(xs, data2)
    #
    # ax3.clear()
    # # ax.plot(xs, data1)
    # ax3.plot(xs, data3)
    #
    # ax4.clear()
    # # ax.plot(xs, data1)
    # ax4.plot(xs, data4)

    ax1.ylabel('MWSD')
    ax1.xlabel('Time(s)')
    #plt.pause(0.01)
ani = animation.FuncAnimation(fig1, animate, interval=30)
plt.show()


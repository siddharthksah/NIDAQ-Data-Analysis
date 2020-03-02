import nidaqmx
import matplotlib.pyplot as plt
import numpy
import pandas as pd
fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
import time

plt.ion()
i=0
data_array = []
with nidaqmx.Task() as task:
     task.ai_channels.add_ai_voltage_chan("Dev6/ai0")
     #task.read()
     start_time = time.time()
     data=task.read(number_of_samples_per_channel=1)
     #print(data)
     data_array.append(data)
     MWSD1 = pd.Series(data_array)
     data1 = MWSD1.rolling(1000).std()
     ax1.clear()
     # ax1.plot(ts, data1, '-b', label = 'Frequency 15Hz 21Hz 24Hz at middle 20 mm from the pressure dispenser source')
     # ax1.plot(ts, data1, '-b', label='Frequency Sweep 1 to 30 Hz at middle 20 mm from the pressure dispenser source')
     ax1.plot(ts, data1, '-b', label='Sweep')
     ax1.legend(loc='upper left')
     ax1.set_xlabel('Freq(Hz)')
     # ax1.set_xlabel('Time(s)')
     ax1.set_ylabel('MWSD of Raw Voltage')
     # # ax1.plot(ts, data1)
     # #plt.scatter(i/10, data[0])
     # plt.plot(i, data[0])
     # # plt.show()
     # plt.xlabel ('Time (s)')
     # plt.ylabel ('Voltage (V)')
     # plt.pause(0.000001)
     # #plt.show()
     # i=i+1

stop_time = time.time() - start_time
print(stop_time)
total_data = (len(data_array))
print(total_data)
#daq_rate = float(total_data) / float(stop_time)
#print(daq_rate)
#numpy.savetxt("savedata1.csv", data_array)


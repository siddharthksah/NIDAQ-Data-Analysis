import nidaqmx
import matplotlib.pyplot as plt

plt.ion()
fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
fig3 = plt.figure()
ax3 = fig3.add_subplot(1, 1, 1)
fig4 = plt.figure()
ax4 = fig4.add_subplot(1, 1, 1)
i=0

with nidaqmx.Task() as task:
     task.ai_channels.add_ai_voltage_chan("Dev6/ai0")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai1")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai2")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai3")
     while i<3000:
         data=task.read(number_of_samples_per_channel=1)

         ax1.scatter(i,data[0], c= 'b')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax2.scatter(i, data[1], c='g')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax3.scatter(i, data[2], c='r')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax4.scatter(i, data[3], c='y')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         #plt.xlim([0, 256])
         plt.pause(0.01)
         i=i+1
         print (data)
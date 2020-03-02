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


i=0

with nidaqmx.Task() as task:
     task.ai_channels.add_ai_voltage_chan("Dev6/ai0")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai1")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai2")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai3")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai4")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai5")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai6")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai7")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai16")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai17")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai18")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai19")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai20")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai21")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai22")
     task.ai_channels.add_ai_voltage_chan("Dev6/ai23")


     while i<30000:
         data=task.read(number_of_samples_per_channel=1000)

         ax1.scatter(i,data[0], c= 'b')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")


         ax2.scatter(i,data[1],c='g')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax3.scatter(i,data[2],c='r')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax4.scatter(i, data[3], c='c')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax5.scatter(i, data[4], c='m')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax6.scatter(i, data[5], c='y')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax7.scatter(i, data[6], c='k')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax8.scatter(i, data[7], c='r')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax9.scatter(i, data[8], c='b')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax10.scatter(i, data[9], c='g')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax11.scatter(i, data[10], c='r')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax12.scatter(i, data[11], c='c')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax13.scatter(i, data[12], c='m')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax14.scatter(i, data[13], c='y')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax15.scatter(i, data[14], c='k')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         ax16.scatter(i, data[15], c='r')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         #plt.xlim([0, 256])
         plt.pause(0.00001)
         i=i+1
         print (data)
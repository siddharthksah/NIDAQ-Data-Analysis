import nidaqmx
import matplotlib.pyplot as plt
import pandas as pd

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

numberofsamples = 1000
xs = []
i=0

rolling_window = 1000

with nidaqmx.Task() as task:
     global n
     n = 0
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


     while i<3000:
         data=task.read(number_of_samples_per_channel=numberofsamples)

         for i in range(numberofsamples):
             xs.append(n / 1000)
             n = n + 1

         MWSD1 = pd.Series(data[0])
         data1 = MWSD1.rolling(rolling_window).std()
         ax1.scatter(xs,data1, c= 'b')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD2 = pd.Series(data[1])
         data2 = MWSD2.rolling(rolling_window).std()
         ax2.scatter(xs,data2,c='g')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD3 = pd.Series(data[2])
         data3 = MWSD3.rolling(rolling_window).std()
         ax3.scatter(xs,data3,c='r')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD4 = pd.Series(data[3])
         data4 = MWSD4.rolling(rolling_window).std()
         ax4.scatter(xs, data4, c='c')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD5 = pd.Series(data[4])
         data5 = MWSD5.rolling(rolling_window).std()
         ax5.scatter(xs, data5, c='m')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD6 = pd.Series(data[5])
         data6 = MWSD6.rolling(rolling_window).std()
         ax6.scatter(xs, data6, c='y')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD7 = pd.Series(data[6])
         data7 = MWSD7.rolling(rolling_window).std()
         ax7.scatter(xs, data7, c='k')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD8 = pd.Series(data[7])
         data8 = MWSD8.rolling(rolling_window).std()
         ax8.scatter(xs, data8, c='w')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD9 = pd.Series(data[8])
         data9 = MWSD9.rolling(rolling_window).std()
         plt.scatter(xs, data9, c='b')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD10 = pd.Series(data[9])
         data10 = MWSD10.rolling(rolling_window).std()
         plt.scatter(xs, data10, c='g')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD11 = pd.Series(data[10])
         data11 = MWSD11.rolling(rolling_window).std()
         plt.scatter(xs, data11, c='r')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD12 = pd.Series(data[11])
         data12 = MWSD12.rolling(rolling_window).std()
         plt.scatter(xs, data12, c='c')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD13 = pd.Series(data[12])
         data13 = MWSD13.rolling(rolling_window).std()
         plt.scatter(xs, data13, c='m')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD14 = pd.Series(data[13])
         data14 = MWSD14.rolling(rolling_window).std()
         plt.scatter(xs, data14, c='y')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD15 = pd.Series(data[14])
         data15 = MWSD15.rolling(rolling_window).std()
         plt.scatter(xs, data15, c='k')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         MWSD16 = pd.Series(data[15])
         data16 = MWSD16.rolling(rolling_window).std()
         plt.scatter(xs, data16, c='w')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")

         #plt.xlim([0, 256])
         plt.pause(0.01)
         i=i+1
         print (data)
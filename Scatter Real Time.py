import nidaqmx
import matplotlib.pyplot as plt

plt.ion()
plt.figure()

i=0

with nidaqmx.Task() as task:
     task.ai_channels.add_ai_voltage_chan("Dev6/ai0")
     while i<300:
         data=task.read(number_of_samples_per_channel=1)
         plt.scatter(i,data[0], c= 'b')
         plt.ylabel("Raw Voltage (V)")
         plt.xlabel("Time(s)")
         #plt.xlim([0, 256])
         plt.pause(0.01)
         i=i+1
         print (data)
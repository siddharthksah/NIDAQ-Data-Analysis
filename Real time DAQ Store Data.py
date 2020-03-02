##################################################################
#IMPORT NECESSARY PACKAGES
##################################################################
import datetime
import os
import sys
import time
from time import sleep
import matplotlib.pyplot as plt
import nidaqmx
import serial

##################################################################



##################################################################
#CREATE THE TEXT FILE TO STORE COM DATA AND CLEAR IT EVERYTIME THE CODE IS RUN
##################################################################
mydir = os.path.join("D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/200130_Ball Bearing Whisker Vortex Gun Underwater/", datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) #mydir is essentially the time stamp and the os path combined
os.makedirs(mydir) #makes the directory with mydir as the name
open('D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/200130_Ball Bearing Whisker Vortex Gun Underwater/fileLocation.txt', 'w').close()
with open('D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/200130_Ball Bearing Whisker Vortex Gun Underwater/fileLocation.txt', "a+") as output:
    output.write(mydir)
outfile =  os.path.join(mydir, "test.txt")   #making path for the text file
##################################################################



##################################################################
#RUN LOOP TO READ AND STORE DATA IN THE TEXT FILE
##################################################################
p = 0
start_time = time.time()
with open(outfile,'a+') as f:
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        while True:
            p = p + 1
            data = task.read(number_of_samples_per_channel=1)
            data = (str(data[0])[0:-10])
            #data = data[1:-1]
            #print(data)
            f.write(data)
            f.write('\n')
            #print("Working!")
            #print(p)
            # if p == 10000:
            #    print(time.time() - start_time)
            #    # print(time.ctime(int(start_time)))
            #    # print(time.ctime(int(time.time())))
            #    break;

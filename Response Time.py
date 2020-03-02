import matplotlib
import matplotlib.animation as animation

matplotlib.use('TkAgg') # do this before importing pylab
import matplotlib.pyplot as plt

from scipy import signal

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


import numpy
import numpy as np
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]













pathForTextFile = ("D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191011/Response_Time_Test/[22]/5s 30s 20s 70PSI.txt")



graph_data = open(pathForTextFile,'r').read()
lines = graph_data.split('\n')
ts = []
xs = []
x = 0
for line in lines:
    if len(line) > 1:
        line = line.split(' ')
        ts.append(float(line[0]))
        xs.append(float(line[1]))
#print(xs)
# print(ts)
xsonethird = xs[:len(xs)//3]
#print(xsonethird)


maxvalue = (max(xsonethird))
minvalue = (min(xsonethird))

tenpercentvalue = ((minvalue + 0.1*(maxvalue - minvalue)))
nintypercentvalue = ((minvalue + 0.9*(maxvalue - minvalue)))

tenpercentvalue = find_nearest(xsonethird, tenpercentvalue)
nintypercentvalue = (find_nearest(xsonethird, nintypercentvalue))

xsonethirdnp = numpy.array(xsonethird)

indexoftenpercent = (xsonethird.index(tenpercentvalue))
indexofnintypercent = (xsonethird.index((nintypercentvalue)))

responsetimereal = (ts[indexofnintypercent]) - (ts[indexoftenpercent])
print(responsetimereal)

# maxelement = numpy.where(xsonethirdnp == numpy.amax(xsonethirdnp))
# minelement = numpy.where(xsonethirdnp == numpy.amin(xsonethirdnp))
#
#
# maxelementindex = int(maxelement[0])
# minelementindex = int(minelement[0])
#
# tenpercent = int(round(minelementindex + 0.1*(maxelementindex - minelementindex)))
# nintypercent = int(round(minelementindex + 0.9*(maxelementindex - minelementindex)))
#print(tenpercent)
#print(nintypercent)
#print((minelementindex))
#print(maxelementindex)
#print(int(minelementindex))
# responsetime = (ts[nintypercent]) - (ts[tenpercent])
# print("The response time: ")
# print(responsetime)


# xslastonethird = xs[len(xs)//3:]
# #print(xslastonethird)
# #print(xsonethird)
# # print(max(xslastonethird))
# # print(min(xslastonethird))
# xslastonethirdnp = numpy.array(xslastonethird)
# maxelementlast = numpy.where(xslastonethirdnp == numpy.amax(xslastonethirdnp))
# minelementlast = numpy.where(xslastonethirdnp == numpy.amin(xslastonethirdnp))
#
# maxelementindexlast = int(maxelementlast[0])
# minelementindexlast = int(minelementlast[0])
# # print(maxelementindexlast)
# # print(minelementindexlast)
# thirtyeightpointsixpercent = int(round(minelementindexlast + 0.632*(maxelementindexlast - minelementindexlast)))
# # print(thirtyeightpointsixpercent)
# #print(tenpercent)
# #print(nintypercent)
# #print((minelementindex))
# #print(maxelementindex)
# #print(int(minelementindex))
# responsetimelast = (ts[thirtyeightpointsixpercent] -ts[maxelementindexlast])
# print("The last response time: ")
# print(responsetimelast)



xslastonethird = xs[len(xs)//3: ]
#print(xsonethird)


maxvaluelast = (max(xslastonethird))
minvaluelast = (min(xslastonethird))

maxelementlast = numpy.where(xslastonethird == numpy.amax(xslastonethird))
maxelementlast = int(maxelementlast[0])
#print(maxelementlast)

thirtyeightpointsixpercent = ((minvaluelast + 0.368*(maxvaluelast - minvaluelast)))
thirtyeightpointsixpercent = find_nearest(xslastonethird, thirtyeightpointsixpercent)
#print(thirtyeightpointsixpercent)


xslastonethirdnp = numpy.array(xslastonethird)

indexofthirtyeightpointsixpercent = (xslastonethird.index(thirtyeightpointsixpercent))
#print(indexofthirtyeightpointsixpercent)

responsetime = ((ts[indexofthirtyeightpointsixpercent] - ts[maxelementlast]) )
print(responsetime)

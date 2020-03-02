import numpy

def getEquidistantPoints(p1, p2, parts):
    return zip(numpy.linspace(p1[0], p2[0], parts+1), numpy.linspace(p1[1], p2[1], parts+1))

item = (list(getEquidistantPoints((147.413,1.016), (152.784,6.378) , 10)))

for items in item:
    print (items)

# print(item[1][1])
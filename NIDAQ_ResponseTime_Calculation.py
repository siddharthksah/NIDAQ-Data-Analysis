"""
NIDAQ_ResponseTime_Calculation.py

This script calculates the response time from a data file obtained from a NIDAQ device.

Author: Siddharth Kumar (www.siddharthsah.com)

"""

import numpy as np
import matplotlib.pyplot as plt

def find_nearest(array, value):
    """
    Finds the nearest value in an array to a given value.

    Args:
        array (numpy.array): The array to search in.
        value (float): The value to find the closest match to.

    Returns:
        float: The closest value in the array to the given value.
    """
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def main():
    """
    The main function reads the data file, calculates the response times and prints them.

    Returns:
        None
    """
    pathForTextFile = "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191011/Response_Time_Test/[22]/5s 30s 20s 70PSI.txt"

    # Read the data file
    with open(pathForTextFile,'r') as file:
        lines = file.read().split('\n')

    # Initialize time and data lists
    ts = []
    xs = []

    # Parse the data file
    for line in lines:
        if len(line) > 1:
            line = line.split(' ')
            ts.append(float(line[0]))
            xs.append(float(line[1]))

    # Calculate the response times
    responsetimereal, responsetime = calculate_response_times(ts, xs)

    # Print the response times
    print(f"The first response time: {responsetimereal}")
    print(f"The last response time: {responsetime}")

def calculate_response_times(ts, xs):
    """
    Calculate the response times from the time and data arrays.

    Args:
        ts (list): The time values.
        xs (list): The data values.

    Returns:
        float: The real response time.
        float: The last response time.
    """
    xsonethird = xs[:len(xs)//3]
    maxvalue = max(xsonethird)
    minvalue = min(xsonethird)

    tenpercentvalue = find_nearest(xsonethird, minvalue + 0.1*(maxvalue - minvalue))
    nintypercentvalue = find_nearest(xsonethird, minvalue + 0.9*(maxvalue - minvalue))

    indexoftenpercent = xsonethird.index(tenpercentvalue)
    indexofnintypercent = xsonethird.index(nintypercentvalue)

    responsetimereal = ts[indexofnintypercent] - ts[indexoftenpercent]

    xslastonethird = xs[len(xs)//3:]
    maxvaluelast = max(xslastonethird)
    minvaluelast = min(xslastonethird)

    thirtyeightpointsixpercent = find_nearest(xslastonethird, minvaluelast + 0.368*(maxvaluelast - minvaluelast))

    indexofthirtyeightpointsixpercent = xslastonethird.index(thirtyeightpointsixpercent)
    maxelementlast = np.argmax(xslastonethird)

    responsetime = ts[indexofthirtyeightpointsixpercent] - ts[maxelementlast]

    return responsetimereal, responsetime

if __name__ == "__main__":
    main()

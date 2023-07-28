"""
NationalInstrumentDataAcquisitionDataVisualizer.py

This script is designed for the visualizing data acquired from the National Instrument Data Acquisition (NIDAQ) device. 
The data is read from a file, processed and plotted for visual inspection. This script uses matplotlib for plotting, scipy 
for data processing and pandas for data handling.

Author: Siddharth Kumar (www.siddharthsah.com)

Note: File paths are hard-coded and should be updated to reflect the location of the source data and desired destination of plots.

The script is organized as follows:
1. Import necessary packages
2. Set plot style
3. Declare figures
4. Specify the location of the source data
5. Define a function for processing and plotting the data
6. Initiate the data processing and plotting
"""

import os
import matplotlib
import matplotlib.animation as animation
import pandas as pd
from matplotlib import style
from scipy import signal
import matplotlib.pyplot as plt
from typing import List

# Set the backend of matplotlib to 'TkAgg'
matplotlib.use('TkAgg')

# Set the style for the plotting
style.use('fivethirtyeight')

# Create a list to store the figures and axes
figures, axes = [], []
# Generate 16 figures and their corresponding axes
for _ in range(16):
    fig, ax = plt.subplots()
    figures.append(fig)
    axes.append(ax)

# Specify the location of the data file
data_file_path = (
    "D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191212_4X4_Sensor_Array_01/sweep1.txt")

# Error message in case of file not found
FILE_NOT_FOUND_ERROR_MESSAGE = f"Error: The data file was not found at the specified location: {data_file_path}"


def animate(i: int):
    """
    Process and plot the data.
    The function reads data from a file, processes the data, and plots the data.

    :param i: An integer that represents the current frame of the animation.
    :return: None
    """
    # Check if the file exists
    if not os.path.isfile(data_file_path):
        print(FILE_NOT_FOUND_ERROR_MESSAGE)
        return

    # Read the data from the file
    try:
        with open(data_file_path, 'r') as file:
            lines = file.read().split('\n')
    except Exception as e:
        print(f"Error while reading the file: {e}")
        return

    # Create empty lists for storing time and sensor data
    ts = []
    xs = [[] for _ in range(16)]

    # Extract data from each line
    for line in lines:
        if line:  # If the line is not empty
            data = line.split()
            ts.append(float(data[0]))

            for i in range(16):
                xs[i].append(float("{0:.6f}".format(float(data[i * 2 + 1]))))

    # Set the parameter for smoothing the data
    smooth_para = 4001

    # Smooth the data using Savitzky-Golay filter
    for i in range(16):
        xs[i] = signal.savgol_filter(xs[i], smooth_para, 2)

    # Plot the data
    for i in range(16):
        ax = axes[i]
        fig = figures[i]

        ax.clear()
        ax.plot(ts, xs[i], '-b', label=f'{i + 1}')
        ax.legend(loc='upper left')
        ax.set_xlabel('Time(s)')
        ax.set_ylabel('MWSD of Raw Voltage')

        save_path = f'D:\SMP\OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/{i + 1}.png'
        fig.savefig(save_path)


ani = animation.FuncAnimation(figures[0], animate, interval=1000)
plt.show()

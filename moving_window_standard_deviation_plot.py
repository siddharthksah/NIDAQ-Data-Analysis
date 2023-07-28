"""
This script processes and visualizes the data from the Whiskers Array Sensing project.
It plots the Moving Window Standard Deviation (MWSD) of Raw Voltage over time for different PSI values.
The data files are assumed to be in the format with comma-separated values (CSV) where the first column is time and the second column is voltage.

Author: Siddharth Kumar (www.siddharthsah.com)
"""

import os
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal
from matplotlib import style

# Set the style for the plotting
style.use('fivethirtyeight')

# Declare the plot figure
fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)

# Define the file paths for the data files
file_paths = [
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/10 PSI Sweep_1.txt",
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/20 PSI Sweep_1.txt",
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/30 PSI Sweep_1.txt",
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/40 PSI Sweep_1.txt",
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/50 PSI Sweep_1.txt",
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/60 PSI Sweep_1.txt",
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/70 PSI Sweep_1.txt",
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/80 PSI Sweep_1.txt",
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/90 PSI Sweep_1.txt",
    "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/100 PSI Sweep_1.txt"
]

def process_file(file_path):
    """
    Function to read and process data file. Extracts time and voltage data. 

    Args:
        file_path: str. Path to the data file.

    Returns:
        Tuple of time and voltage data.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read().split('\n')

        ts = []
        xs = []
        for line in data:
            if len(line) > 1:
                time, voltage = map(float, line.split(','))
                ts.append(time/2)
                xs.append(-voltage)
                if time >= 80:
                    break

        return ts, pd.Series(xs).rolling(300).std()

    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return [], []

def animate(i):
    """
    Function which is called to plot the data.

    Args:
        i: int. Frame number.
    """
    ax1.clear()
    colors = ['-b', '-r', '-y', '-g', '-p', '-c', '-m', '-w', '-rs', '-gs']
    for file_path, color, psi in zip(file_paths, colors, range(10, 110, 10)):
        ts, data = process_file(file_path)
        ax1.plot(ts, data, color, label=f'{psi} PSI')

    ax1.legend(loc='upper left')
    ax1.set_title('Comparison of pulse and no pulse data at 50 PSI Tall Whisker')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('MWSD of Raw Voltage')

# Start the animation
ani1 = animation.FuncAnimation(fig1, animate, interval=30)
plt.show()

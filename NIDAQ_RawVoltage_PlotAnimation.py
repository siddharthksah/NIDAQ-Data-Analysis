"""
NIDAQ_RawVoltage_PlotAnimation.py

This script opens a file containing raw voltage data acquired from a NIDAQ device and 
animates a line plot showing voltage as a function of time.

Author: Siddharth Kumar (www.siddharthsah.com)
"""

import matplotlib
import matplotlib.animation as animation
from matplotlib import style
from scipy import signal

# Ensure 'TkAgg' is set before importing pyplot
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Set the graph style
style.use('fivethirtyeight')

def animate(i, path_for_text_file):
    """
    This function reads the data from a file and animates a line plot.

    Args:
        i: The current frame index.
        path_for_text_file: The path to the text file containing the data.

    Returns:
        None
    """
    # Clear the plot
    ax1.clear()

    try:
        with open(path_for_text_file, 'r') as file:
            graph_data = file.read()
    except FileNotFoundError:
        print(f"Error: {path_for_text_file} does not exist.")
        return

    lines = graph_data.split('\n')
    ts = []
    xs = []
    y = 0

    for line in lines:
        if len(line) > 1:
            try:
                voltage = float(line)
            except ValueError:
                print(f"Error: Invalid data '{line}'")
                continue

            xs.append(voltage)
            y += 0.005
            ts.append(y)

    ax1.plot(ts, xs, '-b', label='Pillar')
    ax1.legend(loc='upper left')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('Raw Voltage(V)')

if __name__ == "__main__":
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    
    # Define the file path here
    path_for_text_file = (
        "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/200130_Ball Bearing Whisker Vortex Gun Underwater/2020-01-30_17-05-18/test.txt"
    )
    
    ani = animation.FuncAnimation(fig, animate, fargs=(path_for_text_file,), interval=10)
    plt.show()

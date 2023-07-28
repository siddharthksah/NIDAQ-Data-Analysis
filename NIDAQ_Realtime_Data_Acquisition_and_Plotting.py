"""
NIDAQ_Realtime_Data_Acquisition_and_Plotting.py

A script to perform real-time acquisition of voltage data from a NIDAQ device, and animate a
rolling standard deviation plot of the captured data.

Author: Siddharth Kumar (www.siddharthsah.com)
"""

# Standard library imports
import os

# Third party imports
import nidaqmx
import pandas as pd
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt

# Setting the appropriate backend before importing pyplot
matplotlib.use('TkAgg')

def acquire_voltage_data():
    """
    Acquires a voltage data sample from a NIDAQ device.

    Returns:
        float: The acquired data sample.
    """
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        data = task.read(number_of_samples_per_channel=1)
    return data[0]

def animate(i, ys, ax):
    """
    Animate function for FuncAnimation.

    Args:
        i (int): The current frame number.
        ys (list): The list of previously captured voltage data.
        ax (matplotlib.axes.Axes): The axes to plot the data on.

    Returns:
        None
    """
    # Append new data
    ys.append(acquire_voltage_data())

    # Calculate rolling standard deviation
    data_series = pd.Series(ys)
    std_dev = data_series.rolling(1000).std()

    # Refresh plot
    ax.clear()
    ax.plot(range(len(std_dev)), std_dev, '-b', label = 'Voltage')
    ax.legend(loc='upper left')
    ax.set_xlabel('Time(s)')
    ax.set_ylabel('Voltage')

def main():
    """
    The main function of the script.

    Returns:
        None
    """
    # Prepare the figure and axes
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    # Prepare the data list
    data = []

    # Create the animation
    ani = animation.FuncAnimation(fig, animate, fargs=(data, ax), interval=1)
    plt.show()

if __name__ == "__main__":
    main()

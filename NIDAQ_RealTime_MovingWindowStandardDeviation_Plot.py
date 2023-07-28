"""
NIDAQ_RealTime_MovingWindowStandardDeviation_Plot.py

This script is used to acquire data from a NIDAQ device in real time and
create a Moving Window Standard Deviation (MWSD) plot for the acquired data.

Author: Siddharth Kumar (www.siddharthsah.com)
"""

# Standard library imports
import time

# Third party imports
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import nidaqmx
import pandas as pd

def acquire_data(task, number_of_samples):
    """
    Acquire data from NIDAQ device.

    Args:
        task (nidaqmx.Task): The task object.
        number_of_samples (int): The number of samples to read.

    Returns:
        list: List of data points.
    """
    return task.read(number_of_samples_per_channel=number_of_samples)

def animate(i, xs, ys, task, number_of_samples, rolling_window):
    """
    Function to be used in FuncAnimation for real time data plotting.

    Args:
        i (int): The current index (unused).
        xs (list): The x values of the plot.
        ys (list): The y values of the plot.
        task (nidaqmx.Task): The task object.
        number_of_samples (int): The number of samples to read per acquisition.
        rolling_window (int): The window size for the moving window standard deviation calculation.

    Returns:
        None
    """
    data = acquire_data(task, number_of_samples)

    # Append x values (time)
    xs += [(i + len(xs)) / 10000 for i in range(number_of_samples)]
    
    # Append y values (data)
    ys += data

    # Calculate Moving Window Standard Deviation
    MWSD = pd.Series(ys).rolling(rolling_window).std()

    # Clear and re-draw the plot
    ax.clear()
    ax.plot(xs, MWSD)
    ax.set_xlabel('Time(s)')
    ax.set_ylabel('MWSD')

def main():
    """
    The main function creates a matplotlib figure, initiates the NIDAQ task,
    and starts the animation for real time data acquisition and plotting.

    Returns:
        None
    """
    # Initialize parameters
    rolling_window = 1000
    number_of_samples = 1000

    # Initialize data lists
    xs = []
    ys = []

    # Create figure for plotting
    fig, ax = plt.subplots()

    # Initiate NIDAQ Task
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan("Dev6/ai0")

    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, task, number_of_samples, rolling_window), interval=30)

    plt.show()

if __name__ == "__main__":
    main()

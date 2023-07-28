"""
NIDAQ_RealTime_RawVoltage_Plot.py

This script is used to acquire data from a NIDAQ device in real time and
create a live plot for the acquired data.

Author: Siddharth Kumar (www.siddharthsah.com)
"""

# Standard library imports
import time

# Third party imports
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import nidaqmx

def acquire_data(task):
    """
    Acquire data from NIDAQ device.

    Args:
        task (nidaqmx.Task): The task object.

    Returns:
        float: Data point from the NIDAQ device.
    """
    return task.read(number_of_samples_per_channel=1)[0]

def animate(i, xs, ys, task):
    """
    Function to be used in FuncAnimation for real time data plotting.

    Args:
        i (int): The current index (unused).
        xs (list): The x values of the plot.
        ys (list): The y values of the plot.
        task (nidaqmx.Task): The task object.

    Returns:
        None
    """
    # Acquire data
    data = acquire_data(task)

    # Append x value (time) and y value (data)
    xs.append(time.time() - start_time)
    ys.append(data)

    # Clear and re-draw the plot
    ax.clear()
    ax.plot(xs, ys)
    ax.set_xlabel('Time(s)')
    ax.set_ylabel('Raw Voltage(V)')
    ax.set_title('Real time Raw Voltage')

def main():
    """
    The main function creates a matplotlib figure, initiates the NIDAQ task,
    and starts the animation for real time data acquisition and plotting.

    Returns:
        None
    """
    # Initialize data lists
    xs = []
    ys = []

    # Create figure for plotting
    fig, ax = plt.subplots()

    # Initiate NIDAQ Task
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")

    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, task), interval=10)

    plt.show()

if __name__ == "__main__":
    main()

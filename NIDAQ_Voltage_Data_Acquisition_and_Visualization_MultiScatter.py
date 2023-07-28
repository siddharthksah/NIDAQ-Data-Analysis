"""
NIDAQ_Voltage_Data_Acquisition_and_Visualization.py

This script is a utility for acquiring and visualizing voltage data from a 
National Instruments Data Acquisition (NIDAQ) device. It reads data from 
four channels and produces a real-time scatter plot for each channel.

Author: Siddharth Kumar (www.siddharthsah.com)
"""

# Standard library imports
import matplotlib.pyplot as plt
import nidaqmx

# External library imports
from nidaqmx.constants import AcquisitionType, TerminalConfiguration

def setup_plots():
    """
    Sets up four scatter plots for real-time data visualization.

    Returns:
        list: List of axis objects for the scatter plots.
    """
    figs = [plt.figure() for _ in range(4)]
    axes = [fig.add_subplot(1, 1, 1) for fig in figs]
    return axes

def add_channels_to_task(task, device="Dev6", channels=("ai0", "ai1", "ai2", "ai3")):
    """
    Adds specified channels to the provided NI-DAQmx task.

    Args:
        task (nidaqmx.Task): The task to which the channels will be added.
        device (str): The name of the device.
        channels (tuple): The names of the channels.

    Returns:
        None
    """
    for channel in channels:
        task.ai_channels.add_ai_voltage_chan(
            f"{device}/{channel}", 
            terminal_config=TerminalConfiguration.RSE
        )

def read_and_plot_data(task, axes, num_samples=1, num_points=3000, colors=('b', 'g', 'r', 'y')):
    """
    Reads data from the channels and plots them in real-time.

    Args:
        task (nidaqmx.Task): The task from which the data is read.
        axes (list): The axis objects on which the data is plotted.
        num_samples (int): The number of samples to read per channel.
        num_points (int): The number of points to read and plot.
        colors (tuple): The colors for the scatter plots.

    Returns:
        None
    """
    for i in range(num_points):
        try:
            data = task.read(number_of_samples_per_channel=num_samples)
        except nidaqmx.DaqError as e:
            print(f"An error occurred while reading data: {e}")
            return

        for ax, datum, color in zip(axes, data, colors):
            ax.scatter(i, datum, c=color)
            ax.set_ylabel("Raw Voltage (V)")
            ax.set_xlabel("Time(s)")
            plt.pause(0.01)

        print(data)

def main():
    """
    The main function of the script that creates the task, adds the channels,
    sets up the plots, and reads & plots the data.
    
    Returns:
        None
    """
    with nidaqmx.Task() as task:
        add_channels_to_task(task)
        axes = setup_plots()
        read_and_plot_data(task, axes)

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()

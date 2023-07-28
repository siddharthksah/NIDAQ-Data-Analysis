"""
DataVisualization_NationalInstrumentDataAcquisition.py

This script is used for visualizing data from the National Instrument Data Acquisition (NIDAQ) device.

Author: Siddharth Kumar (www.siddharthsah.com)

"""

# Import required libraries
import os
import matplotlib
import matplotlib.animation as animation
import pandas as pd
from matplotlib import style
from scipy import signal
import logging

matplotlib.use('TkAgg')  # To use the TkAgg backend for matplotlib


# Configure the logger
logging.basicConfig(filename='DataVisualization.log', level=logging.DEBUG)


# Set the style for the plot
style.use('fivethirtyeight')


def read_data_from_file(file_path: str):
    """
    This function reads the data from the provided file path and returns time and data lists.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.read().split('\n')
            time_list = []
            data_list = []

            for line in lines:
                if len(line) > 1:
                    time, data = map(float, line.split(','))
                    time_list.append(time / 2)
                    data_list.append(-data)
                    if time >= 80:
                        break

            return time_list, data_list

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        raise
    except Exception as e:
        logging.error(f"Error occurred while reading the file: {e}")
        raise


def animate(i):
    """
    This function is called for each animation frame. It reads the data from the files, computes the rolling standard deviation,
    and plots the data.
    """
    # Define file paths
    file_path_1 = "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/20 PSI Sweep_1.txt"
    file_path_2 = "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/30 PSI Sweep_1.txt"

    # Read the data from the files
    ts1, xs1 = read_data_from_file(file_path_1)
    ts2, xs2 = read_data_from_file(file_path_2)

    # Compute the rolling standard deviation
    data1 = pd.Series(xs1).rolling(300).std()
    data2 = pd.Series(xs2).rolling(300).std()

    ax1.clear()
    ax1.plot(ts1, data1, '-b', label='No pulse')
    ax1.plot(ts2, data2, '-r', label='2 Hz pulse')
    ax1.legend(loc='upper left')
    ax1.set_title('Comparison of pulse and no pulse data at 50 PSI Tall Whisker ')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('MWSD of Raw Voltage')


if __name__ == "__main__":

    # Create a figure
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(1, 1, 1)

    # Animate the figure
    ani1 = animation.FuncAnimation(fig1, animate, interval=30)

    # Show the plot
    plt.show()

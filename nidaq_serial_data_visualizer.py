"""
NIDAQ Serial Data Visualizer

This script visualizes serial data from the National Instruments Data Acquisition (NIDAQ) system,
creating an animated plot based on the data collected from a specific source. It is designed to 
run continuously and refresh the data visualization at regular intervals.

Author: Siddharth Kumar (www.siddharthsah.com)

"""

import os
import matplotlib
import matplotlib.animation as animation
import pandas as pd
from matplotlib import style
from scipy import signal

# matplotlib back-end for GUIs
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Choose the 'fivethirtyeight' style for plotting
style.use('fivethirtyeight')

# Declare the figure and axis for the plot
fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)

# Path to the text file containing the data to be visualized
DATA_FILE_PATH = "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/200130_Ball Bearing Whisker Vortex Gun Underwater/sweep3.txt"

def load_data(file_path):
    """
    Load data from a file.
    
    Args:
        file_path (str): Path to the data file.
        
    Returns:
        list of str: List of lines from the data file.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read().split('\n')
        return data
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}.")
        return []
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return []

def extract_data(lines):
    """
    Extract time-series data from lines.
    
    Args:
        lines (list of str): Lines from the data file.
        
    Returns:
        tuple: Time data (list of float), Sensor data (list of float).
    """
    time_data = []
    sensor_data = []

    for line in lines:
        if line:
            data = line.split(' ')
            try:
                time_data.append(float(data[0]))
                sensor_data.append(float(data[1]))
            except IndexError:
                print(f"Warning: Line '{line}' is malformed.")
            except ValueError:
                print(f"Warning: Unable to convert data to float in line '{line}'.")

    return time_data, sensor_data

def plot_data(i):
    """
    Function that's called at each interval by the FuncAnimation object.
    
    Args:
        i (int): Frame number (discarded in this function).
    """
    # Load and parse the data
    data_lines = load_data(DATA_FILE_PATH)
    time_data, sensor_data = extract_data(data_lines)

    # Calculate the rolling standard deviation using a window of 5000
    data_series = pd.Series(sensor_data)
    rolling_std_dev = data_series.rolling(5000).std()

    # Clear the previous plot
    ax1.clear()

    # Plot the new data
    ax1.plot(time_data, rolling_std_dev, '-b', label='Sweep')
    ax1.legend(loc='upper left')
    ax1.set_xlabel('Time(s)')
    ax1.set_ylabel('MWSD of Raw Voltage')

# Create the animation, updating at an interval of 30ms
ani1 = animation.FuncAnimation(fig1, plot_data, interval=30)

# Display the plot
plt.show()

"""
Author: Siddharth Kumar (www.siddharthsah.com)
Script for the National Instrument Data Acquisition (NIDAQ)

This Python script analyses and visualizes data acquired from NIDAQ. 
It creates time series plots for multiple sensors, calculates rolling 
standard deviation, and saves the plots as images.

"""

import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd
from scipy import signal

# Setting the 'fivethirtyeight' style for the plots
style.use('fivethirtyeight')

# Defining the absolute path for the data file
DATA_PATH = "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191212_4X4_Sensor_Array_01/sweep1.txt"

# Defining the directory to save plots
SAVE_DIR = "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191211_Array of Pots/"

# Setting the number of sensors
NUM_SENSORS = 16

def create_figures(num_figures):
    """
    Create matplotlib figures and axes for the given number of figures.

    Args:
    num_figures (int): Number of figures (and axes) to create.

    Returns:
    List[Tuple[plt.Figure, plt.Axes]]: List of tuples. Each tuple contains a figure and its corresponding axes.
    """
    figures = []
    for i in range(num_figures):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        figures.append((fig, ax))
    return figures

def read_and_preprocess_data(path):
    """
    Reads and preprocesses data from the given path.

    Args:
    path (str): The absolute path to the data file.

    Returns:
    List[List[float]]: The processed data with each sub-list representing data for a particular sensor.
    """
    try:
        with open(path, 'r') as f:
            lines = f.read().split('\n')
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return

    # Initialize a list for each sensor's data
    data = [[] for _ in range(NUM_SENSORS)]

    # Preprocess data
    for line in lines:
        if line:
            line_data = line.split()
            for i in range(NUM_SENSORS):
                data[i].append(float("{0:.6f}".format(float(line_data[2*i+1]))))

    return data

def calculate_rolling_std(data, window_size=10001):
    """
    Calculates the rolling standard deviation for the given data.

    Args:
    data (List[List[float]]): The data to calculate the rolling standard deviation on.
    window_size (int, optional): The window size for the rolling standard deviation. Defaults to 10001.

    Returns:
    List[pd.Series]: The calculated rolling standard deviations.
    """
    return [pd.Series(sensor_data).rolling(window_size).std() for sensor_data in data]

def plot_data(figures, ts, data):
    """
    Plots the given data on the provided figures.

    Args:
    figures (List[Tuple[plt.Figure, plt.Axes]]): The figures and axes to plot on.
    ts (List[float]): The time series.
    data (List[pd.Series]): The data to plot.
    """
    for i, (fig, ax) in enumerate(figures):
        ax.clear()
        ax.plot(ts, data[i], '-b', label=f'{i+1}')
        ax.legend(loc='upper left')
        ax.set_xlabel('Time(s)')
        ax.set_ylabel('MWSD of Raw Voltage')
        fig.savefig(os.path.join(SAVE_DIR, f'{i+1}.png'))

def main():
    """
    The main function to execute the data analysis and visualization.
    """
    figures = create_figures(NUM_SENSORS)
    data = read_and_preprocess_data(DATA_PATH)
    ts = list(range(len(data[0])))  # Assuming all sensors have equal number of data points
    rolling_std_data = calculate_rolling_std(data)
    plot_data(figures, ts, rolling_std_data)

if __name__ == "__main__":
    main()

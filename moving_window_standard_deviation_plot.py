"""
A script that processes and visualizes data recorded by the National Instrument Data Acquisition (NIDAQ) tool.
This script reads the data from files, processes them, and generates an animation showing the data trends over time.

Author: Siddharth Kumar (www.siddharthsah.com)

Usage: This script is meant to be run from the command line.
"""

# Standard library imports
import os
import logging
from typing import List, Tuple

# Third party imports
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
from scipy import signal

# Setting the appropriate backend before importing pyplot
matplotlib.use('TkAgg')

# Set the style for the plotting
style.use('fivethirtyeight')

# Configuring the logger
logging.basicConfig(level=logging.INFO)


def load_data_from_file(file_path: str) -> Tuple[List[float], List[float]]:
    """
    Load the data from a text file.

    Args:
        file_path (str): The path to the file.

    Returns:
        Tuple[List[float], List[float]]: A tuple containing two lists:
            - the time-series data (ts)
            - the corresponding measurement data (xs)
    """
    logging.debug(f'Loading data from {file_path}')
    try:
        with open(file_path, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        logging.error(f'{file_path} not found.')
        return [], []

    lines = data.split('\n')
    ts = []
    xs = []

    for line in lines:
        if len(line) > 1:
            line = line.split(',')
            ts.append(float(line[0]) / 2)
            xs.append(-float(line[1]))
            if float(line[0]) >= 80:
                break

    return ts, xs


def process_data(ts: List[float], xs: List[float], window: int = 300) -> pd.Series:
    """
    Process the data with a rolling window standard deviation.

    Args:
        ts (List[float]): The time-series data.
        xs (List[float]): The measurement data.
        window (int): The rolling window size. Defaults to 300.

    Returns:
        pd.Series: The processed data.
    """
    logging.debug('Processing data')
    xs_series = pd.Series(xs)
    data = xs_series.rolling(window).std()

    return data


def animate(i, ax, file_paths: List[str], labels: List[str]):
    """
    Update the plot for each frame of the animation.

    Args:
        i (int): The current frame index.
        ax (object): The matplotlib axes object.
        file_paths (List[str]): The list of file paths to process.
        labels (List[str]): The labels for each line in the plot.
    """
    ax.clear()

    for file_path, label in zip(file_paths, labels):
        ts, xs = load_data_from_file(file_path)
        data = process_data(ts, xs)
        ax.plot(ts, data, label=label)

    ax.legend(loc='upper left')
    ax.set_title('Comparison of pulse and no pulse data at 50 PSI Tall Whisker')
    ax.set_xlabel('Time(s)')
    ax.set_ylabel('MWSD of Raw Voltage')


def main():
    # Set up the figure and axes
    fig, ax = plt.subplots()

    # Define the file paths and labels for each data file
    base_path = "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/191001/Stiff Whisker 2 cm/"
    file_names = [f"{i * 10} PSI Sweep_1.txt" for i in range(1, 11)]
    file_paths = [os.path.join(base_path, file_name) for file_name in file_names]
    labels = [f'{i * 10} PSI' for i in range(1, 11)]

    ani = animation.FuncAnimation(fig, animate, interval=30, fargs=(ax, file_paths, labels))

    plt.show()


if __name__ == '__main__':
    main()

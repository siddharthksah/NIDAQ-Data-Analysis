"""
A script for real-time data acquisition and visualization using the National Instrument Data Acquisition (NIDAQ) tool.

Author: Siddharth Kumar (www.siddharthsah.com)

Usage: This script is meant to be run from the command line.
"""

import nidaqmx
import matplotlib.pyplot as plt
import pandas as pd
import logging

# Logging configuration for debugging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Set interactive mode ON, for real time updating
plt.ion()

# Global counter
n = 0


def create_subplot(fig_num: int) -> "AxesSubplot":
    """
    Create a matplotlib subplot.

    Args:
        fig_num (int): The unique identifier for the figure.

    Returns:
        AxesSubplot: The matplotlib axes subplot instance.
    """
    fig = plt.figure(fig_num)
    ax = fig.add_subplot(1, 1, 1)

    return ax


def get_data_from_channel(task, number_of_samples: int, rolling_window: int) -> "Series":
    """
    Acquires data from the NIDAQ channels and calculates the rolling window standard deviation.

    Args:
        task (nidaqmx.Task): The NIDAQ task to read data from.
        number_of_samples (int): The number of samples to read per channel.
        rolling_window (int): The window size for the rolling standard deviation.

    Returns:
        Series: The processed data series.
    """
    global n
    xs = []

    data = task.read(number_of_samples_per_channel=number_of_samples)
    for i in range(number_of_samples):
        xs.append(n / 1000)
        n = n + 1

    data_series = pd.Series(data)
    processed_data = data_series.rolling(rolling_window).std()

    return processed_data, xs


def plot_data(ax, data, xs, color: str):
    """
    Plot the processed data.

    Args:
        ax (AxesSubplot): The matplotlib axes subplot instance to plot the data.
        data (Series): The processed data to plot.
        xs (List): The x-coordinate data.
        color (str): The color to use for the data in the plot.
    """
    ax.scatter(xs, data, c=color)
    ax.set_ylabel("Raw Voltage (V)")
    ax.set_xlabel("Time(s)")


def main():
    """
    The main function of the script.
    """
    try:
        fig_nums = list(range(1, 17))
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

        ax_list = [create_subplot(num) for num in fig_nums]

        number_of_samples = 1000
        rolling_window = 1000

        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan("Dev6/ai0")
            # Add other channels as necessary
            # ...

            for i in range(3000):
                for ax, color in zip(ax_list, colors):
                    data, xs = get_data_from_channel(task, number_of_samples, rolling_window)
                    plot_data(ax, data, xs, color)
                    plt.pause(0.01)

                logging.debug(data)
    except nidaqmx.DaqError as e:
        logging.error("A DAQmx error occurred: {}".format(e))
    except Exception as e:
        logging.error("An unexpected error occurred: {}".format(e))


if __name__ == '__main__':
    main()

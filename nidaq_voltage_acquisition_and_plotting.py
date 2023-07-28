"""
nidaq_voltage_acquisition_and_plotting.py

This script reads voltage data from a National Instruments Data Acquisition (NIDAQ) device and a text file. It then
creates an animated plot of the data using matplotlib. The script was written specifically for NIDAQ devices but can be
adapted for any time-series voltage data acquisition and visualization.

Author: Siddharth Kumar (www.siddharthsah.com)

This module uses the following libraries: os, nidaqmx, matplotlib, numpy, time, pandas, scipy.
"""

import os
import nidaqmx
import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.animation as animation
import pandas as pd
from scipy import signal

class NIDAQVoltagePlotter:
    """
    Class to acquire voltage data from a NIDAQ device and a text file and create an animated plot of the data.

    Attributes
    ----------
    file_path : str
        path of the text file to read the data from
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_array = []
        self.fig, self.ax = plt.subplots()

    def _get_data_from_device(self):
        """
        Acquire data from the NIDAQ device.
        """
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan("Dev6/ai0")
            data = task.read(number_of_samples_per_channel=1)
            self.data_array.append(data)
            return data

    def animate(self, i):
        """
        Update the plot for each frame.

        Parameters
        ----------
        i : int
            current frame number
        """

        # Acquire data from the NIDAQ device
        data = self._get_data_from_device()
        print(data)
        plt.scatter(i / 10, data[0])
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (V)')
        plt.pause(0.000001)

        # Read data from the text file
        try:
            with open(self.file_path, 'r') as f:
                lines = f.read().split('\n')
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found")
            return
        except Exception as e:
            print(f"Error: {e}")
            return

        ts = []
        xs = []
        for line in lines:
            if len(line) > 0:
                t, x = map(float, line.split(' '))
                if t >= 0:
                    ts.append(t/2)
                    xs.append(x)
                if t >= 60:
                    break

        # Calculate moving window standard deviation
        MWSD1 = pd.Series(xs).rolling(1000).std()

        self.ax.clear()
        self.ax.plot(ts, MWSD1, '-b', label='Sweep')
        self.ax.legend(loc = 'upper left')
        self.ax.set_xlabel('Freq(Hz)')
        self.ax.set_ylabel('MWSD of Raw Voltage')

    def plot(self):
        """
        Create the animated plot.
        """
        ani = animation.FuncAnimation(self.fig, self.animate, interval=30)
        plt.show()


if __name__ == "__main__":
    # Define the path for the text file
    path_for_text_file = "C:/Users/Elgar/Singapore University of Technology and Design/Siddharth Kumar - Whiskers Array Sensing/191110\2 Dispensers\5 9 13 15 Hz 40 Seconds\[22]/sweep1.txt"

    plotter = NIDAQVoltagePlotter(path_for_text_file)
    plotter.plot()  # Start the animation

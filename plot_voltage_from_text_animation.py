"""
plot_voltage_from_text_animation.py

This script reads voltage data from a text file and creates an animated plot using matplotlib. It is written specifically
for the National Instrument Data Acquisition (NIDAQ) but can be used for any time-series voltage data in text file format.

Author: Siddharth Kumar (www.siddharthsah.com)

This module uses the following libraries: os, matplotlib, scipy.
"""

import os
import matplotlib
import matplotlib.animation as animation
from scipy import signal

matplotlib.use('TkAgg') # Set the matplotlib backend
import matplotlib.pyplot as plt

class AnimatedVoltagePlotter:
    """
    Class to create an animated plot of voltage data read from a text file.

    Attributes
    ----------
    file_path : str
        path of the text file to read the data from
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.fig, self.ax = plt.subplots()

    def animate(self, i):
        """
        Read data from text file and update the plot.

        Parameters
        ----------
        i : int
            current frame number, ignored in this function as the whole data is read each time
        """

        try:
            with open(self.file_path,'r') as f:
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
            if len(line) > 1:
                t, x = map(float, line.split(' '))
                ts.append(t)
                xs.append(x)

        xs = signal.savgol_filter(xs, 1001, 2)  # smooth data using Savitzky-Golay filter

        self.ax.clear()
        self.ax.plot(ts, xs, '-r',label='Speed 8.2 m/s')
        self.ax.legend(loc = 'upper left')
        self.ax.set_xlabel('Time(s)')
        self.ax.set_ylabel('Average Voltage(V)')

    def plot(self):
        """
        Create the animated plot.
        """
        ani = animation.FuncAnimation(self.fig, self.animate, interval=1)
        plt.show()


if __name__ == "__main__":
    # Define the path for the text file
    path_for_text_file = "C:/Users/Elgar/Singapore University of Technology and Design/Siddharth Kumar - Whiskers Array Sensing/191023_wind_tunnel/heavy_tip_22_run3_v8.2_on30off120.txt"

    plotter = AnimatedVoltagePlotter(path_for_text_file)
    plotter.plot()  # Start the animation

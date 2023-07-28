"""
This script is used to acquire data from National Instruments Data Acquisition (NIDAQ) devices and plots the data using Matplotlib. The script was created for continuous data logging and live display of the data. The acquired data undergoes a rolling window standard deviation operation, and the resultant data is then plotted in real-time.

Author: Siddharth Kumar (www.siddharthsah.com)

This script uses the following libraries: nidaqmx, matplotlib, pandas, and time
"""

import time
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import nidaqmx
import pandas as pd
from nidaqmx.constants import AcquisitionType
from nidaqmx import DaqError


class NIDAQDataAcquisition:
    """
    A class used to represent the NIDAQ Data Acquisition process

    ...

    Attributes
    ----------
    channels : list
        a list of channels to be read from the NIDAQ device
    number_of_samples : int
        number of samples to be read from each channel
    rolling_window : int
        size of the window for the rolling standard deviation operation
    plot_interval : int
        interval (in milliseconds) at which the plot gets updated

    Methods
    -------
    read_and_plot():
        Initiates the reading from the NIDAQ device and the plotting of data
    _animate(i):
        Function to update the plots; gets called at intervals specified by plot_interval
    """

    def __init__(self, channels, number_of_samples=1000, rolling_window=1000, plot_interval=30):
        self.channels = channels
        self.number_of_samples = number_of_samples
        self.rolling_window = rolling_window
        self.plot_interval = plot_interval
        self.fig, self.axes = plt.subplots(len(channels), 1)
        self.xs = []
        self.ys = [[] for _ in range(len(channels))]
        self.n = 0
        plt.ion()

    def _animate(self, i):
        """Internal method to update the plots"""
        with nidaqmx.Task() as task:
            for channel in self.channels:
                task.ai_channels.add_ai_voltage_chan(channel)
            try:
                data = task.read(number_of_samples_per_channel=self.number_of_samples)
            except DaqError as e:
                print("Error: ", e)
                return

        for i in range(self.number_of_samples):
            self.xs.append(self.n / 1000)
            self.n += 1

        for channel_data, y in zip(data, self.ys):
            y.extend(channel_data)

        for i, ax in enumerate(self.axes):
            ax.clear()
            mwsd = pd.Series(self.ys[i])
            data = mwsd.rolling(self.rolling_window).std()
            ax.plot(self.xs, data)
            ax.set_xlabel('Time(s)')
            ax.set_ylabel('MWSD')

    def read_and_plot(self):
        """Method to start reading from the NIDAQ device and plotting the data"""
        ani = animation.FuncAnimation(self.fig, self._animate, interval=self.plot_interval)
        plt.show()


if __name__ == "__main__":
    # List of channels to be read from the NIDAQ device
    channels = ["Dev6/ai{}".format(i) for i in range(4)]

    data_acquisition = NIDAQDataAcquisition(channels)

    # Start the data acquisition and plotting
    data_acquisition.read_and_plot()

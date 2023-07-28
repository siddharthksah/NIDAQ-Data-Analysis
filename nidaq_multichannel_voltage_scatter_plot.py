"""
nidaq_multichannel_voltage_scatter_plot.py

This script reads voltage data from multiple channels of a National Instruments Data Acquisition (NIDAQ) device and plots the data in real-time using matplotlib.

Author: Siddharth Kumar (www.siddharthsah.com)

This module uses the following libraries: nidaqmx, matplotlib
"""

import nidaqmx
from nidaqmx import DaqError
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class NIDAQMultiChannelVoltagePlotter:
    """
    Class to plot the voltage data read from multiple NIDAQ device channels.

    Attributes
    ----------
    channels : list
        a list of channels to read from the NIDAQ device
    sample_limit : int
        number of samples to read before stopping
    sample_per_read : int
        number of samples to read at each iteration
    """

    def __init__(self, channels, sample_limit=30000, sample_per_read=1000):
        self.channels = channels
        self.sample_limit = sample_limit
        self.sample_per_read = sample_per_read
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'r', 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'r']
        self.figures = [self.create_figure() for _ in channels]

    def create_figure(self):
        """
        Create a matplotlib figure and set the x and y labels.

        Returns:
        --------
        fig : Figure
            The created figure.
        ax : Axes
            The Axes object of the figure.
        """

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel("Time(s)")
        ax.set_ylabel("Raw Voltage (V)")

        return fig, ax

    def plot_data(self):
        """
        Read data from NIDAQ device and plot the data in real-time.
        """

        plt.ion()

        with nidaqmx.Task() as task:
            for channel in self.channels:
                task.ai_channels.add_ai_voltage_chan(channel)

            for i in range(self.sample_limit):
                try:
                    data = task.read(number_of_samples_per_channel=self.sample_per_read)
                except DaqError as e:
                    print(f"Error: {e}")
                    return

                for j, (fig, ax) in enumerate(self.figures):
                    ax.scatter(i, data[j], c=self.colors[j])
                    plt.pause(0.00001)

                print(data)

if __name__ == "__main__":
    channels = ["Dev6/ai{}".format(i) for i in range(24)]  # Specify the channels to be read

    nidaq_voltage_plotter = NIDAQMultiChannelVoltagePlotter(channels)
    nidaq_voltage_plotter.plot_data()  # Start the real-time plotting

"""
nidaq_voltage_sampling_and_animation_plot.py

This module acquires voltage data from National Instruments Data Acquisition (NIDAQ) devices and animates the acquired data using Matplotlib. 

Author: Siddharth Kumar (www.siddharthsah.com)

This module uses the following libraries: nidaqmx, matplotlib, pandas, and time
"""

import time
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import nidaqmx
import pandas as pd
from nidaqmx import DaqError


class NIDAQVoltageSamplerAndAnimator:
    """
    A class that represents a NIDAQ voltage sampler and animator.

    ...

    Attributes
    ----------
    channels : list
        a list of channels to be read from the NIDAQ device
    num_samples : int
        number of samples to be read from each channel
    rolling_window : int
        size of the window for the rolling standard deviation operation
    plot_interval : int
        interval (in milliseconds) at which the plot gets updated
    """

    def __init__(self, channels, num_samples=1000, rolling_window=1000, plot_interval=30):
        self.channels = channels
        self.num_samples = num_samples
        self.rolling_window = rolling_window
        self.plot_interval = plot_interval
        self.fig, self.ax = plt.subplots(1, 1)
        self.xs = []
        self.ys = []
        self.n = 1
        plt.ion()

    def _animate(self, i):
        """
        Animate function that's called periodically by FuncAnimation.

        Args:
            i (int): the current frame index; unused here, but required by FuncAnimation.
        """

        with nidaqmx.Task() as task:
            for channel in self.channels:
                task.ai_channels.add_ai_voltage_chan(channel)

            try:
                data = task.read(number_of_samples_per_channel=self.num_samples)
            except DaqError as e:
                print(f"Error: {e}")
                return

        for i in range(self.num_samples):
            self.xs.append(self.n / 10000)
            self.n += 1

        for element in data[0]:
            self.ys.append(element)

        mwsd = pd.Series(self.ys)
        data = mwsd.rolling(self.rolling_window).std()

        self.ax.clear()
        self.ax.plot(self.xs, data)
        self.ax.set_xlabel('Time(s)')
        self.ax.set_ylabel('MWSD')

    def sample_and_animate(self):
        """
        Start the sampling from NIDAQ device and animation of the acquired data.
        """

        ani = animation.FuncAnimation(self.fig, self._animate, interval=self.plot_interval)
        plt.show()


if __name__ == "__main__":
    channels = ["Dev6/ai{}".format(i) for i in range(4)]  # Specify the channels to be read

    nidaq_sampler_animator = NIDAQVoltageSamplerAndAnimator(channels)
    nidaq_sampler_animator.sample_and_animate()  # Start the sampling and animation

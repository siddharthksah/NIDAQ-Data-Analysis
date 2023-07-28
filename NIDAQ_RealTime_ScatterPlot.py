"""
NIDAQ_RealTime_ScatterPlot.py

This script acquires data from a NIDAQ device and plots a real-time scatter plot of the raw voltage versus time.

Author: Siddharth Kumar (www.siddharthsah.com)
"""

import nidaqmx
import matplotlib.pyplot as plt

def scatter_real_time():
    """
    This function acquires data from the NIDAQ device and plots the scatter plot in real-time.

    Args:
        None

    Returns:
        None
    """
    # Initialize counter
    i=0

    with nidaqmx.Task() as task:
        # Add the voltage channel to task
        task.ai_channels.add_ai_voltage_chan("Dev6/ai0")

        plt.ion()
        plt.figure()
        plt.ylabel("Raw Voltage (V)")
        plt.xlabel("Time(s)")

        # Run data acquisition for 300 samples
        while i<300:
            try:
                data = task.read(number_of_samples_per_channel=1)
            except nidaqmx.DaqError as e:
                print(f"Error: {e}")
                break

            # Plot data
            plt.scatter(i, data[0], c= 'b')
            plt.pause(0.01)

            i += 1

            # Output raw data
            print (data)

        plt.ioff()
        plt.show()

if __name__ == "__main__":
    scatter_real_time()

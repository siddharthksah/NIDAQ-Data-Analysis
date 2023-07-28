"""
NIDAQ_Data_Acquisition_and_Visualization.py

This script acquires voltage data from a NIDAQ device, calculates the moving window standard deviation
of the data, and visualizes it in real-time.

Author: Siddharth Kumar (www.siddharthsah.com)
"""

# Standard library imports
import time

# Third party imports
import nidaqmx
import matplotlib.pyplot as plt
import pandas as pd

def acquire_and_visualize_data():
    """
    Acquires voltage data from a NIDAQ device, calculates the moving window standard deviation
    of the data, and visualizes it in real-time.

    Returns:
        None
    """
    plt.ion()
    fig, ax = plt.subplots()
    data_array = []
    
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev6/ai0")
        start_time = time.time()

        try:
            while True:  # Keep reading data until stopped
                data = task.read(number_of_samples_per_channel=1)
                data_array.append(data)

                # Calculate moving window standard deviation
                MWSD1 = pd.Series(data_array)
                data1 = MWSD1.rolling(1000).std()

                ax.clear()
                ax.plot(range(len(data1)), data1, '-b', label='Sweep')
                ax.legend(loc='upper left')
                ax.set_xlabel('Freq(Hz)')
                ax.set_ylabel('MWSD of Raw Voltage')
                plt.pause(0.000001)
        except KeyboardInterrupt:
            # Allow the data acquisition to be stopped with Ctrl+C
            pass

    stop_time = time.time() - start_time
    print(f"Data acquisition duration: {stop_time} seconds")
    print(f"Total data points acquired: {len(data_array)}")

def main():
    """
    The main function of the script.

    Returns:
        None
    """
    acquire_and_visualize_data()

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()

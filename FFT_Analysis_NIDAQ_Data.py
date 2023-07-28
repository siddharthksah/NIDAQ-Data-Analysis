"""
FFT_Analysis_NIDAQ_Data.py

This Python module performs a Fast Fourier Transform (FFT) on data collected from a National Instruments Data Acquisition 
(NIDAQ) device and visualizes the results. This module reads a text file containing sensor data, processes the data, 
and plots the amplitude over time and the FFT of the data.

Author: Siddharth Kumar (www.siddharthsah.com)

This module uses numpy and matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np
import os

class FFTAnalyzer:
    """
    A class used to perform FFT analysis on data collected from a NIDAQ device.

    ...

    Attributes
    ----------
    filepath : str
        a string containing the path to the data file

    Methods
    -------
    load_data():
        Loads the data from the file and returns the time and amplitude data as numpy arrays.
    fft_analysis():
        Performs an FFT on the amplitude data and plots the results.
    """

    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        """Loads the data from the file and returns the time and amplitude data as numpy arrays."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"The specified file does not exist: {self.filepath}")
        
        try:
            times = []
            amplitudes = []
            with open(self.filepath, 'r') as f:
                for line in f:
                    if len(line) > 1:
                        t, a = line.split()
                        times.append(float(t))
                        amplitudes.append(float(a))
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None, None
        return np.array(times), np.array(amplitudes)

    def fft_analysis(self, times, amplitudes):
        """Performs an FFT on the amplitude data and plots the results."""
        Fs = 25000.0  # Sampling rate
        n = len(amplitudes)  # Length of the signal
        k = np.arange(n)
        T = n / Fs
        frq = k / T  # Two sides frequency range
        frq = frq[range(int(n/2))]  # One side frequency range

        Y = np.fft.fft(amplitudes) / n  # FFT computing and normalization
        Y = Y[range(int(n/2))]

        # Plotting
        fig, ax = plt.subplots(2, 1)
        ax[0].plot(times, amplitudes)
        ax[0].set_xlabel('Time')
        ax[0].set_ylabel('Amplitude')
        ax[1].plot(frq, abs(Y), 'r')  # Plotting the spectrum
        ax[1].set_xlabel('Freq (Hz)')
        ax[1].set_ylabel('|Y(freq)|')
        plt.show()

if __name__ == "__main__":
    filepath = "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/14082019/40 PSI/40 Hz/v vs t.txt"
    analyzer = FFTAnalyzer(filepath)
    times, amplitudes = analyzer.load_data()
    if times is not None and amplitudes is not None:
        analyzer.fft_analysis(times, amplitudes)

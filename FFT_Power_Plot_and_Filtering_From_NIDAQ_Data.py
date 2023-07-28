"""
FFT_Power_Plot_and_Filtering_From_NIDAQ_Data.py
===============================================

This script handles data from the National Instrument Data Acquisition (NIDAQ).
It plots the power of the FFT of a signal, filters out high frequencies, 
and reconstructs the signal using inverse FFT.

Note: This implementation uses a basic filtering technique that is suboptimal,
      and should not be used in a production environment.

Author: Siddharth Kumar (www.siddharthsah.com)

"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack

def read_data_from_file(filepath):
    """
    Read data from a text file at given filepath and parse into x, y coordinates.
    """
    try:
        with open(filepath, 'r') as file:
            lines = file.read().split('\n')

        ts = []
        xs = []

        for line in lines:
            if len(line) > 1:
                line = line.split()
                ts.append(float(line[0]))
                xs.append(float(line[1]))

        return np.array(xs), ts
    
    except Exception as e:
        print(f"Error occurred while reading the file: {str(e)}")
        return None

def compute_fft_and_power(sig, time_step):
    """
    Compute and return FFT and power of the signal
    """
    # The FFT of the signal
    sig_fft = fftpack.fft(sig)

    # And the power (sig_fft is of complex dtype)
    power = np.abs(sig_fft)

    # The corresponding frequencies
    sample_freq = fftpack.fftfreq(sig.size, d=time_step)
    
    return sig_fft, power, sample_freq

def plot_power(sample_freq, power):
    """
    Plot the FFT power.
    """
    # Plot the FFT power
    plt.figure(figsize=(6, 5))
    plt.plot(sample_freq, power)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Power')
    plt.title('FFT Power of Signal')

def find_peak_frequency(sample_freq, power):
    """
    Find and return the peak frequency.
    """
    # Find the peak frequency: we can focus on only the positive frequencies
    pos_mask = np.where(sample_freq > 0)
    freqs = sample_freq[pos_mask]
    peak_freq = freqs[power[pos_mask].argmax()]

    return peak_freq, freqs

def plot_peak_frequency(freqs, power):
    """
    Plot the peak frequency.
    """
    # An inner plot to show the peak frequency
    axes = plt.axes([0.55, 0.3, 0.3, 0.5])
    plt.title('Peak frequency')
    plt.plot(freqs[:8], power[:8])
    plt.setp(axes, yticks=[])

def filter_high_frequencies(sig_fft, sample_freq, peak_freq):
    """
    Remove all the high frequencies and transform back from
    frequencies to signal.
    """
    # We now remove all the high frequencies and transform back from
    # frequencies to signal.
    high_freq_fft = sig_fft.copy()
    high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
    filtered_sig = fftpack.ifft(high_freq_fft)

    return filtered_sig

def plot_signals(time_vec, sig, filtered_sig):
    """
    Plot original and filtered signals.
    """
    plt.figure(figsize=(6, 5))
    plt.plot(time_vec, sig, label='Original signal')
    plt.plot(time_vec, filtered_sig, linewidth=3, label='Filtered signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.legend(loc='best')

if __name__ == "__main__":
    filepath = "C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/14082019/40 PSI/40 Hz/v vs t.txt"
    time_step = 0.00004

    sig, time_vec = read_data_from_file(filepath)
    
    if sig is not None:
        sig_fft, power, sample_freq = compute_fft_and_power(sig, time_step)

        plot_power(sample_freq, power)

        peak_freq, freqs = find_peak_frequency(sample_freq, power)

        plot_peak_frequency(freqs, power)

        filtered_sig = filter_high_frequencies(sig_fft, sample_freq, peak_freq)

        plot_signals(time_vec, sig, filtered_sig)

        plt.show()

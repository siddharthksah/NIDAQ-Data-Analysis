"""
=============================================
Plotting and manipulating FFTs for filtering
=============================================

Plot the power of the FFT of a signal and inverse FFT back to reconstruct
a signal.

This example demonstrate :func:`scipy.fftpack.fft`,
:func:`scipy.fftpack.fftfreq` and :func:`scipy.fftpack.ifft`. It
implements a basic filter that is very suboptimal, and should not be
used.

"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack

############################################################
# Generate the signal
############################################################

# Seed the random number generator
pathForTextFile = ("C:/Users/siddh/Singapore University of Technology and Design/Whiskers Array Sensing/14082019/40 PSI/40 Hz/v vs t.txt")

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)



graph_data = open(pathForTextFile,'r').read()
lines = graph_data.split('\n')
ts = []
xs = []
x = 0
for line in lines:
    if len(line) > 1:
        line = line.split()
        ts.append(float(line[0]))
        xs.append(float(line[1]))

sig = np.array(xs)
time_step = 0.00004
period = 20
############################################################
# Compute and plot the power
############################################################

# The FFT of the signal
sig_fft = fftpack.fft(sig)

# And the power (sig_fft is of complex dtype)
power = np.abs(sig_fft)

# The corresponding frequencies
sample_freq = fftpack.fftfreq(sig.size, d=time_step)

# Plot the FFT power
plt.figure(figsize=(6, 5))
plt.plot(sample_freq, power)
plt.xlabel('Frequency [Hz]')
plt.ylabel('plower')

# Find the peak frequency: we can focus on only the positive frequencies
pos_mask = np.where(sample_freq > 0)
freqs = sample_freq[pos_mask]
peak_freq = freqs[power[pos_mask].argmax()]

# Check that it does indeed correspond to the frequency that we generate
# the signal with
np.allclose(peak_freq, 1./period)

# An inner plot to show the peak frequency
axes = plt.axes([0.55, 0.3, 0.3, 0.5])
plt.title('Peak frequency')
plt.plot(freqs[:8], power[:8])
plt.setp(axes, yticks=[])

# scipy.signal.find_peaks_cwt can also be used for more advanced
# peak detection

############################################################
# Remove all the high frequencies
############################################################
#
# We now remove all the high frequencies and transform back from
# frequencies to signal.

high_freq_fft = sig_fft.copy()
high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
filtered_sig = fftpack.ifft(high_freq_fft)

plt.figure(figsize=(6, 5))
plt.plot(time_vec, sig, label='Original signal')
plt.plot(time_vec, filtered_sig, linewidth=3, label='Filtered signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.legend(loc='best')

############################################################
#
# **Note** This is actually a bad way of creating a filter: such brutal
# cut-off in frequency space does not control distorsion on the signal.
#
# Filters should be created using the scipy filter design code
plt.show()



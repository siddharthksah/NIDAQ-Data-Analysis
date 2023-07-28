"""
NIDAQ_Realtime_Voltage_Data_Animation.py

This script reads voltage data from a text file and visualizes it in real-time using matplotlib's
animation functionality. The data is smoothed using a moving window standard deviation.

Author: Siddharth Kumar (www.siddharthsah.com)
"""

# Standard library imports
from matplotlib import style, animation
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal

# Set the matplotlib backend
plt.switch_backend('TkAgg')

style.use('fivethirtyeight')

# Path for the input text file
INPUT_PATH = "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/190919_01/Red Base Copper Wire[21] Ball Bearing 20PSI/sweep3.txt"

def animate(i, ax):
    """
    Reads data from a text file, smoothes it, and visualizes it using matplotlib's animation.

    Args:
        i (int): Current frame number.
        ax (matplotlib.axes.Axes): The axes object to plot on.

    Returns:
        None
    """
    try:
        with open(INPUT_PATH, 'r') as f:
            lines = f.read().split('\n')
    except FileNotFoundError as e:
        print(f"An error occurred while reading the data file: {e}")
        return

    ts, xs = [], []
    for line in lines:
        if len(line) > 1:
            t, x = map(float, line.split(','))
            ts.append(t)
            xs.append(x)

    MWSD1 = pd.Series(xs)
    data1 = MWSD1.rolling(100).std()

    ax.clear()
    ax.plot(ts, xs, '-b', label='RAW V')
    ax.plot(ts, data1, '-r', label='MWSD(V)')
    ax.set_title('10 PSI 10 Hz')
    ax.legend(loc='upper right')
    ax.set_xlabel('Time(s)')
    ax.set_ylabel('Voltage(V)')

def main():
    """
    The main function of the script that sets up the plot and starts the animation.

    Returns:
        None
    """
    fig, ax = plt.subplots()
    ani = animation.FuncAnimation(fig, animate, fargs=(ax,), interval=10)
    plt.show()

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()

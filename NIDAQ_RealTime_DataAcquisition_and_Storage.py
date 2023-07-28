"""
NIDAQ_RealTime_DataAcquisition_and_Storage.py

This script is intended for real-time data acquisition from a NIDAQ device. The acquired data is
then stored in a text file for further analysis. 

Author: Siddharth Kumar (www.siddharthsah.com)
"""

# Standard library imports
import os
import datetime
import time

# Third party imports
import nidaqmx

def create_data_dir(base_dir):
    """
    Create a directory to store data, named with the current timestamp.

    Args:
        base_dir (str): The base directory in which to create the timestamped directory.

    Returns:
        str: The absolute path of the created directory.
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    data_dir = os.path.join(base_dir, timestamp)
    os.makedirs(data_dir)
    return data_dir

def write_location_to_file(file_path, location):
    """
    Write a location string to a file.

    Args:
        file_path (str): The path of the file to write to.
        location (str): The location string to write.

    Returns:
        None
    """
    with open(file_path, "w") as file:
        file.write(location)

def acquire_data(outfile):
    """
    Acquire data from the NIDAQ device and write it to a file.

    Args:
        outfile (str): The file to write the data to.

    Returns:
        None
    """
    start_time = time.time()
    p = 0

    with open(outfile,'a+') as f:
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan("Dev1/ai0")

            while True:
                p += 1
                data = task.read(number_of_samples_per_channel=1)
                data_str = str(data[0])[0:-10]
                f.write(f"{data_str}\n")

def main():
    """
    Main function of the script. It creates necessary directories and files, and
    initiates the data acquisition process.

    Returns:
        None
    """
    base_dir = "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/200130_Ball Bearing Whisker Vortex Gun Underwater/"
    location_file = os.path.join(base_dir, "fileLocation.txt")
    data_dir = create_data_dir(base_dir)

    write_location_to_file(location_file, data_dir)

    outfile = os.path.join(data_dir, "test.txt")
    acquire_data(outfile)

if __name__ == "__main__":
    main()

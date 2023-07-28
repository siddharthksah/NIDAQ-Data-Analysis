"""
csv_to_txt_with_line_filtering.py

This script converts a CSV file to a TXT file and removes the first five lines from the TXT file. This is especially
useful when handling data from the National Instruments Data Acquisition (NIDAQ) device, where the first few lines of
the data file may not be relevant for subsequent data processing steps.

Author: Siddharth Kumar (www.siddharthsah.com)

This module uses the csv built-in Python library.
"""

import csv
import os

class CSVtoTXTConverter:
    """
    A class used to represent the CSV to TXT Converter.

    ...

    Attributes
    ----------
    csv_file : str
        a string containing the path to the input csv file
    txt_file : str
        a string containing the path to the output txt file

    Methods
    -------
    convert():
        Converts a csv file to a txt file.
    filter_lines(n=5):
        Removes the first n lines from the txt file.
    """

    def __init__(self, csv_file, txt_file):
        self.csv_file = csv_file
        self.txt_file = txt_file

    def convert(self):
        """Converts a csv file to a txt file by reading each row and writing it to the txt file."""
        try:
            with open(self.txt_file, "w") as my_output_file:
                with open(self.csv_file, "r") as my_input_file:
                    [my_output_file.write(" ".join(row) + '\n') for row in csv.reader(my_input_file)]
        except FileNotFoundError:
            print(f"Error: File {self.csv_file} not found.")
        except Exception as e:
            print(f"An error occurred during the conversion process: {e}")
        else:
            print('Conversion completed successfully.')

    def filter_lines(self, n=5):
        """Removes the first n lines from the txt file."""
        try:
            with open(self.txt_file, 'r') as fin:
                data = fin.read().splitlines(True)
            with open(self.txt_file, 'w') as fout:
                fout.writelines(data[n:])
        except FileNotFoundError:
            print(f"Error: File {self.txt_file} not found.")
        except Exception as e:
            print(f"An error occurred during the line filtering process: {e}")
        else:
            print('Line filtering completed successfully.')

if __name__ == "__main__":
    csv_file  = "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/200128_whisker with heavy tip_vortex gun in water/1cm whisker_sweep_50psi_1k_sampling_along contact pad.csv"
    txt_file = "D:/SMP/OneDrive - Singapore University of Technology and Design/Whiskers Array Sensing/200128_whisker with heavy tip_vortex gun in water/1cm whisker_sweep_50psi_1k_sampling_along contact pad.txt"

    converter = CSVtoTXTConverter(csv_file, txt_file)
    converter.convert()
    converter.filter_lines()

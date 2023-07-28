![Header](./header.png)
<p align="center">
  <a href="https://github.com/siddharthksah/NIDAQ-Data-Analysis/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/siddharthksah/NIDAQ-Data-Analysis"></a>
  <a href="https://github.com/siddharthksah/NIDAQ-Data-Analysis/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/siddharthksah/NIDAQ-Data-Analysis"></a>
  <a href="https://github.com/siddharthksah/NIDAQ-Data-Analysis/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/siddharthksah/NIDAQ-Data-Analysis"></a>
  <a href="https://github.com/siddharthksah/NIDAQ-Data-Analysis/blob/master/LICENSE.txt"><img alt="GitHub license" src="https://img.shields.io/github/license/siddharthksah/NIDAQ-Data-Analysis"></a>
</p>

Welcome to the National Instruments Data Acquisition (NIDAQ) Data Acquisition and Analysis repository. This repo contains high-quality Python scripts written by [Siddharth Kumar](www.siddharthsah.com) to manipulate and analyze data collected through NIDAQ.

## Table of Contents 📚

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [What's Inside](#whats-inside)
- [Scripts Included](#scripts-included)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributions](#contributions)
- [Code of Conduct](#code-of-conduct)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Introduction 🎉

This repository aims to provide data scientists, researchers, and hobbyists with efficient and user-friendly tools to analyze and visualize data from National Instruments Data Acquisition (NIDAQ).

## Prerequisites 🧩

Before you begin, ensure you have met the following requirements:

- Python 3.x
- Other dependencies listed in the [requirements.txt](./requirements.txt) file.
  
## Installation 🚀

Clone this repository using

```
git clone https://github.com/siddharthksah/NIDAQ-Data-Analysis.git
```
Install the required dependencies using:
```
pip install -r requirements.txt
```

## Usage 🛠️

Replace `<filename>` with the desired python script from above:

```python
python <filename>.py
```

## What's Inside 👀

This repository is packed with multiple Python scripts focused on NIDAQ data acquisition and analysis. Here's a quick look inside:

1. 📊 **Data Visualization**: Visualize your NIDAQ data with scripts like [DataVisualization_NationalInstrumentDataAcquisition.py](./DataVisualization_NationalInstrumentDataAcquisition.py) and [NIDAQ_RawVoltage_PlotAnimation.py](./NIDAQ_RawVoltage_PlotAnimation.py).

2. 🧮 **FFT Analysis**: Perform Fast Fourier Transform (FFT) on your NIDAQ data with [FFT_Analysis_NIDAQ_Data.py](./FFT_Analysis_NIDAQ_Data.py) and create power plots with [FFT_Power_Plot_and_Filtering_From_NIDAQ_Data.py](./FFT_Power_Plot_and_Filtering_From_NIDAQ_Data.py).

3. 📐 **Data Acquisition & Visualization**: Use scripts like [NIDAQ_Data_Acquisition_and_Visualization.py](./NIDAQ_Data_Acquisition_and_Visualization.py) and [NIDAQ_RealTime_DataAcquisition_and_Storage.py](./NIDAQ_RealTime_DataAcquisition_and_Storage.py) to acquire and visualize your NIDAQ data in real-time.

4. 🔬 **Data Analysis**: Get insightful analysis of your data with [NIDAQ_Data_Analysis_and_Visualization_16.py](./NIDAQ_Data_Analysis_and_Visualization_16.py) and calculate response times with [NIDAQ_ResponseTime_Calculation.py](./NIDAQ_ResponseTime_Calculation.py).

5. 📈 **Real-time Plotting**: Generate real-time plots with scripts like [NIDAQ_RealTime_RawVoltage_Plot.py](./NIDAQ_RealTime_RawVoltage_Plot.py) and [NIDAQ_RealTime_ScatterPlot.py](./NIDAQ_RealTime_ScatterPlot.py).

6. 🎞️ **Animation Plots**: Create engaging animations with [NIDAQ_Realtime_Voltage_Data_Animation_Plot_MWSD.py](./NIDAQ_Realtime_Voltage_Data_Animation_Plot_MWSD.py) and [plot_voltage_from_text_animation.py](./plot_voltage_from_text_animation.py).

7. 🗄️ **Data Conversion**: Convert your data files from CSV to TXT with [csv_to_txt_with_line_filtering.py](./csv_to_txt_with_line_filtering.py).

8. 📏 **Point Calculation**: Calculate equidistant points between two given points with [Get_Equidistant_Points_Between_Two_Points.py](./Get_Equidistant_Points_Between_Two_Points.py).

And many more! Each script is well-documented, making it easy for you to understand the purpose and working of each line of code.


## Scripts Included 📜

1. [DataVisualization_NationalInstrumentDataAcquisition.py](./DataVisualization_NationalInstrumentDataAcquisition.py): A script to visualize data acquired from NIDAQ instruments.
2. [FFT_Analysis_NIDAQ_Data.py](./FFT_Analysis_NIDAQ_Data.py): Conducts Fast Fourier Transform (FFT) analysis on NIDAQ data.
3. [FFT_Power_Plot_and_Filtering_From_NIDAQ_Data.py](./FFT_Power_Plot_and_Filtering_From_NIDAQ_Data.py): Generates FFT Power plots and conducts data filtering.
4. [Get_Equidistant_Points_Between_Two_Points.py](./Get_Equidistant_Points_Between_Two_Points.py): Finds equidistant points between two given points.
5. [NIDAQ_Data_Acquisition_and_Visualization.py](./NIDAQ_Data_Acquisition_and_Visualization.py): A combined script for acquiring and visualizing NIDAQ data.
6. [NIDAQ_Data_Analysis_and_Visualization_16.py](./NIDAQ_Data_Analysis_and_Visualization_16.py): Analyzes and visualizes NIDAQ data with 16 channels.
7. [NIDAQ_RawVoltage_PlotAnimation.py](./NIDAQ_RawVoltage_PlotAnimation.py): Generates animated plots of raw voltage data.
8. [NIDAQ_RealTime_DataAcquisition_and_Storage.py](./NIDAQ_RealTime_DataAcquisition_and_Storage.py): Acquires NIDAQ data in real-time and stores it for future use.
9. [NIDAQ_RealTime_MovingWindowStandardDeviation_Plot.py](./NIDAQ_RealTime_MovingWindowStandardDeviation_Plot.py): Generates real-time moving window standard deviation plots.
10. [NIDAQ_RealTime_RawVoltage_Plot.py](./NIDAQ_RealTime_RawVoltage_Plot.py): Generates real-time plots of raw voltage data.
11. [NIDAQ_RealTime_ScatterPlot.py](./NIDAQ_RealTime_ScatterPlot.py): Generates real-time scatter plots of NIDAQ data.
12. [NIDAQ_Realtime_Data_Acquisition_and_Plotting.py](./NIDAQ_Realtime_Data_Acquisition_and_Plotting.py): A script to acquire and plot NIDAQ data in real-time.
13. [NIDAQ_Realtime_Voltage_Data_Animation_Plot_MWSD.py](./NIDAQ_Realtime_Voltage_Data_Animation_Plot_MWSD.py): Generates real-time animated plots of voltage data with Moving Window Standard Deviation.
14. [NIDAQ_ResponseTime_Calculation.py](./NIDAQ_ResponseTime_Calculation.py): Calculates the response time of NIDAQ instruments.
15. [NIDAQ_Voltage_Data_Acquisition_and_Visualization_MultiScatter.py](./NIDAQ_Voltage_Data_Acquisition_and_Visualization_MultiScatter.py): Acquires voltage data and visualizes it in multiple scatter plots.
16. [NationalInstrumentDataAcquisitionDataVisualizer.py](./NationalInstrumentDataAcquisitionDataVisualizer.py): A comprehensive script for data acquisition and visualization of National Instrument data.
17. [csv_to_txt_with_line_filtering.py](./csv_to_txt_with_line_filtering.py): Converts CSV data files to TXT format with line filtering.
18. [moving_window_standard_deviation_plot.py](./moving_window_standard_deviation_plot.py): Plots moving window standard deviation of data.
19. [moving_window_standard_deviation_scatter_plot_nidaq.py](./moving_window_standard_deviation_scatter_plot_nidaq.py): Creates scatter plots with moving window standard deviation for NIDAQ data.
20. [nidaq_multichannel_voltage_scatter_plot.py](./nidaq_multichannel_voltage_scatter_plot.py): Generates scatter plots for multichannel voltage data from NIDAQ.
21. [nidaq_serial_data_visualizer.py](./nidaq_serial_data_visualizer.py): Visualizes serial data from NIDAQ instruments.
22. [nidaq_voltage_acquisition_and_plotting.py](./nidaq_voltage_acquisition_and_plotting.py): Acquires and plots voltage data from NIDAQ.
23. [nidaq_voltage_sampling_and_animation_plot.py](./nidaq_voltage_sampling_and_animation_plot.py): Samples NIDAQ voltage data and generates animated plots.
24. [plot_voltage_from_text_animation.py](./plot_voltage_from_text_animation.py): Creates animated plots of voltage data read from text files.
25. [realtime_lineplot_moving_window_standard_deviation_nidaq.py](./realtime_lineplot_moving_window_standard_deviation_nidaq.py): Generates real-time line plots with moving window standard deviation for NIDAQ data.


## Contributions :handshake:

Contributions are always welcomed. :smiley: If you have some ideas or improvements, feel free to make a pull request or open an issue to discuss it.

## License :page_facing_up:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements :star2:

I would like to thank my colleagues and everyone who contributed to making this project possible. :heart:

"""
Get_Equidistant_Points_Between_Two_Points.py
=============================================

This script generates a list of equidistant points between two points.
It can be used in various applications, including data analysis, 
geolocation computations, graphical renderings, etc.

Author: Siddharth Kumar (www.siddharthsah.com)

"""

import numpy as np

def get_equidistant_points(p1, p2, parts):
    """
    This function generates a list of equidistant points between two given points.
    
    Parameters:
        p1 (tuple): A tuple that represents the first point.
        p2 (tuple): A tuple that represents the second point.
        parts (int): The number of parts the distance between the points should be divided into.
    
    Returns:
        list: A list of tuples where each tuple represents a point.
    """
    try:
        points = list(zip(np.linspace(p1[0], p2[0], parts+1), np.linspace(p1[1], p2[1], parts+1)))
        return points
    except Exception as e:
        print(f"An error occurred while computing the points: {str(e)}")
        return None

def print_points(points):
    """
    This function prints all the points in the provided list.
    
    Parameters:
        points (list): A list of tuples where each tuple represents a point.
    """
    if points is not None:
        for point in points:
            print(point)

if __name__ == "__main__":
    p1 = (147.413,1.016)
    p2 = (152.784,6.378)
    parts = 10

    points = get_equidistant_points(p1, p2, parts)
    print_points(points)

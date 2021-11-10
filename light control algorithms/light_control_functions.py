"""
Author: Sam Donnelly 
Project: Desktop Christmas Tree
Date Created: October 16, 2021
Date Last Modified: October 16, 2021

Purpose:
- Functions to support the light_control_algorithms.py script


"""

# ---------------------------------------------------------------------------
# Import Libraries
# ---------------------------------------------------------------------------
from math import sin, cos

# ---------------------------------------------------------------------------
# File Locations
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Global Variables
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Functions 
# --------------------------------------------------------------------------- 

def sine_func(A, B, C, D, x):
    return A*sin(B*x - C) + D

def cosine_func(A, B, C, D, x):
    return A*cos(B*x - C) + D



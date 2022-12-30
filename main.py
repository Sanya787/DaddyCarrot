import os
import sys

import pygame


first_level = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 2, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

second_level = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

third_level = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

base_of_levels = [
    first_level,
    second_level,
    third_level
]

PAUSE = False
LEVEL = 0
tile_size = 25
screen_width = 1000
screen_height = 700

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
dead_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
pay_group = pygame.sprite.Group()
finish_group = pygame.sprite.Group()


class Finish(pygame.sprite.Sprite):
    # ------- Создать монетку ------- #
    def __init__(self, image, pos_x, pos_y):

        super().__init__(finish_group, all_sprites)

        self.image = image
        self.image = pygame.transform.scale(self.image, (40, 50))
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class Money(pygame.sprite.Sprite):
    # ------- Создать монетку ------- #
    def __init__(self, image, pos_x, pos_y):

        super().__init__(pay_group, all_sprites)

        self.image = image
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class Lava(pygame.sprite.Sprite):
    # ------- Создать монетку ------- #
    def __init__(self, image, pos_x, pos_y):

        super().__init__(dead_group, all_sprites)

        self.image = image
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


def load_image(filename, colorkey=None):
    # ------- Загрузка изображения ------- #
    path = os.path.join('images', filename)

    if not os.path.isfile(path):
        print(f"Файл с изображением '{path}' не найден")
        sys.exit()

    image = pygame.image.load(path)

    if colorkey is not None:
        image = image.convert()

        if colorkey == -1:
            colorkey = image.get_at((0, 0))

        image.set_colorkey(colorkey)

    return image


see_left = [
    pygame.transform.scale(load_image('carrot_left_1.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_left_2.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_left_3.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_left_4.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_left_5.png'), (50, 72))
]

see_right = [
    pygame.transform.scale(load_image('carrot_right_1.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_right_2.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_right_3.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_right_4.png'), (50, 72)),
    pygame.transform.scale(load_image('carrot_right_5.png'), (50, 72))
]


def take_image(index, see_right_true):
    if see_right_true:
        return see_right[index]
    else:
        return see_left[index]


def draw_grid():
    # ------- Рисовать сетку ------- #
    for line in range(0, 40):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


class Tile(pygame.sprite.Sprite):
    # ------- Создать блок------- #
    def __init__(self, image, pos_x, pos_y):

        super().__init__(tiles_group, all_sprites)

        self.image = image
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect().move(
            tile_size * pos_x, tile_size * pos_y)


class Carrot(pygame.sprite.Sprite):
    speed = 4
    carrot_image = load_image('carrot_right_1.png')

    def __init__(self, x, y):
        super().__init__(player_group, all_sprites)

        self.image = pygame.transform.scale(Carrot.carrot_image, (50, 70))
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.index = 0
        self.jumped = False
        self.dead = False
        self.rect.x = x
        self.count_wait = 0
        self.rect.y = y
        self.vel_y = 0
        self.see_right = False
        self.jump_count = 0

    def draw(self):
        # ------- Рисовать игрока ------- #
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        global room, all_sprites, tiles_group,\
            player_group, pay_group, finish_group, LEVEL, PAUSE, dead_group

        cooldown = 4
        self.count_wait += 1
        if self.count_wait > cooldown and not self.dead:
            self.index += 1
            self.count_wait = 0
            self.index = self.index % 5
            self.image = take_image(self.index, self.see_right)

        if not PAUSE:
            if not self.dead:
                delta_x = 0
                delta_y = 0

                key = pygame.key.get_pressed()

            # ------- Перемещение ------- #
                if key[pygame.K_SPACE] and not self.jumped and self.jump_count < 2:
                    self.vel_y = -13
                    self.jump_count += 1
                    self.jumped = True
                if not key[pygame.K_SPACE]:
                    self.jumped = False
                if key[pygame.K_LEFT]:

                    self.see_right = False
                    delta_x -= Carrot.speed

                if key[pygame.K_RIGHT]:

                    self.see_right = True
                    delta_x += Carrot.speed

                self.vel_y += 1
                if self.vel_y > 10:
                    self.vel_y = 10
                delta_y += self.vel_y
                # ------- Перемещение ------- #

                # ------- Проверка столкновения ------- #
                self.rect.y += delta_y

                if pygame.sprite.spritecollideany(self, tiles_group):

                    tile = pygame.sprite.spritecollide(self, tiles_group, False)[0]

                    self.rect.y -= delta_y
                    if tile.rect[1] - 10 > self.rect.y + 50:
                        self.rect.y = tile.rect[1] - 70
                        self.jump_count = 0

                    elif tile.rect[1] - 10 < self.rect.y + 50:
                        self.rect.y = tile.rect[1] + 25
                        self.vel_y = 0

                self.rect.x += delta_x

                if pygame.sprite.spritecollideany(self, tiles_group):
                    tile = pygame.sprite.spritecollide(self, tiles_group, False)[0]

                    self.rect.x -= delta_x
                    if tile.rect[0] - tile_size / 2 > self.rect.x + 35:
                        self.rect.x = tile.rect[0] - 50

                    elif tile.rect[0] - tile_size / 2 < self.rect.x + 35:
                        self.rect.x = tile.rect[0] + 25

                if pygame.sprite.spritecollideany(self, pay_group):
                    for elem in pay_group:
                        if pygame.Rect.colliderect(elem.rect, self.rect):
                            room.money_up += 1
                            room.text = room.font.render(str(room.money_up), True, (255, 255, 255))
                            elem.kill()

                # ------- Проверка столкновения ------- #

                if self.rect.bottom > screen_height:
                    self.rect.bottom = screen_height
                    delta_y = 0

                if pygame.sprite.spritecollideany(self, finish_group):
                    tiles_group = pygame.sprite.Group()
                    player_group = pygame.sprite.Group()
                    pay_group = pygame.sprite.Group()
                    finish_group = pygame.sprite.Group()
                    dead_group = pygame.sprite.Group()
                    all_sprites = pygame.sprite.Group()

                    LEVEL += 1
                    room = World(base_of_levels[LEVEL])
                if pygame.sprite.spritecollideany(self, dead_group) and not self.see_right:
                    self.image = pygame.transform.scale(load_image('dead_carrot.png'), (50, 70))
                    self.dead = True
                elif pygame.sprite.spritecollideany(self, dead_group) and self.see_right:
                    self.image = pygame.transform.scale(load_image('dead_carrot_right.png'), (50, 70))
                    self.dead = True

                # -------Рисуем хитбокс по размеру игрока------- #
                # pygame.draw.rect(screen, (255, 255, 255), (self.rect[0] + 5, self.rect[1], self.rect[2] - 23, self.rect[3]), 2)
                # -------Рисуем хитбокс по размеру игрока------- #


class ChangeLevel:

    def update(self, event):
        global room, all_sprites, tiles_group, player_group, pay_group, finish_group, LEVEL, dead_group

        if event.type == pygame.MOUSEBUTTONUP and 5 < event.pos[0] < 55 and 5 < event.pos[1] < 55:
            room = Menu()

            all_sprites = pygame.sprite.Group()
            tiles_group = pygame.sprite.Group()
            dead_group = pygame.sprite.Group()
            player_group = pygame.sprite.Group()
            pay_group = pygame.sprite.Group()
            finish_group = pygame.sprite.Group()

        elif event.type == pygame.MOUSEBUTTONUP and 225 < event.pos[0] < 315 and 242 < event.pos[1] < 332:
            room = World(first_level)
            LEVEL = 1
        elif event.type == pygame.MOUSEBUTTONUP and 340 < event.pos[0] < 430 and 242 < event.pos[1] < 332:
            room = World(second_level)
            LEVEL = 2
        elif event.type == pygame.MOUSEBUTTONUP and 455 < event.pos[0] < 535 and 242 < event.pos[1] < 332:
            room = World(third_level)
            LEVEL = 3

    def draw(self):
        screen.blit(pygame.transform.scale(load_image('back.png'), (50, 50)), (5, 5))

        coord_x = [
            225, 340, 455, 570, 685
        ]

        coord_y = [
            242, 357
        ]

        for i in range(2):
            for j in range(5):
                screen.blit(pygame.transform.scale(load_image(f'lvl{i * 5 + j + 1}.png'), (90, 90)), (coord_x[j], coord_y[i]))


class World:
    def __init__(self, data):
        self.font = pygame.font.Font(None, 50)
        self.tile_sprites = pygame.sprite.Group()
        self.text = self.font.render("0", True, (255, 255, 255))
        self.back_button = pygame.transform.scale(load_image('back.png'), (50, 50))
        self.tile_list = []
        self.money_up = 0
        self.money_img = load_image('money.png')
        dirt_img = load_image('dirt.png')
        lava_img = load_image('lava.png')
        grass_img = load_image('grass.png')
        finish_img = load_image('checkpoint.png')

        # ------- Сгенерировать уровень по карте (data) ------- #
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    Tile(dirt_img, col_count, row_count)
                    self.tile_list.append(tile)
                elif tile == 2:
                    Tile(grass_img, col_count, row_count)
                    self.tile_list.append(tile)
                elif tile == 3:
                    Money(self.money_img, col_count, row_count)
                elif tile == 4:
                    Finish(finish_img, col_count, row_count)
                elif tile == 5:
                    self.carrot = Carrot(col_count * tile_size, row_count * tile_size)
                elif tile == 6:
                    Lava(lava_img, col_count, row_count)
                col_count += 1
            row_count += 1

    def update(self, event):
        # ------- Обновить уровень ------- #
        global room, all_sprites, tiles_group, player_group, pay_group, finish_group, PAUSE, dead_group

        if self.carrot.dead:
            if event.type == pygame.MOUSEBUTTONUP and 385 < event.pos[0] < 615 and 290 < event.pos[1] < 340:

                self.carrot.dead = False

                all_sprites = pygame.sprite.Group()
                tiles_group = pygame.sprite.Group()
                dead_group = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                pay_group = pygame.sprite.Group()
                finish_group = pygame.sprite.Group()

                room = World(first_level)

            elif event.type == pygame.MOUSEBUTTONUP and 385 < event.pos[0] < 615 and 365 < event.pos[1] < 414:

                self.carrot.dead = False

                room = Menu()

                all_sprites = pygame.sprite.Group()
                tiles_group = pygame.sprite.Group()
                dead_group = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                pay_group = pygame.sprite.Group()
                finish_group = pygame.sprite.Group()

        if not PAUSE:

            if event.type == pygame.MOUSEBUTTONUP and 945 < event.pos[0] < 995 and 5 < event.pos[1] < 55:
                PAUSE = not PAUSE

        else:

            if event.type == pygame.MOUSEBUTTONUP and 385 < event.pos[0] < 615 and 290 < event.pos[1] < 340:
                PAUSE = not PAUSE

            elif event.type == pygame.MOUSEBUTTONUP and 385 < event.pos[0] < 615 and 365 < event.pos[1] < 414:

                PAUSE = not PAUSE
                room = Menu()

                all_sprites = pygame.sprite.Group()
                tiles_group = pygame.sprite.Group()
                dead_group = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                pay_group = pygame.sprite.Group()
                finish_group = pygame.sprite.Group()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            PAUSE = not PAUSE

        # ------- Обновить нужно только игрока на поле ------- #
        self.carrot.update()

    def draw(self):
        # ------- Нарисовать уровень ------- #
        all_sprites.draw(screen)

        # ------- Счетчик монет ------- #
        screen.blit(pygame.transform.scale(self.money_img, (25, 25)), (3, 3))
        screen.blit(self.text, (31, 0))

        screen.blit(pygame.transform.scale(load_image('pause.png'), (50, 50)), (945, 5))

        if PAUSE:
            screen.blit(load_image('pause_slide.png'), (350, 250))

        if self.carrot.dead:
            screen.blit(load_image('fail_title.png'), (0, 0))
            screen.blit(load_image('fail_slide.png'), (350, 250))

        # ------- Кнопка назад ------- #
        # screen.blit(self.back_button, (0, 0))


class Menu:
    def __init__(self):

        self.image = load_image('button_start.png')
        self.image_change = load_image('button_change_lvl.png')
        self.rect = self.image.get_rect()

    def update(self, event):
        # ------- Обновить меню ------- #
        global room, LEVEL
        # ------- Если нажали начать: ------- #
        if event.type == pygame.MOUSEBUTTONUP and 385 < event.pos[0] < 615 and 250 < event.pos[1] < 300:
            room = World(first_level)
            LEVEL = 1
        elif event.type == pygame.MOUSEBUTTONUP and 385 < event.pos[0] < 615 and 325 < event.pos[1] < 375:
            room = ChangeLevel()
        elif event.type == pygame.MOUSEBUTTONUP and 385 < event.pos[0] < 615 and 400 < event.pos[1] < 450:
            room = ChangeScin()

    def draw(self):
        # ------- Отрисовать меню ------- #
        screen.blit(self.image, (385, 250))
        screen.blit(self.image_change, (385, 325))
        screen.blit(load_image('button_change_scin.png'), (385, 400))
        screen.blit(load_image('title.png'), (0, 15))


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
room = Menu()


def main():
    running = True

    while running:
        # ------- Залить фон ------- #
        screen.blit(load_image('background.png'), (0, 0))

        # ------- Если это какой-то уровень: ------- #
        if isinstance(room, World):
            room.carrot.update()

        # ------- Нажатия ------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # ------- Обновить с event ------- #
            room.update(event)

        # ------- Отрисовать: ------- #
        # draw_grid()
        room.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()

import math
import os
import random
import re
import sys

def staircase(n):
    layer = []
    count = n
    for numbers in range (0, n):
        for numbers in range (0,count-1):
            layer.append(" ")
        for numbers in range (n - len(layer)):
            layer.append("#")
        count -= 1
        print(''.join(str(e) for e in layer))
        layer = []

input = int(input("Pick a number. "))
staircase(input)
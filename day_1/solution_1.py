#!/usr/bin/python

import numpy as np

input = np.loadtxt("input.txt")

for i in range(0, len(input) - 1):
    for j in range(i, len(input)):
        if (input[i] + input[j]) == 2020:
            print(input[i] * input[j])
            break

#!/usr/bin/python

import numpy as np

input = np.loadtxt("input.txt")

for i in range(0, len(input) - 2):
    for j in range(i, len(input) - 1):
        for k in range(j, len(input)):
            if (input[i] + input[j] + input[k]) == 2020:
                print(input[i] * input[j] * input[k])
                break

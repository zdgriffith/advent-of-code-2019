#!/usr/bin/env python

import numpy as np

def passing(numbers):
    diff = np.diff(numbers)

    # TODO: we can surely do better...
    exact_2 = False
    for i in range(5):
        if i == 0:
            if diff[i] == 0 and diff[i+1] != 0:
                exact_2 = True
        elif i == 4:
            if diff[i] == 0 and diff[i-1] != 0:
                exact_2 = True
        else:
            if diff[i-1] != 0 and diff[i] == 0 and diff[i+1] != 0:
                exact_2 = True
            
    return exact_2 & np.all(diff >= 0)

if __name__ == "__main__":
    input_min = 130254
    input_max = 678275
    count = 0
    for number in np.arange(input_min, input_max + 1, 1):
        numbers = np.array([int(i) for i in str(number)])
        if passing(numbers):
            count += 1
    print(count)

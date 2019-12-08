#!/usr/bin/env python

import numpy as np

def passing(numbers):
    diff = np.diff(numbers)
    return np.any(diff == 0) & np.all(diff >= 0)

if __name__ == "__main__":
    input_min = 130254
    input_max = 678275
    count = 0
    for number in np.arange(input_min, input_max + 1, 1):
        numbers = np.array([int(i) for i in str(number)])
        if passing(numbers):
            count += 1
    print(count)
#!/usr/bin/env python

import numpy as np


def mass_to_fuel(mass):
    return mass // 3 - 2


if __name__ == "__main__":
    masses = np.loadtxt('input.txt')
    total = 0
    while np.any(masses):
        masses = np.maximum(mass_to_fuel(masses), 0)
        total += np.sum(masses)
    print(total)

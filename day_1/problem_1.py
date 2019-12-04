#!/usr/bin/env python

import numpy as np


def mass_to_fuel(mass):
    return mass // 3 - 2


if __name__ == "__main__":
    masses = np.loadtxt('input.txt')
    print(np.sum(mass_to_fuel(masses)))

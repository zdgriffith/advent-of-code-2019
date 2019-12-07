#!/usr/bin/env python

import numpy as np

if __name__ == "__main__":
    program = np.loadtxt('input.csv', delimiter=',')
    program[1:3] = [12, 2]

    opcode_indices = np.arange(len(program))[::4]
    commands = [program[i:i+4] for i in opcode_indices]

    for opcode, in_1, in_2, out in commands:
        if opcode == 99:
            break
        elif opcode == 1:
            program[out] = program[in_1] + program[in_2]
        elif opcode == 2:
            program[out] = program[in_1] * program[in_2]
        else:
            raise ValueError('Clearly something went wrong here...')
    print(program[0])


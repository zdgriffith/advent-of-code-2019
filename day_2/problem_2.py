#!/usr/bin/env python

import copy
import numpy as np
from itertools import product

def run(program, noun=0, verb=0):
    program = copy.deepcopy(program)
    program[1:3] = [noun, verb]
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
            raise ValueError(f'invalid opcode value! opcode={opcode}')
    return program[0]


def get_relation(program, arg='noun'):
    ''' this should also get variable powers...'''
    diff = run(program, **{arg: 2}) - run(program, **{arg: 1})
    diff2 = run(program, **{arg: 3}) - run(program, **{arg: 2})

    if diff == diff2:
        return diff

if __name__ == "__main__":
    program = np.loadtxt('input.csv', delimiter=',').astype('int')
    output = 19690720

    intercept = run(program)
    noun_coef = get_relation(program, arg='noun')
    verb_coef = get_relation(program, arg='verb')
    noun = (output - intercept) // noun_coef
    verb = (output - intercept - noun_coef * noun) // verb_coef
    print(f'noun={noun}, verb={verb}')
    
    # In practice the above does not generalize
    # so brute force is also an option...
    for noun, verb in product(range(100), range(100)):
        result = run(program, noun, verb)
        if result == output:
            print(f'noun={noun}, verb={verb}')
            break

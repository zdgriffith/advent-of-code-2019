#!/usr/bin/env python

import csv

import numpy as np
import operator

def run(program, in_code=1):

    ptr = 0
    while ptr < len(program):
        opcode = int(program[ptr][3:])
        
        # instructions that don't have parameter mode
        if opcode == 3:
            program[int(program[ptr+1])] = f'{in_code:05d}'
            ptr += 2
            continue
        elif opcode == 99:
            break
        
        par_mode = [int(m) for m in program[ptr][:3]]
        par_mode.reverse()

        in_par = {}
        for i in range(2):
            if i == 1 and opcode == 4:
                continue
            in_par[i] = int(program[ptr + i + 1])
            if par_mode[i] == 0:
                in_par[i] = int(program[in_par[i]])

        if opcode == 4:
            print(in_par[0])
            ptr += 2
            continue
        elif opcode == 5:
            if in_par[0] != 0:
                ptr = in_par[1]
            else:
                ptr += 3
            continue
        elif opcode == 6:
            if in_par[0] == 0:
                ptr = in_par[1]
            else:
                ptr += 3
            continue
        elif opcode == 7:
            if in_par[0] < in_par[1]:
                out = 1
            else:
                out = 0
            program[int(program[ptr+3])] = f'{out:05d}'
            ptr += 4
            continue
        elif opcode == 8:
            if in_par[0] == in_par[1]:
                out = 1
            else:
                out = 0
            program[int(program[ptr+3])] = f'{out:05d}'
            ptr += 4
            continue

        ops = {1: operator.add, 2: operator.mul}
        if opcode not in ops:
            raise ValueError(f'invalid opcode value! opcode={opcode}')
        ops_func = ops[opcode]
        program[int(program[ptr+3])] = f'{ops_func(in_par[0], in_par[1]):05d}'
        ptr += 4


if __name__ == "__main__":
    with open('TEST.csv') as f:
        csv_reader = csv.reader(f, delimiter=',')
        test = [row for row in csv_reader][0]
        test = [f'{int(i):05d}' for i in test]
        run(test, in_code=5)

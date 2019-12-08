#!/usr/bin/env python

import numpy as np
import pandas as pd

directions = {
    'R': np.array([1, 0]),
    'L': np.array([-1, 0]),
    'U': np.array([0, 1]),
    'D': np.array([0, -1]),
}

def convert_commands(command):
    if not isinstance(command, str):
        return np.array([0, 0])
    else:
        return directions[command[0]] * int(command[1:])


def get_path(start_pos, command):
    idx = np.argmax(np.abs(command))
    steps = np.abs(command).max()
    path = np.array((np.zeros(steps), 1 + np.arange(steps)))
    if idx == 0:
        path = np.flip(path, axis=0)
    if command[idx] < 0:
        path = -path

    path = start_pos[:, np.newaxis] + path
    return path.T.astype(int)


if __name__ == "__main__":
    wires = pd.read_csv('wires.csv', header=None)
    wires = wires.applymap(convert_commands)

    positions = []
    for wire in wires.values:
        path = np.zeros((2, 2))
        wire_pos = []
        for command in wire:
            path = get_path(path.T[:, -1], command)
            wire_pos.extend(list(path))
        positions.append(wire_pos)
    intersections = set(tuple(map(tuple, positions[0]))) & set(tuple(map(tuple, positions[1])))
    intersections -= set(((0, 0), (0, 0)))

    steps = np.zeros(len(intersections))
    for i in range(2):
        indices = [np.nonzero(np.all(positions[i] == np.array(j), axis=1))[0][0] for j in intersections]
        steps += np.array(indices) + 1
    print(steps.min())

#!/usr/bin/env python

if __name__ == "__main__":
    orbits = {}
    with open('input.txt', 'r') as f:
        for line in f.read().splitlines():
            host, sat = line.split(')')
            orbits[sat] = host

    tot_orbits = 0 
    for sat, host in orbits.items():
        tot_orbits += 1
        while host in orbits:
            host = orbits[host]
            tot_orbits += 1
    print(tot_orbits)
#!/usr/bin/env python


def get_orbit_struct(orbits, sat):
    struct = []
    while sat in orbits:
        sat = orbits[sat]
        struct.append(sat)
    return struct


if __name__ == "__main__":
    orbits = {}
    with open('input.txt', 'r') as f:
        for line in f.read().splitlines():
            host, sat = line.split(')')
            orbits[sat] = host

    my_struct = get_orbit_struct(orbits, 'YOU')
    santa_struct = get_orbit_struct(orbits, 'SAN')
    for host in my_struct:
        if host in santa_struct:
            print(my_struct.index(host) + santa_struct.index(host))
            break
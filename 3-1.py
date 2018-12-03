#!/usr/local/bin/python3
import numpy

file = open('3-1-input.txt')
x_max = 1000
y_max = 1000
overlap = 0
fabric = numpy.zeros((y_max, x_max))

print('Dividing fabric...')
for line in file:
    a = line.split()
    x_begin, y_begin = a[2][0:-1].split(',')
    x_move, y_move = a[3].split('x')
    x_begin = int(x_begin)
    y_begin = int(y_begin)
    x_move = int(x_move)
    y_move = int(y_move)

    for x in range(x_begin, x_begin + x_move):
        for y in range(y_begin, y_begin + y_move):
            fabric[y, x] = fabric[y, x] + 1

print('Calculating overlap...')
for x in range(x_max):
    for y in range(y_max):
        if fabric[y,x] > 1:
            overlap = overlap + 1

print(overlap)
print()

print('Finding unique non-overlap...')
file = open('3-1-input.txt')

for line in file:
    a = line.split()
    id = a[0][1:]
    unique = 0
    x_begin, y_begin = a[2][0:-1].split(',')
    x_move, y_move = a[3].split('x')
    x_begin = int(x_begin)
    y_begin = int(y_begin)
    x_move = int(x_move)
    y_move = int(y_move)
    #print(x_begin, y_begin, x_move, y_move)

    for x in range(x_begin, x_begin + x_move):
        for y in range(y_begin, y_begin + y_move):
            if fabric[y, x] > 1:
                unique = unique + 1
    if unique == 0:
        print(id)

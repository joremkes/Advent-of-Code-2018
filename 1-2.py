#!/usr/bin/python3.6
#file = open('1-1-input.txt')

frequency = 0
frequencies = []
answer_found = False

print('Looping through file')
while answer_found == False:
    file = open('1-1-input.txt')

    print('.', end='', flush=True)

    for line in file:
        operator = line[0]
        number = int(line[1:len(line)])

        if operator == '+':
            frequency = frequency + number
        elif operator == '-':
            frequency = frequency - number
        else:
            print('Error')

        if frequency in frequencies:
            print(frequency)
            answer_found = True
            break
        else:
            frequencies.append(frequency)

file = open('1-1-input.txt')

frequency = 0

for line in file:
    operator = line[0]
    number = int(line[1:len(line)])
    if operator == '+':
        frequency = frequency + number
    elif operator == '-':
        frequency = frequency - number
    else:
        print('Error')



print(frequency)

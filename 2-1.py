file = open('2-1-input.txt')
count2 = 0
count3 = 0

for line in file:
    count_list = []
    for letter in line:
        count = line.count(letter)
        count_list.append(count)

    if 2 in count_list:
        count2 = count2 + 1

    if 3 in count_list:
        count3 = count3 + 1

print(count2 * count3)

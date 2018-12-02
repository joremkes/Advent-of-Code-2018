##input = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

file = open('2-1-input.txt')
input = []

for line in file:
    input.append(line)

for a in input:
    for b in input:
        solution = ''
        difference = 0
        for i in range(len(a)):
            if a[i] == b[i]:
                solution = solution + a[i]
            else:
                difference = difference + 1
        if difference == 1:
            print(solution)

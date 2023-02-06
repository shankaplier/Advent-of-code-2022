#_________code of part one___________
'''test = open("Day3.txt", "r")
for x in test:
    midpoint = len(x)//2
    compartment1 = x[:midpoint]
    compartment2 = x[midpoint:]
    for y in compartment1:
        if y in compartment2:
            print(y)
            if ord(y) in range(97,123):
                sum += ord(y)-96
                break
            else:
                sum += ord(y)-38
                break'''

#_________code of part two___________
test = open("Day3.txt", "r")
sum = 0
position = 1
group = []
for x in test:
    while position % 4 != 0:
        group.append(x.split("\n")[0])
        position += 1
        break
    while position % 4 == 0:
        common_1_2 = []
        for y in group[0]:
            if y in group[1] and y in group[2]:
                if y in group[2]:
                    if ord(y) in range(97, 123):
                        sum += ord(y) - 96
                        break
                    else:
                        sum += ord(y) - 38
                        break
        position += 1
        group = []
        break

print(sum)
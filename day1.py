test = open("Day1.txt", "r")
food = {}
i = 1

food[1] = 0
for x in test:
    if x != "\n":
        food[i] += int(x)
    else:
        i += 1
        food[i] = 0

elves = []
x = 3
while x > 0:
    elves.append(food.pop(max(food, key=food.get)))
    x -= 1

sum = 0
for x in elves:
    sum += x

print(sum)



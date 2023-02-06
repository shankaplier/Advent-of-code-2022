test = open("Day2.txt", "r")

global score
score = 0
choice_score = {"X": 1, "Y": 2, "Z": 3}

for x in test:
    opponent = x[0]
    player = x[2]

    if player == "Y":
        score += 3

    if player == "X":
        score += 0

    if opponent == "C" and player == "X":
        score += 6
    else:
        score += 0

    score += choice_score[opponent]

print(score)
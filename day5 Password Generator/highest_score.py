# find highest score without using max()
scores = [55, 92, 29, 99, 13, 98, 91, 29]

highest_score = 0
for score in scores:
    if score > highest_score:
        highest_score = score
print(highest_score)
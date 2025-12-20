student_scores = [150, 142, 285, 120, 171, 184, 149, 24, 355, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
print(high_score)

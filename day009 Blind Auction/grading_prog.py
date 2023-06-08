student_scores = {
    "harry": 81,
    "hermoine": 99,
    "ron": 78,
    "draco": 74,
    "neville": 62
}
# question replace the marks with grandes
# 91 above - outstanding
# 81 to 90 - exceptional
# 71 to 80 - acceptable
# below 80 - fail

for student in student_scores:
    if student_scores[student]>=91 and student_scores[student]<=101:
        student_scores[student] = "outstanding"
    elif student_scores[student]>=81 and student_scores[student]<=90:
        student_scores[student] = "exceptional"
    elif student_scores[student]>=71 and student_scores[student]<=80:
        student_scores[student] = "acceptable"
    else:
        student_scores[student] = "fail"

print(student_scores)
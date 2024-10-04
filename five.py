students_scores = [('John', 85), ('Maria', 62), ('Tom', 76), ('Sarah', 90)]

lowest_student = students_scores[0][0]
lowest_score = students_scores[0][1]

for student, score in students_scores:
    if score < lowest_score:
        lowest_student = student
        lowest_score = score

print("Student with the lowest score:", lowest_student)
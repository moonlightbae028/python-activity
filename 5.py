students_scores = [('John', 85), ('Maria', 92), ('Tom', 76), ('Sarah', 90), ('Keysie', 93)]
highest_score_student = students_scores[0]
for student in students_scores:
    if student[1] > highest_score_student[1]:
        highest_score_student = student
print(highest_score_student[0])  

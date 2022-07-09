def gradingStudents(grades):
    rounded_grades = list()
    for i in range(len(grades)):
        k = (grades[i]//5)*5 + 5
        if (k - grades[i]) < 3 and grades[i] >= 38:
            rounded_grades.append(k)
        else:
            rounded_grades.append(grades[i])
    return rounded_grades

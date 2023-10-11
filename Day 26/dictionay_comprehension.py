# new_dict = {new_key: new_value for item in  list}
# new_dict = {new_key: new_value for (key, value ) in dict.item()}
# new_dict = {new_key: new_value for (key, value ) in dict.item() if test}
import random
import pandas as pd

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {name: random.randint(1,100) for name in names}
print(students_scores)


passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)


student_dict = {
    "student": ["Alex", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)


for (index, row) in student_data_frame.iterrows():
    if row.student == "James":
        print(row.student, row.score)
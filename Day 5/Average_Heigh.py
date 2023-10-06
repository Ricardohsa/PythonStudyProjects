# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_students_heights = 0
qtd_students = len(student_heights)

for heights in student_heights:
    sum_students_heights = sum_students_heights + heights

average_heigths = round((sum_students_heights / qtd_students))
print(average_heigths)
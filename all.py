students = ['John', 'Maria', 'David', 'Samantha']
index = int(input("Enter the index: "))

if 0 <= index < len(students):
    print(students[index])
else:
    print("Index out of range")


numbers = (1, 4, 7, 10, 13, 16)
even_sum = 0
even_count = 0

for number in numbers:
    if number % 2 == 0:  
        even_sum += number
        even_count += 1

if even_count > 0:
    average = even_sum / even_count
    print(average)
else:
    print("No even numbers found")


people = {'users': {'John': 19, 'Emily': 21, 'Sarah': 25, 'Tom': 18}}

for name, age in people['users'].items():
    if age > 19:
        print(name)


numbers = (1, 3, 2, 4, 3, 1, 2, 5, 10)
counts = {}

for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1
        
for number, count in counts.items():
    if count > 1:
        print(number)


students_scores = [('John', 85), ('Maria', 62), ('Tom', 76), ('Sarah', 90)]

lowest_student = students_scores[0][0]
lowest_score = students_scores[0][1]

for student, score in students_scores:
    if score < lowest_score:
        lowest_student = student
        lowest_score = score

print("Student with the lowest score:", lowest_student)
students = ['John', 'Maria', 'David', 'Samantha']
index = int(input("Enter the index: "))

if 0 <= index < len(students):
    print(students[index])
else:
    print("Index out of range")
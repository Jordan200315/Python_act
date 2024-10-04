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

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
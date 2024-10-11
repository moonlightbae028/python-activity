numbers = (1, 3, 2, 4, 3, 1, 2, 5)
repeated_numbers = []
for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1
    if count > 1 and numbers[i] not in repeated_numbers:
        repeated_numbers.append(numbers[i])
        
for number in repeated_numbers:
    print(number)


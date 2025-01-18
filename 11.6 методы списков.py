numbers = [8, 9, 10, 11]
numbers.remove(numbers[1])
numbers.insert(1, 17)
numbers.extend([4, 5, 6])
numbers.remove(numbers[0])
numbers += numbers
numbers.insert(3, 25)
print(numbers)

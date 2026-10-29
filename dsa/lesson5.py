def count_occurrences(number, target):
    count = 0 
    for numbers in number:
        if numbers == target:
            count += 1
    return count

print(count_occurrences([2, 5, 2, 8, 2], target = 2))
print(count_occurrences([1, 4, 7], target = 10))

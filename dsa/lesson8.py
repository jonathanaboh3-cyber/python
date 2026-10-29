def has_duplicates(numbers):
    if len(numbers) > len(set(numbers)):
        return True
    else:
        return False

print(has_duplicates([1, 2, 3, 2]))  
print(has_duplicates([1, 2, 3, 4]))  
print(has_duplicates([]))            
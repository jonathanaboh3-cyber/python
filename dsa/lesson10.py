def move_zeros(numbers):
    result = []

    for number in numbers:
        if number != 0:
            result.append(number)

    zeros = numbers.count(0)

    for i in range(zeros):
        result.append(0)

    return result


print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([1, 2, 3]))
print(move_zeros([0, 0, 5]))

def fibonacci():
    index = len(numbers)
    if num < 2:
        print(numbers[num])
    elif index == num:
        print(numbers[index - 1] + numbers[index - 2])
    elif index < num:
        numbers.append(numbers[index - 1] + numbers[index - 2])
        fibonacci()


num = int(input())
numbers = [0, 1]

fibonacci()

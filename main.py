with open('liczby.txt', 'r') as f:
    content = f.readline().split(', ')
    numbers = []
    letters = []
    for item in content:
        if item.isdigit():
            numbers.append(int(item))
        elif item.isalpha():
            letters.append(item)

print(numbers)
print(letters)

for i in range(len(numbers)):
    print(numbers)
    for j in range(0, len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

for i in range(len(letters)):
    print(letters)
    for j in range(0, len(letters)-i-1):
        if letters[j] > letters[j+1]:
            letters[j], letters[j+1] = letters[j+1], letters[j]

with open('posortowane_liczby.txt', 'w') as f:
    for number in numbers:
        f.write(str(number) + ', ')
    for letter in letters:
        f.write(str(letter) + ', ')

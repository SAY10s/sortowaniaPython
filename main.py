with open('liczby.txt', 'r') as f:
    numbers = f.readline().split(', ')
    print(numbers)
    numbers = [int(l) for l in numbers] #konwersja typu zmiennej, zmienia każdy kolejny indeks na numer
    print(numbers)

for i in range(len(numbers)):
    print(numbers)
    for j in range(0, len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

with open('posortowane_liczby.txt', 'w') as f:
    for number in numbers:
        f.write(str(number) + ', ')

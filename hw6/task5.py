import random

a = random.randint(1, 20)
attempts = 5
counter = 1

print(f"Я загадал число от 1 до 20. У тебя {attempts} попыток!")

while attempts > 0:
    guess = int(input(f"Попытка {counter}. Введите число: "))

    if guess == a:
        print("Ты угадал! Отличная работа.")
        break
    elif guess < a:
        print("Слишком мало!")
    else:
        print("Слишком много!")
    attempts -= 1
    counter += 1

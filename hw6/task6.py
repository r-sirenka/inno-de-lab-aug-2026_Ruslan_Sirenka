a = float(input("Введите первое число:"))
b = float(input("Введите второе число:"))
c = input("Введите оператор  (+, -, *, /):")
if c == "+":
    print (f"Результат: {a} + {b} = {a + b}")
elif c == "-":
    print (f"Результат: {a} - {b} = {a - b}")
elif c == "*":
    print (f"Результат: {a} * {b} = {a * b}")
elif c == "/":
    if b != 0:
        print (f"Результат: {a} / {b} = {a / b}")
    else: 
        print("Деление на ноль!") 
else:
    print (f"Ошибка операции")

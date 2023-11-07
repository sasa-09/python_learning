# запрос вводных данных
x = int(input("1 число: "))
y = int(input("2 число: "))
z = input("операция: ")

answer = 0

# проверка какая будет выполняться операция
if z == "+":
    answer = x + y

if z == "-":
    answer = x - y

if z == "*":
    answer = x * y

if z == "/":
    answer = x / y

if z == "**":
    answer = x ** y


# вывод ответа
print(answer)
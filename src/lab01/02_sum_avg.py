first_value = str(input("Введите превое число: "))
second_value = str(input("Введите второе число: "))
if "," in first_value or second_value:
    first_value = first_value.replace(",", ".")
    second_value = second_value.replace(",", ".")
a = float(first_value)
b = float(second_value)
avg = round((a + b) / 2, 2)
sum = a + b
print(sum, avg)

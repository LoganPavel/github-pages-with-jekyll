what = input("Что делаем?" "+, -, *, /, %:")

a = float(input("Введите первое число "))
b = float(input("Введите второе число "))

if what == ("+"):
	c = a + b
	print(c)
elif what == ("-"):
	c = a - b
	print(c)
elif what == ("*"):
	c = a * b
	print(c)
elif what == ("/"):
	c = a / b
	print(c)
elif what == ("%"):
	c = a % b
	print(c)
else:
	print("Действие невозможно!!")
	()
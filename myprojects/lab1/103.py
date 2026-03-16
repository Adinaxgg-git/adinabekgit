#Если строка состоит только из цифр — вывести "int", иначе — "str".
n=input()
if n.isdigit():
    print("int")
else:
    print("str")
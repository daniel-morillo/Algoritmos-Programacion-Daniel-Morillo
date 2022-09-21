num = input("Introduce un número")
is_valid = True

if num.isnumeric():
    num = int(num)
    if (num % 2 == 0):
        print(f"El número {num} es par")
    else:
        print("El número {} es impar".format(num))
else:
    is_valid= False
    print("ESTO NO SIRVE")


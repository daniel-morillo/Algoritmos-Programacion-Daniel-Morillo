
num1 = (input("Choose first number"))
num2 =(input("Choose first number"))
is_valid = True

if num1.isnumeric():
    num1 = float(num1)
else :
    is_valid= False

if num2.isnumeric():
    num2 = float(num2)
else :
    is_valid= False

if is_valid:
    if num2 == 0:
        print("You can not divide by zero")
    else:
         division= num1/num2
         print(division)    
else:
    print("INVALID NUMBERS")
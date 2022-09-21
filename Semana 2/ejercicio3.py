print("MENU DE OPCIONES \n")
print("""1 = Suma \n 2 = Resta \n   3 = Multiplicación \n  4 = División  \n""")

opcion = int(input("Selecciona una opción de 1 a 4"))

if (opcion == 1):
    num1 = int(input("Teclea tu primer número"))
    num2 = int(input("Teclea tu segundo número"))
    suma = num1 + num2
    print("El resultado es " + str(suma))

elif (opcion == 2):
    num1 = int(input("Teclea tu primer número"))
    num2 = int(input("Teclea tu segundo número"))
    resta = num1 - num2
    print("El resultado es " + str(resta))

elif (opcion == 3):
    num1 = int(input("Teclea tu primer número"))
    num2 = int(input("Teclea tu segundo número"))
    multiplicacion = num1 * num2
    print("El resultado es " + str(multiplicacion))

elif (opcion == 4):
    num1 = int(input("Teclea tu primer número"))
    num2 = int(input("Teclea tu segundo número"))
    division = num1 / num2
    print("El resultado es " + str(division))

else: 
    print("OPCION NO DISPONIBLE \n")

print("Fin de la ejecución")
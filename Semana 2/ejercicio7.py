print("MENU DE OPCIONES \n")
option = int(input("Selecciona una opción: \n1-Vegetariana\n2-No vegetariana\n->"))

if (option == 1):
    ingrediente = int(input("Selecciona una opción: \n1-Pimiento\n2-Tofu\n->"))
    if (ingrediente == 1):
        ingrediente = "Pimiento"
    elif(ingrediente == 2):
        ingrediente = "Tofu"
    else: 
        print("Ingrediente no disponible")
    print("La pizza es vegetariana y tiene mozzarella y {}".format(ingrediente))
elif (option == 2):
    ingrediente = int(input("Selecciona una opción: \n1-jamon\n2-salmon\n3-pepperoni->"))
    if (ingrediente== 1):
        ingrediente= "jamón"
    elif (ingrediente==2):
        ingrediente= "salmón"
    elif (ingrediente==3):
        ingrediente= "pepperoni"
    else:
        print("Ingrediente no disponible")
    print("La pizza no es vegetariana y tiene mozzarella y {}".format(ingrediente))
else:
    print ("Pizza no disponible")

       

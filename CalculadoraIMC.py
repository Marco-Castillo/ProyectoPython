def principal():
    #se solicita datos al usuario y se guardan en variables(nombre, apellido paterno y apellido materno)
    nombre = (input("Ingrese su nombre: "))
    apellidoP = input("Ingrese su apellido paterno: ")
    apellidoM = input("Ingrese su apellido materno: ")

    #si nombre, apellidop o apellidoM estan vacíos el programa imprime un mensaje de error y vuelve a llamar la funcion principal
    if nombre == "":
        print ("Intentalo de nuevo, llena correctamente tu nombre")
        return principal()
    if apellidoP == "":
        print ("Intentalo de nuevo, llena correctamente tu Apellido Paterno")
        return principal()
    if apellidoM == "":
        print ("Intentalo de nuevo, llena correctamente tu Apellido Materno")
        return principal()
   
    #se solicita datos al usuario y se guardan en variables(edad, estatura y peso)
    edad = int(input("ingresa tu edad: "))
    estatura = float (input("ingresa tu estatura en metros: "))
    peso = float(input("ingresa tu peso en kilogramos: "))

    #Se crea una variable de nombre estatura 2 para despues hacer la operación de estatura al cuadrado
    estatura2 = estatura**2
   
    #Se calcula el IMC multiplicando la variable "peso" por la variable que se acaba de crear "estatura2" y se guarda en una variable llamada IMC
    imc = peso/estatura2
   
    #se imprime el nombre completo, concatenando las variables de nombre, apellidoP y apellidoM
    print(f"\n\n\n\nTu nombre completo es : "+ nombre + " " + apellidoP + " " + apellidoM)
   
    #se crea una condición la cual evalua la edad para arrojar un mensaje y decir si eres menor o mayor de edad
    if (edad < 18):
        print(f"{edad} años, niñ@ todavía te piden la autorización de un adulto")
    else:
        print(f"{edad} años, ya estas en la edad del mundo de las facturas y los impuestos")
   
    #se imprime los datos que se solicitaron en un inicio "peso" "estatura"
    print(f"Tu peso es : {peso} kg.")
    print(f"Tu estatura es : {estatura} m.")
   
    #se crea una condición para arrojar un mensaje dependiendo de el resultado que se obtuvo al realizar el calculo de IMC
    if (imc >= 0 and imc<=18.5):
        print(f"Tu IMC es de {imc}, precaución estas por de bajo de tu peso\n\n")
    elif (imc >= 18.5 and imc<=24.9):
        print(f"Tu IMC es de {imc}, Muy bien te encuentras en tu peso ideal\n\n")
    elif (imc >= 25 and imc<=29.9):
        print(f"Tu IMC es de {imc}, lo que indica que tienes sobrepeso\n\n")
    elif (imc >= 30):
        print(f"Tu IMC es de {imc}, Mucho cuidado tienes obesidad\n\n")
        
principal()

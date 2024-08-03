def principal():
    nombre = (input("Ingrese su nombre: "))
    apellidoP = input("Ingrese su apellido paterno: ")
    apellidoM = input("Ingrese su apellido materno: ")
    edad = int(input("ingresa tu edad: "))
    estatura = float (input("ingresa tu estatura en metros: "))
    peso = float(input("ingresa tu peso en kilogramos: "))

    if nombre == "":
        print ("Intentalo de nuevo, llena correctamente tu nombre")
        return principal()
    if apellidoP == "":
        print ("Intentalo de nuevo, llena correctamente tu Apellido Paterno")
        return principal()
    if apellidoM == "":
        print ("Intentalo de nuevo, llena correctamente tu Apellido Materno")
        return principal()

    estatura2 = estatura**2
    imc = peso/estatura2
    
    print(f"Tu nombre completo es : "+ nombre + " " + apellidoP + " " + apellidoM)

    if (edad < 18):
        print("Niñ@ todavía te piden la autorización de un adulto")
    else:
        print("¡Ya estas en la edad del mundo de las facturas y los impuestos!")
    
    print(f"Tu peso es : {peso}")
    print(f"Tu estatura es : {estatura}")
    if (imc >= 0 and imc<=18.5):
        print("Bajo de peso")
    elif (imc >= 18.5 and imc<=24.9):
        print("Tu peso es ideal")
    elif (imc >= 25 and imc<=29.9):
        print("Tienes Sobrepeso")
    elif (imc >= 30):
        print("Estas Obesoooooooo")
    
    

    
principal()
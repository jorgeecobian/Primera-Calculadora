import math

print("1. Sumar   2. Restar")
print("3. Multiplicar  4. Dividir")
print("5. Raiz Cuadrada  6.Potencia")
print("------------------------------")

opciones=int(input("Opciones (ponga uno de los 4 numeros):"))

print("------------------------------")

while (opciones != 1 and opciones != 2 and opciones != 3 and opciones != 4 and opciones != 5 and opciones !=6):
    print("El numero introducido no corresponde con ninguna de las opciones.")
    opciones=int(input("Vuelva a escoger una de las cuatro opciones:"))

if (opciones == 1):
    numero=int(input("Introduzca el primer número:"))
    numero2=int(input("Introduzca el segundo número:"))
    print(numero,"+",numero2,"=", numero + numero2)

elif (opciones == 2):
    numero=int(input("Introduzca el primer número:"))
    numero2=int(input("Introduzca el segundo número:"))
    print(numero,"-",numero2,"=", numero - numero2)

elif (opciones == 3):
    numero=int(input("Introduzca el primer número:"))
    numero2=int(input("Introduzca el segundo número:"))
    print(numero,"x",numero2,"=", numero * numero2)

elif (opciones == 4):
    numero=int(input("Introduzca el primer número:"))
    numero2=int(input("Introduzca el segundo número:"))
    print(numero,"/",numero2,"=", numero / numero2)

elif (opciones == 5):
    numero=int(input("Introduzca el un número:"))
    print("Raíz cuandrada de",numero,"=",math.sqrt(numero))

elif (opciones == 6):
    numero=int(input("Introduzca la base:"))
    numero2=int(input("Introduzca el exponente:"))
    print(numero,"^",numero2,"=",numero ** numero2)
    

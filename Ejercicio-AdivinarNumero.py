# Programa para adivinar número.
import random
intentosRealizados = 0

print('Hola ¿Cual es tu nombre?')
miNombre = input()
número = random.randint(1, 30)

print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 30.')

while intentosRealizados < 6:
    print('Intenta adivinar.') 
    estimación = input()
    estimación = int(estimación)

    intentosRealizados = intentosRealizados + 1

    if estimación < número:
        print ('El número es muy bajo.') 
    if estimación > número:
        print('El número es muy alto.')
    if estimación == número:
        break 

if estimación == número:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')

if estimación != número:
    número = str(número)
    print('Pues no. El número que estaba pensando era ' + número)

def main():
        respuesta=input("¿Quieres seguir jugando?: y/n: ")
        if(respuesta == "n"):
            print("Juego finalizado")
            n = True

main()
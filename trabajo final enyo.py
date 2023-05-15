import random 

print ('¡Bienvenido usuario al menu principal de Enyogames')
print ('¡Comencemos!')

def piedra_papel_tijera ():
    print ('¡Bienvenido al juego de piedra, papel y tijera!')
    print ('¡Comencemos!')
    while (True):
        
        opciondeusuario= int (input('Ingrese que opción quiere: 1 piedra, 2 papel o 3 tijera (4 cancelar): '))
        if opciondeusuario in [1,2,3]:
            opcioncomputadora=random.randint(1,3)
            print('Yo escogí: '+ str (opciondeusuario))
            print('La computadora escogió : ' + str (opcioncomputadora)) 

            if opciondeusuario == opcioncomputadora: 
                print('Es empate')
            elif (opciondeusuario == 1 and opcioncomputadora ==2) or (opciondeusuario==3 and opcioncomputadora == 1) : 
                print( 'Usted perdió, gana la computadora')
                
            elif (opciondeusuario == 1 and opcioncomputadora ==3) or (opciondeusuario==2 and opcioncomputadora ==1):
                print ('Usted ganó')
        elif (opciondeusuario == 4):
            print ('Gracias por jugar, ¡vuelva pronto!')
            break 

        else:
            print ('No es correcta su opción, intente nuevamente')

def advinar_un_numero ():
    print ('¡Bievenido al juego de adivinar un número! Les deseamos suerte')
    print ('¡Comencemos!')
    while (True):
        
        opciondeusuario= int (input('¿Adivine un número del 1 al 10? (11 para cancelar)'))
        if opciondeusuario in [1,2,3,4,5,6,7,8,9,10]:
            opcioncomputadora=random.randint(1,10)
            print('Yo escogí: '+ str (opciondeusuario))
            print('La computadora escogió: ' + str (opcioncomputadora)) 

            if opciondeusuario == opcioncomputadora: 
                print('Adivinaste')
            elif (opciondeusuario != opcioncomputadora):
             print( 'Usted perdió, gana la computadora')
        elif (opciondeusuario == 11):
            print ('Gracias por jugar, ¡vuelva pronto!')
            break 
         
        else:
            print ('No es correcta su opción, intente nuevamente')         
            

valor_minimo = 1
valor_maximo = 6

def lanzar_un_dado ():
    print ('¡Bienvenido al juego de tirar un dado!')
    print ('¡Comencemos!')
    while (True):
    
        opciondeusuario= int (input('Por favor tire los dados o pulse 7 para salir: '))
        if opciondeusuario in [1,2,3,4,5,6]:
            opcioncomputadora=random.randint(valor_minimo,valor_maximo)
            print('Salió el número: ' + str (opciondeusuario))
            print('El número de la computadora es : ' + str (opcioncomputadora)) 

            if opciondeusuario == opcioncomputadora: 
             print('Es empate')
            elif (opciondeusuario < opcioncomputadora) : 
             print( 'Usted perdió, gana la computadora')
                
            elif (opciondeusuario > opcioncomputadora) :
                print ('Usted ganó')
            elif (opciondeusuario == 7):
             print ('Gracias por jugar, ¡vuelva pronto!')
            break 

    else:
        print ('No es correcta su opción, intente nuevamente')  



import matplotlib.pyplot as plt 
import numpy as np


def graficar_una_función_matemática ():
    x = np.arange(0,4*np.pi,0.1)   # start,stop,step
    y = np.sin(x)

    plt.plot(x,y)
    plt.show()
    
          

while (True):
    opciondeusuario= int (input('Ingrese que opción quiere: 1 piedra, papel o tijera \n 2 adivina un número \n 3 lanzar dados \n 4 graficar una función \n (6 cancelar): '))
    if opciondeusuario == 1: 
        piedra_papel_tijera ()   

    elif opciondeusuario == 2:
        advinar_un_numero () 
    
    elif opciondeusuario == 3:
        lanzar_un_dado ()
    elif opciondeusuario == 4:
         graficar_una_función_matemática ()
    elif opciondeusuario == 6:
     break



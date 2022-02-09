# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 08:52:43 2022

@author: FernandoSastrePérez
"""
jugar = "si"
while jugar == "si":
    
    print("BUENAS BUENAS BUENAS BIENVENIDO AL CASINO FERNANDO DONDE LAS GANAS NO TE ESTAMOS FRENANDO ")
    print()
    print("Jugar al BLACKJACK - 1")
    
    juego = int(input("¿A que quieres jugar? "))
    print()
    if juego == 1:
        
        ganancias = 0
        #Entramos al blackjack
        print("Buenas,  vamos a jugar al juego del 21" )
        print()
        
        #Declaramos variables necesarias
        punt = 0
        cartas = 0
        cartas_variable = [1, 1]
        
        #Le creamos el nombre y lo metemos en la lista
        usuario = input("Escribe tu nombre como jugador: ")
        print()
        
        #Le hacemos un monedero
        dinero = int(input("¿Cuanto dinero tienes? "))
        apuesta = int(input("¿Cuanto apuestas? "))
        
        #Abrimos el bucle de juego
        while cartas < len(cartas_variable) and punt < 21:
            
            #Ponemos el generador de numeros al azar
            import random
            resultado = random.randint(1,10)
            
            #Iniciamos los filtros de numeros para descubrir la puntuacion
            if resultado == 1:
                valor = int(input("¿Oh vaya cuanto quieres que valga tu AS 1 o 11? "))
                if valor == 1:
                    punt += 1
                if valor == 11:
                    punt += 11
                cartas += 1
                print(f"Te ha salido {resultado} que has hecho que valga {valor} llevas {punt}")
                print()
            if resultado == 2:
                punt += 2
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            if resultado == 3:
                punt += 3
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            if resultado == 4:
                punt += 4
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            if resultado == 5:
                punt += 5
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            if resultado == 6:
                punt += 6
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            if resultado == 7:
                punt += 7
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            if resultado == 8:
                punt += 8
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            if resultado == 9:
                punt += 10
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            if resultado == 10:
                punt += 10
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            print(f"Llevas {punt} puntos en {cartas} carta/s")
            print()
            
            #Declaramos el limite de puntuacion y ponemos la opcion de GAME OVER
            if punt > 21:
                print(f"Oh vaya te has pasado dado que tienes {punt} puntos y el maximo son 21 has perdido {apuesta} te queda {dinero - apuesta} 😱😱😱")
                ganancias = dinero - apuesta
            #Ofrecemos nuevas "cartas" al jugador dandole a elegir
            if cartas >= 2 and punt <= 21:
                mas = input(f"¿Quieres otra carta? Llevas {cartas}: ")
                print()
                if mas == "Si" or mas == "SI" or mas == "si":
                    (cartas_variable) += [1]
                if mas == "No" or mas == "NO" or mas == "no":
                    
                    #Le criticamos su jugada
                    if punt < 10:
                        print(f"Joe eres un betta como puedes deçjar de pedir cartas con {punt} puntos no ganas dinero 🤨🤨🤨🤨")
                    if punt >= 18 and punt <= 20:
                        print(f"Wow has jugado bastante bien tienes una buena puntuacion eh, tienes {punt} puntos como has jugado tan bien {(dinero - apuesta) + apuesta * 1.75} 😃😃😃😃")
                        ganancias = (dinero - apuesta) + apuesta * 1.75
                    if punt == 21:
                        print(f"Wow ha sido exacto en {cartas} cartas tienes {(dinero - apuesta) + apuesta * 3} 🥳🥳🥳🥳")
                        ganancias = (dinero - apuesta) + apuesta * 3
                    if punt > 10 and punt < 18:
                        print(f"Bastante mediocre tienes {punt} puntos")
            print()
        jugar = input("¿Quieres jugar a algo mas? ")
        jugar = jugar.lower()
        print()
        
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
    print("Jugar a la RULETA - 2")
    
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
            elif resultado == 2:
                punt += 2
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            elif resultado == 3:
                punt += 3
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            elif resultado == 4:
                punt += 4
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            elif resultado == 5:
                punt += 5
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            elif resultado == 6:
                punt += 6
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            elif resultado == 7:
                punt += 7
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            elif resultado == 8:
                punt += 8
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            elif resultado == 9:
                punt += 10
                cartas += 1
                print(f"Te ha salido {resultado}")
                print()
            elif resultado == 10:
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
            elif cartas >= 2 and punt <= 21:
                mas = input(f"¿Quieres otra carta? Llevas {cartas}: ")
                print()
                if mas == "Si" or mas == "SI" or mas == "si":
                    (cartas_variable) += [1]
                elif mas == "No" or mas == "NO" or mas == "no":
                    
                    #Le criticamos su jugada
                    if punt < 10:
                        print(f"Joe eres un betta como puedes deçjar de pedir cartas con {punt} puntos no ganas dinero 🤨🤨🤨🤨")
                    elif punt >= 18 and punt <= 20:
                        print(f"Wow has jugado bastante bien tienes una buena puntuacion eh, tienes {punt} puntos como has jugado tan bien {(dinero - apuesta) + apuesta * 1.75} 😃😃😃😃")
                        ganancias = (dinero - apuesta) + apuesta * 1.75
                    elif punt == 21:
                        print(f"Wow ha sido exacto en {cartas} cartas tienes {(dinero - apuesta) + apuesta * 3} 🥳🥳🥳🥳")
                        ganancias = (dinero - apuesta) + apuesta * 3
                    elif punt > 10 and punt < 18:
                        print(f"Bastante mediocre tienes {punt} puntos")
            print()
        jugar = input("¿Quieres jugar a algo mas? ")
        jugar = jugar.lower()
        print()
        
        
    if juego == 2:
        
            #Creamos variable ganancias
            ganancias = 0
            
            
            #Presentamos el juego
            print("Bienvenido a la ruleta de la fortuna donde nunca hay dias malos")
            print("Mira como se lanza la bolita GIRA QUE GIRA")
            
            #Le creamos el nombre y lo metemos en la lista
            usuario = input("Escribe tu nombre como jugador: ")
            print()
            
            #Creamos el numero aleaorio que sera donde cae la bolita
            import random
            resultado = random.randint(1,5)
            
            #Creamos el numero aleatorio que decide color
            import random
            color = random.randint(1,2)
            
            #Creamos una capacidad de apuestas
            tipo_apuesta = int(input("A que quieres apostar (1 = color) (2 = numero): "))
            
            
            
            if tipo_apuesta == 1:
                
                #SI HAS ACERTADO EL COLOR
                dinero = int(input("¿Cuanto dinero tienes? "))
                apuesta = int(input("¿Cuanto puedes apostar? "))
                color_apuesta = int(input("De que color quieres que sea tu apuesta (1 = rojo) (2 = negro): "))
                if color == color_apuesta:
                    print("Has acertado el color")
                    print()
                    print(f"Has gando y tienes {(dinero - apuesta)+ apuesta*1.5}")
                    ganancias = apuesta * 1.5 
                
                #SI HAS FALLADO EL COLOR
                else:
                    if color == 1:
                        print("HA SALIDO ROJO")
                        print()
                        print(f"Tu color no es el correcto dado que el color es el rojo te quedan {dinero - apuesta}")
                        ganancias = - apuesta
                        print()
                        print(f"Tienes unas ganacias de {ganancias} monedas")
                    elif color == 2:
                        print("HA SALIDO NEGRO")
                        print()
                        print(f"Tu color no es el correcto dado que el color es el negro te quedan {dinero - apuesta}")
                        ganancias = - apuesta
                        print()
                        print(f"Tienes unas ganacias de {ganancias} monedas")
                        
            elif tipo_apuesta == 2:
                
                #SI HAS ACERTADO EL LUGAR
                dinero = int(input("¿Cuanto dinero tienes? "))
                apuesta = int(input("¿Cuanto puedes apostar? "))
                lugar_apuesta = int(input("Elige una casilla de las 5: "))
                if lugar_apuesta == resultado:
                    print(f"OJO HAS ACERTADO la bolita ha caido en donde apostaste que es {resultado} te quedan {(dinero - apuesta) + apuesta * 4}")
                    ganancias = apuesta * 4
                    print()
                    print(f"Tienes unas ganacias de {ganancias} monedas")
                else:
                    print(f"Oh vaya la bolita no ha caido en {lugar_apuesta} porque ha caido en {resultado} te has quedado  con {dinero - apuesta}")
                    ganancias = dinero - apuesta
                    print()
                    print(f"Tienes unas ganacias de {ganancias} monedas")
            jugar = input("¿Quieres jugar a algo mas? ")
            jugar = jugar.lower()
            print()
            
            
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
        
        
    elif juego == 2:
        
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
            
    elif juego == 3:
        #Entramos al juego de los dados
        print("Bueno bueno vamos a jugar a los dados lets go")
        
        #Generamos lo que es el reusltado de dado
        import random
        resultado = random.randint(1,10)
        
        #Definimos el multiplicador
        mult = 1
        
        #Definimos las ganancias
        ganancias = 0
        
        #Explica el juego
        print("Te explico, si sacas en un dado de 10 caras un 1 o 2 pierdes la apuesta y todo tu progreso")
        print("Si scacas algo que no sea eso como eso se te multiplica por 1.(ese numero)")
        print("Saca un 6 pues se multiplica por 1.6")
        
        #Le creamos el nombre y lo metemos en la lista
        usuario = input("Escribe tu nombre como jugador: ")
        print()
        
        #Generamos variables del monedero
        dinero = int(input("¿Cuanto dinero tienes? "))
        apuesta = int(input("¿Cuanto puedes apostar? "))
        #Definimos el querer jugar mas
        mas = "si"
        
        #Creamos fichero
        fichero_dados = open("Ganancias dados.txt", 'a')
        
        #Marcamos que no puede apostar EXACTAMENTE lo que tiene
        if dinero != apuesta:
            #Marcamos la posibilidad de ganar
            while resultado > 2 and mas == "si":
                
                #Le contamos lo que ha salido
                print(f"Ojo ha salido un {resultado} es decir se te multiplica tus {apuesta} por {mult + (resultado / 10)} tienes {(dinero - apuesta) + (apuesta * (mult + (resultado / 10)))}")
                print()
                
                #Le contamos como va
                ganancias = apuesta * (mult + (resultado / 10))
                dinero = (dinero - apuesta) + (apuesta * (mult + (resultado / 10)))
                print()
                print(f"Llevas {ganancias} de ganancias")
                
                #Le ofrecemos seguir
                mas = input("¿Quieres mas? ")
                mas  = mas.lower()
                print()
                if mas != "si":
                    print()
                    print(f"Oh vale pues te quedas con  {(dinero - apuesta) + (apuesta * (mult + (resultado / 10)))} y tienes unas ganancias de {ganancias} ")
                    
                    #Añadimos info al fichero
                    fichero_dados.write(f"{usuario}, debido a que ha salido un {resultado} sus {apuesta} de apuesta se han multiplicado por {mult + (resultado / 10)} y ha acabado con {(dinero - apuesta) + (apuesta * (mult + (resultado / 10)))} ha tenido unas ganancias de {ganancias}" + "\n")
                    #Cerramos fichero
                    fichero_dados.close()
                
                apuesta = (apuesta * (mult + (resultado / 10)))
                print(f"Estas apostando {apuesta} dineros")
                print()
                
                #Le tiramos de nuevo el dado
                import random
                resultado = random.randint(1,9)
            
                #Marcamos la posibilidad de perder
            while resultado == 1 or resultado == 2:
                print(f"Oh vaya ha salido un {resultado} y has perdido tus maravillosos {apuesta}")
                ganancias = - apuesta
                dinero = dinero + ganancias
                print(f"Como has perdido te quedan {dinero} dineros")
                print()
                
                #Añadimos info al fichero
                fichero_dados.write(f"{usuario}, oh vaya ha salido un {resultado} y has perdido tus maravillosos {apuesta} y te quedan {dinero - apuesta} teniendo unas ganancias de {ganancias}" + "\n")
                #Cerramos fichero
                fichero_dados.close()
                
                #Le tiramos de nuevo el dado
                import random
                resultado = random.randint(1,10)
            
            #Se va sabiendo las ganancias
            print()
            print(f"Has tenido unas gannacias de {ganancias}")
            
        else:
            print("No puedes apostar lo que tienes o apuestas mas o menos")
            print()
            
    elif juego == 4:
        mas = "si"
            
        print("Vale vamos a jugar a las apuestas, jugaras contra mi")
        print("Tu obtendras un numero y segun su valor apostaras contra mi que tendre otro numero apostando, solo con participar un minimo (tu dinero total / 15) sera tu apuesta minima y tu eliges si apuestas mas")
        print()
        print("En caso de empate ganas tu")
        
        usuario = input("¿Como te llamas? ")
        
        #Creamos monedero
        dinero = int(input("¿Cuanto dinero tienes? "))
        print()
        dinero_final = dinero
        
        #Creamos fichero
        fichero_apuestas = open("Ganancias apuestas.txt", "a")
            
        #Monedero Banca
        banca = 100000
        a_banca = 0
        
        apost = "si"
        
        #Creamos el bucle del juego
        while mas == "si" and apost == "si":
            
            #Creamos la variable full
            import random
            full = random.randint(1,300)
            
            #Creamos los resultados con los que apostamos
            import random
            ia = random.randint(1,10)
            
            import random
            p1 = random.randint(1,10)
            
            #Creamos variable para que la IA mienta
            import random
            m = random.randint(1,3)
            
            #La IA va con todo
            if full == 1:
                a_banca = banca
                print("Voy con {banca} es muy buen resultado el mio")
                print()
            
            #La IA no va con todo
            else:
                if ia > 8:
                    #IA decide con cuanto juega
                    import random
                    a_banca = random.randint(1000,4000)
                    if m == 1:
                        print("Meh")
                        print()
                    else:
                        print("SE VIENEN COSITAS")
                        print()
                elif ia > 5 and ia <= 8:
                    #IA decide con cuanto juega
                    import random
                    a_banca = random.randint(700,1000)
                    if m == 2:
                        print("SE VIENEN COSITAS")
                        print()
                    else:
                        print("Meh")
                        print()
                elif ia > 0 and ia <= 5:
                    #IA decide con cuanto juega
                    import random
                    a_banca = random.randint(500,700)
                    if m == 3:
                        print("SE VIENEN COSITAS")
                        print()
                    else:
                        print("Meh")
                        print()
            
            #Se muestra el resutltado del jugador y se le dan pistas de su numero
            if p1 > 7 and p1 <= 10:
                print("Tu numero esta bastante bien (8-10)")
                #Le ofrecemos apostar mas
                apost = input("¿Quieres apostar mas? ")
                apost = apost.lower()
                if apost == "si":
                    print()
                    #Le ofrecemos cuanto mas quiere apostar
                    cant = int(input("¿Cuanto quieres apostar? "))
                    print()
                else:
                    dinero = - (dinero / 15)
            elif p1 <= 7 and p1 > 4:
                print("Tu numero es pichi picha (5-7)")
                #Le ofrecemos apostar mas
                apost = input("¿Quieres apostar mas? ")
                apost = apost.lower()
                if apost == "si":
                    print()
                    #Le ofrecemos cuanto mas quiere apostar
                    cant = int(input("¿Cuanto quieres apostar? "))
                    print()
                else:
                    dinero = - (dinero / 15)
            elif p1 > 0 and p1 <= 4:
                print("Tu numero es una mierda")
                #Le ofrecemos apostar mas
                apost = input("¿Quieres apostar mas? ")
                apost = apost.lower()
                if apost == "si":
                    print()
                    #Le ofrecemos cuanto mas quiere apostar
                    cant = int(input("¿Cuanto quieres apostar? "))
                    print()
                else:
                    dinero_final = dinero_final - dinero / 15
                    banca += dinero / 15
            
            #Suceso del full
            elif full == 1:
                a_banca = banca
                print("Voy con {banca} es muy buen resultado el mio")
                print()
            
            #Hubieses ganado pero no jugaste
            elif ia <= p1 and apost != "si":
                print(f"Hubieses ganado pero no has querido apostar porque has sacado un {p1} y yo he sacado un {ia} asique te quedan {dinero_final} yo tengo {banca}")
                
            #Hubieses perdido pero no jugaste
            elif p1 < ia and apost != "si":
                print(f"Hubieses perdido asique has hecho bien en no apostar debido a que he sacado un {ia} y tu has sacado un {p1} asique te quedan {dinero_final} yo tengo {banca}")
                
            #Has ganado apostando
            elif ia <= p1 and apost == "si":
                dinero_final = dinero_final + a_banca
                banca -= a_banca
                print(f"Has ganado y encima apostando {cant}, has sacado un {p1} y yo he sacado un {ia} y he apostado {a_banca} asique has acabado con {dinero_final} me quedan {banca}")
                
            #Has perdido apostando
            elif p1 < ia and apost == "si":
                banca += (dinero / 15 + cant) + a_banca
                dinero_final = dinero_final - cant - dinero/15
                print(f"Joe has perdido y encima has apostado {cant}, he sacado un {ia} apostado {a_banca} y tu has sacado un {p1} te quedan {dinero_final} yo tengo {banca}")
        
        #Manipulamos fichero
        fichero_apuestas.write(f"{usuario} ha apostado {cant} habiendo sacado un {p1} y yo {ia}")
        #Cerramos fichero
        fichero_apuestas.close()
        
    elif juego == 5:
        bola = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        C = [1, 2, 3, 4, 5, 6, 7]
        cont = []
        acier = 0
        
        print("Bueno vamos a jugar al bingo de 15 casillas tienes 7 opciones")
        print("Las reglas son las siguientes:")
        print()
        print("Eliges 5 numeros de 15 posibles y dependiendo de los que aciertes tu apuesta se multiplicara por lo correspondiente")
        print("Solo se tiraran 6 veces la bolita")
        print("Puedes apostar las 5 veces al mismo numero y si lo aciertas te contaran todas las veces apostadas como acierto")
        print()
        print("Posibles puntuaciones:")
        print("0 aciertos apuesta perdida")
        print("1 aciertos apuesta perdida")
        print("2 aciertos apuesta perdida")
        print("3 aciertos apuesta x 1,5")
        print("4 aciertos apuesta x 2")
        print("5 aciertos apuesta x 3,5")
        
        #Creamos fichero
        fichero_bingo = open("Ganancias bingo.txt", "a")
        
        #Creamos usuario
        usuario = input("¿Como te llamas? ")
        
        #Creamos monedero
        dinero = int(input("¿Cuanto dinero tienes? "))
        apuesta = int(input("¿Cuanto apuestas? "))
        ganancias = 0
        
        #Creamos el carton
        n1 = int(input("1) Elige un numero del (1 al 17): "))
        while n1 > 17:
            n1 = int(input("1) Elige un numero del (1 al 17): "))
        n2 = int(input("2) Elige un numero del (1 al 17): "))
        while n2 > 17:
            n2 = int(input("2) Elige un numero del (1 al 17): "))
        n3 = int(input("3) Elige un numero del (1 al 17): "))
        while n3 > 17:
            n3 = int(input("3) Elige un numero del (1 al 17): "))
        n4 = int(input("4) Elige un numero del (1 al 17): ")) 
        while n4 > 17:
            n4 = int(input("4) Elige un numero del (1 al 17): "))
        n5 = int(input("5) Elige un numero del (1 al 17): "))
        while n5 > 17:
            n5 = int(input("5) Elige un numero del (1 al 17): "))
        print()
        print(f"Tus numeros elegidos son {n1} {n2} {n3} {n4} {n5}")
        print()    
        for i in C:
            #Creamos la bolita que sale
            import random
            p = len(bola)
            bolan = random.randint (1, p)
            del bola[bolan - 1]
            print()
            cont += [bolan]
            #Creamos los condicionantes
            print("Veamos donde cae esta _______________________________________________________________________")
            print()
            if n1 == bolan or n2 == bolan or n3 == bolan or n4 == bolan or n5 == bolan:
                print(f"¡WOW! Has acertado ha salido {bolan} y es uno de los tuyos LETS GOOO")
            else:
                print(f"¡Noooooo! Una pena el numero que ha salido es el {bolan} veamos el siguiente")
                print()
                print(f"Quedan estos numeros {bola}")
                
            if n1 == bolan:
                n1 = "P"
                acier += 1
            elif n2 == bolan:
                n2 = "P"
                acier += 1
            elif n3 == bolan:
                n3 = "P"
                acier += 1
            elif n4 == bolan:
                n4 = "P"
                acier += 1
            elif n5 == bolan:
                n5 = "P"
                acier += 1
                
            print()
            
        print(f"Has acabado con {acier} aciertos")
        print()
        if acier == 1 or acier == 0 or acier == 2:
            ganancias = -apuesta
            dinero = dinero - apuesta
            print(f"Has apostado {apuesta} con {acier} aciertos asique te quedan {dinero}")
            print()
            print(f"Has tenido unas ganancias de {ganancias}")
        elif acier == 3:
            ganancias = apuesta * 1.5
            dinero = dinero + ganancias - apuesta
            print(f"Has apostado {apuesta} teniendo {acier} aciertos asique te has ganado y te quedan {dinero}")
            print()
            print(f"Has tenido unas ganancias de {ganancias}")
        elif acier == 4:
            ganancias = apuesta * 2
            dinero = dinero + ganancias - apuesta
            print(f"Has apostado {apuesta} teniendo {acier} aciertos asique te has ganado y te quedan {dinero}")
            print()
            print(f"Has tenido unas ganancias de {ganancias}")
        elif acier == 5:
            ganancias = apuesta * 3.5
            dinero = dinero + ganancias - apuesta
            print(f"Has apostado {apuesta} teniendo {acier} aciertos asique te has ganado y te quedan {dinero}")
            print()
            print(f"Has tenido unas ganancias de {ganancias}")
                
        #Escribimos en el fichero
        fichero_bingo.write(f"{usuario} ha tenido unas ganancias de {ganancias} habiendo apostado {apuesta} y ha acabado con un total en su bolsillo de {dinero} HA ACERTADO {acier}"+ "\n")
        #Cerramos fichero
        fichero_bingo.close() 
        fichero_bingo.close()
        
    elif juego == 6:
        #PRESENTAMOS EL JUEGO
        print("Buenas soy la maquina tragaperras la que se traga todo lo que me eches estas son las reglas:")
        print("SOLO puedes cambiar de apuesta si has ganado")
        print("Puedes dejar de jugar por cada tirada")
        print()
        print("ESTOS SON LOS PREMIOS:")
        print("DIAMANTE = APUESTA X 40")
        print("PREMIO   = APUESTA X 19")
        print("COIN     = APUESTA X 10")
        print("UVA      = APUESTA X 5")
        print("NADA     = APUESTA PERDIDA")
        print()
        print("Hay 4 posibles premios:")
        print( "DIAMANTE--DIAMANTE--DIAMANTE")
        print("PREMIO----PREMIO-----PREMIO")
        print("COIN------COIN-------COIN")
        print("UVA-------UV-A-------UVA")
        print("KAKA------KAKA-------KAKA")
        print()
        print("Tienes que tirar y ver si caen 3 juntos")
        print()
        print("-------------------------------------------------------------------------------------------")
        print()

        #VARIABLE DE JUGAR MUCHO DE SEGUIDO
        mas = "si"


        #CREAMOS UN MONEDERO
        dinero = int(input("¿Cuanto dinero tienes? "))
        apuesta = int(input("¿Cuanto dinero apuestas? "))
        print()
        ganancias = 0
        cambio = "no"
        a = 0

        while mas == "si":

            #CREAMOS LA POSIBILIDAD DE CAMBIAR DE APUESTA
            if a != 0:
                cambio = input("¿Cambias tu apuesta? ")
                print()
                cambio = cambio.lower()
                if cambio == "si":
                    apuesta = int(input("¿Cuanto dinero apuestas? "))
                    print()

            elif ganancias < -10000:
                mas == "A"
                print("Lo sentimos pero tienes demasiadas perdidas FUERA")
                break

            #CREAMOS LO QUE SALE EN CADA UNA        
            import random
            pri = random.randint(1, 30)
            import random
            seg = random.randint(1, 30)
            import random
            ter = random.randint(1, 30)

            #DIAMANTE
            if pri == 1:
                pri = "DIAMANTE"
            elif seg == 1:
                seg = "DIAMANTE"
            elif ter == 1:
                ter = "DIAMANTE"

            #PREMIO
            if pri == 2 or pri == 3:
                pri = "PREMIO"
            elif seg == 2 or seg == 3:
                seg = "PREMIO"
            elif ter == 2 or ter == 3:
                ter = "PREMIO"

            #COIN
            if pri in range (4, 9):
                pri = "COIN"
            elif seg in range (4, 9):
                seg = "COIN"
            elif ter in range (4, 9):
                ter = "COIN"

            #UVA
            if pri in range (9, 21):
                pri = "UVA"
            elif seg in range (9, 21):
                seg = "UVA"
            elif ter in range (9, 21):
                ter = "UVA"

            #MIERDA
            if pri in range (21, 31):
                pri = "NADA"
            elif seg in range (21, 31):
                seg = "NADA"
            elif ter in range (21, 31):
                ter = "NADA"

            if not (pri == "DIAMANTE" and seg == "DIAMANTE" and ter == "DIAMANTE") or (pri == "PREMIO" and seg == "PREMIO" and ter == "PREMIO") or (pri == "COIN" and seg == "COIN" and ter == "COIN") or (pri == "UVA" and seg == "UVA" and ter == "UVA"):
                print(f"Oh vaya has fallado ha salido {pri}-{seg}-{ter}")
                dinero = dinero - apuesta
                ganancias = ganancias - apuesta
                print(f"Te quedan {dinero}")
                print(f"Llevas unas ganancias de {ganancias}")
            else:
                if pri == "DIAMANTE" and seg == "DIAMANTE" and ter == "DIAMANTE":
                    print(f"Has tenido suerte y ha salido {pri}-{seg}-{ter}")
                    dinero = dinero + apuesta * 40
                    ganancias = ganancias + apuesta * 40
                    print(f"Ojo has tenido suerte eh tu {apuesta} se ha multiplicado x 40 y tienes {dinero}")
                    print(f"Llevas unas ganancias de {ganancias}")
                    #PONEMOS COMO POSIBILIDAD EL CAMBIAR DE APUESTA
                    a += 1
                elif pri == "PREMIO" and seg == "PREMIO" and ter == "PREMIO":
                    print(f"Has tenido suerte y ha salido {pri}-{seg}-{ter}")
                    dinero = dinero + apuesta * 19
                    ganancias = ganancias + apuesta * 19
                    print(f"Ojo has tenido suerte eh tu {apuesta} se ha multiplicado x 19 y tienes {dinero}")
                    print(f"Llevas unas ganancias de {ganancias}")
                    #PONEMOS COMO POSIBILIDAD EL CAMBIAR DE APUESTA
                    a += 1
                elif pri == "COIN" and seg == "COIN" and ter == "COIN":
                    print(f"Has tenido suerte y ha salido {pri}-{seg}-{ter}")
                    dinero = dinero + apuesta * 10
                    ganancias = ganancias + apuesta * 10
                    print(f"Ojo has tenido suerte eh tu {apuesta} se ha multiplicado x 10 y tienes {dinero}")
                    print(f"Llevas unas ganancias de {ganancias}")
                    #PONEMOS COMO POSIBILIDAD EL CAMBIAR DE APUESTA
                    a += 1
                elif pri == "UVA" and seg == "UVA" and ter == "UVA":
                    print(f"Has tenido suerte y ha salido {pri}-{seg}-{ter}")
                    dinero = dinero + apuesta * 5
                    ganancias = ganancias + apuesta * 5
                    print(f"Ojo has tenido suerte eh tu {apuesta} se ha multiplicado x 5 y tienes {dinero}")
                    print(f"Llevas unas ganancias de {ganancias}")
                    #PONEMOS COMO POSIBILIDAD EL CAMBIAR DE APUESTA
                    a += 1



            #VARIABLE DE SEGUIR        
            mas = input("¿Quieres jugar mas? ")
            mas = mas.lower()

        print()
        print(f"Te vas con unas ganancias de {ganancias}") 

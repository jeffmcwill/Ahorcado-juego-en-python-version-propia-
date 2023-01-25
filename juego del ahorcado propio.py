import time
import random
import os
import numpy

#juego de ahorcado propio.
#se le agrego el sistema para que se añadan las funciones y los dibujos del muñequito.
#falta agregarle un selecctor de palabras aleatorias
#que si elige alguna de esas palabras, de ciertas pistas que varien
#pistas como "possee vocales", "tiene 6 letras" cosas asi.
#mejorar aspectos graficos.
#poner numero de intentos...
#vidas...
#finalizar partida con estadisticas
#poner menu de posibles palabras...

#JUEGO FINALIZADO Y TESTEADO.

#-----------------------------------------

puntajeGanador = []
puntajePerdedor = []
intentos = []
#-----------------------------------------

def salir():

	user = 0

	while True:

		try:

			print("--------------------------")
			print("- SALIR o SEGUIR JUGANDO -")
			print("--------------------------")
			print("-       1. SALIR         -")
			print("-       2. SEGUIR        -")
			print("-       3. MENU          -")
			print("--------------------------")

			user = int(input("> "))

			if user == 1:
				os.system("cls")
				print("salir...")
				time.sleep(1)

			#pantalla final al salir del juego.
				
				print("///////////////")
				print("// GAME OVER //")
				print("///////////////")
				print("----------------------------")
				print(f"PARTIDAS GANADAS: {sumaTotal(puntajeGanador)}.")
				print(f"PARTIDAS PERDIDAS: {sumaTotal(puntajePerdedor)}")
				print(f"TOTAL DE INTENTOS: {sumaTotal(intentos)}.")
				print("----------------------------")
				time.sleep(5)
				break

			elif user == 2:
				os.system("cls")
				print("Ok. Sigamos jugando :3")
				ahorcado()
				break

			elif user == 3:
				os.system("cls")
				print("Ok, vamos al menu...")
				main()
				break

		except:
			print("Ingrese los comandos soportados por el programa.")
			continue

def sumaTotal(lista):
	suma = 0
	for elem in lista:
		suma+=elem
	return suma

#dibujos del ahorcado.
#---------------------------

def dibujo6():

	print(".____.      ")
	print("|    |      ")
	print("|    O      ")
	print("| ---|---   ")
	print("|    |      ")
	print("|   | |     ")
	print("|   | |     ")
	print("|           ")
	print("-------")
	print("----------")
	print("------------")

def dibujo5():
	
	print(".____.      ")
	print("|    |      ")
	print("|    O      ")
	print("| ---|---   ")
	print("|    |      ")
	print("|   |       ")
	print("|   |       ")
	print("|           ")
	print("-------")
	print("----------")
	print("------------")


def dibujo4():
	
	print(".____.      ")
	print("|    |      ")
	print("|    O      ")
	print("| ---|---   ")
	print("|    |      ")
	print("|          ")
	print("|          ")
	print("|           ")
	print("-------")
	print("----------")
	print("------------")

def dibujo3():
	
	print(".____.      ")
	print("|    |      ")
	print("|    O      ")
	print("|    |      ")
	print("|    |      ")
	print("|           ")
	print("|           ")
	print("|           ")
	print("-------")
	print("----------")
	print("------------")

def dibujo2():
	
	print(".____.  ")
	print("|    |  ")
	print("|    o  ")
	print("|       ")
	print("|       ")
	print("|       ")
	print("|       ")
	print("|       ")
	print("-------")
	print("----------")
	print("------------")


def dibujo1():

	print(".____. ")
	print("|    | ")
	print("|      ")
	print("|      ")
	print("|      ")
	print("|      ")
	print("|      ")
	print("|      ")
	print("-------")
	print("----------")
	print("------------")

#sistema de juego principal. (aqui se ejecuta todo el juego completo :3)

"""
#-----------------------------------------
#sistema de seleccion de palabras para el ahorcado.

sopadepalabras = ["ajo","maiz","banana","tarta","zapallo","pileta"]

palabraRandom = numpy.random.choice(sopadepalabras)

palabra = []

palabra.append(palabraRandom)
"""
#-----------------------------------------
#tengo que hacer un sistema que compruebe si la palabra que ingresa el jugador es la seleccionada
#caso contrario dira no, y cpmtiuara el juego
#poner una lista y comprobar que esa palabra ensta en esa lista
#la paabra que ingresa el jugador, si esta en la lista, gana.
#SISTEMA HECHO :3

#crear un sistema de puntuaciones.
#hecho igual corregirlo.

def ahorcado():

	#-----------------------------------------
	#sistema de seleccion de palabras para el ahorcado.

	sopadepalabras = ["ajo","maiz","banana","tarta","zapallo","pileta"]

	palabraRandom = numpy.random.choice(sopadepalabras)

	palabra = []

	palabra.append(palabraRandom)

	#-----------------------------------------

	equivocarse = [0]

	print("Ok... la palabra que pienso...")

	#tablero inicial... (se añade primero ya que sera la primera vez que se deja)

	dibujo1()

	while True:

		try:

			#muestra la palabra que es la respuesta (sacado por obvias razones.)
			
			#print(palabra)
			
			print("¿Que palabra sera?")
			print("--------------------")
			palabreria = input("> ")

			#------------------------

			#algoritmo que busca la palabra ingresada por el usuario.
			
			comprobar = palabra.index(palabreria)
			
			#------------------------

			if comprobar == 0:

				punto1 = 1
				puntajeGanador.append(punto1)

				print("////////////////////")
				print("// ¡¡Has ganado!! //")
				print("////////////////////")
				print("---------------------------")
				print(f"LA PALABRA ERA {palabra}.")
				print(f"PARTIDAS GANADAS: {sumaTotal(puntajeGanador)}.")
				print(f"PARTIDAS PERDIDAS: {sumaTotal(puntajePerdedor)}")
				print(f"TOTAL DE INTENTOS: {sumaTotal(intentos)}.")
				print("---------------------------")
				
				time.sleep(3)
				os.system("cls")
				salir()
				break
				

#se agrega value error ya que el string es buscado como numero, al no encontrarse lanza ese
#error...
		
		except ValueError:

			if sumaTotal(equivocarse) == 0:
					
				os.system("cls")
				print("¡¡Incorrecto!!")

				dibujo2()
					
				puntoerror = 1
				intentos.append(puntoerror)
				equivocarse.append(puntoerror)

				continue

			elif sumaTotal(equivocarse) == 1:

				os.system("cls")
				print("¡¡Incorrecto!!")
					
				dibujo3()
					
				puntoerror = 1
				intentos.append(puntoerror)
				equivocarse.append(puntoerror)

				continue

			elif sumaTotal(equivocarse) == 2:

				os.system("cls")
				print("¡¡Incorrecto!!")
					
				dibujo4()
					
				puntoerror = 1
				intentos.append(puntoerror)
				equivocarse.append(puntoerror)

				continue

			elif sumaTotal(equivocarse) == 3:

				os.system("cls")
				print("¡¡Incorrecto!!")
					
				dibujo5()
					
				puntoerror = 1
				intentos.append(puntoerror)
				equivocarse.append(puntoerror)

				continue

			elif sumaTotal(equivocarse) == 4:

				os.system("cls")
				print("¡¡Incorrecto!!")

				print("¡¡TIENES SOLO UNA OPORTUNIDAD MAS!!")
					
				dibujo6()
					
				puntoerror = 1
				intentos.append(puntoerror)
				equivocarse.append(puntoerror)

				continue

			elif sumaTotal(equivocarse) == 5:

				print("¡¡Incorrecto!!")

				punto1 = 1
				intentos.append(puntoerror)
				puntajePerdedor.append(punto1)

				print("////////////")
				print("/ PIERDES. /")
				print("////////////")
				print("---------------------------")
				print(f"LA PALABRA ERA {palabra}.")
				print(f"PARTIDAS GANADAS: {sumaTotal(puntajeGanador)}.")
				print(f"PARTIDAS PERDIDAS: {sumaTotal(puntajePerdedor)}")
				print(f"TOTAL DE INTENTOS: {sumaTotal(intentos)}.")
				print("---------------------------")

				time.sleep(3)
				os.system("cls")
				salir()
				break

#-------------------------------------------------

def posibles():

	user2 = 0

	while True:

		try:
			print("------------------------------------------------")
			print("Posibles palabras:")
			print("------------------------------------------------")
			print("ajo","maiz","banana","tarta","zapallo","pileta")
			print("------------------------------------------------")

			print("(1 para cerrar.)")

			user2 = int(input("> "))

			if user2 == 1:
				os.system("cls")
				print("OK, volviendo al menu...")
				main()
				break

			elif user2 != 1:
				print("Error. Numero incorrecto solo agregue 1 para salir.")
				continue

		except:
			print("Error. comandos ingresados no soportados por el programa.")
			continue

#-------------------------------------------------

def main():

	user = 0

	while True:

		try:

			print("--------------------")
			print("- JUEGO DEL ORCADO -")
			print(".____.             -")
			print("|    |             -")
			print("|    O             -")
			print("| ---|---          -")
			print("|    |             -")
			print("|   | |            -")
			print("|   | |            -")
			print("|                  -")
			print("--------------------")
			print("-    1. Jugar      -")
			print("-    2. Palabras   -")
			print("-    3. Salir      -")
			print("--------------------")

			user = int(input("> "))

			if user == 1:	
				os.system("cls")
				print("Ok empezemos el juego...")
				time.sleep(2)
				ahorcado()
				break

			elif user == 2:
				os.system("cls")
				print("Ok, te mostrare la lista de las posibles palabras...")
				time.sleep(2)
				posibles()
				break

			elif user == 3:
				os.system("cls")
				print("Saliendo del juego...")
				time.sleep(1)

				print("///////////////")
				print("// GAME OVER //")
				print("///////////////")
				print("----------------------------")
				print(f"PARTIDAS GANADAS: {sumaTotal(puntajeGanador)}.")
				print(f"PARTIDAS PERDIDAS: {sumaTotal(puntajePerdedor)}")
				print(f"TOTAL DE INTENTOS: {sumaTotal(intentos)}.")
				print("----------------------------")
				
				time.sleep(5)
				break
				break

			else:
				print("ERROR: Numero ingresado no correcto. agregue los soportados por el programa.")
				continue

		except:
			print("ERROR: caracteres erroneos, agregue solo numeros soportados por el programa.")
			continue

#--------------
#ahorcado()
main()
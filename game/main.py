import random


def elegir_opciones():
  opciones = ("piedra","papel","tijera")
  user_option = input("piedra, papel o tijera : ")
  user_option = user_option.lower()
  # usamos la funcion random para elegir aleatoriamente la     opcion de la computadora con random.choice

  computer_option = random.choice(opciones)

  # para verificar si la opcion del usuario es valida realizamos un if

  if user_option not in opciones:
    print("opcion incorrecta >:c")
    return None,None
    #continue          # evita que se ejecute todo el codigo de           abajo y vuelve a iniciar el ciclo en este refactor no es necesario
  print("*"*15)
  print("opcion del usuario : ",user_option)
  print("opcion de la computadora : ",computer_option)
  return user_option, computer_option

def reglas(user_option, computer_option,ganadas_usuario,ganadas_pc):
  if user_option == computer_option:
    print("EMPATE")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("piedra gana a tijera")
      print("user gano!!")
      ganadas_usuario += 1
    else:
      print("papel gana a piedra")
      print("computer gano !!")
      ganadas_pc +=1

  elif user_option == "papel":
    if computer_option == "piedra":
      print("papel gana a piedra")
      print("usuario gana !!")
      ganadas_usuario +=1
    else:
      print("tijera gana a papel")
      print("computer gana !!")
      ganadas_pc +=1

  elif user_option == "tijera":
    if computer_option == "papel":
      print("tijera gana a papel")
      print("usuario gana !!")
      ganadas_usuario += 1
    else:
      print("piedra gana a tijera")
      print("computer gana !!!")
      ganadas_pc += 1

  else:
    print("no has digitado ninguna de las opciones")

  return ganadas_usuario, ganadas_pc
  
def definir_ganador(ganadas_usuario,ganadas_pc):
  if ganadas_usuario == 2:
    print("usuario ha ganado la partida!!!!!")
    exit()

  if ganadas_pc == 2:
    print("computador ha ganado la partida!!!!!")
    exit()

def correr_juego():
  rondas = 1
  ganadas_usuario = 0
  ganadas_pc = 0
  while True:

    print("*"*15)
    print("ROUND :", rondas)
    print("*"*15)

    print("puntos del usuario :",ganadas_usuario)
    print("puntos de pc :",ganadas_pc)
    rondas += 1
    # leemos los dos valores que nos retorna la funcion elegir_opciones
    user_option, computer_option = elegir_opciones()
    ganadas_usuario,ganadas_pc= reglas(user_option,                  
    computer_option,ganadas_usuario,ganadas_pc) 
    definir_ganador(ganadas_usuario,ganadas_pc)
    
      


  
correr_juego()
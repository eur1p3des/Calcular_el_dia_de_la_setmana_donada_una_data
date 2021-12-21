#Impotem la biblioteca math, que ens servirà per a obtindre la part entera de la divisió
import math

#Demanem que s'introdueixi la data.
dia = input('Si us plau entra el dia del mes que t\'interesa buscar: ')
mes = input('A continuació entra el mes (en valor numèric) que t\'interesa buscar: ')
any = input('Finalment, introdueix l\'any del que vols calcular el dia de la setmana: ')

#Declarem els dies que té cada mes en un array
dies_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
#Calculem el dia del mes en modul 7.
mes_mod = [0]
for i in range(11):
  dia_mod = (dies_mes[i]+mes_mod[i])%7
  mes_mod.append(dia_mod)
  
#Declarem el text dels díes
textdies = ["Diumenge", "Dilluns", "Dimarts", "Dimecres", "Dijous", "Dissabte"]

#Creem diverses funcions per a fer els càlculs
#Funció que busca quants anys han passat desde 1900
def anys_passats(any):
  return int(any-1900)
#Funció que busca quants anys de traspàs hi han hagut
def anys_de_taspas(any):
  #Amb l'opció math.trunc, eliminem els decimals de la divisió.
  return int(math.trunc((anys_passats(any)-1)/4))
#Funció per a trobar en quin dia de la setmana va començar el nostre any.
def inici_any(any):
  return int((anys_passats(any) + anys_de_taspas(any) + 1)%7)
#Funció que retorna el dia corresponent al mes:
def diames(mes):
  return int(mes_mod[mes-1])
#Funció que retorna 1 si és any de traspàs i 0 si no ho és.
def any_de_traspas(mes,any):
  #Comprovem que l'any sigui divisible per 4,100 i 400. En cas que ho sigui per a tots, mirarà si el mes es superior a febrer, en cas que es compleixin totes les condicions, es retornarà cert (és a dir, es un any de traspàs), en cas contrari retornarà fals.
  if (any%4) == 0:
    if(any%100) == 0:
      if(any%400) == 0:
        if (mes > 2 and mes <= 12):
          return True
    else:
      return False
  else:
   return False       
#Calculem el dia de la setmana en valor
def valor_dia_setmana(dia,mes,any):
  #Si la funció que mira si és un any de traspàs ens diu que ho és, realitzem l'operació sumant un 1 al final (abans de calcular el modul 7), en cas contrari, no li sumem cap valor més i realitzem el modul.
  if (any_de_traspas(mes, any)):
    valor = (anys_passats(any) + anys_de_taspas(any) + diames(mes) + dia + 1) % 7
  else:
    valor = (anys_passats(any) + anys_de_taspas(any) + diames(mes) + dia + 0) % 7
  return valor   

#Mostrem a quin dia de la setmana correspon la data introduida per l'usuari.
print()
print("El dia de la setmana corresponent a la data", dia,"/",mes,"/",any," és: ",textdies[valor_dia_setmana(int(dia),int(mes),int(any))])
print()
print()
input("Premeu la tecla \'Enter\' per a sortir del programa")
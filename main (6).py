import random

horca = \
    '''  
        |****
        |   *
        ¿   *  
  0123456   *
*************
'''
simbolos = '0123456'


def hola():
  print(
    'Bienvenido al ahorcado de jugadores de futbol (todos actualmente en activo y de los más reconocidos actualmente) :) '
  )


def inicio(lista):
  palabra = random.choice(lista).lower()
  tablero = ['_'] * len(palabra)
  return tablero, palabra, []


def escenario0(error):
  escena = horca
  for i in range(0, len(simbolos)):
    simbolo = simbolos[i] if i < error else ' '
    escena = escena.replace(str(i), simbolo)
  print(escena)


def tablero0(tablero, errores):
  for espacio in tablero:
    print(espacio, end=' ')
  print()
  print()
  if len(errores) > 0:
    print('Letras falladas:', *errores)
    print()


def pedir(tablero, errores):
  correct = False
  while not correct:
    letra = input('Inserta una letra (a-z): ').lower()
    correct = 'a' <= letra <= 'z' and len(letra) == 1
    if not correct:
      print('Carácter incorrecto')
    else:
      correct = letra not in tablero + errores
      if not correct:
        print('Letra repetida')
  return letra


def corregir(letra, palabra, tablero, errores):
  if letra in palabra:
    print('Letra correcta :) ')
    tablero1(letra, palabra, tablero)
  else:
    print('Letra incorrecta :/ ')
    errores.append(letra)


def tablero1(letra, palabra, tablero):
  for indice, letra_palabra in enumerate(palabra):
    if letra == letra_palabra:
      tablero[indice] = letra


def espacios0(tablero):
  return '_' not in tablero


def jugar(lista):

  tablero, palabra, errores = inicio(lista)
  while len(errores) < len(simbolos):
    escenario0(len(errores))
    tablero0(tablero, errores)
    letra = pedir(tablero, errores)
    corregir(letra, palabra, tablero, errores)
    if espacios0(tablero):
      print('Has acertado la palabra :)')
      break
  else:
    print(f'No has certado la palabra :( , la palabra era {palabra}.')
    escenario0(len(errores))

  tablero0(tablero, errores)


def otra():
  return input('¿Quieres probar de nuevo? (s = sí ; otro carácter = no): ')


def despedida():
  print('Muchas gracias :) ')


if __name__ == '__main__':

  lista = [
    'messi', 'mbappe', 'cristiano', 'haaland', 'modric', 'benzema', 'neymar',
    'salah', 'lewandowski', 'neuer', 'maguire', 'hakimi', 'ramos', 'busquets',
    'griezmann', 'joselu', 'donnaruma', 'vinicius', 'pedri', 'gavi', 'morata',
    'koulibaly', 'miltao', 'courtois', 'muller', 'kimmich', 'casemiro', 'pogba','muriqi'
  ]

  hola()
  while True:
    jugar(lista)
    if otra() != 's': break
  despedida()
"""
#Pistas (no podido integrar en el código ya acabado)
lista = [
'messi':'Delantero sudamericano', 
'mbappe':'Delantero europeo', 
'cristiano':'Delantero europeo', 
'haaland':'Delantero europeo', 
'modric':'Mediocampisa europeo', 
'benzema':'Delantero europeo', 
'neymar':'Delantero sudamericano', 
'salah':'Delantero africano', 
'lewandowski':'Delantero europeo', 
'neuer':'Portero europeo', 
'maguire':'Defensa europeo', 
'hakimi':'Defensa africano', 
'ramos':'Defensa europeo', 
'busquets':'Mediocampisa europeo', 
'griezmann':'Delantero europeo', 
'joselu':'Delantero europeo', 
'donnaruma':'Portero europeo', 
'vinicius':'Delantero sudamericano', 
'pedri':'Mediocampisa europeo', 
'gavi':'Mediocampisa europeo', 
'morata':'Delantero europeo', 
'koulibaly':'Defensa africano', 
'miltao':'Defensa sudamericano', 
'courtois':'Portero europeo', 
'muller':'Mediocampisa europeo', 
'kimmich':'Mediocampisa europeo', 
'casemiro':'Mediocampisa sudamericano', 
'pogba':'Mediocampisa europeo',
'muriqi':'Delantero europeo']
"""

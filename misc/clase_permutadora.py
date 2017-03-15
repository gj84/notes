import codecs

class Permutador:
  def __init__(self):
    self.lista = []
    self.index = 0
    self.anagramas = []
    
  def permutar(self,lista_an,longitud=None,anag_an=[]): #same itertools.permutation, but it's recursive
    if longitud == None:
      longitud = len(lista_an)
      self.lista = []
    for k in range(0,len(lista_an)):
      anag_new = anag_an + [lista_an[k]]
      lista_new = lista_an[:]
      lista_new.pop(k)
      if len(anag_new) == longitud:
        self.lista.append(anag_new)
      self.permutar(lista_new,longitud,anag_new)

  def avanzar(self):
    if self.index < len(self.lista)-1:
      self.index += 1
      return self.lista[self.index]
    else: return None

  def retroceder(self):
    if self.index > 0:
      self.index -= 1
      return self.lista[self.index]
    else: return None    

  def actual(self):
    return self.lista[self.index]

  def mostrar_lista(self):
    for elemento in self.lista:
      print elemento

  def buscar_anagramas(self,diccionariopath,codificacion='utf_8'):
    diccionario = codecs.open(diccionariopath,'r',codificacion)
    for palabra in diccionario:
      if palabra[0] in self.lista[0]:
        for elemento in self.lista:        
          if ''.join(elemento) == palabra[:-1]:
            if palabra[:-1] not in self.anagramas:
              self.anagramas.append(palabra[:-1])
    diccionario.close()

#Ejemplo
#path = 'vocabulario.txt'
#permut = Permutador()
#permut.permutar(list('mora'))
#permut.buscar_anagramas(path,'utf_8')    
#for anagrama in permut.anagramas:
#  print anagrama

#>>> 
#amor
#mora
#omar
#ramo
#roma

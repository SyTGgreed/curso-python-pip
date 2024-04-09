import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    lector = csv.reader(csvfile, delimiter=',')
    header = next(lector) # lee la primera linea del archivo, asi obtenemos las llaves keys
    data = []  # ---> lista vacia
    #print(header)
    for fila in lector:
      # creamos una variable iterable para unir por medio de zip las llaves y los valores
      iterable = zip(header, fila)
      #print(list(iterable))

      # utilizamos dictionary commprehension para crear un diccionario con los valores
      pais_dict = {key: value for key, value in iterable}
      #print(pais_dict)
      data.append(pais_dict) # ---> agregamos el diccionario a la lista data
      
    #print(data)
    return data

# para ejecutar el archivo como un script desde la terminal

if __name__== '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])  # ---> imprime el primer elemento de la lista data
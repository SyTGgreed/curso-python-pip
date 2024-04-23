import pandas as pd
def obtener_poblacion(country_dict):
  poblacion_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
    
  #keys = ['col', 'bol']
  #Values = [300, 400]

  # devolvemos un array de las claves y otro de valores para poder graficar

  labels = poblacion_dict.keys()
  values = poblacion_dict.values()
   
  return labels, values

def poblacion_por_pais(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

def datos_poblacion_mundial(data,continente):
  
  data = list(filter(lambda item: item['Continent'] == continente, data))
  #data = data[data['Continent']==continente]   #----> utilizando la hoja de datos con pandas
  paises = list(map(lambda x: x['Country/Territory'], data))
  #paises = data['Country'].values   # -----------> utilizando hoja de datos con pandas
  porcentaje = list(map(lambda x: x['World Population Percentage'], data))
  #porcentaje = data['World Population Percentage'].values #----> aqui igual
  
  pais_porcentaje = list(zip(paises, porcentaje))
  #print(pais_porcentaje)
  diccionario = {key : value for key, value in pais_porcentaje}
  print(diccionario)
  print('*'*10)
  print(len(diccionario))
  keys = diccionario.keys()
  values = diccionario.values()
  return keys,values
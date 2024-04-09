import csv
import utilidades
import charts
import read_CSV


def leer_csv(path):
  data = read_CSV.read_csv('./app/data.csv')
  country = input('Type Country => ')
  result = utilidades.poblacion_por_pais(data, country)

  # si el resultado encuentra algo lo toma como mayor a cero
  if len(result) > 0:
    country = result[0]
    labels, values = utilidades.obtener_poblacion(country)
    charts.generar_bar_chart(labels,values)
    
  return data


  
  

if __name__ =="__main__":
  data = leer_csv('./app/data.csv')
  print(data)
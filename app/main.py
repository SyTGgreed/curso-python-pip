import utilidades
import read_CSV
import charts
import pandas as pd



def run():
  
  data = read_CSV.read_csv('data.csv')
  #data = pd.read_csv('data.csv')     # -----> leer hoja de datos con pandas
  print(data)
  continente = input('digita el continente: ')
  country = input('digita el pais : ')
  print(data['Country/Territory'==country])
  resultado = utilidades.poblacion_por_pais(data, country)
  print(resultado)
  



  if len(resultado) > 0:
    country = resultado[0]
    labels, values = utilidades.obtener_poblacion(country)
    charts.generar_bar_chart(country['Country/Territory'],labels, values)
  #utilidades.datos_poblacion_mundial(data)

  labels, values = utilidades.datos_poblacion_mundial(data,continente)
  charts.generar_pie_chart(labels, values)


# para manejar la dualidad  se utiliza if __name__ == '__main__':
if __name__ == '__main__':
  run()
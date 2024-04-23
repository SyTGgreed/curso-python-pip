import matplotlib.pyplot as plt
# se puede poner un alias para no tener que escribir toda la libreria

def generar_bar_chart(name,labels,values):
  figura,coordenadas = plt.subplots()

  coordenadas.bar(labels,values)
  plt.savefig(f'./imagenes/{name}.png')
  plt.close()

def generar_pie_chart(labels,values): # grafica de torta
  figura,coordenadas = plt.subplots()
  coordenadas.pie(values,labels=labels)
  coordenadas.axis('equal')
  plt.savefig('charts_pie_final.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a','b','c']
  values = [100,200,80]
  #generar_bar_chart(labels,values)
  generar_pie_chart(labels,values)
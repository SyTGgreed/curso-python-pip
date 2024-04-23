import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()        # creamos una instancia

@app.get('/')      # creacion de ruta
def get_list():
    return [1,2,3]

@app.get('/contact',response_class=HTMLResponse)      # creacion de ruta
def get_list():
    return """
        <h1> hola soy una pagina</h1>
        <p> soy un parrafo </p>
    """



def run():
    store.get_categories()

if __name__== '__main__':
    run()


#importacion de todo lo necesario
from flask import Flask, render_template

app= Flask(__name__)

#creamos la ruta al archivo html para que se visualice en el navegador
@app.route('/')
def pagina_inicio():
    return render_template('inicio.html')#render_template hay que importarlo

@app.route('/login')
def login():
    return render_template('login.html')#render_template hay que importarlo

@app.route('/formulario_registro')
def formulario_registro():
    return render_template('formulario_registro.html')#render_template hay que importarlo

@app.route('/productos')
def productos():
    return render_template('productos-inicio.html')#render_template hay que importarlo


#ejecutamos el servidor para que se actualice automaticamente
if __name__ == '__main__':
    app.run(debug=True, port=4555)
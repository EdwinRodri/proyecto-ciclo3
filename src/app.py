#importacion de todo lo necesario
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

#creamos al app
app= Flask(__name__)
app.secret_key = 'Hola_mundo'
#creamos la conexion Base de Datos
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='bd_proyecto'
db = MySQL(app)


app.secret_key = "super secret key"
#creamos la ruta al archivo html para que se visualice en el navegador
@app.route('/')
def pagina_inicio():
    return render_template('inicio.html')#render_template hay que importarlo

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/formulario_registro')
def formulario_registro():
    return render_template('formulario_registro.html')


@app.route('/productos')
def productos():
    return render_template('productos-inicio.html')


#metodos [POST, GET, UPDATE, DELETE] Base de Datos
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST': #validamos que sea el metodo POST
        nombre = request.form['nombre']#accedemos a los datos del formulario por la funcion request.form
        apellido = request.form['apellido']#lo que va entre corchetes es el name que esta en el input   del formulario
        correo = request.form['correo']
        celular = request.form['celular']
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']     
        #generamos el curso paso fundamental, "db" es como guardamos la conexion de la base de datos arriba
        cursor = db.connection.cursor()
        #creamos la sentencia SQL
        cursor.execute('INSERT INTO registro (nombre, apellido, celular, email, usuario, contraseña) VALUES (%s,%s, %s, %s, %s, %s)', (nombre, apellido, celular, correo, usuario, contraseña))
        #ejecutamos la sentencia con la conexion a la base de datos
        db.connection.commit()
        return redirect(url_for('formulario_registro')) #dentro de los parentecis url_for, va la funcion
                                                        #de la ruta que queremos redirecionarno

#metodo validar datos de iniciar sesion
@app.route('/inicio', methods=['GET', 'POST'])                                                     
def iniciar_sesion():
    if request.method == 'POST':
        usuario = request.form['username']
        contraseña = request.form['password']
        # print(usuario)
        # print(contraseña)
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM registro WHERE usuario=%s AND contraseña=%s',(usuario, contraseña))
        cuenta = cursor.fetchone()
        
        if cuenta:
            session['loggedin'] = True
            session['username'] = cuenta[5]
            return redirect(url_for('productos'))
        else:
            return 'Algo salio mal'
    
    return redirect(url_for('login'))
#ejecutamos el servidor para que se actualice automaticamente
if __name__ == '__main__':
    app.run(debug=True, port=4555)
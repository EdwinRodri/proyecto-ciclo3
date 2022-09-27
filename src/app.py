#importacion de todo lo necesario
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import random

#creamos al app
app= Flask(__name__)
#comoponente necesario para hacer el Login convertir la password en una secret_key
app.secret_key = 'Hola_mundo'

#creamos la conexion Base de Datos
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='bd_proyecto'
db = MySQL(app)


app.secret_key = "super secret key"


#rutas Principales

#creamos la ruta al archivo html para que se visualice en el navegador
@app.route('/')
def pagina_inicio():
    return render_template('inicio.html')#render_template hay que importarlo

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return render_template('login.html')

@app.route('/crudAdmin')
def crudAmin():
    return render_template('crudAdminInformacion.html')

@app.route('/formulario_registro')
def formulario_registro():
    return render_template('formulario_registro.html')


@app.route('/productos')
def productos():
    return render_template('productos-inicio.html')

@app.route('/food')
def food():
    return render_template('crudFood.html')

@app.route('/administrarFood')
def administrarfood():
    #traemos los datos de la base de datos para mostrarlos cuando se vea esta pagina
    cursor = db.connection.cursor()
    cursor.execute('SELECT * FROM food')
    data = cursor.fetchall()#esta funcion guarda los datos selecionados de la tabla de la BD
    #print(data)
    #pasamos esos datos como parametros para que el html de esta pagina los renderice por medio de un Bucle for
    return render_template('administrarFood.html', datos= data)




#rutas para la pagina Login y Registro

#metodos [POST, GET, UPDATE, DELETE] Base de Datos
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST': #validamos que sea el metodo POST
        nombre = request.form['nombre']#accedemos a los datos del formulario por la funcion request.form
        apellido = request.form['apellido']#lo que va entre corchetes es el name que esta en el input   del formulario
        correo = request.form['correo']
        celular = request.form['celular']
        # usuario = request.form['usuario']
        contraseña = request.form['contraseña']
             
        #creamos un usuario aleatorio, para que el sistema me entregue un user aleatorio
        user = nombre+apellido
        userFinal= user+str(random.randrange(100))
         
        #generamos el curso paso fundamental, "db" es como guardamos la conexion de la base de datos arriba
        cursor = db.connection.cursor()
        #creamos la sentencia SQL
        cursor.execute('INSERT INTO registro (nombre, apellido, celular, email, usuario, contraseña) VALUES (%s,%s, %s, %s, %s, %s)', (nombre, apellido, celular, correo, userFinal, contraseña))
        #ejecutamos la sentencia con la conexion a la base de datos
        db.connection.commit()
        flash('Contacto agregado con exito, su usuario es: ' + userFinal)
        return redirect(url_for('formulario_registro')) #dentro de los parentecis url_for, va la funcion
                                                           #de la ruta que queremos redirecionarno
        

#metodo validar datos de iniciar sesion
@app.route('/inicio', methods=['GET', 'POST'])                                                     
def iniciar_sesion():
    if request.method == 'POST':#validamos que sea el metodo Post
        usuario = request.form['username'] #recuperamos los valosresde los inputs del respectivo template y los guardamos en una variable
        contraseña = request.form['password']
        # print(usuario)
        # print(contraseña)

        if usuario != 'admin01':
            cursor = db.connection.cursor()#creamos el cursor para manejar la conexion a la base de datos y lo guardamos en una barible para que se mas comodo
            cursor.execute('SELECT * FROM registro WHERE usuario=%s AND contraseña=%s',(usuario, contraseña))#ejecutamos la sentencia SQL con el cursor
            cuenta = cursor.fetchone()#y guardamos los datos que me trae la ejecucion de la sentencia            
            if cuenta:
                session['loggedin'] = True
                session['username'] = cuenta[5] 
                return redirect(url_for('productos'))
            else:
                usuario=''
                contraseña=''
                flash('El usuario no esta registrado, porfavor crea una cuenta')
                return redirect(url_for('login'))
        
        else:
            cursor = db.connection.cursor()#creamos el cursor para manejar la conexion a la base de datos y lo guardamos en una barible para que se mas comodo
            cursor.execute('SELECT * FROM registro WHERE usuario=%s AND contraseña=%s',('admin01', contraseña))#ejecutamos la sentencia SQL con el cursor
            cuenta = cursor.fetchone()#y guardamos los datos que me trae la ejecucion de la sentencia
            if cuenta:
                session['loggedin'] = True
                session['username'] = cuenta[5] 
                return redirect(url_for('crudAmin'))
            else:
                usuario=''
                contraseña=''
                flash('El usuario no esta registrado, porfavor crea una cuenta')
                return redirect(url_for('login'))
            
    
    return redirect(url_for('login'))




#Rutas para administrarFood

#Ruta Agregar nuevo Food
@app.route('/addFood', methods=['POST'])
def addFood():
    if request.method == 'POST': #validamos que sea el metodo POST
        nombre = request.form['Nombre']#accedemos a los datos del formulario por la funcion request.form
        descripcion = request.form['Descripcion']
        precio = request.form['Precio']
        # print(nombre)
        # print(descripcion)
        # print(precio)
         
        #generamos el curso paso fundamental, "db" es como guardamos la conexion de la base de datos arriba
        cursor = db.connection.cursor()
        #creamos la sentencia SQL
        cursor.execute('INSERT INTO food (Nombre, Descripcion, Precio) VALUES (%s,%s, %s)', (nombre, descripcion, precio))
        #ejecutamos la sentencia con la conexion a la base de datos
        db.connection.commit()
        flash('la comida se agrego con exido')
        return redirect(url_for('administrarfood')) #dentro de los parentecis url_for, va la funcion

#Ruta eliminar un Food
@app.route('/delete/<string:id>')
def deleteFood(id):
    cursor = db.connection.cursor()
    cursor.execute('Delete FROM food WHERE id = %s',[id])
    db.connection.commit()
    flash('El producto ha sido Removido con Exito')
    return redirect(url_for('administrarfood'))

#Ruta Editar un Food
#esta ruta me recolecta los datos que se van actualizar y me los pega en los campos
@app.route('/edit/<string:id>')
def editFood(id):
    #creamos el cursor para ejecutar loa sentencia SQL
    cursor = db.connection.cursor()
    #creamos la Sentencia
    cursor.execute('SELECT * FROM food WHERE id = %s',[id])
    #recolectamos los datos de esa senyencia con el cursor y la funcion .fetchall()
    data = cursor.fetchall()
    #print(data[0])
    #despues de terminar renderizamos la pagina
    return render_template('editFood.html', datos = data[0])
#esta sigue siendo la ruta /edit, pero esta parte permite editar los elemntos traidos con anterioridad
@app.route('/update/<string:id>', methods=['POST'])
def updateFood(id):
    if request.method == 'POST':
        #recolectamos los datos del formulario
        nombre = request.form['Nombre']#accedemos a los datos del formulario por la funcion request.form
        descripcion = request.form['Descripcion']
        precio = request.form['Precio']
        # print(nombre)
        #creamos el cursor 
        cursor = db.connection.cursor()
        #creamos la sentencia SQL con el cursor
        cursor.execute("""
                    UPDATE food 
                    SET Nombre = %s,
                            Descripcion = %s,
                            Precio = %s
                        WHERE id = %s
                    """, (nombre, descripcion, precio, id))
        #ejecutamos esa sentencia SQL
        db.connection.commit()
        #mostramos un mensaje por pantalla
        flash('Producto Actualizado con Exito')
        #renderizamos la pagina requerida
        return redirect(url_for('administrarfood'))
        
        
    
    
    
    
    

#ejecutamos el servidor para que se actualice automaticamente
if __name__ == '__main__':
    app.run(debug=True, port=4555)
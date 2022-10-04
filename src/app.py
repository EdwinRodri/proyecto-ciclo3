#importacion de todo lo necesario
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
from flask_mysqldb import MySQL
from datetime import datetime
import random
import os

#creamos al app
app= Flask(__name__)
#comoponente necesario para hacer el Login convertir la password en una secret_key
app.secret_key = 'Hola_mundo'

#creamos la conexion Base de Datos
app.config['MYSQL_HOST']='sql10.freemysqlhosting.net'
app.config['MYSQL_USER']='sql10524054'
app.config['MYSQL_PASSWORD']='zU3wssZTbT'
app.config['MYSQL_DB']='sql10524054'
db = MySQL(app)


app.secret_key = "super secret key"


CARPETA = os.path.join('uploads')
app.config['CARPETA']=CARPETA

#ruta para las fotos que se puedan mostrar en los CRUDS
@app.route('/uploads/<nuevoNombreFoto>')
def uploads(nuevoNombreFoto):
    #send_from_directory es el modulo de flask que se importo paera que se pueda mostrar las imagenes
    return send_from_directory(app.config['CARPETA'], nuevoNombreFoto)
    

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

@app.route('/formulario_registro')
def formulario_registro():
    return render_template('formulario_registro.html')






#Rutas del Administrador user admin01
@app.route('/crudAdmin')
def crudAmin():
    return render_template('crudAdminInformacion.html')

@app.route('/administrarFood')
def administrarfood():
    #traemos los datos de la base de datos para mostrarlos cuando se vea esta pagina
    cursor = db.connection.cursor()
    cursor.execute('SELECT * FROM food')
    data = cursor.fetchall()#esta funcion guarda los datos selecionados de la tabla de la BD
    #print(data)
    #pasamos esos datos como parametros para que el html de esta pagina los renderice por medio de un Bucle for
    return render_template('administrarFood.html', datos= data)

@app.route('/administrarEvents')
def administrarEvents():
    #traemos los datos de la base de datos para mostrarlos cuando se vea esta pagina
    cursor = db.connection.cursor()
    cursor.execute('SELECT * FROM eventos')
    data = cursor.fetchall()#esta funcion guarda los datos selecionados de la tabla de la BD
    #print(data)
    #pasamos esos datos como parametros para que el html de esta pagina los renderice por medio de un Bucle for
    return render_template('administrarEvents.html', datos= data)

@app.route('/administrarClientes')
def administrarClientes():
    #traemos los datos de la base de datos para mostrarlos cuando se vea esta pagina
    cursor = db.connection.cursor()
    cursor.execute('SELECT * FROM registro')
    data = cursor.fetchall()#esta funcion guarda los datos selecionados de la tabla de la BD
    #print(data)
    #pasamos esos datos como parametros para que el html de esta pagina los renderice por medio de un Bucle for
    return render_template('viewsAdministrar/administrarClientes.html', datos= data)




#rutas del cliente user diferente a admin01

#esta ruta sale despuesde iniciar sesion con el usuario de un cliente
@app.route('/productos')
def productos():
    cursor = db.connection.cursor()
    cursor.execute('SELECT * FROM registro')#ejecutamos la sentencia SQL con el cursor
    cuenta = cursor.fetchall()#y guardamos los datos que me trae la ejecucion de la sentencia
    print(cuenta)
    return render_template('productos-inicio.html', cuenta=cuenta[1])

#ruta que muetra el CRUD DE comida para el cliente
@app.route('/comida')
def comida():
    cursor = db.connection.cursor()
    cursor.execute('SELECT * FROM food')
    data = cursor.fetchall()#esta funcion guarda los datos selecionados de la tabla de la BD
    
    #pasamos esos datos como parametros para que el html de esta pagina los renderice por medio de un Bucle for
    return render_template('viewsClient/comida.html', datos= data)


#ruta que muestra el CRUD de eventos para clientes
@app.route('/eventosDisponibles')
def eventosDisponibles():
    cursor = db.connection.cursor()
    cursor.execute('SELECT * FROM eventos')
    data = cursor.fetchall()#esta funcion guarda los datos selecionados de la tabla de la BD
    
    #pasamos esos datos como parametros para que el html de esta pagina los renderice por medio de un Bucle for
    return render_template('viewsClient/eventos.html', datos=data)








#rutas y configuraciones para la pagina Login y Registro

#Ruta Registro
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
        
#Login
#metodo validar datos de iniciar sesion, adicional sirve par recuperar el id y poder luego mostrar los datos del cliente en la pagina cuenta
@app.route('/inicio', methods=['GET', 'POST'])                                                     
def iniciar_sesion():
    if request.method == 'POST':#validamos que sea el metodo Post
        usuario = request.form['username']#recuperamos los valosresde los inputs del respectivo template y los guardamos en una variable
        contraseña = request.form['password']
        print('datos')
        print(usuario)
        print(contraseña)

        if usuario != 'admin01':
            cursor = db.connection.cursor()#creamos el cursor para manejar la conexion a la base de datos y lo guardamos en una barible para que se mas comodo
            cursor = db.connection.cursor()#creamos el cursor para manejar la conexion a la base de datos y lo guardamos en una barible para que se mas comodo
            cursor.execute('SELECT * FROM registro WHERE usuario=%s AND contraseña=%s',(usuario, contraseña))#ejecutamos la sentencia SQL con el cursor
            cuenta = cursor.fetchone()#y guardamos los datos que me trae la ejecucion de la sentencia
            print(cuenta) 
                      
            if cuenta:
                session['loggedin'] = True
                session['username'] = cuenta[5] 
                return render_template('productos-inicio.html', cuenta=cuenta)
                #return redirect(url_for('productos'))
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
        foto = request.files['File']
        descripcion = request.form['Descripcion']
        precio = request.form['Precio']
        
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        
        if foto.filename != '':
            nuevoNombreFoto = tiempo+foto.filename
            foto.save("uploads/"+nuevoNombreFoto)
        # print(nombre)
        # print(descripcion)
        # print(precio)
         
        #generamos el curso paso fundamental, "db" es como guardamos la conexion de la base de datos arriba
        cursor = db.connection.cursor()
        #creamos la sentencia SQL
        cursor.execute('INSERT INTO food (Nombre, Foto, Descripcion, Precio) VALUES (%s,%s, %s, %s)', (nombre, nuevoNombreFoto, descripcion, precio))
        #ejecutamos la sentencia con la conexion a la base de datos
        db.connection.commit()
        flash('la comida se agrego con exido')
        return redirect(url_for('administrarfood')) #dentro de los parentecis url_for, va la funcion

#Ruta eliminar un Food
@app.route('/delete/<string:id>')
def deleteFood(id):
    cursor = db.connection.cursor()
    
    cursor.execute('SELECT Foto FROM food WHERE id=%s', [id])
    fila = cursor.fetchall() 
    os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
    
    cursor.execute('Delete FROM food WHERE id = %s',[id])
    db.connection.commit()
    flash('El producto ha sido Removido con Exito')
    return redirect(url_for('administrarfood'))

#Ruta Editar un Food
#esta ruta me recolecta los datos que se van actualizar y me los pega en los campos de la nueva ruta
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
        nombre = request.form['Nombre']
        foto = request.files['File']
        descripcion = request.form['Descripcion']
        precio = request.form['Precio']
        id=request.form['Id']
        
        #creamos el cursor 
        cursor = db.connection.cursor()
        
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        
        if foto.filename != '':
            nuevoNombreFoto = tiempo+foto.filename
            foto.save("uploads/"+nuevoNombreFoto)
            
            cursor.execute('SELECT Foto FROM food WHERE id=%s', [id])
            fila = cursor.fetchall()
            
            os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
            cursor.execute('UPDATE food SET Foto=%s WHERE id=%s', (nuevoNombreFoto,id))
            db.connection.commit()
        
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



#Rutas para administrarEvents 

#ruta Agregar nuevo Evento  
@app.route('/addEvents', methods=['POST'])
def addEvents():
    if request.method == 'POST': #validamos que sea el metodo POST
        nombre = request.form['Nombre']
        foto = request.files['File']
        descripcion = request.form['Descripcion']
        precio = request.form['Precio']
        
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        
        if foto.filename != '':
            nuevoNombreFoto = tiempo+foto.filename
            foto.save("uploads/"+nuevoNombreFoto)
         
        #generamos el curso paso fundamental, "db" es como guardamos la conexion de la base de datos arriba
        cursor = db.connection.cursor()
        #creamos la sentencia SQL
        cursor.execute('INSERT INTO eventos (NombreEvento, Imagen, Lugar, Hora) VALUES (%s,%s, %s, %s)', (nombre, nuevoNombreFoto, descripcion, precio))
        #ejecutamos la sentencia con la conexion a la base de datos
        db.connection.commit()
        flash('El Evento se agrego con exido')
        return redirect(url_for('administrarEvents')) #dentro de los parentecis url_for, va la funcion

#Ruta eliminar un Events
@app.route('/deleteEvents/<string:id>')
def deleteEvents(id):
    cursor = db.connection.cursor()
    
    cursor.execute('SELECT Imagen FROM eventos WHERE id=%s', [id])
    fila = cursor.fetchall()
    os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
    
    cursor.execute('Delete FROM eventos WHERE id = %s',[id])
    db.connection.commit()
    flash('El Evento ha sido Removido con Exito')
    return redirect(url_for('administrarEvents'))

#Ruta Editar un Events
#esta ruta me recolecta los datos que se van actualizar y me los pega en los campos
@app.route('/editEvents/<string:id>')
def editEvents(id):
    #creamos el cursor para ejecutar loa sentencia SQL
    cursor = db.connection.cursor()
    #creamos la Sentencia
    cursor.execute('SELECT * FROM eventos WHERE id = %s',[id])
    #recolectamos los datos de esa senyencia con el cursor y la funcion .fetchall()
    data = cursor.fetchall()
    #print(data[0])
    #despues de terminar renderizamos la pagina
    return render_template('editEvent.html', datos = data[0])
#esta sigue siendo la ruta /editEvents, pero esta parte permite editar los elemntos traidos con anterioridad
@app.route('/updateEvents/<string:id>', methods=['POST'])
def updateEvents(id):
    if request.method == 'POST':
        #recolectamos los datos del formulario
        nombre = request.form['Nombre']
        foto = request.files['File']
        descripcion = request.form['Descripcion']
        precio = request.form['Precio']
        
        #creamos el cursor 
        cursor = db.connection.cursor()
        
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        
        if foto.filename != '':
            nuevoNombreFoto = tiempo+foto.filename
            foto.save("uploads/"+nuevoNombreFoto)
            
            cursor.execute('SELECT Imagen FROM eventos WHERE id=%s', [id])
            fila = cursor.fetchall()
            
            os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
            cursor.execute('UPDATE eventos SET Imagen=%s WHERE id=%s', (nuevoNombreFoto,id))
            db.connection.commit()
        
        #creamos la sentencia SQL con el cursor
        cursor.execute("""
                    UPDATE eventos 
                    SET NombreEvento = %s,
                            Lugar = %s,
                            Hora = %s
                        WHERE id = %s
                    """, (nombre, descripcion, precio, id))
        #ejecutamos esa sentencia SQL
        db.connection.commit()
        #mostramos un mensaje por pantalla
        flash('Evento Actualizado con Exito')
        #renderizamos la pagina requerida
        return redirect(url_for('administrarEvents'))   
    

#ruta Eliminar Cliente
@app.route('/deleteCliente/<string:id>')
def deleteCliente(id):
    cursor = db.connection.cursor()
    cursor.execute('Delete FROM registro WHERE id = %s',[id])
    db.connection.commit()
    
    
    flash('El Cliente ha sido Removido con Exito')
    return redirect(url_for('administrarClientes'))


#ruta Editar Cliente
@app.route('/editCliente/<string:id>')
def editCliente(id):
    #creamos el cursor para ejecutar loa sentencia SQL
    cursor = db.connection.cursor()
    #creamos la Sentencia
    cursor.execute('SELECT * FROM registro WHERE id = %s',[id])
    #recolectamos los datos de esa senyencia con el cursor y la funcion .fetchall()
    data = cursor.fetchall()
    #print(data[0])
    #despues de terminar renderizamos la pagina
    return render_template('viewsAdministrar/buscarCliente.html', datos = data[0])
@app.route('/updateCliente/<string:id>', methods=['POST'])
def updateCliente(id):
    if request.method == 'POST':
        #recolectamos los datos del formulario
        nombre = request.form['Nombre']
        apellido = request.form['Apellido']
        celular = request.form['Celular']
        email = request.form['Email']
        contraseña = request.form['Contraseña']

        #creamos el cursor 
        cursor = db.connection.cursor()
        
        #creamos la sentencia SQL con el cursor
        cursor.execute("""
                    UPDATE registro 
                    SET nombre = %s,
                            apellido = %s,
                            celular = %s,
                            email = %s,
                            contraseña = %s
                        WHERE id = %s
                    """, (nombre, apellido, celular, email, contraseña, id))
        #ejecutamos esa sentencia SQL
        db.connection.commit()
        #mostramos un mensaje por pantalla
        flash('Cliente Actualizado con Exito')
        #renderizamos la pagina requerida
        return redirect(url_for('administrarClientes'))   





#ruta mostrar cuenta del Cliente
@app.route('/cuentaCliente/<string:id>')
def cuentaCliente(id):
    cursor = db.connection.cursor()
    #creamos la Sentencia
    cursor.execute('SELECT * FROM registro WHERE id = %s',[id])
    #recolectamos los datos de esa senyencia con el cursor y la funcion .fetchall()
    data = cursor.fetchall()
    print(data[0])
    #despues de terminar renderizamos la pagina
    return render_template('viewsClient/cuentaCliente.html', datos=data[0])

@app.route('/updateCuentaCliente/<string:id>', methods=['POST'])
def updateCuentaCliente(id):
    if request.method == 'POST':
        #recolectamos los datos del formulario
        celular = request.form['Celular']
        email = request.form['Email']
        contraseña = request.form['Contraseña']

        #creamos el cursor 
        cursor = db.connection.cursor()
        
        #creamos la sentencia SQL con el cursor
        cursor.execute("""
                    UPDATE registro 
                    SET celular = %s,
                            email = %s,
                            contraseña = %s
                        WHERE id = %s
                    """, (celular, email, contraseña, id))
        #ejecutamos esa sentencia SQL
        db.connection.commit()
        #mostramos un mensaje por pantalla
        flash('Su cuenta se ha Actualizado con Exito' )
        #renderizamos la pagina requerida
        return redirect(url_for('productos'))   





#ruta añadir al carrito
# @app.route('/addCarrito', methods=['POST'])
# def addCarrito():
#     if request.method == 'POST': #validamos que sea el metodo POST
        nombre = request.form['NombreP']
        descripcion = request.form['DescripcionP']
        precio = request.form['PrecioP']
        cantidad = request.form['CantidadP']
       
        cursor = db.connection.cursor()
        #creamos la sentencia SQL
        cursor.execute('INSERT INTO carritocomida (NombreP, DescripcionP, PrecioP, CantidadP) VALUES (%s,%s,%s,%s)', (nombre, descripcion, precio, cantidad))
        #ejecutamos la sentencia con la conexion a la base de datos
        db.connection.commit()
        # flash('la comida se agrego con exido al carrito')
        return 'Recivido en el carrito' #dentro de los parentecis url_for, va la funcion
        # return redirect(url_for('comida')) #dentro de los parentecis url_for, va la funcion


#ruta Reservaciones
@app.route('/reservacion/<string:id>')
def reservacion(id):
    flash('La Reservacion Fue Exitosa')
    return redirect(url_for('eventosDisponibles'))





#ejecutamos el servidor para que se actualice automaticamente
if __name__ == '__main__':
    app.run(debug=True)
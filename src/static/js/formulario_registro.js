//importamos del dom, los elementos necesario
const inputName = document.getElementById('name')
const inputLastName = document.getElementById('lastName')
const inputCelular = document.getElementById('celular')
const inputEmail = document.getElementById('email')
const input = document.getElementById('password')
const formulario = document.getElementById('formulario')

//creamos un evento donde el evento submit del formulario se iba a cumplir con cuiertas caracteristicas
formulario.addEventListener('submit', function(e) {
    var input_passwor = input.value

    //validar si la contyraseña ingresada cumple con las especificaciones, en test caso la longitud
    
    if(inputName!='' && inputLastName != '' && inputCelular != '' && inputEmail!= ''){
        if(input_passwor.length < 10){
            e.preventDefault();
            swal('Warning','La contraseña tiene menos de 10 caracteres')    
            console.log(input_passwor)
        }else{
            swal('Felicidades','La Cuenta ha sido creada con Exito', 'success')
            formulario.submit()
        }
    }
})


const inputUser = document.getElementById('usuarioLogin')
const inputContra= document.getElementById('contraLogin')
const formulario = document.getElementById('formulario_login')
const btnIniciar = document.getElementById('btnIniciar')


formulario.addEventListener('submit', function(e) {
    var input_User = inputUser.value
    var input_passwor = inputContra.value
    console.log(input_User, input_passwor)
    if((input_User == '')&&(input_passwor=='')){
        e.preventDefault();
        console.log(input_User)
        console.log(input_passwor)
        swal('Por Favor ingrese un Usuario o Contraseña')    
    }else if((input_User == '')&&(input_passwor != '')){
        e.preventDefault();
        swal('Por Favor ingrese su Usuario')
    }else if((input_User != '')&&(input_passwor == '')){
        e.preventDefault();
        swal('Por Favor ingrese la Contraseña')
    }
})



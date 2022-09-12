//importamos del dom, los elementos necesario

input = document.getElementById('password')
formulario = document.getElementById('formulario')

//creamos un evento donde el evento submit del formulario se iba a cumplir con cuiertas caracteristicas
formulario.addEventListener('submit', function(e) {
    input_passwor = input.value
    //validar si la contyraseña ingresada cumple con las especificaciones, en test caso la longitud
    if(input_passwor.length < 10){
        e.preventDefault();
        alert('La contraseña tiene menos de 10 caracteres')    
        console.log(input_passwor)
    }else{
        formulario.submit()
    } 
})


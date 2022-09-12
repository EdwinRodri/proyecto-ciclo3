inputUser = document.getElementById('usuarioLogin')
inputContra= document.getElementById('contraLogin')
formulario = document.getElementById('formulario_login')


formulario.addEventListener('submit', function(e) {
    input_User = inputUser.value
    input_passwor = inputContra.value
    console.log(input_User, input_Passwor)
    if((input_User == '')||(input_passwor=='')){
        
        console.log(input_User)
        console.log(input_Passwor)
        alert('Por Favor ingrese un Usuario')    
    }else{
        e.preventDefault();
        //formulario.submit()
    } 
})



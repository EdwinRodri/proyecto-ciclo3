const botones = document.getElementById('botonAgregarComida')
const btnFila= document.getElementById('filaBtn')
const cantidad= document.getElementById('cantidades')




btnFila.addEventListener('click', (e)=>{
    e.preventDefault();
    if(e.target.classList[1]=='btn-primary'){
        if (cantidad.value == '0'){
            console.log(cantidad.value)
            swal('warning', 'Porfavor ingrese una cantidad', 'error')
        }else{
            swal('Exito','Su Pedido llegara Pronto')
        }
    }
    
 
});



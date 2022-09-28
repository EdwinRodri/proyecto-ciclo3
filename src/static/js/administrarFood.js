const btnDelete = document.getElementById('botonDelete')

btnDelete.addEventListener('click', function(e){
    if(btnDelete){
        if(!confirm('Estas Seguro de Borrar?')){
            e.preventDefault();
        }
        
    }
})
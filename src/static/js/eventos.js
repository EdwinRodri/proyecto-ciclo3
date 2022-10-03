const botones = document.getElementById('btnsReservar')
const btnFila = document.getElementById('filaBtn')
const btnArray = document.getElementById('arraybtns')
const hora = document.getElementById('valorHora')


// btnArray.forEach(element => {
//     element.addEventListener('click', () => {
//         alert('buenas')
//     })
// });
console.log([btnArray])

btnFila.addEventListener('click', (e)=>{
    e.preventDefault();
    if (e.target.classList[1]=='btn-info'){
        console.log(botones.textContent)
        if(botones.textContent == 'Reservar'){
            swal('Felicidades','Reserva Exitosa', 'success')
            botones.style.backgroundColor ='red'
            botones.textContent = 'Cancelar Reserva'
            console.log(e.target)
        }else if(botones.textContent == 'Cancelar Reserva'){
            botones.style.backgroundColor ='purple'
            botones.textContent = 'Reservar'
            console.log(botones.textContent)
            swal('Warning','Reserva Cancelada','warning')
        }
    }
   
 
});


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
        swal('Reserva Exitosa')
        botones.style.backgroundColor ='red'
        botones.textContent = 'Cancelar Reserva'
        console.log(e.target)
    }
 
});


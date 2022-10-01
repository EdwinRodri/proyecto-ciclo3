const botones = document.getElementById('btnsReservar')
const btnFila = document.getElementById('filaBtn')
const hora = document.getElementById('valorHora')

console.log(hora.value)

console.log(btnFila.lastElementChild)

const arr = [btnFila]
console.log(arr)

btnFila.childNodes.forEach(element => {
    element.addEventListener('click', () =>{
        console.log(hora.value)
    })
});




btnFila.addEventListener('click', (e)=>{
    e.preventDefault();
    console.log(e.target)
    if(e.target.classList[0] == 'horaClase'){
        console.log(hora.textContent)
    }
    if (e.target.classList[1]=='btn-info'){
        alert('hola')
    }
 
});


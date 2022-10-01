// const btnDisminuir = document.getElementById('btnDisminuir')
// const btnAumentar = document.getElementById('btnAumentar')
// const valorCantidad = document.getElementById('valorCantidad')
// const agregarCarrito = document.getElementById('btnAgregar')


// console.log(valorCantidad.textContent)

// agregarCarrito.addEventListener('click', (e)=>{
//     let valor = valorCantidad.textContent
//     Number(valor)
//     valorCantidad.innerHTML= valor * 3
// })

const valor = document.getElementsByClassName('claseDeInputs')

valor.forEach(valores =>{
    console.log(valores.value)
})


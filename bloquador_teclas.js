
const enable=()=> {
    let rows = document.getElementsByClassName('btn')
    for (var item of rows) {
        item.classList.remove('d-none')
    }
  }

const disabled=()=> {
    let rows = document.getElementsByClassName('btn')
    for (var item of rows) {
        item.classList.add('d-none')
    }
  }

const colocar_aviso = () =>{
      const aviso = JSON.parse(localStorage.getItem('db_aviso')) ?? []
      localStorage.setItem('db_aviso', JSON.stringify(['aviso','aviso']))
  }

const remover_aviso = () =>{
      localStorage.setItem('db_aviso', JSON.stringify(['']))
  }

const verifica_aviso = () =>{
    const aviso = JSON.parse(localStorage.getItem('db_aviso')) ?? []
    console.log(aviso.length);
    if (aviso.length>1){
        disabled()
        alert("Não identificamos o pagamento do sistema, efetue o pagamento.");
        setTimeout(enable, 10000); 
    }    
}

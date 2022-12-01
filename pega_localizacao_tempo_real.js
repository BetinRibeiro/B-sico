

const retorna_localizacao=()=>{
    return navigator.geolocation.getCurrentPosition(salvar_log)

}

function salvar_log(posicao){
    //console.log(posicao);
    //verifica se a ultima envio tem mais de 4 hrs
    //fazer a função!!!
    enviar_dados(posicao);
    //salva o horario desse envio de log
}


const enviar_dados= (dados) => {
    const settings = {
        "async": true,
        "crossDomain": true,
        "url": "##Link da minha api que salva os logs",
        "method": "POST",
        "headers": {
            "cookie": "session_id_acs_empresas=fhadjksghiucvnoçasnfvvhsdiudgfh",
            "Content-Type": "application/json"
    },
    "processData": false,
    "data": `{\n\t\t\"descricao\": \"{Foi}\",\n\t\t\"latitude\": \"${dados.coords.latitude}\",\n\t\t\"longitude\": \"${dados.coords.longitude}\",\n\t\t\"horario\": \"${dados.timestamp}\"\n}`
};



retorna_localizacao()
//faz a impressao
$.ajax(settings).done(function (response) {
    console.log(response);
});
}

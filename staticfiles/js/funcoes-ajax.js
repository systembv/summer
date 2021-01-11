function compraPecas(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/estoque/computar_compra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            console.log(result);
            $("#mensagem").text(result.mensagem);
        }
    });
}



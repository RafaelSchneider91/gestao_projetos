function usuarios_projeto() {
    idProjeto = window.location.pathname.split('/').filter(Boolean).pop()
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value

    // data = new FormData()

    // data.append('id_projeto', id_projeto)

    fetch("usuarios_projeto/" + idProjeto, {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: json.stringify({
            id: idProjeto
        })

    }).then(function(result) {
        return result.json()
    }).then(function(data){
        console.log(data)
        // console.log(id_projeto)
        // document.getElementById('usuarios_projeto').style.display = 'block'

        // div_usuario = document.getElementById('usuarios_projeto')
        // div_usuario.innerHTML = ""
        
        // for(i=0; i < data['usuario'].length; i++){

        //     div_usuario.innerHTML += "<form action='#' method='POST'>\
        //             <div class='row'>\
        //                 <div class='col-md'>\
        //                     <input class='form-control' name='carro' type='text' value='"+ data['usuario'][i][0]['fields']['first_name'] + ' ' + data['usuario'][i][0]['fields']['last_name'] + "'>\
        //                 </div>\
        //                 <div class='col-md'>\
        //                     <input class='form-control' name='placa' type='text' value='"+ data['perfil'][i][0]['fields']['perfil'] + "'>\
        //                 </div>\
        //                 <div class='col-md'>\
        //                     <input class='form-control' type='text' name='ano' value='1' >\
        //                 </div>\
        //             </div>\
        //                     </form><br>"
        // }

        // console.log(data)
    })
}


function usuarios_projeto_teste() {
    
    fetch('http://127.0.0.1:8000/projeto/2')
  .then(response => response.json())
  .then(data => {
    // processa os dados retornados pelo servidor
    const usuarios = data.usuarios; // assume-se que a resposta contém uma lista de usuários do projeto
    
    // fazer algo com a lista de usuários, por exemplo, exibir na página
    const listaDeUsuarios = document.querySelector('#lista-de-usuarios');
    usuarios.forEach(usuario => {
      const item = document.createElement('li');
      item.textContent = usuario.nome;
      listaDeUsuarios.appendChild(item);
    });
  })
  .catch(error => {
    console.error('Erro ao buscar usuários do projeto', error);
  });

}
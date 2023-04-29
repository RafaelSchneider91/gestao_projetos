function add_usuarios_projeto2(){
    container = document.getElementById('form-usuario')
    const usuarios = '{% for usuario in usuarios %} <option value={{usuario.usuario_id}}>{{usuario}}</option>{% endfor %}'


    // html = "<br>  <div class='row'> <div class='col-md'> <input type='text' placeholder='usuario' class='form-control' name='usuario' > </div>\
    // <div class='col-md'><input type='text' placeholder='perfil' class='form-control' name='perfil' ></div>\
    //  <div class='col-md'> <input type='checkbox' placeholder='recebe email' class='form-control' name='recebe_email'> </div> </div>"

    html = "<div> <table class='tabela' cellpadding='20'> <tr> <th>Usuario</th> <th>Perfil</th>  <th>Recebe Email?</th> </tr>  <tr>\
                <td><select class='form-select input-tarefa' name='faseprojeto'>\
                </select></td>\
                <td> <input type='text' placeholder='perfil' class='form-control' name='perfil'> </td>\
                <td> <input type='checkbox' placeholder='recebe email' class='form-control' name='recebe_email'></td> </tr> </table> </div>"

    container.innerHTML += html
}


function add_usuarios_projeto() {
    projeto = document.getElementById('projeto_select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    // console.log(csrf_token)
    id_projeto = projeto.value

    data = new FormData()
    data.append('id_projeto', id_projeto)

    fetch("/add_usuarios_projeto/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data

    }).then(function(result) {
        return result.json()
    }).then(function(data){
        // console.log(data)
        document.getElementById('add_usuarios_projeto').style.display = 'block'

        div_usuario = document.getElementById('add_usuarios_projeto')
        div_usuario.innerHTML = ""
        
        for(i=0; i < data['usuario'].length; i++){
            console.log(data['usuario'][i][0]['fields']['first_name'] + ' ' + data['usuario'][i][0]['fields']['last_name'] )
            // console.log(data['usuario'][i][0]['fields']['first_name'])

            div_usuario.innerHTML += "<form action='' method=''><div class='row'>\
            <div class='col_md'>\
            <input type='text' name = 'usuario' value='"+ data['usuario'][i][0]['fields']['first_name'] + ' ' + data['usuario'][i][0]['fields']['last_name'] + "'>\
            </div></div><br>"



        }



    })
}


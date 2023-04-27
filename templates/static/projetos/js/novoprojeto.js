function add_usuarios_projeto(){
    container = document.getElementById('form-usuario')
    const usuarios = '{% for usuario in usuarios %} <option value={{usuario.usuario_id}}>{{usuario}}</option>{% endfor %}'


    // html = "<br>  <div class='row'> <div class='col-md'> <input type='text' placeholder='usuario' class='form-control' name='usuario' > </div>\
    // <div class='col-md'><input type='text' placeholder='perfil' class='form-control' name='perfil' ></div>\
    //  <div class='col-md'> <input type='checkbox' placeholder='recebe email' class='form-control' name='recebe_email'> </div> </div>"

    html = "<div> <table class='tabela' cellpadding='20'> <tr> <th>Usuario</th> <th>Perfil</th>  <th>Recebe Email?</th> </tr>  <tr>\
                <td><select class='form-select input-tarefa' name='faseprojeto'>\
                "+ usuarios +"</select></td>\
                <td> <input type='text' placeholder='perfil' class='form-control' name='perfil'> </td>\
                <td> <input type='checkbox' placeholder='recebe email' class='form-control' name='recebe_email'></td> </tr> </table> </div>"

    container.innerHTML += html
}

function dados_usuarios() {

    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value

    fetch("/usuarios/dados_usuarios/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token
        },
        

    })
}


function dados_usuarios() {
    $.ajax({
        url: '/dados_usuarios/',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
        console.log(data)
        },
        error: function(xhr, status, error) {
            console.error('Erro ao obter dados do modelo: ', error);
        }
    });
}





function add_usuarios_projeto() {
    // usuario = document.getElementById('usuario-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    // console.log(csrf_token)
    // id_usuario = usuario.value

    // data = new FormData()
    // data.append('id_usuario', id_usuario)

    fetch("/add_usuarios_projeto/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        // body: data

    }).then(function(result) {
        return result.json()
    }).then(function(data){
        console.log(data)
        document.getElementById('add_usuarios_projeto')
    })
}


function add_usuarios_projeto(){
    container = document.getElementById('form-usuarios')
    
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value

    html = "<div><br><div class='row'><div class='col-md'><label>Usuario:</label><select class='form-control' name='usuario'><option value='a'>aaaaaaaaaaaa</option></select>\
    </div><div class='col-md'><label>Perfil:</label><select class='form-control' name='perfil'> <option value='a'>aaaaaaaaaaaa</option></select></div>\
    <div class='col-md'><label>Recebe_email:</label><br><input type='checkbox' name='recebe_email' value='true'></div></div></div>"

    container.innerHTML += html

    url = 'add_usuarios_projeto/'

    const response = fetch(url, {
        method: "GET",
        headers: {
            'X-CSRFToken': csrf_token,
        },
    

    }).then(function(result){
        console.log(result)
    })

    
}




// function add_usuarios_projeto() {
//     projeto = document.getElementById('projeto_select')
//     csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
//     // console.log(csrf_token)
//     id_projeto = projeto.value

//     data = new FormData()
//     data.append('id_projeto', id_projeto)

//     fetch("/add_usuarios_projeto/", {
//         method: "POST",
//         headers: {
//             'X-CSRFToken': csrf_token,
//         },
//         body: data

//     }).then(function(result) {
//         return result.json()
//     }).then(function(data){
//         // console.log(data)
//         document.getElementById('add_usuarios_projeto').style.display = 'block'

//         div_usuario = document.getElementById('add_usuarios_projeto')
//         div_usuario.innerHTML = ""
        
//         for(i=0; i < data['usuario'].length; i++){
//             // console.log(data['usuario'][i][0]['fields']['first_name'] + ' ' + data['usuario'][i][0]['fields']['last_name'] )
//             // console.log(data['usuario'][i][0]['fields']['first_name'])

//             // div_usuario.innerHTML += "<form action='' method='' class='form_usuarios'>\
//             // <th class='th_usuarios'>\
//             //     <input type='text' name = 'usuario' value='"+ data['usuario'][i][0]['fields']['first_name'] + ' ' + data['usuario'][i][0]['fields']['last_name'] + "'>\
//             // </th><br>\
//             // <th class='th_usuarios'>\
//             //     <input type='text' name = 'usuario' value='"+ data['perfil'][i][0]['fields']['perfil'] + "'>\
//             // </th></th><br></form>"


//             div_usuario.innerHTML += "<form action='#' method='POST'>\
//                     <div class='row'>\
//                         <div class='col-md'>\
//                             <input class='form-control' name='carro' type='text' value='"+ data['usuario'][i][0]['fields']['first_name'] + ' ' + data['usuario'][i][0]['fields']['last_name'] + "'>\
//                         </div>\
//                         <div class='col-md'>\
//                             <input class='form-control' name='placa' type='text' value='"+ data['perfil'][i][0]['fields']['perfil'] + "'>\
//                         </div>\
//                         <div class='col-md'>\
//                             <input class='form-control' type='text' name='ano' value='1' >\
//                         </div>\
//                     </div>\
//                             </form><br>"



//         }

//         console.log(data)


//     })
// }


// (async function novo_projeto_addusuario (){
//     try {

//         projeto = document.getElementById('projeto_select')
        

//         const headers = {
//             'Content-Type': 'application/json',
//             'testando': 'teste',
//         };

//         const init = {
//             method: 'POST',
//             headers: headers,
//             body: JSON.stringify ( {
//                 title: 'testando'
//             }),
//         };

//         const response = await fetch('/add_usuarios_projeto/', init, );
//         const jsonData = await response.json();
//         console.log(jsonData);
//     } 
//     catch(erro){
//         console.log('deu erro', erro);
//     }
    
// })();





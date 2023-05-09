function add_usuarios_projeto(){
    container = document.getElementById('form-usuarios')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
  
    url = '/novo_projeto/add_usuarios_projeto/'
   

    const response = fetch(url, {
        method: "GET",
        headers: {
            'X-CSRFToken': csrf_token,
        }
    })
    .then(function(result){
        return result.json()
        // console.log('TESTE1')

    }).then(function(data){
        
        // console.log(data['usuarios'][0]['user']['username'])
        // console.log(data['perfil'])
        // console.log(data['usuarios'])

        // // Itera sobre os usuários e adiciona uma nova opção para cada um
        // data['usuarios'].forEach(function(usuario) {
        //     var id = usuario['pk'];
        //     var username = usuario['fields']['first_name'] + " " + usuario['fields']['last_name'] ;
        //     var option = document.createElement('option');
        //     option.value = id + '|' + username;
        //     option.text = username;
        //     var select = document.getElementById('usuario');
        //     select.appendChild(option);
        //   });

    //     const usuario =
    //    data['usuarios'].forEach(function(usuario) {
    //     var username = usuario['user']['first_name'] + " " + usuario['user']['last_name'];
    //     var option = document.createElement('option');
    //     var id_username = usuario['user']['pk']
    //     option.value = id_username;
    //     option.text = username;
    //     var select = document.getElementById('usuario');
    //     select.appendChild(option);
    // });

    //     data['perfil'].forEach(function(perfil1) {
    //         var perfil = perfil1['perfil']['perfil'];
    //         var option = document.createElement('option');
    //         // var id_username = usuario['user']['pk']
    //         option.value = perfil;
    //         option.text = perfil;
    //         var select = document.getElementById('perfil');
    //         select.appendChild(option);
    //   });

        
    for(i=0; i<data['usuarios'].length; i++){
        console.log(data['usuarios'][i]['user']['username'])

        html = "<div><br><div class='row'><div class='col-md'>\
            <label>Usuario:</label>\
            <select class='form-control'  name='usuario'><option value=''>"+ data['usuarios'][i]['user']['first_name'] +"</option></select>\
            </div><div class='col-md'>\
            <label>Perfil:</label>\
            <select class='form-control' id='perfil' name='perfil'> <option value=''>Selecione o perfil...</option></select>\
            </div><div class='col-md'>\
            <label>Recebe_email:</label>\
            <br><input type='checkbox' name='recebe_email' value='true'></div></div></div>"


        container.innerHTML += html
      }

    })
    
    // html = "<div><br><div class='row'><div class='col-md'>\
    //         <label>Usuario:</label>\
    //         <select class='form-control' id='usuario' name='usuario'><option value=''>Selecione um usuario...</option></select>\
    //         </div><div class='col-md'>\
    //         <label>Perfil:</label>\
    //         <select class='form-control' id='perfil' name='perfil'> <option value=''>Selecione o perfil...</option></select>\
    //         </div><div class='col-md'>\
    //         <label>Recebe_email:</label>\
    //         <br><input type='checkbox' name='recebe_email' value='true'></div></div></div>"


    // container.innerHTML += html
    
};


// div_usuarios = document.getElementById('usuario')
// for(i=0; i<data['usuarios'].length; i++){
//     console.log(data['usuarios'][i]['fields']['username'])
// }

// function add_usuarios_projeto(){
// // url = 'add_usuarios_projeto/'
// url = 'https://jsonplaceholder.typicode.com/posts'

// const response = fetch(url)
// .then(function(responseData){
//     console.log(responseData)
// })
// };



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





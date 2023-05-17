function add_usuarios_projeto() {
    const container = document.getElementById('form-usuarios');
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const url = '/novo_projeto/add_usuarios_projeto/';
  
    fetch(url, {
      method: 'GET',
      headers: {
        'X-CSRFToken': csrf_token,
      },
    })
    .then(function(result) {
      return result.json();
    })
    .then(function(data) {
        const selectUsuario = document.createElement('select')
        selectUsuario.setAttribute('id', 'usuario')
        selectUsuario.setAttribute('name', 'usuario')
        selectUsuario.className = 'form-control' // adiciona a classe CSS

        const selectPerfil = document.createElement('select')
        selectPerfil.setAttribute('id', 'perfil')
        selectPerfil.setAttribute('name', 'perfil')
        selectPerfil.className = 'form-control' // adiciona
  
      
      
        for (let i = 0; i < data['usuarios'].length; i++) {
        const usuario = data['usuarios'][i]['user']['first_name']+ " " +  data['usuarios'][i]['user']['last_name'] ;
        const idusuario = data['usuarios'][i]['id']
        const option = document.createElement('option');
        option.text = usuario;
        option.value = idusuario;
        selectUsuario.add(option);
      }


      for (let i = 0; i < data['perfil'].length; i++) {
        const perfil = data['perfil'][i]['perfil']['perfil'];
        const idusuario = data['perfil'][i]['id']
        const option = document.createElement('option');
        option.text = perfil;
        option.value = idusuario;
        selectPerfil.add(option);
      }


      // console.log(data)
  
      const html = `<div>
                      <br>
                      <div class='row'>
                        <div class='col-md'>
                          <label>Usuario:</label>
                          ${selectUsuario.outerHTML}
                        </div>
                        <div class='col-md'>
                          <label>Perfil:</label>
                          ${selectPerfil.outerHTML}
                        </div>
                        <div class='col-md'>
                          <label>Recebe_email:</label>
                          <br>
                          <input type='checkbox' name='recebe_email' value='true'>
                        </div>
                      </div>
                    </div> <br>`;
  
      container.innerHTML += html;

      // console.log(data['perfil'])

      // const btnAddUsuario = document.getElementById('btn-add-usuario');
      // btnAddUsuario.removeEventListener('click', add_usuarios_projeto);
    });
  }
  
  
  
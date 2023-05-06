var afazerList = document.getElementById('afazer');
var fazendoList = document.getElementById('EmAndamento');
var pendenteList = document.getElementById('pendente');
var concluidoList = document.getElementById('concluido');


var sortable = Sortable.create(afazerList, {
    group: 'kanban',
    animation: 150,
    onEnd: function (evt) {
        console.log('Tarefa movida de A fazer para ' + evt.to.id);
    }
});

var sortable2 = Sortable.create(fazendoList, {
    group: 'kanban',
    animation: 150,
    onEnd: function (evt) {
        console.log('Tarefa movida de Fazendo para ' + evt.to.id);
    }
});

var sortable3 = Sortable.create(pendenteList, {
    group: 'kanban',
    animation: 150,
    onEnd: function (evt) {
        console.log('Tarefa movida de Pendente para ' + evt.to.id);
    }
})

var sortable4 = Sortable.create(concluidoList, {
    group: 'kanban',
    animation: 150,
    onEnd: function (evt) {
        console.log('Tarefa movida de Concluido para ' + evt.to.id);
    }
})


// $(document).ready(function() {
//     // identifica o botão "Close" e associa a ação de fechar o modal
//     $(".btn-close").click(function() {
//       $("#exampleModal").modal("hide");
//     });
//   });
  


// alterar projeto em tarefas
function alteraprojeto() {
    var selectElement = document.getElementById("projeto_select");
    var selectedValue = parseInt(selectElement.value);
    var data = new FormData();
    data.append('id_projeto', selectedValue);
    

    // console.log([...data.entries()]); //Envio do ID do projeto

    var csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
   
    var url = 'tarefas/alteraprojeto/';  // define a URL do endpoint do Django que receberá o valor

    var options = {
        method: 'POST',
        body: data,
        headers: {
          'X-CSRFToken': csrf_token // adiciona o token CSRF, se necessário
        }
      };

    // console.log(selectedValue) //id do projeto

    
    fetch(url, options) // envia a requisição com fetch
    .then(function(result) {
        return result.json()
    })
    .then(function(data){

        // console.log(data)

        div_tarefas_afazer = document.getElementById('afazer')
        div_tarefas_EmAndamento = document.getElementById('EmAndamento')
        div_tarefas_pendente = document.getElementById('pendente')
        div_tarefas_concluido = document.getElementById('concluido')

        div_tarefas_afazer.innerHTML = ""
        div_tarefas_EmAndamento.innerHTML = ""
        div_tarefas_pendente.innerHTML = ""
        div_tarefas_concluido.innerHTML = ""


        // console.log(data['tarefas'][0]['fields']['status_tarefa']) 

        for (i=0; i<data['tarefas'].length; i++){
            if (data['tarefas'][i]['fields']['status_tarefa'] === 'N') { // verifica se o status da tarefa é 'N = NÃO INICIADO'
                // console.log(data['tarefas'][i]['fields']['nome'])
                // console.log(data['tarefas'][i]['id_tarefa'])
        
                div_tarefas_afazer.innerHTML += "<div value='"+ data['tarefas'][i]['id_tarefa'] + "'class='task'>"+ data['tarefas'][i]['fields']['nome'] +"</div>"
            }
            else if (data['tarefas'][i]['fields']['status_tarefa'] === 'E') { // verifica se o status da tarefa é 'E = EM ANDAMENTO'
                // console.log(data['tarefas'][i]['fields']['nome'])
        
                div_tarefas_EmAndamento.innerHTML += "<div value='"+ data['tarefas'][i]['id_tarefa'] + "' class='task'>"+ data['tarefas'][i]['fields']['nome'] +"</div>"
            }
            else if (data['tarefas'][i]['fields']['status_tarefa'] === 'P') { // verifica se o status da tarefa é 'P = PENDENTE'
                // console.log(data['tarefas'][i]['fields']['nome'])
        
                div_tarefas_pendente.innerHTML += "<div value='"+ data['tarefas'][i]['id_tarefa'] + "' class='task'>"+ data['tarefas'][i]['fields']['nome'] +"</div>"
            }
            else if (data['tarefas'][i]['fields']['status_tarefa'] === 'C') { // verifica se o status da tarefa é 'P = PENDENTE'
                // console.log(data['tarefas'][i]['fields']['nome'])
        
                div_tarefas_concluido.innerHTML += "<div value='"+ data['tarefas'][i]['id_tarefa'] + "' class='task'>"+ data['tarefas'][i]['fields']['nome'] +"</div>"
            }
        }
    })
}


//editar a tarefa abrir o modal
// Defina a função para abrir a modal
function openModal() {
    // Selecione o modal pelo ID
    const modal = $('#myModal');
  
    // Exiba o modal
    modal.css('display', 'block');
  
    // Defina a ação para fechar a modal quando o usuário clicar no botão de fechar ou fora do modal
    const span = $('.close')[0];
    span.onclick = function() {
      modal.css('display', 'none');
    }
    window.onclick = function(event) {
      if (event.target == modal[0]) {
        modal.css('display', 'none');
      }
    }
  }
  
// var todoList = document.getElementById('todo');
// var doingList = document.getElementById('doing');
// var doneList = document.getElementById('done');


// var sortable = Sortable.create(todoList, {
//     group: 'kanban',
//     animation: 150,
//     onEnd: function (evt) {
//         console.log('Tarefa movida de A fazer para ' + evt.to.id);
//     }
// });

// var sortable2 = Sortable.create(doingList, {
//     group: 'kanban',
//     animation: 150,
//     onEnd: function (evt) {
//         console.log('Tarefa movida de Fazendo para ' + evt.to.id);
//     }
// });

// var sortable3 = Sortable.create(doneList, {
//     group: 'kanban',
//     animation: 150,
//     onEnd: function (evt) {
//         console.log('Tarefa movida' + evt.to.id);
//     }
// })

var afazerList = document.getElementById('afazer');
var fazendoList = document.getElementById('fazendo');
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


$(document).ready(function() {
    // identifica o botão "Close" e associa a ação de fechar o modal
    $(".btn-close").click(function() {
      $("#exampleModal").modal("hide");
    });
  });
  


// alterar projeto em tarefas
function alteraprojeto() {
    // console.log('teste')
    var selectElement = document.getElementById("projeto_select");
    // var selectedValue = selectElement.value;
    var selectedValue = parseInt(selectElement.value);

    // console.log(selectedValue)

    var data = new FormData();
    data.append('id_projeto', selectedValue);

    console.log([...data.entries()]);


    var csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value

    // console.log(csrf_token)

    // define a URL do endpoint do Django que receberá o valor
    var url = 'tarefas/alteraprojeto/';

    var options = {
        method: 'POST',
        body: data,
        headers: {
          'X-CSRFToken': csrf_token // adiciona o token CSRF, se necessário
        }
      };

    console.log(selectedValue)

    // envia a requisição com fetch
    fetch(url, options)
    .then(function(result) {
        return result.json()
    })
    .then(function(data){
        console.log(data)
        
        tarefa = document.getElementById('nome_tarefa')
        tarefa.value = data['nome']

        descricao = document.getElementById('descricao_tarefa')
        descricao.value = data['descricao']



    })
}

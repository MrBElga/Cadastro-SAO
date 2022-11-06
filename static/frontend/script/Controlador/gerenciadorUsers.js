class GerenciadorUsers{
    #listaUsers;
    constructor(){
        this.#listaUsers = [];
    }

    obterUser(){
        return this.#listaUsers;
    }

    adicionarUser(user){
       fetch('https://pacific-hollows-14259.herokuapp.com/user',
       {
            method:"POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
       }).then((resposta) => {
        if(resposta.ok)
        {
            let elemVisualizacaoTabela = document.querySelector("[data-Tabela]");
            this.exibirTabelaAcolhedores(elemVisualizacaoTabela);
            alert('Usuario cadastrado com sucesso');
        }
        });
    }

    removerUser(user){
       
       for (let i=0; i < this.#listaUsers.length; i++)
       {
           if (this.#listaUsers[i].nome == user.nome){
               this.#listaUsers.splice(i,1);
               break; 
           } 
       }
       this.salvar();    
    }


    restaurar(alvo){
        fetch('https://pacific-hollows-14259.herokuapp.com/user',
        {
            method:"GET",
            headers:{ "Content-Type" : "application/json"}
        }).then((resposta) => {
            if (resposta.ok){
                return resposta.json();//retorna tambem uma promessa (promise)
            }
            else{
                console.error("Erro ao realizar a busca por Usuarios!");
                this.exibirTabelaUsuarios(alvo);
            }
        }).then((dados) => {
            this.#listaUsers = dados;
            this.exibirTabelaUsuarios(alvo);
        });
    }

    exibirTabelaUsuarios(alvo){
        let elemVisualizacao = alvo
        elemVisualizacao.innerHTML = "";
        
        if (this.#listaUsers.length > 0)
        {
            let tabela = document.createElement("table");
            tabela.className = "table table-striped table-hover";
            let cabecalhoTabela = document.createElement("thead");
            cabecalhoTabela.innerHTML = "<tr> \
                                           <th>ID</th>\
                                           <th>Nome</th> \
                                           <th>NickName</th> \
                                           <th>Data Nasc</th> \
                                           <th>Genero</th> \
                                           <th>Email</th> \
                                           <th>Senha</th> \
                                        </tr>";
            tabela.appendChild(cabecalhoTabela);
            
            let corpoTabela = document.createElement("tbody");
            for (let i = 0; i < this.#listaUsers.length; i++)
            {
                let linha = document.createElement("tr");
                linha.innerHTML = "<td>" + this.#istaUsers[i].id+ "</td>" + 
                                  "<td>" + this.#listaUsers[i].cpf + "</td>" +
                                  "<td>" + this.#listaUsers[i].nome + "</td>" +
                                  "<td>" + this.#listaUsers[i].endereco + "</td>" +
                                  "<td>" + this.#listaUsers[i].cidade + "</td>" +
                                  "<td>" + this.#listaUsers[i].uf + "</td>" +
                                  "<td>" + this.#listaUsers[i].cep + "</td>" +
                                  "<td>" + this.#listaUsers[i].renda + "</td>" +
                                  "<td>" + "<button onclick='excluirUsersTabela(" + i +")' type='button' class='btn btn-danger'>Excluir</button></td>";
                corpoTabela.appendChild(linha);
            }
            tabela.appendChild(corpoTabela);
            elemVisualizacao.appendChild(tabela);
        }
        else{
            elemVisualizacao.innerHTML = "<p>Não foi possível obter Usuarios no servidor</p>";
        }
    }

}
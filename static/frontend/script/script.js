var gerenciadorUsers;
var formularioCadastro = document.forms[0];

function inicio(){
    gerenciadorUsers = new GerenciadorUsers();
    //gerenciadorUsers.salvar();
    gerenciadorUsers.restaurar();
    if(document.querySelector("[data-Tabela]")!=null)
        gerenciadorUsers.exibirTabelaUsers(elemVisualizacaoTabela);
    if(formularioCadastro != null){
        formularioCadastro.onsubmit = () => {
            let dadosValidos = validarDados();
            if (dadosValidos){
            
                let elemNome     = document.getElementById("nome");
                let elemNickName = document.getElementById("nickName");
                let elemDataNasc = document.getElementById("dataNasc");
                let elemGenero   = document.querySelector("input[name='genero']:checked");
                let elemEmail    = document.getElementById("email");
                let elemSenha    = document.getElementById("senha");
            
            
                let user = new User(0,elemNome.value,elemNickName.value,
                                    elemDataNasc.value,elemGenero.value,
                                    elemEmail.value,elemSenha.value);

                gerenciadorUsers.adicionarUser(user);            
                let elemVisualizacaoTabela = document.querySelector("[data-Tabela]");
                gerenciadorUsers.exibirTabelaUsers(elemVisualizacaoTabela);
            }
            return dadosValidos
        }
    }
}

function validarDados(){
// dados válidos verdadeiro ou falso
    let elemMensagem = document.querySelector("[data-Mensagem]");

    let elemNome = document.getElementById("nome");
    if (elemNome.value.length == 0){
        elemMensagem.innerHTML = "O nome deve ser informado!";
        return false;
    }
   

    let elemNickName = document.getElementById("nickName");
    if(elemNickName.value.length == 0){
        elemMensagem.innerHTML = "O NickName deve ser informado!!";
        return false;
    }

    let elemDataNasc = document.getElementById("dataNasc");
    if (elemDataNasc.value.length == 0){
        elemMensagem.innerHTML = "Informe a data de nascimento";
        return false;
    }
    
    let elemEmail = document.getElementById("email");
    if(elemEmail.value.length == 0){
        elemMensagem.innerHTML = "Informe o E-mail";
        return false;
    }
    let elemVemail = document.getElementById("Vemail");
    if(elemVemail.value != elemEmail.value){
        elemMensagem.innerHTML = "Os emails não são iguais";
        return false;
    }

    let elemSenha = document.getElementById("senha");
    if(elemSenha.value.length == 0){
        elemMensagem.innerHTML = "Informe uma senha valida";
        return false;
    }

    let elemVSenha = document.getElementById("Vsenha");
    if(elemVSenha.value != elemSenha.value){
        elemMensagem.innerHTML = "As Senhas informadas não são iguais";
        return false;
    }  
    return true;
}

window.onload = inicio;
//window.addEventListener("load", inicio);


class User{
    #id
    #nome;
    #nickName;
    #dataNasc;
    #genero;
    #email;
    #senha;
    


    constructor(id,nome,nickName, dataNasc, genero, email,senha){
        this.#id = id;
        this.#nome = nome;
        this.#nickName = nickName;
        this.#dataNasc = dataNasc;
        this.#genero = genero;
        this.#email = email;
        this.#senha = senha;
    }

    get id(){
        return this.#id;
    }

    set id(novoId)
    {
        this.#id = novoId;
    }
    get nome(){
        return this.#nome;
    }

    set nome(novoNome){
        this.#nome = novoNome;    
    }
    get nickName(){
        return this.#nickName;
    }

    set nickName(novoNickName){
        this.#nickName = novoNickName;
    } 

    get dataNasc(){
        return this.#dataNasc;
    }

    set dataNasc(data){
        this.#dataNasc = data;
    }

    get genero(){
        return this.#genero;

    }

    set genero(novoGenero){
        this.#genero = novoGenero;
    }

    get email(){
        return this.#email;
    }

    set email(novoEmail){
        this.#email = novoEmail;
    }

    get senha(){
        return this.#senha;
    }

    set senha(novaSenha){
        this.#senha = novaSenha;

    }
    //override toJSON() da classe pai

    toJSON(){
        return {
            id : this.#id,
            nome : this.#nome,
            nickName : this.#nickName,
            dataNasc: this.#dataNasc,
            genero : this.#genero,
            email : this.#email,
            senha : this.#senha
        }
    }

}
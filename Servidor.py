
from flask import Flask, request, make_response, jsonify

from backend.Persistencia.UsuarioDB import UsuarioBD
from backend.Modelo.Usuario import User


app = Flask(__name__)

@app.route("/")
def index():
    return "<p>O pai tá on!</p>"

#o endereço da informação, e seus métodos de requisição permitidos
@app.route("/usuario", methods=["GET", "POST", "PUT", "DELETE"])
@app.route("/usuario/<int:id>", methods=["POST","GET", "PUT", "DELETE"])
def usuario(id=None):
    usuarioBD = UsuarioBD()
    if request.method == "GET":
        if id:
            usuario = usuarioBD.consultar(id)
            if usuario:
                return make_response(jsonify(usuario[0].toJSON()))
            else:
                return make_response(jsonify(usuario))
        else:
            usuario = usuarioBD.consultar("")
            listaUsers = []
            for usuario in usuario:
                listaUsers.append(usuario.toJSON())
            return make_response(jsonify(listaUsers))

    elif request.method == "POST":
        if id:
            return make_response(jsonify({
                "status":"erro",
                "mensagem":"Método POST não permitido quando o código é informado na url!"
            }))
        else:
            dados       = request.get_json()
            nome        = dados.get("nome")
            nickName    = dados.get("nickName")
            dataNasc    = dados.get("dataNasc")
            genero      = dados.get("genero")
            email       = dados.get("email")
            senha       = dados.get("senha")
            if  nome and dataNasc and genero and \
                email and senha:
                usuario = User(0, nome, nickName, dataNasc,genero,
                                      email, senha)
                usuarioBD.incluir(usuario)
                return make_response(jsonify({
                    "status":"ok",
                    "id":usuario.id
                }))
            else:
                return make_response(jsonify({
                   "status":"erro",
                   "mensagem":"Informe todos os dados para cadastrar um usuario. Veja a documentação da API!"     
                }))


    elif request.method == "PUT":
        if id:
            dados       = request.get_json()
            nome        = dados.get("nome")
            nickName    = dados.get("nickName")
            dataNasc    = dados.get("dataNasc")
            genero      = dados.get("genero")
            email       = dados.get("email")
            senha       = dados.get("senha")
            if  nome and dataNasc and genero and \
                email and senha:
                
                usuario = User(0, nome, nickName, dataNasc,genero,
                                      email, senha)

                if len(usuarioBD.consultar(id)) > 0:
                    usuarioBD.alterar(usuario)
                    return make_response(jsonify(
                        {
                            "status":"ok",
                            "mensagem":"Usuario alterado com sucesso!"
                        }
                    ))
                else:
                    return make_response(jsonify(
                        {
                            "status":"erro",
                            "mensagem":"Usuario não existe na base de dados!"
                        }
                    ))
        else:
            return make_response(jsonify({
                "status":"erro",
                "mensagem":"Especifique o id do Usuario que deseja alterar"
            }))
    else:#elif request.method == "DELETE":
        pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
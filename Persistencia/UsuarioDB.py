
from Modelo.Usuario import User
import sqlite3

caminhoBancoDados = './Persistencia/dados/BancoDeDados.bd'

class UsuarioBD():

    def __init__(self):
        self.__conexao = sqlite3.connect(caminhoBancoDados)
        with self.__conexao as con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS User(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    nickName TEXT NOT NULL,
                    dataNasc TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    email TEXT NOT NULL,
                    senha INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
                )
            """)
            con.commit()
    
    def incluir(self, usuario):
        if isinstance(usuario, User):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                INSERT INTO User (nome, nickName, dataNasc,
                genero, email, senha)
                VALUES (?,?,?,?,?,?)
                """,[usuario.nome, usuario.nickName,
                     usuario.dataNasc, usuario.genero,
                     usuario.email, usuario.senha])
                usuario.id = cursor.lastrowid
                con.commit()


    def alterar(self, usuario):
        if isinstance(usuario, User):
            with self.__conexao as con:
                con.execute("""
                    UPDATE User SET nome = ?,
                    nickName = ?, dataNasc = ?, genero =?, 
                    email = ?, senha = ?
                    WHERE id = ?
                """, [usuario.nome, usuario.nickName,
                     usuario.dataNasc, usuario.genero,
                     usuario.email, usuario.senha])
                con.commit()

    def excluir(self, usuario):
        if isinstance(usuario, User):
            with self.__conexao as con:
                con.execute("DELETE FROM User id = ?",
                [usuario.id])
                con.commit()

    def consultar(self, termoBusca):
        with self.__conexao as con:
            cursor = con.cursor()
            if isinstance(termoBusca, int):
                #consultar um User de código X
                cursor.execute("""
                SELECT id, nome, nickName, dataNasc,
                genero, email, senha FROM User 
                WHERE codigo = ?
                """,[termoBusca])
                resultado = cursor.fetchone()
                if resultado:
                    usuario = User(resultado[0], resultado[1],
                    resultado[2], resultado[3], resultado[4], resultado[5],
                    resultado[6])
                    return [usuario]    
                else:
                    return []
            elif isinstance(termoBusca,str):
                #consultar um User de nome Y
                cursor.execute("""
                           SELECT id, nome, nickName,
                           dataNasc, genero, email,
                           senha FROM User 
                           WHERE nome like ?
                """, ['%' + termoBusca + "%"])
                resultados = cursor.fetchall()
                if resultados:
                    listaUsers = []
                    for resultado in resultados:
                        usuario = User(resultado[0], resultado[1],
                        resultado[2], resultado[3], resultado[4], resultado[5],
                        resultado[6])
                        listaUsers.append(usuario)
                    return listaUsers
                else:
                    return []
            else:
                return []
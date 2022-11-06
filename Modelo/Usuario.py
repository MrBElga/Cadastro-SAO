class User():
    def __init__(self, id=0, nome="", nickName="",
                        dataNasc="", genero="", email="",
                        senha=""):
        self.__id=id
        self.__nome=nome
        self.__nickName=nickName
        self.__dataNasc=dataNasc
        self.__genero=genero
        self.__email=email
        self.__senha=senha
    
    #get
    @property
    def id(self):
        return self.__id
    
    #set
    @id.setter
    def id(self, novoId):
        self.__id=novoId


    #get
    @property
    def nome(self):
        return self.__nome
    
    #set
    @nome.setter
    def nome(self,novoNome):
        self.__nome=novoNome
    
    #get
    @property
    def nickName(self):
        return self.__nickName
    
    #set
    @nickName.setter
    def nickName(self,novoNickName):
        self.__nickName=novoNickName

    #get
    @property
    def dataNasc(self):
        return self.__dataNasc
    
    #set
    @id.setter
    def dataNasc(self,novoData):
        self.__dataNasc=novoData

    #get
    @property
    def genero(self):
        return self.__genero
    
    #set
    @genero.setter
    def genero(self,novoGenero):
        self.__genero=novoGenero

    #get
    @property
    def email(self):
        return self.__email
    
    #set
    @email.setter
    def email(self,novoEmail):
        self.__email=novoEmail
    
    #get
    @property
    def senha(self):
        return self.__senha
    
    #set
    @senha.setter
    def senha(self,novoSenha):
        self.__senha=novoSenha

    def toJSON(self):
        return {
                    "id"             : self.__id,
                    "nome"           : self.__numeroPassaporte,
                    "nickName"       : self.__nome,
                    "dataNasc"       : self.__dataNasc,
                    "genero"         : self.__genero,
                    "email"          : self.__email,
                    "senha"          : self.__senha
                }   
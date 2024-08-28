class Cadastro:
    def __init__(self ,nome ,idade ,sexo , telefone ,endereco):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.telefone = telefone
        self.endereco = endereco

        def __str__(self):
            return f' seu nome: {self.nome} sua idade: {self.idade} seu sexo: {self.sexo} seu email: {self.email} seu telefone: {self.telefone} seu endereco: {self.endereco}'
        
        cad1 = Cadastro ('Daniel',17,'nasc','daniel@gmail.com','41 99999-8888','rua:84')
        print(cad1)
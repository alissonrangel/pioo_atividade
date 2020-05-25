class Pessoa:
    # pass
    ''' 
    # as variaveis são declaradas no construtor
    nome = ""
    cpf = ""
    data_nascimento = ""
    '''
    def __init__(self, nome, data_nascimento, idade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.idade = idade
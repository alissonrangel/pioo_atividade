class Pessoa:

    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf        
        self.contas = []

    def mostrar_nome(self):
        print("Nome: ",self.nome)
        
    def mostrar_data_nascimento(self):
        print("Data de nascimento: ", self.data_nascimento)

    def mostrar_cpf(self):
        print("CPF: ",self.cpf)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        print("**************CONTAS*************")
        for conta in self.contas:
            print(conta.nome, " - ",conta.tipo, " - valor: R$", conta.valor, " - vencimento:", conta.data_vencimento)
        print("************FIM CONTAS***********")
    
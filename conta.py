class Conta:
    def __init__(self, nome, tipo, data_vencimento, valor):
        self.nome = nome
        self.tipo = tipo
        self.data_vencimento = data_vencimento
        self.valor = valor

    def nome_da_pessoa(self):
        if (self.tipo == "a pagar"):
            print("Credor: ", self.nome)
        else:
            print("Devedor: ", self.nome)
            
    def tipo_de_conta(self):
        print("Tipo: ", self.tipo)
    
    def mostrar_data_vencimento(self):
        print("Data do vencimento: ", self.data_vencimento)

    def valor_da_conta(self):
        print("Valor: R$", self.valor)
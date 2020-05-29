from pessoa import Pessoa
from conta import Conta

p1 = Pessoa("Alisson","07/04/1983", "123.456.789-12")

c1 = Conta("Carlos","a receber","25/05/2020", 250.00)
print("Dados da C1")
c1.nome_da_pessoa()
c1.tipo_de_conta()
c1.valor_da_conta()
c1.mostrar_data_vencimento()

c2 = Conta("Isac","a pagar","26/05/2020", 150.00)
print("\n\nDados da C2")
c2.nome_da_pessoa()
c2.tipo_de_conta()
c2.valor_da_conta()
c2.mostrar_data_vencimento()

c3 = Conta("Rodrigo","a receber","28/05/2020", 450.00)
print("\n\nDados da C3")
c3.nome_da_pessoa()
c3.tipo_de_conta()
c3.valor_da_conta()
c3.mostrar_data_vencimento()

p1.adicionar_conta(c1)
p1.adicionar_conta(c2)
p1.adicionar_conta(c3)
print("\n\nDados da P1")
p1.mostrar_nome()
p1.mostrar_cpf()
p1.mostrar_data_nascimento()
p1.listar_contas()


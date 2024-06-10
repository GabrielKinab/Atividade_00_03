# 1) Criando a Classe de Pessoa
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f"Pessoa: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}"

    def aniversario(self):
        self.idade += 1

    @property
    
    def saudacao(self):
        if self.profissao == "Médico":
            return f"Olá Bem Vindo Dr. {self.nome}"
        elif self.profissao == "Professor":
            return f"Olá Bem Vindo Prof. {self.nome}"
        else:
            return f"Olá Bem Vindo {self.nome}, como vai?"

# 2) Criando uma Classezinha da ContaBancaria
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo
        self.ativo = False

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self._saldo}"

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print("Não Aceito: Pufavor coloque um numero positivo.")

# 3) Criando uma Classe para o ClienteBanco
class ClienteBanco:
    def __init__(self, nome, idade, profissao, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.endereco = endereco
        self.telefone = telefone

    @classmethod
    def conta(cls):
        return ContaBancaria("Titular", 1040)

# Testando as classes

# 1) Pessoa
pessoa = Pessoa("Roberto Kenlirck tarto", 32, "Programador")
print(pessoa)
print(pessoa.saudacao)
pessoa.aniversario()
print(pessoa)

# 2) ContaBancaria
conta1 = ContaBancaria("Elisabete Alzélia Clara", 1644)
conta2 = ContaBancaria("Lorenzo Malbec", 1510)
conta3 = ContaBancaria("Maicom Leandro", 2190)
conta4 = ContaBancaria("Evelin Franciéle", 1364)
print(conta1)
print(conta2)
print(conta3)
print(conta4)

ContaBancaria.ativar_conta(conta1)
print("Conta ativa:", conta1.ativo)

# 3) ClienteBanco
cliente1 = ClienteBanco("Catarina Lisama", 28, "Designer", "Rua Avenida Franciolo Cascal, 152", "99469-0348",)
cliente2 = ClienteBanco("Móta Moreira ", 32, "Médico", "Rua Liério Consck, 566", "9977-0626",)
cliente3 = ClienteBanco("Ana", 33, "Professor", "Rua Celtinho Almugueiro, 149", "9953-0418",)

print(cliente1.nome, cliente1.idade, cliente1.profissao)
print(cliente2.nome, cliente2.idade, cliente2.profissao)
print(cliente3.nome, cliente3.idade, cliente3.profissao)

# 4) Método de classe para a conta ClienteBanco
conta_cliente = ClienteBanco.conta()
print(conta_cliente)

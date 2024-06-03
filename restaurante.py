class Restaurante:
    
    categoria = None

    def __init__(self, nome, categoria):
       
        self.nome = nome
       
        self.categoria = categoria
       
        self.ativo = False

# 1) Atribuindo o valor 'Italiana' ao atributo categoria da instância restaurante_praca

restaurante_praca = Restaurante('Nome do Restaurante', 'Categoria do Restaurante')

# 2) Acessando o valor do atributo nome da instância restaurante_praca

nome_do_restaurante = restaurante_praca.nome

# 3) Verificando o valor inicial do atributo ativo e exibindo uma mensagem

if restaurante_praca.ativo:
  
    print("O restaurante está ativo.")
else:
  
    print("O restaurante está em desenvolvimento.")

# 4) Acessando o valor do atributo de classe categoria pela classe Restaurante

categoria = Restaurante.categoria

# 5) Mudando o valor do atributo nome para u 'Bistrô'

restaurante_praca.nome = 'Bistrô'

# 6) Criando uma nova instância da classe Restaurante chamada restaurante_pizza

restaurante_pizza = Restaurante('Pizza Place', 'Fast Food')

# 7) Verificando se a categoria da instância restaurante_pizza é 'Fast Food'

if restaurante_pizza.categoria == 'Fast Food':
  
    print("A categoria da instância restaurante_pizza é 'Fast Food'.")

# 8) Mudando o estado da instância restaurante_pizza para ativo

restaurante_pizza.ativo = True

# 9) Imprimindo no console o nome e a categoria da instância do restaurante_praca

print(restaurante_praca.nome, restaurante_praca.categoria)

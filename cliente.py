class Cliente:

    # Construtor + Atributos

    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

        # Métodos - ações

    def imprimir(self): 
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

        
     
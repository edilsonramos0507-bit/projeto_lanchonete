class Produto:

    def __init__(self, cod, desc, categoria, preco):
        self.codigo=cod
        self.descricao=desc
        self.categoria=categoria
        self.preco=preco

    def imprimir(self):
         print(f"\n|----------- Produto cód. {self.codigo}-------------|")
         f"\n|Descrição: {self.descricao}                   |"
         f"\n|Tipo: {self.categoria}                        |"
         f"\n|Preço: R$ {self.preco:.2f}               |"
         f"\n|-------------------------------------------------------|"
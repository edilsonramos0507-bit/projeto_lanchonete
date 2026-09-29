import os
from cliente import Cliente
from produto import Produto
from itemPedido import ItemPedido
from pedido import Pedido
 
os.system("cls")
 
#Cadastrar Cliente
novoCli = Cliente(nome="João",
                 endereco="Rua boa, nº00", telefone="67 (+55) 7265-1233")
 
#Cadastrar Produto
siri = Produto(cod=1,desc="Hámburger de Siri", categoria="Lanche",
               preco=20.55)
refri = Produto(cod=2, desc="Tubaina", categoria="Bebidas",
                preco=5.6)
 
novoCli.imprimir()
siri.imprimir
refri.imprimir()
 
#Pedido
item1 = ItemPedido(produto=siri, obs="Cebola extra", qtd=2, desconto=2)
item2 = ItemPedido(produto=refri, obs="", qtd=2, desconto=0)

itens = [item1, item2]

pedido = Pedido (cliente=novoCli, data="14.02.2030", hora="19:40", itemPedido=itens, num="67 (+55) 7265-1233", pagamento="Cartão")
pedido.imprimir()
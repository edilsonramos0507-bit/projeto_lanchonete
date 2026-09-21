from pedido import Pedido 

from cliente import Cliente
#criar um objeto - representar um elemento - dar valores 
#novoPedido = Pedido(1, "14/09/2026", "21:10", "Rafael",
                    #["X-Salada", "X-Bacon"], "Pix")

##### Oque eu posso fazer com o objeto #####
#acessar um atributo 
#print(novoPedido.num)
#print(novoPedido.status)
#alterar os dados de um atributo 
#novoPedido.cliente="Rafael Martins"
#print(novoPedido.cliente)

#chamando os metodos 
#novoPedido.imprimir()
#novoPedido.atualizar_pedido("Em preparação")

#acessar o id - private
#novoPedido.__Num=2
#print(novoPedido.__num) #acessar
#novoPedido.imprimir()

#print(novoPedido.getNum())
#novoPedido.setNum(2)
#print(novoPedido.getNum())

#novoPedido.setIten("X-Calabresa")
#novoPedido.imprimir()


novoCliente = Cliente(endereco="Rua Vital Brasil",nome="Raniele",
                      telefone="67 9 9999-5588")

novoCliente.imprimir()
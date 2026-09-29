class Pedido:
    status = "Recebido"
 
    def __init__(self, num, data, hora, cliente, itemPedido, pagamento):
        self.num = num
        self.data = data
        self.hora = hora
        self.cliente = cliente
        self.__itemPedido = itemPedido
        self.pagamento = pagamento
 
    def atualizarPedido(self, novoStatus):
        self.status = novoStatus
 
    def imprimir(self):
        print(f"\n|--------- Pedido nº {self.num} ----------|"
              f"\n|Data: {self.data}                        |"
              f"\n|Horário: {self.hora}                     |"
              f"\n|Cliente: {self.cliente.nome}             |"
              f"\n||"
              f"\n|Método de Pagamento: {self.pagamento}    |"
              f"\n|Endereço: {self.cliente.endereco}        |"
              f"\n|Telefone: {self.cliente.telefone}        |"
              f"\n|Status: {self.status}                    |"
              f"\n|-----------------------------------------|")
        for item in self.__itemPedido:
            print(f"\nProduto: {item.produto.descricao} - Qtd: {item.quantidade} - Total: {item.totalItem()}")
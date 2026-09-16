class Pedido:
    #não define os atributos
    status="Recebido"

    #Método construtor  - instancia recebe os valor do objeto
    def __init__(self, num, data, hora, cliente, itens, pag):
        #self é chamar atributos;
        self.__num=num#private - não ser acessado bem alterado por outra classses 
        self.data=data#publico - pode ser acessado e alterado por outras classes 
        self.hora=hora
        self.cliente=cliente
        self.__itens=itens
        self.pagamento=pag

        #método - ação 
    def atualizar_pedido(self, novoStatus):     
            self.status=novoStatus

    def imprimir(self):
        print(f"\n------------------- Pedido N° {self.num} --------------------"
                f"\nData: {self.data} - Horário: {self.hora} "
                f"\nCliente: {self.cliente}")

     #encapsulamento
    def setNum(self, numero): #setado-alterado indiretamente pois num é privado 
            self.__num=numero

    def getMum(self): #acessar a informação de variavel private
            return self.num

    def setiten(self, item): #controla as informações 
            self.__iten.appen(item)

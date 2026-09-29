# 🍔 Projeto lanchonete 
Nesse projeto eu estou aprendendo o back end de um site de uma lanchonete com o professor Rafael do curso de **Técnico de desenvolvimento de software** do **SENAC** da turma de 2025.50.05

## ➡️ como rodar o projeto ##
1. Instale na versão mais recente do python
2. Faça git clone https://github.com/edilsonramos0507-bit/projeto_lanchonete.git
3. Abra a pasta do projeto e abra no VS code:
    - Digite CMD na barra de endereço do MS Explore;
    - Digite cODE . no terminal;
4. Abr o arquivo Main.py e clique em executar; 

## 🔎 Entendendo as classes ##
#criar um objeto - representar um elemento - dar valores 
#novoPedido = Pedido(1, "14/09/2026", "21:10", "Rafael",
                    #["X-Salada", "X-Bacon"], "Pix")

## Oque eu posso fazer com o objeto ##
```python
criar um objeto - representar um elemento - dar valores 
novoPedido = Pedido(1, "14/09/2026", "21:10", "Rafael",
                    ["X-Salada", "X-Bacon"], "Pix")

#### Oque eu posso fazer com o objeto #####
acessar um atributo 
print(novoPedido.num)
print(novoPedido.status)
alterar os dados de um atributo 
novoPedido.cliente="Rafael Martins"
print(novoPedido.cliente)

chamando os metodos 
novoPedido.imprimir()
novoPedido.atualizar_pedido("Em preparação")

acessar o id - private
novoPedido.__Num=2
print(novoPedido.__num) #acessar
novoPedido.imprimir()

print(novoPedido.getNum())
novoPedido.setNum(2)
print(novoPedido.getNum())

novoPedido.setIten("X-Calabresa")
novoPedido.imprimir()

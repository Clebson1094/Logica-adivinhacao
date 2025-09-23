from logica import caixa
from time import sleep

caixa1 = caixa()

print("Bem vindo ao caixa do supermercado")

while True:
    codigo = int(input("Digite o código do produto (ou 0 para finalizar a compra): "))

    if codigo == 0:
        print("Finalizando compra...")
        sleep(1)
        print(f"Valor total da compra: R$ {caixa1.valor_de_compra:.2f}")
        valor_pago = float(input("Digite o valor pago pelo cliente: R$ "))
        troco = caixa1.troco(valor_pago)
        print(f"Troco: R$ {troco:.2f}" if troco else "Sem troco")
        print(f"Valor atual no caixa: R$ {caixa1.valor_inicial_do_caixa:.2f}")
        print("Volte sempre!")
        break

    produto = caixa1.passar_produto(codigo)

    if produto:
        print(f"Produto: {produto['NOME']} - Valor: R$ {produto['VALOR']}")
        caixa1.valor_de_compra += produto["VALOR"]
        caixa1.listar_produtos()
        print(f"Valor parcial da compra: R$ {caixa1.valor_de_compra:.2f}")
        continue

    else:
        print("Produto não encontrado")
        nome = input("Digite o nome do produto: ")
        valor = float(input("Digite o valor do produto: "))
        caixa1.cadastrar_produtos(nome, valor)
        print("Produto cadastrado com sucesso")
        continue
from random import randint

class Box:
    def __init__(self):
        self.produtos = [
            {
                "NOME": "LARANJA",
                "VALOR": 2.58,
                "CODIGO": 699545554744154
            }
        ]
        self.quantidade_produtos = {}
        self.valor_de_compra = 0
        self.valor_inicial_do_caixa = 220

    def to_generate_code(self):
        return randint(100000000000000, 999999999999999)

    def register_product(self, nome, valor, codigo=None):
        if codigo is None:
            codigo = self.to_generate_codeo()

        self.produtos.append({
            "NOME": nome,
            "VALOR":valor,
            "CODIGO": codigo
        })
        print(f"Produto {nome} cadastrado com código: {codigo}")

    def check_product(self, codigo):
        for produto in self.produtos:
            if codigo == produto["CODIGO"]:
                if produto["NOME"] in self.quantidade_produtos:
                    self.quantidade_produtos[produto["NOME"]] += 1
                else:
                    self.quantidade_produtos[produto["NOME"]] = 1
                return produto
        return None

    def list_product(self):
        for produto in self.produtos:
            quantidade = self.quantidade_produtos.get(produto["NOME"], 0)
            if quantidade > 0:
                print(f"Quantidade: {quantidade} - Produto: {produto['NOME']} - Valor: R$ {produto['VALOR']}")
            else:
                pass

    def change(self, valor_pago):
        if valor_pago < self.valor_de_compra:
            pass
        elif valor_pago == self.valor_de_compra:
            self.valor_de_compra = 0
            self.quantidade_produtos = {}
        else:
            troco = valor_pago - self.valor_de_compra
            self.valor_de_compra = 0
            self.quantidade_produtos = {}
            self.valor_inicial_do_caixa += valor_pago
            self.valor_inicial_do_caixa -= troco
            return troco
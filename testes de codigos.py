def deposito(carteira):
    while True:
        try:
            deposito = float(input("Digite o valor de deposito"))
            if deposito <= 0:
                print("Não é aceito deposito zerado ou negativo")
                continue
            else:
                print("Prestou")
                carteira += deposito
                return carteira
        except ValueError:
            print("Coloque o valor em números por favor!")
            continue

saldo = 0

saldo = deposito(saldo)

print(saldo)
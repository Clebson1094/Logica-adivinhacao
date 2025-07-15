import os
nome = input("Digite seu nome")


with open("Ranking.txt", "a+") as f:
    f.write(f"{nome}\n")
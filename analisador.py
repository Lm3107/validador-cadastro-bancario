import csv

arquivo = "movimentacoes.csv"

total_entrada = 0
total_saida = 0
maior = 0

with open(arquivo, newline="", encoding="utf-8") as f:
    leitor = csv.DictReader(f)

    for linha in leitor:
        valor = float(linha["valor"])
        tipo = linha["tipo"]

        if valor > maior:
            maior = valor

        if tipo == "entrada":
            total_entrada += valor
        else:
            total_saida += valor


saldo = total_entrada - total_saida

print("Resumo das movimentações")
print("Entradas:", total_entrada)
print("Saídas:", total_saida)
print("Saldo:", saldo)
print("Maior valor:", maior)

if maior >= 10000:
    print("Atenção: movimentação alta detectada")

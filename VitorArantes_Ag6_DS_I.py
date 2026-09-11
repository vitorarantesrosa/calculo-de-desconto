# input inicial
compra = float(input("Qual o valor da compra em R$? "))

# variável para cálculo do desconto
desconto = 0

# separador
print("============================================")

# identação
if compra < 200:
    desconto = 0.05
    print ("Você ganhou um desconto de 5%!")
elif compra >= 200 and compra <= 300:
    desconto = 0.10
    print ("Você ganhou um desconto de 10%!")
elif compra > 300:
    print ("Você ganhou um desconto de 15%!")
    desconto = 0.15

# separador
print("============================================")

# processamento
calculo = compra * desconto
valorfinal = compra - calculo

# mensagem final
print(f"O valor a pagar é R${valorfinal:.2f}")

# separador
print("============================================")

# mensagem para finalizar o programa e deixar os resultados anteriores à mostra
input("Digite ENTER para encerrar o programa.")

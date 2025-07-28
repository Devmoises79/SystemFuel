def abastecer(preco_litro):
    try:
        valor_reais = float(input("Digite o valor em reais (R$): "))
        litros = valor_reais / preco_litro
        print(f"Você receberá {litros:.2f} litros.\n")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.\n")

def calcular_viagem(preco_litro):
    try:
        distancia = float(input("Distância da viagem (em km): "))
        consumo = float(input("Consumo médio do veículo (km/l): "))
        litros_necessarios = distancia / consumo
        custo_estimado = litros_necessarios * preco_litro
        print(f"Você precisará de {litros_necessarios:.2f} litros.")
        print(f"Custo estimado: R$ {custo_estimado:.2f}\n")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.\n")

def menu_feedback():
    print("\n====== AVALIAÇÃO DO SERVIÇO ======")
    print("1 - Péssimo 😠")
    print("2 - Ruim 😕")
    print("3 - Regular 😐")
    print("4 - Bom 🙂")
    print("5 - Excelente 😄")
    try:
        nota = int(input("Como você avalia o atendimento? (1 a 5): "))
        if 1 <= nota <= 5:
            print("Obrigado pelo seu feedback!\n")
        else:
            print("Nota inválida. Por favor, insira um número de 1 a 5.\n")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.\n")

def menu_principal():
    preco_litro = 5.49
    while True:
        print("\n====== MENU COMBUSTÍVEL ======")
        print("1 - Abastecer por valor")
        print("2 - Calcular média de viagem")
        print("3 - Avaliar atendimento")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            abastecer(preco_litro)
        elif opcao == "2":
            calcular_viagem(preco_litro)
        elif opcao == "3":
            menu_feedback()
        elif opcao == "0":
            print("\nSistema finalizado. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar sistema
menu_principal()

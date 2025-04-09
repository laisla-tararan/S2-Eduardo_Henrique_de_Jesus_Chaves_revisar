def mostrar_menu():
    print("\n🐾 Bem-vindo ao PetShop da Vilma 🐾")
    print("1 - Banho 🛁 - R$30")
    print("2 - Tosa ✂️ - R$40")
    print("3 - Consulta 🩺 - R$100")
    print("4 - Vacina 💉 - R$80")
    print("5 - Finalizar e pagar")
    print("6 - Sair sem pagar 😅")

def calcular_total(servicos):
    total = 0
    for s in servicos:
        if s == "1":
            total += 30
        elif s == "2":
            total += 40
        elif s == "3":
            total += 100
        elif s == "4":
            total += 80
    return total

def nome_pet():
    nome = input("Qual o nome do seu pet? ")
    print("Show! Vamos cuidar bem do", nome)
    return nome

def processar_servicos():
    carrinho = []
    while True:
        mostrar_menu()
        escolha = input("Escolha um serviço (1 a 6): ")

        if escolha == "5":
            if len(carrinho) > 0:
                total = calcular_total(carrinho)
                print(f"\nServiços escolhidos: {len(carrinho)}")
                print(f"Total a pagar: R${total}")
                print("Valeu por confiar no PetShop da Vilma! 🐶✨")
            else:
                print("Você não escolheu nada ainda, ué 😅")
            break
        elif escolha == "6":
            print("Saindo... Volta quando quiser 🐾")
            break
        elif escolha in ["1", "2", "3", "4"]:
            carrinho.append(escolha)
            print("Serviço adicionado com sucesso ✅")
        else:
            print("Opção inválida! Tenta de novo...")

def petshop():
    print("🐾🐾 PETSHOP DA VILMA 🐾🐾")
    nome_pet()
    processar_servicos()

# roda o programa
petshop()
def calculadora() :
    while True:
        print ("Selecione a operaçao desejada")
        print ("1. Soma")
        print ("2. Subtraçao")
        print ("3. Multiplicaçao")
        print ("4. Divisao")
        print ("5. Sair")

        escolha = input("Digite o numero da operaçao desejada: ")

        if escolha == '5':
            print("Obrigado por usar a calculadora do marcin")
            break

        elif escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))

            if escolha == '1':
                print("Resultado:", num1 + num2)
            elif escolha == '2':
                print("Resultado", num1 - num2)
            elif escolha == '3':
                print("Resultado", num1 * num2)
            elif escolha == '4':
                if num2 != 0:
                    print("Resultado:", num1 / num2)
                else:
                    print("Erro! Divisao por zero.")
        else:
            print("Escolha invalida. Tente Novamente")



# Chamada da funçao principal
calculadora()

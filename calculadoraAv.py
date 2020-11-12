# Dicionário se receber como operador, retorna a seguinte equação com o numerador e denominador que receber
operadores = {
    "+": lambda op1, op2: op1 + op2,
    "-": lambda op1, op2: op1 - op2,
    "*": lambda op1, op2: op1 * op2,
    "/": lambda op1, op2: op1 / op2
}

# Função que recebe a lista e calcula de acordo com o operador


def conta(texto, operador):
    # Inicia o indice em 0
    indice = 0
    # Pula uma linha
    print("")
    # While se indice for menor que o tamannho da lista
    while indice < len(texto):
        # Se item da lista, texto[indice], for o operador especificado entra no if
        if texto[indice] == operador:
            # Variavel resultado recebe o resultado do seguinte dicionário:
            # Dicionário recebe o operador e o compara em usa lista,
            resultado = operadores[texto[indice]](
                # Dicionário recebe o numero anterior do operador e posterior, operador = texto[indice], numero anterior = texto[indice - 1] e posterior = texto[indice + 1]
                # Converte o valor em float para poder fazer a operação no dicionário
                float(texto[indice - 1]), float(texto[indice + 1]))
            # Valor anterior ao operador recebe resultado
            texto[indice - 1] = resultado
            # Operador é excluido na lista
            del texto[indice]
            # O número posterior, agr atual após a exclusão do operador, também é excluido
            del texto[indice]
            # Indice retorna a 0 paraprocurar mais ocorrencias do Operador
            indice = 0
        # Se item da lista, texto[indice], não for o operador especificado faz indice + 1
        indice += 1
    # Print da lista depois de todas as ocorrencias do operador
    print(texto)
    #retorna a lista agora calculada
    return texto

# Função para separa os números(1, 2, 3..) e operadores(+, -, *, /) em uma lista


def separador(texto):
    # Lista de operadores
    operador = ("(", ")", "+", "-", "*", "/")

    # For para colocar um espaço antes e depois dos operadores
    # For x em operador
    for x in operador:
        # Texto recebido do Input, troca os operadores por eles mesmos mais um espaço antes e depois e salva nele mesmo
        texto = texto.replace(x, " " + x + " ")
    # Transforma o texto em uma lista, usando como base de corte os espaços
    texto = texto.split(" ")

    # Printa para ver como ficou a lista
    print(texto)

    # Código antigo
    """
    numero = ""
    operador_atual = ""
    indice = 0
    resultado = 0
    for x in texto:
        if x != "+" and x != "-" and x != "*" and x != "/" and numero != "":
            resultado = operadores[operador_atual](float(numero), float(x))
            print(resultado)
            numero = resultado
        elif x != "+" and x != "-" and x != "*" and x != "/":
            numero = x
            print (numero)
        else:
            operador_atual = x
    """
    # Faz o texto entrar na função para rebeber ele mesmo após fazer todas as contas do operador especificado
    texto = conta(texto, "*")
    texto = conta(texto, "/")
    texto = conta(texto, "+")
    texto = conta(texto, "-")
    # Pula uma linha
    print("")
    # Exibe o resultado
    print(texto)
    # Retorna o resultado
    return texto


# Saída(Função (Entrada(Print da pergunta)))
print(separador(input("Digite a equação: ")))
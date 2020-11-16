contas = {
    "+": lambda op1, op2: op1 + op2,
    "-": lambda op1, op2: op1 - op2,
    "*": lambda op1, op2: op1 * op2,
    "/": lambda op1, op2: op1 / op2
}


operadores = ["*", "/"]
sinais = ["+", "-"]
parenteses = ["(", ")"]

operandos = operadores + sinais
prioridades = operadores + sinais + parenteses


def separador(texto):
    for x in prioridades:
        texto = texto.replace(x, " " + x + " ")
        texto = texto.replace("  ", " ")
    return texto.strip().split(" ")


def sinalizador(texto):
    indice = 1
    while indice < len(texto):
        if texto[indice] in sinais and texto[indice - 1] in sinais:
            if texto[indice] == texto[indice - 1]:
                texto[indice - 1] = "+"
                del texto[indice]
            else:
                texto[indice - 1] = "-"
                del texto[indice]
            indice = 1
            continue
        if texto[indice] in sinais and texto[indice - 1] in operadores:
            if texto[indice] == "+":
                del texto[indice]
            if texto[indice] == "-" and isinstance(texto[indice + 1], float):
                del texto[indice]
                texto[indice] *= -1
        if texto[0] == "+" and isinstance(texto[1], float):
            del texto[0]
            indice = 1
            continue
        if texto[0] == "-" and isinstance(texto[1], float):
            del texto[0]
            texto[0] *= -1
            indice = 1
            continue
        indice += 1
    return texto


def numerador(texto):
    indice = 0
    while indice < len(texto):
        if not texto[indice] in prioridades:
            texto[indice] = float(texto[indice])
        indice += 1
    return texto


def ordenador(texto):
    indice = len(texto) - 1
    while indice >= 0:
        if texto[indice] == "(":
            del texto[indice]
            texto[indice] = ordem(sinalizador(texto[indice:]))[0]
            indice += 1
            for x in texto[indice:]:
                if x == ")":
                    del texto[indice]
                    texto = sinalizador(texto)
                    break
                del texto[indice]
            indice = len(texto) - 1
        indice -= 1
    return texto


def conta(texto, operador):
    indice = 0
    while indice < len(texto):
        if indice != 0 and isinstance(texto[indice], float) and isinstance(texto[indice - 1], float):
            texto[indice - 1] = contas["*"](
                texto[indice - 1], texto[indice])
            del texto[indice]
            indice -= 1
            continue
        if texto[indice] == ")":
            if operador == "-":
                del texto[indice]
            break
        elif texto[indice] == operador:
            resultado = contas[texto[indice]](
                texto[indice - 1], texto[indice + 1])
            texto[indice - 1] = resultado
            del texto[indice]
            del texto[indice]
            indice -= 1
            continue
        indice += 1
    return texto


def ordem(texto):
    texto = conta(texto, "*")
    texto = conta(texto, "/")
    texto = conta(texto, "+")
    return conta(texto, "-")


def calculadoraAv(texto):
    texto = separador(texto)
    print("Pós separador:")
    print(texto)
    print("")

    texto = numerador(texto)
    print("Pós numerador")
    print(texto)
    print("")

    texto = sinalizador(texto)
    print("Pós sinalizador:")
    print(texto)
    print("")

    texto = ordenador(texto)
    print("Pós ordenador")
    print(texto)
    print("")
    
    print("Resposta: ")
    return ordem(texto)[0]


numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
valores = numeros + prioridades


def existe(texto):
    if texto == "":
        return False
    for caractere in texto:
        if not caractere in valores:
            return False
    return True


def decimal(texto):
    indice = 1
    while len(texto) > 2 and indice < len(texto):
        condicao = bool(texto[indice] == "." and (not texto[indice - 1] in numeros or texto[indice - 1]
            == "." or not texto[indice + 1] in numeros or texto[indice + 1] == "."))
        if condicao:
            return False
        indice += 1
    return True


def quantidade_de_parenteses(texto):
    abre_parenteses = 0
    fecha_parenteses = 0
    for caractere in texto:
        if caractere == "(":
            abre_parenteses += 1
        if caractere == ")":
            fecha_parenteses += 1
    if abre_parenteses != fecha_parenteses:
        return False
    return True


def ordem_dos_parenteses(texto):
    for caractere in texto:
        if caractere == "(":
            break
        elif caractere == ")":
            return False
    indice = len(texto) - 1
    while indice >= 0:
        if texto[indice] == ")":
            break
        elif texto[indice] == "(":
            return False
        indice -= 1
    return True


def ordem_dos_operandos(texto):
    indice = 1
    if texto[-1] in operandos:
        return False
    while indice < len(texto):
        condicao = bool((texto[indice] in operadores and (texto[indice - 1] in operandos or texto[indice - 1] == "("))
                        or (texto[indice] in operandos and (texto[indice + 1] in operadores or texto[indice + 1] == ")")))
        if condicao:
            return False
        indice += 1
    return True


def vazio(texto):
    indice = 0
    while indice < len(texto):
        if texto[indice] == ")" and (texto[indice - 1] == "(" or texto[indice - 1] in operandos):
            return False
        indice += 1
    return True


def verificacao(texto):
    print("")
    while True:
        condicao = bool(existe(texto) and decimal(texto) and quantidade_de_parenteses(
            texto) and ordem_dos_parenteses(texto) and ordem_dos_operandos(texto) and vazio(texto))
        if condicao:
            break
        print("Existe: " + str(existe(texto)) + ", Decimal válido: " + str(decimal(texto)) + ", Quantidade de parenteses iguais: " + str(quantidade_de_parenteses(
            texto)) + ", Ordem dos parênteses correta: " + str(ordem_dos_parenteses(texto)) + ", Ordem dos operadores correta: " + str(ordem_dos_operandos(texto)) + ", Não há parenteses vazios: " + str(vazio(texto)))
        print("")
        texto = input("Equação inválida, digite novamente: ")
    print("Existe: " + str(existe(texto)) + ", Decimal válido: " + str(decimal(texto)) + ", Quantidade de parenteses iguais: " + str(quantidade_de_parenteses(
        texto)) + ", Ordem dos parênteses correta: " + str(ordem_dos_parenteses(texto)) + ", Ordem dos operadores correta: " + str(ordem_dos_operandos(texto)) + ", Não há parenteses vazios: " + str(vazio(texto)))
    print("")
    return texto


print(calculadoraAv(verificacao(input("Digite a equação: "))))

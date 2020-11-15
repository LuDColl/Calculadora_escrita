contas = {
    "+": lambda op1, op2: op1 + op2,
    "-": lambda op1, op2: op1 - op2,
    "*": lambda op1, op2: op1 * op2,
    "/": lambda op1, op2: op1 / op2
}

operadores = ["(", ")", "+", "-", "*", "/"]


def conta(texto, operador):
    indice = 0
    while indice < len(texto):
        if indice != 0 and isinstance(texto[indice], float) and isinstance(texto[indice - 1], float):
            texto[indice - 1] = contas["*"](
                texto[indice - 1], texto[indice])
            del texto[indice]
            indice -= 1
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
        indice += 1
    return texto


def separador(texto):
    for x in operadores:
        texto = texto.replace(x, " " + x + " ")
        texto = texto.replace("  ", " ")
    return texto.strip().split(" ")


def numerador(texto):
    indice = 0
    while indice < len(texto):
        if not texto[indice] in operadores:
            texto[indice] = float(texto[indice])
        indice += 1
    return texto


def ordem(texto):
    texto = conta(texto, "*")
    texto = conta(texto, "/")
    texto = conta(texto, "+")
    return conta(texto, "-")


def aspas(texto):
    indice = len(texto) - 1
    while indice >= 0:
        if texto[indice] == "(":
            del texto[indice]
            texto[indice] = ordem(texto[indice:])[0]
            indice += 1
            for x in texto[indice:]:
                if x == ")":
                    del texto[indice]
                    break
                del texto[indice]
            indice = len(texto) - 1
        indice -= 1
    return texto


def calculadoraAv(texto):
    texto = separador(texto)
    texto = numerador(texto)
    texto = aspas(texto)
    return ordem(texto)[0]


equacao = input("Digite a equação: ")


numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
valores = numeros + operadores


def existe(texto):
    for caractere in texto:
        if not caractere in valores:
            return False
    return True


def decimal(texto):
    indice = 1
    while len(texto) > 2 and indice < len(texto):
        if texto[indice] == ".":
            if not texto[indice - 1] in numeros:
                return False
            elif texto[indice - 1] == ".":
                return False
            if not texto[indice + 1] in numeros:
                return False
            elif texto[indice + 1] == ".":
                return False
        indice += 1
    return True


def quantidade_de_parenteses(texto):
    abre_parenteses = 0
    fecha_parenteses = 0
    for caractere in texto:
        if caractere == "(":
            abre_parenteses += 1
    for caractere in texto:
        if caractere == ")":
            fecha_parenteses += 1
    if abre_parenteses != fecha_parenteses:
        return False
    return True


def ordem_dos_parenteses(texto):
    ordem = bool(0)
    for caractere in texto:
        if caractere == "(":
            ordem = 1
            break
        elif caractere == ")":
            return False
    indice = len(texto) - 1
    while indice >= 0:
        if texto[indice] == ")":
            ordem = 1
            break
        elif texto[indice] == "(":
            return False
        indice -= 1
    return ordem


def vazio(texto):
    indice = 1
    while len(texto) > 1 and indice < len(texto):
        if texto[indice - 1] == "(":
            if texto[indice] in operadores:
                if texto[indice] != "(":
                    return False
        indice += 1
    return True


def verificacao(texto):
    while True:
        if existe(texto) and decimal(texto) and quantidade_de_parenteses(texto) and ordem_dos_parenteses(texto) and vazio(texto):
            break
        texto = input("Equação inválida, digite novamente: ")
    return texto


print(calculadoraAv(verificacao(equacao)))

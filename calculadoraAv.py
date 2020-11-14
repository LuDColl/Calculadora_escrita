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


numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
valores = numeros + operadores


def verificacao(equacao):
    indice = 0
    abre_parenteses = 0
    fecha_parenteses = 0
    while indice < len(equacao):
        if not equacao[indice] in valores:
            equacao = input("Equação inválida, digite novamente: ")
            indice = 0
        if equacao[indice] == "(":
            abre_parenteses += 1
        if equacao[indice] == ")":
            fecha_parenteses += 1
        indice += 1
    if abre_parenteses != fecha_parenteses:
        equacao = input("Equação inválida, digite novamente: ")
        indice = 0
    return equacao


print(calculadoraAv(verificacao(equacao)))

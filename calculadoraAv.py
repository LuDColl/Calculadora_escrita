contas = {
    "+": lambda op1, op2: op1 + op2,
    "-": lambda op1, op2: op1 - op2,
    "*": lambda op1, op2: op1 * op2,
    "/": lambda op1, op2: op1 / op2
}

operadores = ["(", ")", "+", "-", "*", "/"]


def conta(texto, operador):
    indice = 0
    print("")
    while indice < len(texto):
        if texto[indice] == operador:
            resultado = contas[texto[indice]](
                texto[indice - 1], texto[indice + 1])
            texto[indice - 1] = resultado
            del texto[indice]
            del texto[indice]
            indice = 0
        indice += 1
    print(texto)
    return texto


def separador(texto):
    for x in operadores:
        texto = texto.replace(x, " " + x + " ")
    return texto.split(" ")


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


def calculadoraAv(texto):
    texto = separador(texto)
    texto = numerador(texto)
    return ordem(texto)


equacao = input("Digite a equação: ")

indice = 0
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
valores = numeros + operadores

while indice < len(equacao):
    if not equacao[indice] in valores:
        equacao = input("Equação inválida, digite novamente: ")
        indice = 0
    indice += 1

print(calculadoraAv(equacao))

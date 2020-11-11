operadores = {
    "+": lambda op1, op2: op1 + op2,
    "-": lambda op1, op2: op1 - op2,
    "*": lambda op1, op2: op1 * op2,
    "/": lambda op1, op2: op1 / op2
}

def conta(texto, operador):
    indice = 0
    print("")
    while indice < len(texto):
        if texto[indice] == operador:
            resultado = operadores[texto[indice]](float(texto[indice - 1]), float(texto[indice + 1]))
            texto[indice - 1] = resultado
            del texto[indice]
            del texto[indice]
            indice = 0
        indice += 1
    print(texto)
    return texto

def separador(texto):
    operador = ("(", ")", "+", "-", "*", "/")
    numero = ""
    operador_atual = ""
    indice = 0
    resultado = 0
    for x in operador:
        texto = texto.replace(x, " " + x + " ")
    texto = texto.split(" ")
    print (texto)


    """
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
    texto = conta(texto, "*")
    texto = conta(texto, "/")
    texto = conta(texto, "+")
    texto = conta(texto, "-")
    print ("")
    print(texto)
    return texto

print(separador(input("Digite a equação: ")))

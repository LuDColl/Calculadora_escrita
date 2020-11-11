operadores = {
    "+": lambda op1, op2: op1 + op2,
    "-": lambda op1, op2: op1 - op2,
    "*": lambda op1, op2: op1 * op2,
    "/": lambda op1, op2: op1 / op2
}


def separador(texto):
    operador = ("(", ")", "+", "-", "*", "/")
    numero = ""
    operador_atual = ""
    indice = 0
    for x in operador:
        texto = texto.replace(x, " " + x + " ")
    texto = texto.split(" ")
    for x in texto:
        print(x)


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
    for x in texto:
        if x == "*":
            resultado = operadores[x](float(texto[indice - 1]), float(texto[indice + 1]))
            texto[indice - 1] = resultado
            del texto[indice]
            del texto[indice]
            indice -= 1
        indice += 1
    for x in texto:
        print(x)
    return resultado

print(separador(input("Digite a equação: ")))

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
    for x in operador:
        texto = texto.replace(x, " " + x + " ")
    texto = texto.split(" ")
    for x in texto:
        print(x)
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
    return resultado

print(separador(input("Digite a equação: ")))
# Kernel do algorítimo
contas = {
    "+": lambda op1, op2: op1 + op2,
    "*": lambda op1, op2: op1 * op2,
    "/": lambda op1, op2: op1 / op2
}

# Todas as listas
sinais = ["+", "-"]
operadores = ["*", "/"]
parenteses = ["(", ")"]
parenteses_com_operandos = [
    ")" + x for x in (operadores)] + [
    x + "(" for x in (sinais + operadores)]
prioridades = parenteses + operadores + sinais
numeros = [str(x) for x in range(10)]
valores = numeros + prioridades


# Funções Booleanas
def eh_um_numero(valor):
    if isinstance(valor, float):
        return True
    else:
        return False


# Funções
def tirar_espacos_duplos(texto):
    while "  " in texto:
        texto = texto.replace("  ", " ")
    return texto

print(prioridades)
def separador(texto):
    for prioridade in prioridades:
        texto = texto.replace(prioridade, " " + prioridade + " ")
    return tirar_espacos_duplos(texto).strip().split(" ")


def juntador(texto): return "".join(texto)


def numerador(lista):
    for indice in range(len(lista)):
        if not lista[indice] in prioridades:
            lista[indice] = float(lista[indice])
    return lista


def sinalizador(texto):
    sinais_juntos = [primeiro +
                     segundo for primeiro in sinais for segundo in sinais]
    for sinal_junto in sinais_juntos:
        while sinal_junto in texto:
            if sinal_junto[0] == sinal_junto[1]:
                texto = texto.replace(sinal_junto, " ")
            else:
                texto = texto.replace(sinal_junto, "-")
    texto = numerador(separador(texto))
    for indice in range(len(texto)):
        anterior_eh_negativo = texto[indice - 1] == "-"
        if eh_um_numero(texto[indice]) and anterior_eh_negativo:
            texto[indice] *= -1
            del texto[indice - 1]
    return texto


def deletador_de_parenteses(valor_lateral):
    if eh_um_numero(valor_lateral):
        return "*"
    else:
        return valor_lateral


def ordenador(lista):
    for indice in range(len(lista) - 1, - 1, - 1):
        if lista[indice] == "(":
            for indice_final in range(len(lista[indice + 1:])):
                if lista[indice_final] == ")":
                    lista[indice + 1] = ordem(
                        sinalizador(lista[indice + 1:indice_final - 1]))
                    del lista[indice + 1:indice_final - 1]
                    if indice + 1 == len(lista) - 1 or not(
                        eh_um_numero(lista[indice + 1])):
                        del lista[indice + 1]
                    break
    return lista


def conta(texto, operador):
    indice = 0
    while indice < len(texto):
        nao_eh_o_primeiro = indice != 0
        eh_um_numero = isinstance(texto[indice], float)
        anterior_eh_um_numero = isinstance(
            texto[indice - 1], float)
        soma = nao_eh_o_primeiro and eh_um_numero and anterior_eh_um_numero
        if soma:
            texto[indice - 1] = contas["+"](
                texto[indice - 1], texto[indice])
            del texto[indice]
            indice -= 1
            continue
        elif texto[indice] == operador:
            eh_parenteses = operador == "(" or operador == ")"
            eh_o_ultimo = indice == len(texto) - 1
            if eh_parenteses and eh_o_ultimo:
                del texto[indice]
                break
            elif eh_parenteses:
                texto[indice] = "*"
            texto[indice - 1] = contas[texto[indice]](
                texto[indice - 1], texto[indice + 1])
            del texto[indice]
            del texto[indice]
            indice -= 1
            continue
        indice += 1
    return texto


def ordem(texto):
    texto = conta(texto, "*")
    texto = conta(texto, "(")
    texto = conta(texto, ")")
    texto = conta(texto, "/")
    texto = conta(texto, "+")
    return conta(texto, "-")


def calculadoraAv(texto):
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


print(calculadoraAv(input("Digite a equação: ")))

"""
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
        print("F")
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
"""

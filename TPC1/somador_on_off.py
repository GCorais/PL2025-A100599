def somador_on_off(sequencia):
    soma = 0
    i = 0
    active = True
    resultado = ""

    while i < len(sequencia):
        if sequencia[i].lower() == "o":
            if sequencia[i+1].lower() == "f" and sequencia[i+2].lower() == "f":
                active = False
                i += 3
                continue
            elif sequencia[i+1].lower() == "n":
                active = True
                i += 2
                continue
        elif i < len(sequencia) and sequencia[i].isdigit():
            num = ""
            while sequencia[i].isdigit():
                num += sequencia[i]
                i += 1
            if active:
                soma += int(num)
            continue
        elif sequencia[i] == "=":
            resultado += str(soma) + "\n"
        i += 1
    return resultado

if __name__ == "__main__":
    with open("data.txt", "r", encoding="utf-8") as file:
        linhas = file.readlines()

    for linha in linhas:
        linha = linha.strip()
        if linha:
            resultado = somador_on_off(linha)
            print(resultado)
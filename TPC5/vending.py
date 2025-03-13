import json
from datetime import datetime

def carregar_stock(ficheiro="stock.json"):
    try:
        with open(ficheiro, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_stock(stock, ficheiro="stock.json"):
    with open(ficheiro, "w") as f:
        json.dump(stock, f, indent=4)

def listar_produtos(stock):
    print("maq:\n cod | nome | quantidade | preço")
    print("---------------------------------")
    for produto in stock:
        print(f"{produto['cod']}    {produto['nome']}   {produto['quant']}  {produto['preco']}€")

def formatar_saldo(saldo):
    euros = saldo // 100
    centimos = saldo % 100
    return f"{euros}e{centimos}c" if euros > 0 else f"{centimos}c"

def inserir_moeda(saldo, moedas):
    valores = {"1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}
    for moeda in moedas:
        moeda = moeda.lower().strip()
        if moeda in valores:
            saldo += valores[moeda]
        else:
            print(f"Moeda inválida ignorada: {moeda}")
    return saldo

def selecionar_produto(stock, saldo, codigo):
    for produto in stock:
        if produto["cod"] == codigo:
            if produto["quant"] > 0:
                if saldo >= int(produto["preco"] * 100):
                    produto["quant"] -= 1
                    saldo -= int(produto["preco"] * 100)
                    print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
                else:
                    print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                    print(f"maq: Saldo = {formatar_saldo(saldo)}; Pedido = {formatar_saldo(int(produto['preco'] * 100))}")
            else:
                print("maq: Produto esgotado")
            return saldo
    print("maq: Produto inexistente")
    return saldo

def calcular_troco(saldo):
    moedas = {"1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}
    troco = {}
    for moeda, valor in moedas.items():
        quantidade = saldo // valor
        if quantidade > 0:
            troco[moeda] = quantidade
            saldo -= quantidade * valor
    return ", ".join([f"{v}x {k}" for k, v in troco.items()])

def adicionar_produto(stock, codigo, nome, quantidade, preco):
    produto_existente = next((p for p in stock if p["cod"] == codigo), None)
    if produto_existente:
        produto_existente["quant"] += quantidade
        print(f"maq: Produto '{produto_existente['nome']}' atualizado. Nova quantidade: {produto_existente['quant']}")
    else:
        stock.append({"cod": codigo, "nome": nome, "quant": quantidade, "preco": preco})
        print(f"maq: Produto '{nome}' adicionado com sucesso.")
    guardar_stock(stock)
    return stock


def main():
    stock = carregar_stock()
    print(f"maq: {datetime.today().date()}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    saldo = 0
    while True:
        comando = input(">> ").strip()
        partes = comando.split(" ")
        if partes[0].upper() == "LISTAR":
            listar_produtos(stock)
        elif partes[0].upper() == "MOEDA":
            moedas = comando[6:].replace(".", "").split(", ")
            saldo = inserir_moeda(saldo, moedas)
            print(f"maq: Saldo = {formatar_saldo(saldo)}")
        elif partes[0].upper() == "SELECIONAR":
            if len(partes) > 1:
                saldo = selecionar_produto(stock, saldo, partes[1])
                print(f"maq: Saldo = {formatar_saldo(saldo)}")
            else:
                print("maq: Código do produto não especificado.")
        elif partes[0].upper() == "ADICIONAR":
            try:
                if len(partes) < 5:
                    raise ValueError
                codigo = partes[1]
                quantidade = int(partes[-2])
                preco = float(partes[-1])
                nome = " ".join(partes[2:-2])  # Junta o nome corretamente
                stock = adicionar_produto(stock, codigo, nome, quantidade, preco)
            except ValueError:
                print("maq: Comando inválido. Use: ADICIONAR <código> <nome> <quantidade> <preço>")
        elif partes[0].upper() == "SAIR":
            troco = calcular_troco(saldo)
            if troco:
                print(f"maq: Pode retirar o troco: {troco}")
            print("maq: Até à próxima")
            guardar_stock(stock)
            break
        else:
            print("maq: Comando inválido")


if __name__ == "__main__":
    main()
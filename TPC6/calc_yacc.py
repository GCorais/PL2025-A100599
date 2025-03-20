import ply.yacc as yacc

from calc_lex import tokens

def p_operacao_1(p):
    "operacao : calc"
    p[0] = p[1]

def p_operacao_2(p):
    "operacao : operacao ADD calc"
    p[0] = p[1] + p[3]

def p_operacao_3(p):
    "operacao : operacao SUB calc"
    p[0] = p[1] - p[3]

def p_calc_1(p):
    "calc : expressao"
    p[0] = p[1] 

def p_calc_2(p):
    "calc : calc DIV expressao"
    p[0] = p[1] / p[3]

def p_calc_3(p):
    "calc : calc MULT expressao"
    p[0] = p[1] * p[3]

def p_expressao_1(p):
    "expressao : NUMBER"
    p[0] = p[1]

def p_expressao(p):
    "expressao : AP operacao FP"
    p[0] = p[2]

def p_error(p):
    print("Erro sintático no input!")

parser = yacc.yacc()

with open("input.txt", "r") as f:
    linhas = f.readlines()

with open("output.txt", "w") as f_out:
    for linha in linhas:
        linha = linha.strip()
        if linha:
            r = parser.parse(linha)
            resultado = f"Expressão: {linha} => Resultado: {r}\n"
            f_out.write(resultado)
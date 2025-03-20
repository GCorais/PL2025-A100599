# TPC6: Analisador Sintático
- 📅 **Data**: 20/03/2025
- 👤 **Aluno**: Gonçalo Antunes Corais, A100599
<img src="../foto.jpeg" alt="Fotografia" width="200"/>

## Resumo

O código desenvolvido tem como objetivo criar um analisador sintático capaz de realizar cálculos matemáticos. Para tal recorremos às tokens do analisador léxico criado em `calc_lex.py` para, depois, o analisador sintático criado em `calc_yacc.py` calcular as seguintes operações:

- Soma
- Subtração
- Multiplicação
- Divisão

## Resultados

Criei o ficheiro `input.txt` com alguns exemplos de expressões matemáticas e, após executarmos o comando `python3 calc_yacc.py`, os resultados dessas expressões irão aparecer no ficheiro `output.txt`. Alguns exemplos de expressões e resultados são os seguintes:

```
Expressão: 3 + 5 => Resultado: 8
Expressão: 10 - 2 * 4 => Resultado: 2
Expressão: 15 / (3 + 2) => Resultado: 3.0
Expressão: 18 / (3 * (2 + 1)) => Resultado: 2.0
```
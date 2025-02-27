# TPC3: Conversor de MarkDown para HTML
- 📅 **Data**: 27/02/2025
- 👤 **Aluno**: Gonçalo Antunes Corais, A100599
<img src="../foto.jpeg" alt="Fotografia" width="200"/>

## Resumo

O código desenvolvido tem como objetivo criar um conversor de Markdown para HTML em Python para os elementos descritos na "Basic Syntax" da Cheat Sheet como títulos (#, ##, ...), listas, imagens, etc.

## Resultados

Para obter os resultados é necessário correr o comando `python3 conversor.py` no terminal e, de seguida, vai ser pedido um texto em Markdown. Após colocar o texto, é preciso clicar no Enter duas vezes e o resultado em HTML irá aparecer no ficheiro [resultados.txt](resultados.txt). Por exemplo, após correr o comando acima e colocarmos como input o seguinte:

```
1. Primeiro
2. Segundo
3. Terceiro
```

O resultado que aparece em [resultados.txt](resultados.txt) vai ser:

```
<ol>
<li>Primeiro</li>
<li>Segundo</li>
<li>Terceiro</li>
</ol>
```
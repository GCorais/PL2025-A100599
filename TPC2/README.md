# TPC2: Análise de um dataset de obras musicais
- 📅 **Data**: 20/02/2025
- 👤 **Aluno**: Gonçalo Antunes Corais, A100599
<img src="../foto.jpeg" alt="Fotografia" width="200"/>

## Resumo

O código desenvolvido tem como objetivo, sem usar o módulo CSV do python, ler um dataset, processá-lo e obter os seguintes resultados:

- Listar ordenada alfabeticamente dos compositores musicais;
- Distribuição das obras por período: quantas obras catalogadas em cada período;
- Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras
desse período.

Para um busca eficiente dos dados usei a seguinte expressão regular:
 `r';(?=(?:[^"]*"[^"]*")*[^"]*$)'`

## Resultados

Para obter os resultados pretendidos é necessário correr o comando `python3 processador.py` no terminal. De seguida irá aparecer o ficheiro txt [resultados.txt](resultados.txt) onde aparecem os nomes dos compositores ordenados alfabeticamente, número de obras por período e, finalmente, a lista de obras por ordem alfabética por período
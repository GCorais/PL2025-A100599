# TPC4: Analisador Léxico
- 📅 **Data**: 27/02/2025
- 👤 **Aluno**: Gonçalo Antunes Corais, A100599
<img src="../foto.jpeg" alt="Fotografia" width="200"/>

## Resumo

O código desenvolvido tem como objetivo construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases utilizando a biblioteca `ply.lex` do python. No meu caso, as tokens definidas foram as seguintes:

- COMMENT
- SELECT
- VAR
- WHERE
- LIMIT
- STRING
- DOT
- AC
- FC
- NUMBER
- PREFIX_NAME
- A

## Resultados

Por exemplo, dada a seguinte frase:

```
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

Ao executar o comando `python3 analisador.py` vão aparecer os resultados seguintes no terminal:

```
LexToken(COMMENT,'# DBPedia: obras de Chuck Berry',2,1)
LexToken(SELECT,'select',4,34)
LexToken(VAR,'?nome',4,41)
LexToken(VAR,'?desc',4,47)
LexToken(WHERE,'where',4,53)
LexToken(AC,'{',4,59)
LexToken(VAR,'?s',5,65)
LexToken(A,'a',5,68)
LexToken(PREFIX_NAME,'dbo:MusicalArtist',5,70)
LexToken(DOT,'.',5,87)
LexToken(VAR,'?s',6,93)
LexToken(PREFIX_NAME,'foaf:name',6,96)
LexToken(STRING,'"Chuck Berry"@en',6,106)
LexToken(DOT,'.',6,123)
LexToken(VAR,'?w',7,129)
LexToken(PREFIX_NAME,'dbo:artist',7,132)
LexToken(VAR,'?s',7,143)
LexToken(DOT,'.',7,145)
LexToken(VAR,'?w',8,151)
LexToken(PREFIX_NAME,'foaf:name',8,154)
LexToken(VAR,'?nome',8,164)
LexToken(DOT,'.',8,169)
LexToken(VAR,'?w',9,175)
LexToken(PREFIX_NAME,'dbo:abstract',9,178)
LexToken(VAR,'?desc',9,191)
LexToken(FC,'}',10,197)
LexToken(LIMIT,'LIMIT',10,199)
LexToken(NUMBER,1000,10,205)
```
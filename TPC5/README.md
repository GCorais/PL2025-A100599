# TPC5: Máquina de Vending
- 📅 **Data**: 13/03/2025
- 👤 **Aluno**: Gonçalo Antunes Corais, A100599
<img src="../foto.jpeg" alt="Fotografia" width="200"/>

## Resumo

O código desenvolvido tem como objetivo o desenvolvimento de um código capaz de simular uma máquina de vending. Esta máquina vai ter um stock guardado em `stock.json` com o código, nome, quantidade e preço de cada produto que pode ser adquirido. Na máquina vão ser possíveis realizar as seguintes ações:

- LISTAR - para listar os produtos disponíveis
- ADICIONAR - para adicionar produtos sejam eles novos ou já existentes
- MOEDA - para o saldo
- SELECIONAR - para selecionar um produto e ele ser adquirido
- SAIR - sair da máquina devolvendo, caso exista, o troco

## Resultados

Aqui está um exemplo de uma simulação de compra de um produto na máquina de vending após executar o comando `python3 vending.py`.

```
maq: 2025-03-13, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR
maq:
 cod | nome | quantidade | preço
---------------------------------
A23    água 0.5L   11  0.7€
A10    Coca-Cola 0.5L   14  1.2€
>> MOEDA 1e, 20c, 5c, 5c .
maq: Saldo = 1e30c
>> SELECIONAR A23
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 60c
>> SELECIONAR A23
maq: Saldo insuficiente para satisfazer o seu pedido
maq: Saldo = 60c; Pedido = 70c
maq: Saldo = 60c
>> ADICIONAR A23 água 0.5L 6 0.7
maq: Produto 'água 0.5L' atualizado. Nova quantidade: 16
>> SAIR
maq: Pode retirar o troco: 1x 50c, 1x 10c
maq: Até à próxima
```
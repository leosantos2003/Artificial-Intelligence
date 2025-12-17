# T3 - Busca em Grafos (8-Puzzle) 

## 1. Identificação do Grupo
Bernardo Fellini Oliveira - 00323402 - Turna B

Vinícius Gross Castro - 00324541 - Turna B

Leonardo Rocha dos Santos	- 00341831 - Turna B

## 2. Bibliotecas Adicionais

Este trabalho utiliza apenas bibliotecas padrão do Python 3.12 (especificamente `heapq` e `itertools` que já vêm incluídas). Não é necessária a instalação de nenhuma biblioteca adicional.

## 3. Análise de Desempenho

A tabela abaixo detalha o desempenho dos algoritmos de busca A* para o estado inicial **"2_3541687"**, conforme solicitado no enunciado.

| Algoritmo | Nós Expandidos | Tempo Decorrido (s) | Custo da Solução (Ações) |
| :--- | :---: | :---: | :---: |
| `astar_hamming` | 13506 | 0.235481 | 23 |
| `astar_manhattan` | 1830 | 0.033321 | 23 |
# T3 - Graph Search (8-Puzzle)

## 1. Group Identification
Bernardo Fellini Oliveira - 00323402 - Turma B

Vinícius Gross Castro - 00324541 - Turma B

Leonardo Rocha dos Santos	- 00341831 - Turma B

## 2. Additional Libraries

This work uses only standard Python 3.12 libraries (specifically `heapq` and `itertools`, which are already included). No additional libraries need to be installed.

## 3. Performance Analysis

The table below details the performance of the A* search algorithms for the initial state **"2_3541687"**, as requested in the problem statement.

| Algorithm | Expanded Nodes | Time Elapsed (s) | Solution Cost (Stocks) |
| :--- | :---: | :---: | :---: |
| `astar_hamming` | 13506 | 0.235481 | 23 |
| `astar_manhattan` | 1830 | 0.033321 | 23 |
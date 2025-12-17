\# T4 \- Inteligência Artificial: Busca com Adversário

\*\*Agente:\*\* \`o\_cara\`

\#\# 1\. Identificação do Grupo  
Bernardo Fellini Oliveira \- 00323402 \- Turma B  
Vinícius Gross Castro \- 00324541 \- Turma B  
Leonardo Rocha dos Santos	\- 00341831 \- Turma B

\#\# 2\. Bibliotecas Adicionais

Este trabalho utiliza apenas bibliotecas padrão do Python 3 (especificamente \`math\` para \`inf\` no algoritmo minimax).

Não é necessária a instalação de nenhuma biblioteca adicional para a execução.

\#\# 3\. Avaliação da Poda Alfa-Beta (Tic-Tac-Toe Misere)

Conforme solicitado no item "a" da seção 2.2 do enunciado, foi realizada uma avaliação do desempenho do agente que escolhemos nomear como  \`o\_cara\` no Jogo da Velha Invertido. 

O algoritmo implementado foi o Minimax com poda alfa-beta e profundidade ilimitada (\`max\_depth \= \-1\`)

Os resultados dos testes manuais foram:

\*\*O minimax sempre ganha ou empata jogando contra o \`randomplayer\`?\*\*

\* \*\*Sim.\*\* Em testes executados contra o \`randomplayer\`, o agente \`o\_cara\` (jogando com a estratégia ótima) nunca perdeu. O resultado foi um empate, provando que o agente joga de forma a não cometer erros.

\*\*O minimax sempre empata consigo mesmo?\*\*  
\* \*\*Sim.\*\* Ao executar \`o\_cara\` (Pretas) contra \`o\_cara\` (Brancas), o resultado da partida foi um empate. Isso indica que ambos os agentes estão jogando a estratégia ótima, e o jogo termina com o tabuleiro cheio sem que nenhum jogador seja forçado a perder.

\*\*O minimax não perde para você quando você usa a sua melhor estratégia?\*\*  
\* \*\*Sim.\*\* O agente nunca perdeu para um jogador humano. Nos testes, houveram dois resultados:  
        1\.  O jogador humano cometeu um erro (alinhando três peças) e \*\*perdeu\*\* (o agente \`o\_cara\` venceu).  
        2\.  O jogador humano jogou com a melhor estratégia e a partida terminou em \*\*empate\*\*.

\---

\#\# 4\. Avaliação e Implementação (Othello)

Conforme solicitado no item “b” da seção 2.2 do enunciado, foi realizado um torneio entre os 3 algoritmos Minimax com heurísticas diferentes sendo usados pelo agente ‘o\_cara’. Cada algoritmo enfrentou cada outro 2 vezes, uma vez jogando primeiro e outra vez jogando por último.

Cada algoritmo Minimax foi executado com poda alfa-beta e profundidade fixa limitada de 5 níveis (a maior profundidade que não ultrapassou o limite estipulado de 5 segundos por jogada).

Nossa heurística customizada foi uma combinação das heurísticas de valor posicional e contagem de peças, em adição a mais duas heurísticas:

* **Heurística de Mobilidade Imediata:** considera estados em que o jogador possui mais jogadas legais do que o seu oponente como melhor. Quanto maior a diferença entre jogadas legais entre o jogador e o oponente, melhor o estado  
* **Heurística da Mobilidade Potencial:** considera estados em que as peças do adversário estão rodeadas de espaços em branco como melhores, pois representam estados em que o jogador provavelmente terá mais oportunidades de ataque futuramente.

Essa heurística customizada foi baseada a partir desses dois sites:  
[**http://home.datacomm.ch/t\_wolf/tw/misc/reversi/html/index.html**](http://home.datacomm.ch/t_wolf/tw/misc/reversi/html/index.html)  
[**https://www.cs.cornell.edu/\~yuli/othello/othello.html**](https://www.cs.cornell.edu/~yuli/othello/othello.html)  
Eles descrevem cada um, em alto nível, uma implementação de bot de Othello usando busca Minimax com poda alfa-beta e heurísticas, e afirmam que a mobilidade das peças no Othello é uma das melhores heurísticas a serem seguidas.  
Nossa principal diferença em questões heurísticas foi manter a heurística de contagem de peças com mesmo peso relativo comparado com as outras heurísticas, pois vimos no torneio que isso resultou no melhor resultado para nossa heurística customizada.

Os resultados do Torneio entre os algoritmos com heurísticas diferentes foram:

* Contagem de peças X Valor posicional:  
  Pontuação: **22 x 42**  
  Vitória: **Valor posicional**  
* Valor posicional X Contagem de peças:  
  Pontuação: **22 x 42**  
  Vitória: **Contagem de peças**  
* Contagem de peças X Heurística customizada:  
  Pontuação: **19 x 45**  
  Vitória: **Heurística customizada**  
* Heurística customizada X Contagem de peças:  
  Pontuação: **41 x 23**  
  Vitória: **Heurística customizada**  
* Valor posicional X Heurística customizada:  
  Pontuação: **20 x 44**  
  Vitória: **Heurística customizada**  
* Heurística customizada X Valor posicional:  
  Pontuação: **37 x 27**  
  Vitória: **Heurística customizada**


**Resultados finais:** 

1. Heurística customizada: **4 vitórias**  
2. Valor posicional e Contagem de peças: **1 Vitória cada (**peças capturadas iguais para as duas heurísticas**)**

Pelo resultado, claramente a heurística de maior sucesso foi a nossa customizada, que ganhou todas as suas partidas. Pelos resultados podemos assumir que o jogador que joga por último possui vantagem no jogo.


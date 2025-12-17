import random
from typing import Tuple
from ..tttm.gamestate import GameState
from ..tttm.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e também modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Retorna uma jogada calculada pelo algoritmo minimax para o estado de jogo fornecido.
    :param state: estado para fazer a jogada
    :return: tupla (int, int) com as coordenadas x, y da jogada (lembre-se: 0 é a primeira linha/coluna)
    """

    # Chama o minimax_move com profundidade ilimitada (-1) e
    # passa a função 'utility' deste arquivo como a função de avaliação.
    # O jogo é pequeno (max 9 jogadas), então a profundidade ilimitada é viável.
    return minimax_move(state, -1, utility)


def utility(state: GameState, player: str) -> float:
    """
    Retorna a utilidade de um estado terminal para o Jogo da Velha INVERTIDO.
    :param state: o estado terminal a ser avaliado.
    :param player: o jogador que iniciou a busca (o "eu" do minimax).
    """
    
    # Pega o vencedor do estado terminal.
    # O gamestate.py já lida com a lógica invertida:
    # 'state.winner()' retorna quem VENCEU (ou seja, quem NÃO alinhou 3).
    winner = state.winner()

    if winner == player:
        # Se o vencedor é o 'player' (nosso agente), é uma vitória.
        return 1.0
    elif winner is None:
        # Se não há vencedor (empate), utilidade é 0.
        return 0.0
    else:
        # Se o vencedor é o oponente, é uma derrota.
        return -1.0

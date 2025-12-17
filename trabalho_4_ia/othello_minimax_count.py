import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Importamos 'inf' para representar infinito (positivo e negativo)
from math import inf

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Retorna uma jogada calculada pelo algoritmo minimax para o estado de jogo fornecido.
    :param state: estado para fazer a jogada
    :return: tupla (int, int) com as coordenadas x, y da jogada (lembre-se: 0 é a primeira linha/coluna)
    """

    # chama o minimax_move com profundidade limitada pela constante MAX_DEPTH  e
    # passa a função 'evaluate_count' deste arquivo como a função de avaliação.
    # Como o jogo possui máximo de 64 jogadas, busca ilimitada é inviável

    MAX_DEPTH = 5
    return minimax_move(state, MAX_DEPTH, evaluate_count)


def evaluate_count(state: GameState, player: str) -> float:
    """
    Avalia um estado de Othello a partir do ponto de vista de um dado jogador. 
    Se o estado é terminal, retorna a utilidade do estado. 
    Senão, retorna uma estimativa de seu valor baseado na heurística de contagem de peças.
    :param state: estado a ser avalizado (instancia de GameState)
    :param player: jogador para qual o estado será avaliado (B or W)
    :return: float representando a pontuação do estado
    """
    board = state.get_board()
    opponent =  board.opponent(player)

    if not state.is_terminal():
        return board.num_pieces(player) - board.num_pieces(opponent)
    
    winner = state.winner()

    # Pelas regras do Othello, a pontuação do vencedor é: (o total de peças da cor do vencedor) + (o total de espaços vazios no tabuleiro no estado final).
    if winner == player:
        return board.num_pieces(player) + board.num_pieces(board.EMPTY)
    else:
        return board.num_pieces(opponent) + board.num_pieces(board.EMPTY)
    

    


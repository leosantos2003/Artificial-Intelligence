import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

# mask template adjusted from https://web.fe.up.pt/~eol/IA/MIA0203/trabalhos/Damas_Othelo/Docs/Eval.html
# could optimize for symmetries but just put all values here for coding speed :P
# DO NOT CHANGE! 
EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100]
]


def make_move(state) -> Tuple[int, int]:
    """
    Retorna uma jogada calculada pelo algoritmo minimax para o estado de jogo fornecido.

    :param state: estado para fazer a jogada
    :return: tupla (int, int) com as coordenadas x, y da jogada (lembre-se: 0 é a primeira linha/coluna)
    """

    # chama o minimax_move com profundidade limitada pela constante MAX_DEPTH  e
    # passa a função 'evaluate_count' deste arquivo como a função de avaliação.
    # Como o jogo possui máximo de 64 jogadas, busca ilimitada é inviável

    MAX_DEPTH = 5
    return minimax_move(state, MAX_DEPTH, evaluate_mask)

def evaluate_mask(state: GameState, player: str) -> float:
    """
    Avalia um estado de Othello a partir do ponto de vista de um dado jogador. 
    Se o estado é terminal, retorna a utilidade do estado. 
    Senão, retorna uma estimativa de seu valor baseado na heurística do valor posicional das peças.
    Você deve usar o EVAL_TEMPLATE acima para computar o valor posicional das peças

    :param state: estado a ser avalizado (instancia de GameState)
    :param player: jogador para qual o estado será avaliado (B or W)
    :return: float representando a pontuação do estado
    """
    board = state.get_board()
    opponent =  board.opponent(player)

    if state.is_terminal():
        winner = state.winner()

        # Pelas regras do Othello, a pontuação do vencedor é: (o total de peças da cor do vencedor) + (o total de espaços vazios no tabuleiro no estado final).
        if winner == player:
            return board.num_pieces(player) + board.num_pieces(board.EMPTY)
        else:
            return board.num_pieces(opponent) + board.num_pieces(board.EMPTY)

    player_score = 0
    opponent_score = 0

    for i, row in enumerate(board.tiles):
        for j, tile in enumerate(row):
            if tile == player:
                player_score += EVAL_TEMPLATE[i][j]
            elif tile == opponent:
                opponent_score += EVAL_TEMPLATE[i][j]

    return player_score - opponent_score



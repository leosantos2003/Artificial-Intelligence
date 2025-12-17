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


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Retorna uma jogada calculada pelo algoritmo minimax para o estado de jogo fornecido.

    :param state: estado para fazer a jogada
    :return: tupla (int, int) com as coordenadas x, y da jogada (lembre-se: 0 é a primeira linha/coluna)
    """
    # chama o minimax_move com profundidade limitada pela constante MAX_DEPTH  e
    # passa a função 'evaluate_custom' deste arquivo como a função de avaliação.
    # Como o jogo possui máximo de 64 jogadas, busca ilimitada é inviável

    MAX_DEPTH = 5
    return minimax_move(state, MAX_DEPTH, evaluate_custom)

def count_other_color_empty_adjacencies(board: Board, y: int, x: int) -> int:
    """
    Conta os espaços vazios adjacentes a uma posição do tabuleiro nas coordenadas x,y.
    Essa posição terá uma peça do oponente, e a quantidade de espaços vazios ao seu redor
    sugerem uma possibilidade maior de realizar capturas significativas no futuro,
    já que teremos mais opções de capturas.
    Obs: linhas e colunas no tabuleiro e na matriz são invertidas. 

    :param board: configuração do tabuleiro considerando o estado atual da função "evaluate_custom" 
    :param y: índice da linha/matriz <-> coluna/tabuleiro da posição cujas posições adjacentes serão analisadas
    :param x: índice da coluna/matriz <-> linha/tabuleiro da posição cujas posições adjacentes serão analisadas
    :return: int entre 0-4 que conta quantos espaços adjacentes à posição analisada estão vazios
    """
    result = 0
    if board.is_within_bounds((x-1,y)):
        if board.tiles[x-1][y] == board.EMPTY:
            result += 1
    if board.is_within_bounds((x+1,y)):
        if board.tiles[x+1][y] == board.EMPTY:
            result += 1
    if board.is_within_bounds((x,y-1)):
        if board.tiles[x][y-1] == board.EMPTY:
            result += 1
    if board.is_within_bounds((x,y+1)):
        if board.tiles[x][y+1] == board.EMPTY:
            result += 1
    
    return result

def evaluate_custom(state: GameState, player:str) -> float:
    """
    Avalia um estado de Othello a partir do ponto de vista de um dado jogador. 
    Se o estado é terminal, retorna a utilidade do estado. 
    Senão, retorna uma estimativa de seu valor baseado em uma heurística customizada.
    Essa heurística combina a heurística do do valor posicional das peças e a de contagem de peças com duas outras:
    A heurística de maximizar opções de jogadas para o jogador e minimizar jogadas para o oponente,
    e a heurística de maximizar a mobilidade futura do jogador ao buscar estados em que peças do oponente
    estejam adjacentes a espaços vazios.

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
        
    player_positional_score = 0
    opponent_positional_score = 0
    potential_mobility = 0

    for i, row in enumerate(board.tiles):
        for j, tile in enumerate(row):
            if tile == player:
                player_positional_score += EVAL_TEMPLATE[i][j]
            elif tile == opponent:
                # Considera a mobilidade potencial.
                # Quanto maior o total de espaços vazios ao redor das peças do oponente,
                # maiores as chances de realizar capturas melhores futuramente.
                potential_mobility += count_other_color_empty_adjacencies(board, i, j)
                opponent_positional_score += EVAL_TEMPLATE[i][j]

    # A heurística do valor posicional das peças é muito poderosa para não ser usada,
    # mesmo comparando com todas as outras heurísticas vistas combinadas
    positional_score = player_positional_score - opponent_positional_score

    # Considera a mobilidade imediata do jogador em relação a do seu oponente neste estado.
    # Quanto maior a diferença de jogadas legais, mais escolhas o jogador terá, o que resulta numa maior
    # probabilidade de ter jogadas boas em estados futuros.
    legal_move_score = len(board.legal_moves(player)) - len(board.legal_moves(opponent))

    # Heurítica da Contagem de peças. 
    # Quanto maior a diferença entre o total de peças do jogador comparado com o total de peças do oponente, melhor a posição.
    # Sem usar essa heurísitca esse algoritmo performa ainda melhor contra a heurísitca do valor posicional sozinha,
    # mas acaba perdendo contra a de contagem de peças sozinha.
    count_score = board.num_pieces(player) - board.num_pieces(opponent)
        
    return positional_score + legal_move_score + potential_mobility + count_score

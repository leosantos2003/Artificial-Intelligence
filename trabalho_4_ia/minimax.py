import random
from typing import Tuple, Callable

# Importamos 'inf' para representar infinito (positivo e negativo)
from math import inf

# ------------------------------------------------------------------
# FUNÇÕES AUXILIARES _max_value E _min_value
# ------------------------------------------------------------------
# Estas são as funções recursivas que implementam a poda alfa-beta.
# Note que 'player' aqui é o JOGADOR RAIZ (quem iniciou a busca),
# para que a função de avaliação (eval_func) saiba de qual 
# perspectiva avaliar o estado.

def _max_value(state, depth: int, max_depth: int, eval_func: Callable, player: str, alpha: float, beta: float):
    """
    Função do jogador MAX (quem quer maximizar o score).
    """
    # Condição de parada: profundidade máxima atingida ou estado terminal
    if (max_depth != -1 and depth == max_depth) or state.is_terminal():
        return eval_func(state, player)

    v = -inf
    # A classe GameState garante que o 'player' em next_state é alternado em tttm.
    for move in state.legal_moves():
        next_state = state.next_state(move)

        # Em Othello, pode ser o caso que o mesmo jogador jogue mais de uma vez seguida caso o oponente não tenha jogadas legais no próximo estado.
        # Nesse caso, chamamos novamente a função _max_value pois a próxima jogada também será feita com o objetivo de maximizar o score
        # Não é necessário tratar casos em que nenhum jogador tem jogadas legais pois nesse caso entramos num estado terminal e calcularemos
        # o resultado final do jogo não importa se chamarmos _max_value ou _min_value 
        if next_state.player == state.player:
            v = max(v, _max_value(next_state, depth + 1, max_depth, eval_func, player, alpha, beta))
        else:
            v = max(v, _min_value(next_state, depth + 1, max_depth, eval_func, player, alpha, beta))
        
        # Poda Alfa-Beta
        if v >= beta:
            return v
        alpha = max(alpha, v)
    
    return v


def _min_value(state, depth: int, max_depth: int, eval_func: Callable, player: str, alpha: float, beta: float):
    """
    Função do jogador MIN (quem quer minimizar o score).
    """
    # Condição de parada: profundidade máxima atingida ou estado terminal
    if (max_depth != -1 and depth == max_depth) or state.is_terminal():
        return eval_func(state, player)

    v = inf

    # Cada sucessor aqui será uma jogada de MAX.
    for move in state.legal_moves():
        next_state = state.next_state(move)
        
        # Em Othello, pode ser o caso que o mesmo jogador jogue mais de uma vez seguida caso o oponente não tenha jogadas legais no próximo estado.
        # Nesse caso, chamamos novamente a função _min_value pois a próxima jogada também será feita com o objetivo de minimizar o score.
        # Não é necessário tratar casos em que nenhum jogador tem jogadas legais pois nesse caso entramos num estado terminal e calcularemos
        # o resultado final do jogo não importa se chamarmos _min_value ou _max_value 
        if next_state.player == state.player:
            v = min(v, _min_value(next_state, depth + 1, max_depth, eval_func, player, alpha, beta))
        else:
            v = min(v, _max_value(next_state, depth + 1, max_depth, eval_func, player, alpha, beta))
        
        # Poda Alfa-Beta
        if v <= alpha:
            return v
        beta = min(beta, v)
    
    return v

# ------------------------------------------------------------------
# FUNÇÃO PRINCIPAL
# ------------------------------------------------------------------

def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:
    """
    Retorna uma jogada calculada pelo algoritmo minimax com poda alfa-beta.
    :param state: estado para fazer a jogada (instância de GameState)
    :param max_depth: profundidade máxima de busca (-1 = ilimitada)
    :param eval_func: a função para avaliar um estado terminal ou folha
    :return: tupla (int, int) com as coordenadas x, y da jogada
    """
    
    # Obtém o jogador que está fazendo a jogada (o jogador RAIZ)
    player = state.player
    
    # Pega todas as jogadas legais
    moves = state.legal_moves()
    if not moves:
        return None  # Não há jogadas possíveis

    best_move = None
    best_score = -inf
    alpha = -inf
    beta = inf
    
    # A profundidade inicial é 0
    current_depth = 0

    # Itera sobre todas as jogadas legais no nível raiz
    # O nó raiz é MAX. Cada jogada leva a um estado que será avaliado por MIN.
    for move in moves:
        next_state = state.next_state(move)
        
        # Chama _min_value para o oponente
        score = _min_value(next_state, current_depth + 1, max_depth, eval_func, player, alpha, beta)
        
        # Atualiza a melhor jogada encontrada
        if score > best_score:
            best_score = score
            best_move = move
        
        # Atualiza o alfa (melhor valor para MAX até agora)
        alpha = max(alpha, best_score)
        
    return best_move

from typing import Iterable, Set, Tuple

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai:Nodo, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        raise NotImplementedError


def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    def swap_chars(s: str, i: int, j: int) -> str:
        """Função auxiliar para trocar caracteres nos índices i e j."""
        lst = list(s)
        lst[i], lst[j] = lst[j], lst[i]
        return "".join(lst)

    sucessores = set()
    pos_vazio = estado.find('_')

    # Ações representam o movimento do espaço vazio 
    # O grid é 3x3 (índices 0-8)

    # Mover 'acima' (espaço vazio sobe)
    # Não pode estar na primeira linha (índices 0, 1, 2)
    if pos_vazio > 2:  
        novo_estado = swap_chars(estado, pos_vazio, pos_vazio - 3)
        sucessores.add(("acima", novo_estado))

    # Mover 'abaixo' (espaço vazio desce)
    # Não pode estar na última linha (índices 6, 7, 8)
    if pos_vazio < 6:  
        novo_estado = swap_chars(estado, pos_vazio, pos_vazio + 3)
        sucessores.add(("abaixo", novo_estado))

    # Mover 'esquerda' (espaço vazio vai para a esquerda)
    # Não pode estar na primeira coluna (índices 0, 3, 6)
    if pos_vazio % 3 > 0:  
        novo_estado = swap_chars(estado, pos_vazio, pos_vazio - 1)
        sucessores.add(("esquerda", novo_estado))

    # Mover 'direita' (espaço vazio vai para a direita)
    # Não pode estar na última coluna (índices 2, 5, 8)
    if pos_vazio % 3 < 2:  
        novo_estado = swap_chars(estado, pos_vazio, pos_vazio + 1)
        sucessores.add(("direita", novo_estado))

    return sucessores


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

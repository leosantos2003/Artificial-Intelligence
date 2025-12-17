from typing import Iterable, Set, Tuple
import heapq, itertools

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai:'Nodo', acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def __eq__(self, other):
        """
        Define que dois nodos são iguais se os seus estados forem iguais.
        Isso é útil para verificar se um estado já está em um conjunto (set) 
        ou dicionário (dict). 
        """
        if isinstance(other, Nodo):
            return self.estado == other.estado
        return False

    def __hash__(self):
        """
        Define o hash do nodo como o hash de seu estado.
        Isso permite que nodos sejam adicionados a conjuntos (sets) 
        ou usados como chaves em dicionários (dicts). 
        """
        return hash(self.estado)
    
    # Opcional: um método de representação para facilitar a depuração (debug)
    def __repr__(self):
        """
        Retorna uma representação em string do nodo.
        """
        return f"Nodo(estado='{self.estado}', acao='{self.acao}', custo={self.custo})"


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
    conjunto_sucessores = set()
    
    # Chama a função sucessor com o estado do nodo atual
    tuplas_sucessores = sucessor(nodo.estado) 
    
    # Para cada (ação, estado_seguinte) retornado
    for acao, novo_estado in tuplas_sucessores:
        # Cria um novo nodo
        # O pai é o nodo atual
        # O custo é o custo do nodo atual + 1
        novo_nodo = Nodo(
            estado=novo_estado,
            pai=nodo,
            acao=acao,
            custo=nodo.custo + 1
        )
        # Adiciona o novo nodo ao conjunto
        conjunto_sucessores.add(novo_nodo)
            
    return conjunto_sucessores

OBJETIVO = "12345678_"

# --- Funções Auxiliares para o A* ---

# Pré-calcula a posição (linha, coluna) de cada peça no estado objetivo
# Isso acelera o cálculo da heurística Manhattan
GOAL_POS = {tile: (i // 3, i % 3) for i, tile in enumerate(OBJETIVO)}

def h_hamming(estado: str) -> int:
    """
    Heurística de Hamming: número de peças fora do lugar.
    """
    dist = 0
    for i in range(len(estado)):
        # Ignora o espaço vazio '_'
        if estado[i] != '_' and estado[i] != OBJETIVO[i]:
            dist += 1
    return dist

def h_manhattan(estado: str) -> int:
    """
    Heurística de Manhattan: soma das distâncias (em linhas + colunas)
    de cada peça até sua posição correta.
    """
    dist_total = 0
    for i in range(len(estado)):
        tile = estado[i]
        if tile != '_':
            # Posição atual da peça
            atual_row, atual_col = i // 3, i % 3
            # Posição objetivo da peça (pré-calculada)
            goal_row, goal_col = GOAL_POS[tile]
            
            # Distância de Manhattan
            dist_total += abs(atual_row - goal_row) + abs(atual_col - goal_col)
    return dist_total

def is_solvable(estado: str) -> bool:
    """
    Verifica se um estado do 8-puzzle tem solução.
    Um estado só tem solução se o número de inversões for par
    (assumindo que o objetivo "12345678_" tem 0 inversões).
    """
    estado_sem_vazio = estado.replace('_', '')
    inversoes = 0
    for i in range(len(estado_sem_vazio)):
        for j in range(i + 1, len(estado_sem_vazio)):
            # Se uma peça maior vem antes de uma menor
            if estado_sem_vazio[i] > estado_sem_vazio[j]:
                inversoes += 1
    
    # Se o número de inversões for par, é solucionável.
    return inversoes % 2 == 0

def construir_caminho(nodo_final: Nodo) -> list[str]:
    """
    Refaz o caminho do nodo final até o inicial, coletando as ações.
    """
    acoes = []
    nodo_atual = nodo_final
    # Volta pelos pais até chegar no nodo raiz (pai=None)
    while nodo_atual.pai is not None:
        acoes.append(nodo_atual.acao)
        nodo_atual = nodo_atual.pai
    
    # As ações foram adicionadas da última para a primeira,
    # então precisamos inverter a lista.
    acoes.reverse()
    return acoes

def a_star_search(estado_inicial: str, heuristica) -> list[str]:
    """
    Implementação genérica do algoritmo A* (conforme pseudocódigo).
    :param estado_inicial: str, estado inicial
    :param heuristica: function, a função heurística (h_hamming ou h_manhattan)
    :return: lista de ações ou None
    """
    
    # Se o estado não tem solução, retorna None (conforme enunciado)
    if not is_solvable(estado_inicial):
        return None

    # Se o estado inicial já é o objetivo, retorna lista vazia (conforme enunciado)
    if estado_inicial == OBJETIVO:
        return []

    nodo_inicial = Nodo(estado=estado_inicial, pai=None, acao=None, custo=0)
    
    # Fronteira (F): Fila de prioridades (min-heap)
    # Armazena tuplas: (f_custo, contador, nodo)
    # f_custo = g + h = nodo.custo + heuristica(nodo.estado)
    # 'contador' é para desempate (tie-breaker), caso dois nodos tenham o mesmo f_custo
    fronteira_heap = []
    contador = itertools.count()
    
    h_inicial = heuristica(nodo_inicial.estado)
    f_inicial = nodo_inicial.custo + h_inicial # g=0
    
    heapq.heappush(fronteira_heap, (f_inicial, next(contador), nodo_inicial))
    
    # Explorados (X): Conjunto de estados (strings) já visitados
    explorados = set() 

    while fronteira_heap: # loop: se F = ø: retornar FALHA
        
        # Retira o nodo 'v' com menor 'f' da fronteira
        f_v, _, v = heapq.heappop(fronteira_heap)

        # se v ∈ X: (se já exploramos este *estado*, pulamos)
        if v.estado in explorados:
            continue

        # se v é o objetivo: retornar caminho s-v
        if v.estado == OBJETIVO:
            return construir_caminho(v)

        # Insere v em X
        explorados.add(v.estado)

        # Expande o nodo 'v'
        # Cria Node 'u' pra cada vizinho de 'v'
        for u in expande(v):
            
            # se u ∉ X: (se o estado sucessor 'u' *não* foi explorado)
            if u.estado not in explorados:
                g_u = u.custo
                h_u = heuristica(u.estado)
                f_u = g_u + h_u
                
                # Insere 'u' em F
                heapq.heappush(fronteira_heap, (f_u, next(contador), u))

    # Se a fronteira ficar vazia e não achou a solução, falha.
    return None

def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return a_star_search(estado, h_hamming)


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    return a_star_search(estado, h_manhattan)

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
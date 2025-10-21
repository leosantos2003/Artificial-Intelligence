import numpy as np


def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """

    # Obter valores mínimos e máximos para normalização
    minx = min(data[:,0])
    maxx = max(data[:,0])
    miny = min(data[:,1])
    maxy = max(data[:,1])

    # Normalizar os dados (Min-Max Scaling)
    # Normaliza 'x' (features)
    x = (data[:,0] - minx) / (maxx - minx)

    # Normaliza 'y' (valores reais)
    valor_real = (data[:,1] - miny) / (maxy - miny)

    # Calcular as predições com os dados normalizados
    predicoes = w*x +b

    # Calcular o MSE usando os valores normalizados
    erro_quadratico_medio = np.mean((predicoes - valor_real)**2)

    return erro_quadratico_medio


def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """

    # Obter valores mínimos e máximos para normalização
    minx = min(data[:,0])
    maxx = max(data[:,0])
    miny = min(data[:,1])
    maxy = max(data[:,1])

    # Normalizar os dados (Min-Max Scaling)
    x = (data[:,0] - minx) / (maxx - minx)
    y = (data[:,1] - miny) / (maxy - miny)

    # Calcular a predição (hipótese) com dados normalizados
    hx = w*x + b

    # Calcular os gradientes (derivadas parciais da função de custo MSE)
    # Gradiente em relação a 'b' (bias): d_cost/d_b = 2 * (hx - y)
    b_grad = np.mean(2 * (hx - y))

    # Gradiente em relação a 'w' (peso): d_cost/d_w = 2 * x * (hx - y)
    w_grad = np.mean(2 * x * (hx - y))

    # Atualizar os parâmetros usando a taxa de aprendizado
    novo_b = b - (alpha * b_grad)
    novo_w = w - (alpha * w_grad)

    return novo_b.item(), novo_w.item()


def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """

    # Inicializa listas para armazenar o histórico dos parâmetros
    # O tamanho é (num_iterations + 1) para incluir os valores iniciais
    valores_b = [0 for _ in range(num_iterations + 1)]
    valores_w = [0 for _ in range(num_iterations + 1)]

    # Define os valores iniciais na posição 0
    valores_b[0] = b
    valores_w[0] = w

    # Loop de treinamento
    for i in range(1, num_iterations + 1):
        # Calcula os novos b e w usando o passo do gradiente
        # com os valores da iteração anterior (i-1)
        b_novo, w_novo = step_gradient(valores_b[i - 1], valores_w[i - 1], data, alpha)

        # Armazena os novos valores na posição atual (i)
        valores_b[i] = b_novo
        valores_w[i] = w_novo

    return valores_b, valores_w
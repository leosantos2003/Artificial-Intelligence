import numpy as np


def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """

    """
    # 1. Separamos as colunas em x e y
    x = data[:, 0] # Primeira coluna (área do terreno)
    y_real = data[:, 1] # Segunda coluna (preço real)
    
    # 2. Calculamos o preço previsto usando a equação da reta
    y_previsto = (w * x) + b # Equação da reta: y=ax+b

    # 3. Calculamos a diferença (erro) ao quadrado dos valores real e previsto
    erro_quadrado = (y_real - y_previsto) ** 2

    # 4. Calculamos a média dos erros
    mse = np.mean(erro_quadrado)

    return mse
    """

    minx = min(data[:,0])
    maxx = max(data[:,0])
    miny = min(data[:,1])
    maxy = max(data[:,1])
    x = (data[:,0] - minx) / (maxx - minx)
    predicoes = w*x +b
    valor_real = (data[:,1] - miny) / (maxy - miny)
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

    """
    N = float(len(data))
    x = data[:, 0]
    y_real = data[:, 1]

    y_previsto = (w * x) + b

    erro = y_real - y_previsto

    # 1. Calculamos os gradientes (derivadas parciais da função de custo MSE)
    b_grad = -(2/N) * np.sum(erro)
    w_grad = -(2/N) * np.sum(x * erro)

    novo_b = b - (alpha * b_grad)
    novo_w = w - (alpha * w_grad)

    return novo_b, novo_w
    """
    minx = min(data[:,0])
    maxx = max(data[:,0])
    miny = min(data[:,1])
    maxy = max(data[:,1])
    x = (data[:,0] - minx) / (maxx - minx)
    y = (data[:,1] - miny) / (maxy - miny)
    hx = w*x + b
    novo_b = b - alpha*(np.mean(2*(hx - y)))
    novo_w = w - alpha*(np.mean(2*x*(hx - y)))

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

    """
    # 1. Criamos listas para armazenar o histórico dos parâmetros
    b_history = []
    w_history = []

    # 2. Loop de treinamento
    for i in range(num_iterations):
        # i. Executa um passo do gradiente descendente para obter os novos b e w
        b, w = step_gradient(b, w, data, alpha)

        # ii. Armazena os novos valores nas listas de histórico
        b_history.append(b)
        w_history.append(w)

    return b_history, w_history
    """
    valores_b = [0 for _ in range(num_iterations+1)]
    valores_w = [0 for _ in range(num_iterations+1)]
    valores_b[0] = b
    valores_w[0] = w

    for i in range(1,num_iterations+1):
        valores_b[i], valores_w[i] = step_gradient(valores_b[i-1], valores_w[i-1], data, alpha)

    return valores_b, valores_w

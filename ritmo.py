distancias_predefinidas = [5, 10, 15, 21.097, 41.195]

print("Qual é a distância que você deseja calcular?")

# exibe as opções de distâncias pré-definidas
opcoes_predefinidas = " | ".join([str(distancia) + " Km" for distancia in distancias_predefinidas])
print(f"Escolha uma das distâncias pré-definidas ({opcoes_predefinidas}) ou digite uma distância qualquer:")

# lê a entrada do usuário
entrada = input().strip()

# verifica se a entrada do usuário corresponde a uma das distâncias pré-definidas
if entrada in [str(distancia) for distancia in distancias_predefinidas]:
    distancia = float(entrada)
else:
    try:
        distancia = float(entrada)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        exit()

print(f"Você escolheu calcular a distância de {distancia} Km.")

import PySimpleGUI as sg

# Definindo as distâncias pré-definidas em Km
distancias = [5, 10, 15, 21.097, 41.195]

# Definindo o layout da tela para perguntar a distância
layout_distancia = [[sg.Text('Escolha uma das distâncias pré-definidas ou insira uma distância qualquer (em Km):')],
                    [sg.Combo(values=distancias, size=(10,1), key='-DISTANCIA_COMBO-'),
                     sg.InputText(size=(10,1), key='-DISTANCIA_INPUT-')],
                    [sg.Button('Ok'), sg.Button('Cancelar')]]

# Definindo o layout da tela para perguntar o ritmo
layout_ritmo = [[sg.Text('Qual o ritmo desejado (em minutos por Km)?')],
                [sg.InputText(size=(10,1), key='-RITMO-')],
                [sg.Button('Ok'), sg.Button('Cancelar')]]

# Definindo o layout da tela para mostrar o resultado
layout_resultado = [[sg.Text('Tempo Total:'), sg.Text('', size=(10,1), key='-TEMPO_TOTAL-')],
                    [sg.Text('Velocidade Média (Km/h):'), sg.Text('', size=(10,1), key='-VELOCIDADE_MEDIA-')]]

# Definindo o layout da tela para perguntar o pace
layout_pace = [[sg.Text('Qual o pace desejado (em minutos por Km)?')],
               [sg.InputText(size=(10,1), key='-PACE-')],
               [sg.Button('Ok'), sg.Button('Cancelar')]]

# Definindo o layout da tela principal
layout_principal = [[sg.Button('Calcular Tempo total e Velocidade Média'), sg.Button('Calcular Pace e Velocidade Média')],
                    [sg.Button('Sair')]]

# Criando as janelas
janela_distancia = sg.Window('Distância', layout_distancia)
janela_ritmo = sg.Window('Ritmo', layout_ritmo)
janela_pace = sg.Window('Pace', layout_pace)
janela_resultado = sg.Window('Resultado', layout_resultado)
janela_principal = sg.Window('Calculadora de Corrida', layout_principal)

# Loop principal do programa
while True:
    evento_principal, valores_principal = janela_principal.read()
    if evento_principal == sg.WINDOW_CLOSED or evento_principal == 'Sair':
        break
    elif evento_principal == 'Calcular Tempo total e Velocidade Média':
        evento_distancia, valores_distancia = janela_distancia.read()
        if evento_distancia == sg.WINDOW_CLOSED or evento_distancia == 'Cancelar':
            continue
        elif valores_distancia['-DISTANCIA_COMBO-'] != '':
            distancia = float(valores_distancia['-DISTANCIA_COMBO-'])
        elif valores_distancia['-DISTANCIA_INPUT-'] != '':
            distancia = float(valores_distancia['-DISTANCIA_INPUT-'])
        evento_ritmo, valores_ritmo = janela_ritmo.read()
        if evento_ritmo == sg.WINDOW_CLOSED or evento_ritmo == 'Cancelar':
            continue
        ritmo = float(valores_ritmo['-RITMO-'])
        tempo_total_min = ritmo * distancia
        tempo_total_horas =

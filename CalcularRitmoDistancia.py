import PySimpleGUI as sg

# Define as distâncias pré-definidas
distances = {"5 km": 5, "10 km": 10, "15 km": 15, "Meia maratona (21.097 km)": 21.097, "Maratona (42.195 km)": 42.195}

# Define a interface gráfica da tela 1
layout1 = [
    [sg.Text("Escolha a distância:")],
    [sg.Radio(text, "DISTANCE", default=(key == "5 km"), key=key) for key, text in distances.items()],
    [sg.Radio("Outra distância:", "DISTANCE", key="OTHER"), sg.InputText(key="OTHER_DISTANCE", size=(10, 1), disabled=True)],
    [sg.Text("Ritmo desejado por km (minutos):"), sg.InputText(key="PACE", size=(5, 1))],
    [sg.Button("Calcular"), sg.Button("Cancelar")]
]

# Define a interface gráfica da tela 2
layout2 = [
    [sg.Text("Tempo total:", size=(20, 1)), sg.Text("", size=(20, 1), key="TOTAL_TIME")],
    [sg.Text("Velocidade média (km/h):", size=(20, 1)), sg.Text("", size=(20, 1), key="AVG_SPEED")],
    [sg.Button("Voltar")]
]

# Define a interface gráfica da tela 3
layout3 = [
    [sg.Text("Pace (min/km):", size=(20, 1)), sg.Text("", size=(20, 1), key="PACE_RESULT")],
    [sg.Text("Velocidade média (km/h):", size=(20, 1)), sg.Text("", size=(20, 1), key="AVG_SPEED_RESULT")],
    [sg.Button("Voltar")]
]

# Cria as janelas
window1 = sg.Window("Calculadora de corrida - Tela 1", layout1)
window2 = sg.Window("Calculadora de corrida - Tela 2", layout2)
window3 = sg.Window("Calculadora de corrida - Tela 3", layout3)

while True:
    event1, values1 = window1.read()  # Lê os eventos da tela 1
    
    if event1 in (sg.WINDOW_CLOSED, "Cancelar"):  # Fecha a aplicação caso o usuário feche a janela ou clique em Cancelar
        break
    
    distance = None
    if values1["OTHER"]:  # Lê a distância informada pelo usuário caso ele tenha selecionado a opção "Outra distância"
        try:
            distance = float(values1["OTHER_DISTANCE"])
        except ValueError:
            sg.popup("Por favor, informe uma distância válida.", title="Erro")
            continue
    else:  # Lê a distância selecionada pelo usuário caso ele tenha escolhido uma das distâncias pré-definidas
        for key, value in distances.items():
            if values1[key]:
                distance = value
                break
    
    try:
        pace = float(values1["PACE"])  # Lê o ritmo informado pelo usuário
    except ValueError:
        sg.popup("Por favor, informe um ritmo válido.", title

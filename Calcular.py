import PySimpleGUI as sg

# Distâncias pré-definidas em metros
distances = {"5 km": 5000, "10 km": 10000, "15 km": 15000, "Meia-maratona": 21095, "Maratona": 42195}

# Layout da interface gráfica
layout = [
    [sg.Text("Distância"), sg.Combo(list(distances.keys()), key="-DISTANCE-"), sg.Text("Ritmo (min/km)"), sg.InputText(key="-PACE-")],
    [sg.Radio("Calcular Tempo Total e Velocidade Média", "radio_calculation", default=True, key="-TIME_SPEED-"), sg.Radio("Calcular Ritmo e Velocidade Média", "radio_calculation", key="-PACE_SPEED-")],
    [sg.Button("Calcular")],
    [sg.Text("Resultado"), sg.Text("", key="-OUTPUT-")]
]

# Criação da janela
window = sg.Window("Calculadora de Corrida", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    
    # Obtem a distância e o ritmo do usuário
    distance = distances[values["-DISTANCE-"]]
    pace = float(values["-PACE-"])
    
    # Verifica qual opção de cálculo foi selecionada
    if values["-TIME_SPEED-"]:
        # Calcula o tempo total e a velocidade média
        time = pace * distance / 60
        speed = distance / 1000 / (time / 60)
        
        # Exibe o resultado
        window["-OUTPUT-"].update(f"Tempo Total: {time:.2f} minutos\nVelocidade Média: {speed:.2f} km/h")
        
    elif values["-PACE_SPEED-"]:
        # Calcula o ritmo e a velocidade média
        pace_time = pace / distance * 60
        speed = distance / 1000 / (pace_time / 60)
        
        # Exibe o resultado
        window["-OUTPUT-"].update(f"Ritmo: {pace_time:.2f} minutos/km\nVelocidade Média: {speed:.2f} km/h")

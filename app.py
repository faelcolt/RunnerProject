import PySimpleGUI as sg

# Crie uma lista de distâncias de corrida pré-definidas
distances = ["5 km", "10 km", "15 km", "Meia-maratona", "Maratona"]
distance_values = [5000, 10000, 15000, 21095, 42195]

# Crie a interface gráfica do usuário
layout = [[sg.Text("Distância de corrida:")],
          [sg.Button(distance) for distance in distances],
          [sg.Text("Ritmo (min/km):"), sg.InputText()],
          [sg.Button("Calcular")],
          [sg.Text("Resultado: "), sg.Text("", key="-OUTPUT-")]]

window = sg.Window("Calculadora de corrida", layout)

# Crie um loop de eventos para a janela
while True:
    event, values = window.read()
    
    # Se o usuário clicar no botão "Calcular"
    if event == "Calcular":
        pace = float(values[0])
        distance = distance_values[distances.index(values[1])]
        
        # Calcule o tempo necessário para percorrer a distância a um ritmo específico
        time = pace * distance / 60
        
        # Exiba o resultado na janela
        window["-OUTPUT-"].update(f"{time:.2f} minutos")
    
    # Se o usuário fechar a janela
    if event == sg.WINDOW_CLOSED:
        break

window.close()

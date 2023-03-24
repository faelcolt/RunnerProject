from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    distancias = [5, 10, 15, 21.097, 41.195]
    distancia = float(request.form['distancia'])
    ritmo = float(request.form['ritmo'])
    tempo_total_min = ritmo * distancia
    tempo_total_horas = tempo_total_min / 60
    velocidade_media = distancia / tempo_total_horas
    return render_template('resultado.html', tempo_total=tempo_total_horas, velocidade_media=velocidade_media)

if __name__ == '__main__':
    app.run(debug=True)

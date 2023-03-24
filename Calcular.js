<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Calculadora de Corrida</title>
  </head>
  <body>
    <div>
      <button id="tempo-velocidade-btn">Calcular Tempo total e Velocidade Média</button>
      <button id="pace-velocidade-btn">Calcular Pace e Velocidade Média</button>
      <button id="sair-btn">Sair</button>
    </div>

    <div id="distancia-modal" style="display: none">
      <h3>Escolha uma das distâncias pré-definidas ou insira uma distância qualquer (em Km):</h3>
      <select id="distancia-combo">
        <option value=""></option>
        <option value="5">5 Km</option>
        <option value="10">10 Km</option>
        <option value="15">15 Km</option>
        <option value="21.097">21.097 Km</option>
        <option value="41.195">41.195 Km</option>
      </select>
      <input type="number" id="distancia-input" />
      <button id="distancia-ok-btn">Ok</button>
      <button id="distancia-cancelar-btn">Cancelar</button>
    </div>

    <div id="ritmo-modal" style="display: none">
      <h3>Qual o ritmo desejado (em minutos por Km)?</h3>
      <input type="number" id="ritmo-input" />
      <button id="ritmo-ok-btn">Ok</button>
      <button id="ritmo-cancelar-btn">Cancelar</button>
    </div>

    <div id="pace-modal" style="display: none">
      <h3>Qual o pace desejado (em minutos por Km)?</h3>
      <input type="number" id="pace-input" />
      <button id="pace-ok-btn">Ok</button>
      <button id="pace-cancelar-btn">Cancelar</button>
    </div>

    <div id="resultado-modal" style="display: none">
      <h3>Resultado:</h3>
      <p>Tempo Total: <span id="tempo-total"></span></p>
      <p>Velocidade Média (Km/h): <span id="velocidade-media"></span></p>
    </div>

    <script>
      const distanciaModal = document.getElementById("distancia-modal");
      const distanciaCombo = document.getElementById("distancia-combo");
      const distanciaInput = document.getElementById("distancia-input");
      const distanciaOkBtn = document.getElementById("distancia-ok-btn");
      const distanciaCancelarBtn = document.getElementById("distancia-cancelar-btn");
      const ritmoModal = document.getElementById("ritmo-modal");
      const ritmoInput = document.getElementById("ritmo-input");
      const ritmoOkBtn = document.getElementById("ritmo-ok-btn");
      const ritmoCancelarBtn = document.getElementById("ritmo-cancelar-btn");
      const paceModal = document.getElementById("pace-modal");
      const paceInput = document.getElementById("pace-input");
      const paceOkBtn = document.getElementById("pace-ok-btn");
      const paceCancelarBtn = document.getElementById("pace-cancelar-btn");
      const resultadoModal = document.getElementById("

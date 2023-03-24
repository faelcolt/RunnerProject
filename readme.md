Calculadora de Corrida
Este programa é uma calculadora de corrida que permite calcular o tempo total e a velocidade média ou o pace e a velocidade média de uma corrida, a partir da distância e do ritmo inseridos pelo usuário.

Requisitos
O programa utiliza a biblioteca PySimpleGUI para criar a interface gráfica, portanto é necessário ter essa biblioteca instalada.

Utilização
Ao executar o programa, uma janela principal será aberta com três botões: "Calcular Tempo total e Velocidade Média", "Calcular Pace e Velocidade Média" e "Sair".

Ao clicar em um dos botões de cálculo, será aberta uma nova janela para inserir a distância ou o pace, e outra janela para inserir o ritmo desejado. A distância pode ser escolhida a partir de uma lista de distâncias pré-definidas ou pode ser inserida uma distância qualquer. O ritmo deve ser inserido em minutos por Km.

Ao clicar em "Ok" na janela de inserção de distância e ritmo, o programa irá calcular o tempo total e a velocidade média ou o pace e a velocidade média, dependendo da opção selecionada pelo usuário, e mostrará os resultados em uma nova janela.

Código
O código utiliza a biblioteca PySimpleGUI para criar a interface gráfica e é dividido em quatro janelas: janela_distancia, janela_ritmo, janela_pace e janela_resultado. O loop principal do programa é executado na janela_principal e controla o fluxo de execução do programa de acordo com as opções selecionadas pelo usuário.

As distâncias pré-definidas são armazenadas em uma lista chamada "distancias". O layout da janela de inserção de distância é definido na variável "layout_distancia" e contém uma caixa de combinação para escolher uma das distâncias pré-definidas e uma caixa de texto para inserir uma distância qualquer.

O layout da janela de inserção de ritmo é definido na variável "layout_ritmo" e contém uma caixa de texto para inserir o ritmo desejado.

O layout da janela de resultado é definido na variável "layout_resultado" e contém dois rótulos para mostrar o tempo total e a velocidade média ou o pace e a velocidade média, dependendo da opção selecionada pelo usuário.

O layout da janela de inserção de pace é definido na variável "layout_pace" e contém uma caixa de texto para inserir o pace desejado.

O layout da janela principal é definido na variável "layout_principal" e contém três botões para escolher a opção desejada e sair do programa.

O loop principal do programa é executado enquanto a janela principal estiver aberta e controla o fluxo de execução do programa de acordo com as opções selecionadas pelo usuário. Quando o usuário seleciona a opção "Calcular Tempo total e Velocidade Média", o programa abre a janela de inserção de distância, espera que o usuário insira a distância e o ritmo, calcula o tempo total e a velocidade média e mostra os resultados na janela de resultado. Quando o usuário seleciona a opção "Calcular Pace e Velocidade Média", o programa abre a janela de inserção de pace,
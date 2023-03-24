'''Este código define uma função chamada calcular_ritmo que recebe dois argumentos: 
a distância da corrida em quilômetros e o ritmo da corrida em minutos por quilômetro. 
A função retorna uma tupla contendo o tempo necessário para completar a corrida em minutos e o ritmo em segundos por quilômetro.

Para usar a função, basta definir os valores de distancia e ritmo_por_km no exemplo de uso e, 
em seguida, chamar a função calcular_ritmo. O código imprimirá a distância, 
o ritmo, o tempo necessário e o ritmo em segundos por quilômetro.'''

def calcular_ritmo(distancia, ritmo_por_km):
    # distancia em quilômetros, ritmo em minutos por quilômetro
    tempo = distancia * ritmo_por_km
    ritmo = divmod(tempo, distancia)
    ritmo_em_minutos = round(ritmo[1] / 60, 2)
    return (tempo, ritmo_em_minutos)

# Exemplo de uso:
distancia = 10  # distancia em quilômetros
ritmo_por_km = 5.5  # ritmo em minutos por quilômetro

tempo, ritmo_em_minutos = calcular_ritmo(distancia, ritmo_por_km)

print(f"Distância: {distancia} km")
print(f"Ritmo: {ritmo_por_km} min/km")
print(f"Tempo necessário: {tempo} minutos")
print(f"Ritmo em segundos: {ritmo_em_minutos} segundos/km")


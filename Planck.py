h = 6.62607015e-34
pi = 3.141592653589793
float = h / (2 * pi)

def energia_ponto_zero(frequencia):
    omega = 2 * pi * frequencia
    energia = 0.10 * float * omega
    return energia 

frequencia = 1e14
energia = energia_ponto_zero(frequencia)

print(f'A energia do ponto zero para a frequência {frequencia} Hz é {energia} joules.')

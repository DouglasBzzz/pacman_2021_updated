"""
import pygame

pygame.init()

para testar os imports da biblioteca de jogos.

"""

import pygame

pygame.init()

#constantes
AMARELO = (255,255,0)
BRANCO = (255,255,255)
VERMELHO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
PRETO = (0,0,0)
VELOCIDADE = 4
RAIO = 30

#fim das constantes

tela = pygame.display.set_mode((640,480),0)
x = 10
y = 10
velocidade_x = VELOCIDADE
velocidade_y = VELOCIDADE

#loop do jogo

while True:
    #calcula as regras

    x += velocidade_x
    y += velocidade_y

    if x+RAIO > 640:
        velocidade_x = -VELOCIDADE
    if x-RAIO < 0:
        velocidade_x = VELOCIDADE
    if y+RAIO > 480:
        velocidade_y = -VELOCIDADE
    if y-RAIO < 0:
        velocidade_y = VELOCIDADE

    #pintar as coisas na tela

    tela.fill(PRETO)

    pygame.draw.circle(tela, AZUL, (int(x),int(y)), RAIO, 3)
    pygame.display.update()

    #verificamos os eventos do usuário

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
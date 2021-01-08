import pygame

pygame.init()

tela = pygame.display.set_mode((800,600),0)

AMARELO = (255,255,0)
PRETO = (0,0,0)

class Pacman:
    def __init__(self):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 800//30
        self.velocidade_x = 10
        self.velocidade_y = 10
        self.raio = int(self.tamanho//2)

    def cacular_regras(self):
        self.coluna += self.coluna + self.velocidade_x
        self.linha += self.linha + self.velocidade_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

        if self.centro_x + self.raio > 800:
            self.velocidade_x -= 1
        if self.centro_x - self.raio < 0:
            self.velocidade_x = 1
        if self.velocidade_y + self.raio > 600:
            self.velocidade_y -= 1
        if self.velocidade_y - self.raio < 0:
            self.velocidade_y = 1

    def desenhar(self, tela):
        #corpo
        pygame.draw.circle(tela, AMARELO,(self.centro_x, self.centro_y),self.raio, 0)

        #boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        #olhos
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.7)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def desenhar_espelhado(self, tela): #o espelhado é com a boca virada para a esquerda
        # corpo
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        #boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x - self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x - self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        #olhos
        olho_x = int(self.centro_x - self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

if __name__ == '__main__':
    pacman = Pacman()
    while True:

        #calcular as regras - movimentacao do personagem, quadro a quadro
        pacman.cacular_regras()

        #pintar a tela
        tela.fill(PRETO)
        pacman.desenhar(tela)
        pygame.display.update()
        #pygame.time.delay(1000)

        #caputra os eventos
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
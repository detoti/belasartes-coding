import pygame
from pygame.locals import *
from sys import exit
from random import randint

#iniciando o PyGame
pygame.init()

#sons
pygame.mixer.music.set_volume(0.1)
soundtrack = pygame.mixer.music.load('soundtrack.mp3')
somColision = pygame.mixer.Sound('quermaischa.mp3')
somMorreu = pygame.mixer.Sound('morreu.mp3')
pygame.mixer.music.play(-1)

#tamanho da tela
largura = 640
altura = 480

#posiçao inicial da cobra
xCobra = int(largura/2) 
yCobra = int(altura/2)

#velocidade da cobra
velocidade = 10
xControle = velocidade
yControle = 0

#area onde as maças podem spawnar
xMaca = randint(40, 600)
yMaca = randint(50, 430)

#inicio da contagem de pontos
pontos = 0
#fonte padrão do placar
fonte = pygame.font.SysFont('arial', 20, bold=True, italic=True)

#configuraçōes
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Dona Marocas')
relogio = pygame.time.Clock()
listaCobra = []
comprimentoInicial = 5
morreu = False

#aumentar a cobra conforme pontuação
def aumentaCobra(listaCobra):
    for XeY in listaCobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

#configuraçōes de reinicio
def reiniciarGame():
    global pontos, comprimentoInicial, xCobra, yCobra, listaCobra, listaCabeca, xMaca, yMaca, morreu
    pontos = 0
    comprimentoInicial = 5
    xCobra = int(largura/2) 
    yCobra = int(altura/2)
    listaCobra = []
    listaCabeca = []
    xMaca = randint(40, 600)
    yMaca = randint(50, 430)
    morreu = False

#inicio
while True:
    relogio.tick(30)
    tela.fill((204,255,255))
    
#placar
    mensagem = f'Xícaras de Chá: {pontos}'
    textoFormatado = fonte.render(mensagem, True, (0,0,0))
    
#configuraçōes de saída da tela    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
#controle
        if event.type == KEYDOWN:
            if event.key == K_a:
                if xControle == velocidade:
                    pass
                else:
                    xControle = -velocidade
                    yControle = 0
            if event.key == K_d:
                if xControle == -velocidade:
                    pass
                else:
                    xControle = velocidade
                    yControle = 0
            if event.key == K_w:
                if yControle == velocidade:
                    pass
                else:
                    yControle = -velocidade
                    xControle = 0
            if event.key == K_s:
                if yControle == -velocidade:
                    pass
                else:
                    yControle = velocidade
                    xControle = 0

    xCobra = xCobra + xControle
    yCobra = yCobra + yControle


#objetos   
    cobra = pygame.draw.rect(tela, (51,255,153), (xCobra,yCobra,20,20))
    maca = pygame.draw.circle(tela, (255, 153, 255), (xMaca + 10, yMaca + 10), 10)
    
    
#colisao
    if cobra.colliderect(maca):
        xMaca = randint(40, 600)
        yMaca = randint(50, 430)
        pontos += 1
        somColision.play()
        comprimentoInicial = comprimentoInicial + 1

#desenha a borda da tela
    borda = pygame.Rect(0, 0, largura, altura)
    pygame.draw.rect(tela, (255, 255, 255), borda, 5)

#lista para tamanho da cobra
    listaCabeca = []
    listaCabeca.append(xCobra)
    listaCabeca.append(yCobra)
    
    listaCobra.append(listaCabeca)

# Verifica se a cobra colidiu com a borda ou com a cauda
    if listaCabeca[0] < 0 or listaCabeca[0] > largura or listaCabeca[1] < 0 or listaCabeca[1] > altura or len(listaCobra) != len(set(map(tuple, listaCobra))): 
        fonte2 = pygame.font.SysFont('arial', 15, True, True)
        mensagem = 'Dona Marocas não aguenta mais chá! Pressione a tecla R para jogar novamente'
        textoFormatado = fonte2.render(mensagem, True, (0,0,0))
        retTexto = textoFormatado.get_rect()
        somMorreu.play()
        morreu = True

#tela de game over
        while morreu:
            tela.fill((204,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
#tecla para reinicio de game
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciarGame()

            retTexto.center = (largura//2, altura//2) 
            tela.blit(textoFormatado, retTexto)
            pygame.display.update()

    
    if xCobra > largura:
        xCobra = 0
    if xCobra < 0:
        xCobra = largura
    if yCobra < 0:
        yCobra = altura
    if yCobra > altura:
        yCobra = 0

    if len(listaCobra) > comprimentoInicial:
        del listaCobra[0]

    aumentaCobra(listaCobra)

    tela.blit(textoFormatado, (450,40))
    pygame.display.update()

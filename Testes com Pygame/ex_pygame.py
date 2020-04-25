import pygame

def main():
    # Definições dos objetos / variáveis
    pygame.init()
    tela = pygame.display.set_mode((600, 500)) #Funciona com parenteses ou colchetes
    pygame.display.set_caption("Iniciando com Pygame")
    relogio = pygame.time.Clock()
    cor_branca = (255,255,255)
    cor_vermelha = (255,0,0)
    cor_verde = (0,128,0)
    cor_laranja = (255,140,0)
    cor_amarela = (255,255,0)
    cor_azul = (30,144,255)
    cor_violeta = (138,43,226)
    cor_rosa = (255,20,147)
    cor_cinza = (128,128,128)
    sup1 = pygame.Surface([200,200])
    sup1.fill(cor_azul)
    sup2 = pygame.Surface([100,100])
    sup2.fill(cor_verde)

    ret = pygame.Rect(10, 10, 45, 45)
    ret2 = pygame.Rect(80, 100, 100, 60)

    sair = False

    pygame.font.init()

    font_padrao = pygame.font.get_default_font()
    fonte_perdeu = pygame.font.SysFont(font_padrao, 45)
    fonte_ganhou = pygame.font.SysFont(font_padrao, 30)

    audio_explosao = pygame.mixer.Sound('explosion-02.ogg')

    # Desenvolvimento do programa ou jogo
    while sair == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                #ret = ret.move(10,10)
                pygame.mouse.set_pos(150,150)
            #if event.type == pygame.MOUSEMOTION:
                #ret = ret.move(-10,-10)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ret.move_ip(-10,0)
                if event.key == pygame.K_RIGHT:
                    ret.move_ip(10,0)
                if event.key == pygame.K_UP:
                    ret.move_ip(0,-10)
                if event.key == pygame.K_DOWN:
                    ret.move_ip(0,10)
                if event.key == pygame.K_SPACE:
                    ret.move_ip(10,10)
                if event.key == pygame.K_BACKSPACE:
                    ret.move_ip(-10,-10)

        relogio.tick(27) #define a taxa de atualização

        tela.fill(cor_branca)

        tela.blit(sup1, (25,30)) # Coloca em tela a superfície na posição inicial
        tela.blit(sup2, [150,150])
        tela.blit(sup2, [250, 70])

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos() # Armazena a posição do mouse nas variáveis de posição do objeto
        ret.left -= ret.width/2
        ret.top -= ret.height/2
        if ret.colliderect(ret2):
            text = fonte_perdeu.render('COLIDIU', 1, cor_vermelha)
            audio_explosao.play()
            audio_explosao.set_volume(0.2)
            tela.blit(text, (150,450))
            (ret.left, ret.top) = (xant, yant)

        pygame.draw.rect(tela, cor_laranja, ret) # Desenha o objeto na tela e na cor
        pygame.draw.rect(tela, cor_rosa, ret2)
        pygame.display.update()

    pygame.quit()

main()

import pygame
import random

pygame.init()
sfondo = pygame.image.load('immagini/sfondo.png')
uccello = pygame.image.load('immagini/uccello.png')
base = pygame.image.load('immagini/base.png')
gameover = pygame.image.load('immagini/gameover.png')
tubo_giu = pygame.image.load('immagini/tubo.png')
tubo_su = pygame.transform.flip(tubo_giu, False, True)

SCHERMO = pygame.display.set_mode((288, 512))
FPS = 50
VEL_AVANZ = 3


class tubi_classe:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75, 150)
        SCHERMO.blit(tubo_giu, (self.x, self.y + 210))
        SCHERMO.blit(tubo_su, (self.x, self.y - 210))

    def avanza_e_disegna(self):
        self.x -= VEL_AVANZ


def disegna_oggetti():
    SCHERMO.blit(sfondo, (0, 0))
    SCHERMO.blit(uccello, (uccellox, uccelloy))
    SCHERMO.blit(base, (basex, 400))
    for t in tubi:
        t.avanza_e_disegna()


def inizializza():
    global uccellox, uccelloy, uccello_vely, basex
    global tubi
    uccellox, uccelloy = 60, 150
    uccello_vely = 0
    basex = 0
    tubi = []
    tubi.append(tubi_classe())


def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)


inizializza()


def hai_perso():
    SCHERMO.blit(gameover, (50, 180))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()


while True:
    uccello_vely += 1
    uccelloy += uccello_vely + 1
    basex -= VEL_AVANZ
    if basex < -45: basex = 0
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            uccello_vely = -10
        if (event.type == pygame.QUIT):
            pygame.quit()
    if tubi[-1].x < 150: tubi.append(tubi_classe())
    if uccelloy > 380:
        hai_perso()
    disegna_oggetti()
    aggiorna()

from classes.Feu import Feu
from classes.Eau import Eau
from classes.Normal import Normal
from classes.Terre  import Terre
from classes.Combat  import Combat
import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800,600))
background=pygame.image.load("background.png")
pygame.display.set_caption("pokemon")
font = pygame.font.SysFont("calibri", 20, bold=True)

pokemons=[Feu("Salameche"),Terre("Sabelette")]
combat=Combat((pokemons[0],pokemons[1]))
running=True
while running:
    screen.blit(background,(0,0))
    space=0
    for pokemon in pokemons:
        test=pokemon.affiche_infos().split(",",1)
        pokemon = font.render(test[0], True, pygame.Color((63,72,204)))
        pokemon2 = font.render(test[1], True, pygame.Color((63,72,204)))
        screen.blit(pokemon,(0,space))
        screen.blit(pokemon2,(0,space+20))
        space+=100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            piocher=False 
        if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] in range(181,360) and pygame.mouse.get_pos()[1] in range(470,540):
                    finish=combat.play()
                elif pygame.mouse.get_pos()[0] in range(457,651) and pygame.mouse.get_pos()[1] in range(470,540):
                    running=False

                    
    pygame.display.update()
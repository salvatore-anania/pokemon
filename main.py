from classes.Type  import Type
from classes.Combat  import Combat
from classes.Sauvegarde  import Sauvegarde
from classes.Charger  import Charger
from classes.Equipe  import Equipe
from random  import randint
import pygame
sauvergarde=Charger()

def affiche_equipe(x,y,equipe):
    for pokemon in equipe.get_equipe():
            if pokemon.is_alive():
                pokemon_image=pygame.image.load(pokemon.get_image())
                screen.blit(pokemon_image,(x,y))
                x+=50

def affiche_poke_info(x,y,pokemon):
    test=pokemon.affiche_infos().split(",",1)
    pokemon_image=pygame.image.load(pokemon.get_image())
    pokemon_info = font.render(test[0], True, pygame.Color((63,72,204)))
    equipe_info = font.render(test[1], True, pygame.Color((63,72,204)))
    screen.blit(pokemon_info,(x-pokemon_info.get_width()/2,y))
    screen.blit(equipe_info,(x-equipe_info.get_width()/2,y+20))
    screen.blit(pokemon_image,(x+200,y))

def set_adversaire():
    equipe=Equipe()
    for i in range(6):
        pos=randint(0,17)
        equipe.add_pokemon(Type(pokemons[pos],1,pokemons[pos]))
    return equipe
            
debutX=95
largeur=100
debutY=80
hauteur=145
insecte=[range(debutX+largeur*0,debutX+largeur*1),range(debutY+hauteur*0,debutY+hauteur*1)]
tenebre=[range(debutX+largeur*1,debutX+largeur*2),range(debutY+hauteur*0,debutY+hauteur*1)]
dragon=[range(debutX+largeur*2,debutX+largeur*3),range(debutY+hauteur*0,debutY+hauteur*1)]
electrik=[range(debutX+largeur*3,debutX+largeur*4),range(debutY+hauteur*0,debutY+hauteur*1)]
fee=[range(debutX+largeur*4,debutX+largeur*5),range(debutY+hauteur*0,debutY+hauteur*1)]
kombat=[range(debutX+largeur*5,debutX+largeur*6),range(debutY+hauteur*0,debutY+hauteur*1)]

feu=[range(debutX+largeur*0,debutX+largeur*1),range(debutY+hauteur*1,debutY+hauteur*2)]
vol=[range(debutX+largeur*1,debutX+largeur*2),range(debutY+hauteur*1,debutY+hauteur*2)]
spectre=[range(debutX+largeur*2,debutX+largeur*3),range(debutY+hauteur*1,debutY+hauteur*2)]
plante=[range(debutX+largeur*3,debutX+largeur*4),range(debutY+hauteur*1,debutY+hauteur*2)]
sol=[range(debutX+largeur*4,debutX+largeur*5),range(debutY+hauteur*1,debutY+hauteur*2)]
glace=[range(debutX+largeur*5,debutX+largeur*6),range(debutY+hauteur*1,debutY+hauteur*2)]

normal=[range(debutX+largeur*0,debutX+largeur*1),range(debutY+hauteur*2,debutY+hauteur*3)]
poison=[range(debutX+largeur*1,debutX+largeur*2),range(debutY+hauteur*2,debutY+hauteur*3)]
psy=[range(debutX+largeur*2,debutX+largeur*3),range(debutY+hauteur*2,debutY+hauteur*3)]
roche=[range(debutX+largeur*3,debutX+largeur*4),range(debutY+hauteur*2,debutY+hauteur*3)]
acier=[range(debutX+largeur*4,debutX+largeur*5),range(debutY+hauteur*2,debutY+hauteur*3)]
eau=[range(debutX+largeur*5,debutX+largeur*6),range(debutY+hauteur*2,debutY+hauteur*3)]

choix=[insecte,tenebre,dragon,electrik,fee,kombat,feu,vol,spectre,plante,sol,glace,normal,poison,psy,roche,acier,eau]

pygame.init()
saving=Sauvegarde()
screen = pygame.display.set_mode((800,600))
background=pygame.image.load("image/background.png")
attaque=pygame.image.load("image/background_attack.png")
types=pygame.image.load("image/types.jpg")
pygame.display.set_caption("pokemon")
font = pygame.font.SysFont("calibri", 25, bold=True)
connection=pygame.image.load("image/connection.png")

pokemons=["insecte","tenebre","dragon","electrik","fee","combat","feu","vol","spectre","plante","sol","glace","normal","poison","psy","roche"
          ,"acier","eau"]
equipe=Equipe()
running=True
choose=False
username=''
color=(63,72,204)
connect=False
while running:
    while not connect:
        input_box = pygame.Rect(253, 85, 320, 32)
        color_active = pygame.Color('lightskyblue3')
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                    color = color_active
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        poke_exist=sauvergarde.lire_pokemon(username)
                        if poke_exist:
                            for pokemon_equipe in poke_exist:
                                equipe.add_pokemon(Type(pokemon_equipe[0],int(pokemon_equipe[1]),pokemon_equipe[2],pokemon_equipe[3]
                                                        ,float(pokemon_equipe[4]),pokemon_equipe[5]))
                        saving.save(username)
                        screen.blit(connection,(0,0))
                        active=False
                        connect=True
                        color=(63,72,204)
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    elif len(username)<20:
                        username += event.unicode
        txt_surface = font.render(username, True, color)
        screen.blit(connection,(0,0))
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        
        pygame.display.flip()
        equipeadverse=set_adversaire()
            
    while not choose:
        if not equipe.complete():
            screen.blit(background,(0,0))
            screen.blit(types,(95,80))
            choose_pokemon = font.render(f"Choissisez le type de vos pokemon : {len(equipe.get_equipe())}/6", True, pygame.Color((63,72,204)))
            screen.blit(choose_pokemon,(400-choose_pokemon.get_width()/2,30))
        elif equipe.complete():
            choose=True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                choose=True
            for pos in range(len(choix)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] in choix[pos][0] and pygame.mouse.get_pos()[1] in choix[pos][1]:
                        if not equipe.complete():
                            equipe.add_pokemon(Type(pokemons[pos],1,pokemons[pos]))
                            saving.save(username,equipe.get_save())
                            poke_exist=sauvergarde.lire_pokemon(username)      
        pygame.display.update()
        
    for pokemon in equipeadverse.get_equipe():
        if pokemon.is_alive():
            poke_choose_adverse=pokemon
    for pokemon in equipe.get_equipe():
        if pokemon.is_alive():
            combat=Combat((poke_choose_adverse,pokemon))
            poke_choose=pokemon
    screen.blit(attaque,(0,0))
    if not combat.winner_name():
        space=0
        affiche_poke_info(200,0,poke_choose_adverse)
        affiche_poke_info(200,200,poke_choose)
 
        affiche_equipe(0,50,equipeadverse)
        affiche_equipe(0,250,equipe)
        for attaque_info in poke_choose.get_attaques():
            attaque_infos = font.render(attaque_info[0], True, pygame.Color((182,122,87)))
            screen.blit(attaque_infos,(attaque_info[2][0]-attaque_infos.get_width()/2,attaque_info[2][1]))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] in range(181,360) and pygame.mouse.get_pos()[1] in range(378,447):
                    combat.play("1")
                elif pygame.mouse.get_pos()[0] in range(457,651) and pygame.mouse.get_pos()[1] in range(378,447):
                    combat.play("2")
                if pygame.mouse.get_pos()[0] in range(181,360) and pygame.mouse.get_pos()[1] in range(470,540):
                    combat.play("3")
                elif pygame.mouse.get_pos()[0] in range(457,651) and pygame.mouse.get_pos()[1] in range(470,540):
                    combat.play("4")
    else:
        screen.blit(background,(0,0))
        pokemon_image=pygame.image.load(combat.winner().get_image())
        gagnant = font.render(f"le gagnant est {combat.winner_name()} !", True, pygame.Color((63,72,204)))
        screen.blit(pokemon_image,(400,100))
        screen.blit(gagnant,(400-gagnant.get_width()/2,50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] in range(181,360) and pygame.mouse.get_pos()[1] in range(470,540):
                        choose=0
                        if combat.winner()==poke_choose:
                            poke_choose.exper()
                            poke_choose.evolution()
                            saving.save(username,equipe.get_save())
                            equipeadverse=set_adversaire()
                        else:
                            for pokemon in equipe.get_equipe():
                                pokemon.soin()
                            saving.save(username,equipe.get_save())
                    if pygame.mouse.get_pos()[0] in range(457,651) and pygame.mouse.get_pos()[1] in range(470,540):
                        running=False
                        saving.save(username,equipe.get_save())
      
    pygame.display.update()
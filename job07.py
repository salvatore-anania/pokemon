from random import randint
import pygame
import time

class Carte:
    def __init__(self,couleur,valeur,image):
        self.__couleur=couleur
        self.__valeur=valeur
        self.__image=image
        
    def get_valeur(self):
        return self.__valeur
    def set_valeur(self,valeur):
        self.__valeur=valeur
    
    def affiche(self,screen,x,y):
        screen.blit(self.__image,(x,y))
    
class Jeu:
    def __init__(self):
        self.__paquet=[]
        
    def remplir_paquet(self):
        couleur=["coeur","carreau","trefle","pique"]
        change_color=0
        for i in range(1,53):
            if i%13==1:
                self.__paquet.append(Carte(couleur[change_color],11,pygame.image.load(f"card/{couleur[change_color]}/{couleur[change_color]}A.png")))
            elif i%13==0:
                self.__paquet.append(Carte(couleur[change_color],10,pygame.image.load(f"card/{couleur[change_color]}/{couleur[change_color]}K.png")))
                change_color+=1
            elif i%13==11:
                self.__paquet.append(Carte(couleur[change_color],10,pygame.image.load(f"card/{couleur[change_color]}/{couleur[change_color]}V.png")))
            elif i%13==12:
                self.__paquet.append(Carte(couleur[change_color],10,pygame.image.load(f"card/{couleur[change_color]}/{couleur[change_color]}Q.png")))
            else:
                self.__paquet.append(Carte(couleur[change_color],i%13,pygame.image.load(f"card/{couleur[change_color]}/{couleur[change_color]}{i%13}.png")))
        return self.__paquet
    
    def get_paquet(self):
        return self.__paquet
    
    def __set_paquet(self,paquet):
        self.__paquet=paquet
    
    def distribuer(self):
        pioche =randint(0,len(self.__paquet)-1)
        piocher=self.__paquet[pioche]
        self.__paquet.remove(piocher)
        return piocher

class Main():
    def __init__(self):
        self.__main=[]
        
    def get_paquet(self):
        return self.__main
    
    def piocher(self,carte):
        self.__main.append(carte)
        
    def affiche(self,screen,x=0,y=0):
        for carte in self.__main:
            carte.affiche(screen,x,y)
            x+=80
            
    def calcul_main(self):
        total_main=0
        for carte in self.__main:
            total_main+=carte.get_valeur()
            
        return total_main
    
    def main_plus_forte(self,main):
        if self.calcul_main()<main.calcul_main() and main.calcul_main()<21:
            return font.render("vous avez perdu !", True, pygame.Color((63,72,204)))
        else:
            return font.render("vous avez gagné !", True, pygame.Color((63,72,204)))
        
    def test_ace(self,screen):
        main=self.get_paquet()
        choose=True
        if main[len(main)-1].get_valeur()==11:
            while choose:
                for test in pygame.event.get():
                    screen.blit(back_choose,(0,0))
                    joueur.affiche(screen,200,355)
                    if test.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pos()[0] in range(181,360) and pygame.mouse.get_pos()[1] in range(470,540):
                            main[len(main)-1].set_valeur(1)
                            choose=False
                            return False
                        elif pygame.mouse.get_pos()[0] in range(457,651) and pygame.mouse.get_pos()[1] in range(470,540):
                            main[len(main)-1].set_valeur(11)
                            choose=False
                            return False
                pygame.display.update()
        return False

pygame.init()

screen = pygame.display.set_mode((800,600))
back=pygame.image.load("card/background.png")
back_replay=pygame.image.load("card/background_replay.png")
back_choose=pygame.image.load("card/background_choose.png")
pygame.display.set_caption("space invaders")
font = pygame.font.SysFont("calibri", 50, bold=True)
ace_not_choosed=True
choose=False
running=True
while running:
    paquet=Jeu()
    joueur=Main()
    croupier=Main()
    paquet.remplir_paquet()
    piocher=True
    perdu=False
    screen.blit(back,(0,0))
    
    for i in range (2):
        joueur.piocher(paquet.distribuer())
        ace_not_choosed=True
        if ace_not_choosed:
            ace_not_choosed=joueur.test_ace(screen)
            screen.blit(back,(0,0))
        croupier.piocher(paquet.distribuer())
    while piocher:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                piocher=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] in range(181,360) and pygame.mouse.get_pos()[1] in range(470,540):
                    joueur.piocher(paquet.distribuer())
                    ace_not_choosed=True
                elif pygame.mouse.get_pos()[0] in range(457,651) and pygame.mouse.get_pos()[1] in range(470,540):
                    piocher=False
        if ace_not_choosed:
            ace_not_choosed=joueur.test_ace(screen)
            screen.blit(back,(0,0))
        joueur.affiche(screen,200,355)
        if joueur.calcul_main()>21:
            perdu=True
            piocher=False
        pygame.display.update()
    piocher=True
    
    while piocher and not perdu and running:
        croupier.affiche(screen,200,90)
        if croupier.calcul_main()<17:
            croupier.piocher(paquet.distribuer())
        else:
            piocher=False
 
                 
    if not perdu:
        texte=joueur.main_plus_forte(croupier)
    else:
        texte = font.render("vous avez perdu !", True, pygame.Color((63,72,204)))
        
    screen.blit(back_replay,(0,0))
    screen.blit(texte, (400-(texte.get_width()/2), 250))
    croupier.affiche(screen,200,90)
    joueur.affiche(screen,200,355)
    end=True
    while end and running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                end=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] in range(181,360) and pygame.mouse.get_pos()[1] in range(470,540):
                        end=False
                    elif pygame.mouse.get_pos()[0] in range(457,651) and pygame.mouse.get_pos()[1] in range(470,540):
                        running=False
                    
        pygame.display.update()
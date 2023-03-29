from classes.Pokemon import Pokemon

class Combat:
    def __init__(self,pokemons):
        self.pokemons=pokemons
        self.__attaquant=0
        self.__defenseur=1
        
    def is_alive(self,index):
        if self.pokemons[index].get_PV()<=0:
            return False
        else:
            return True
    
    def winner(self):
        if self.is_alive(0) and not self.is_alive(1):
            return self.pokemons[1].get_name()
        elif self.is_alive(1) and not self.is_alive(0):
            return self.pokemons[1].get_name()
        else:
            return False
        
    def calcul_type_attack_power(self,attaquant,defenseur):
        type_attaquant=attaquant.get_type()
        type_defenseur=defenseur.get_type()
        power_attaquant=attaquant.get_power_attack()
        if type_attaquant=="eau":
            if type_defenseur=="eau" or type_defenseur=="normal":
                return power_attaquant
            elif type_defenseur=="feu":
                return power_attaquant*2
            elif type_defenseur=="terre":
                return power_attaquant*0.5
        elif type_attaquant=="feu":
            if type_defenseur=="feu" or type_defenseur=="normal":
                return power_attaquant
            elif type_defenseur=="terre":
                return power_attaquant*2
            elif type_defenseur=="eau":
                return power_attaquant*0.5
        elif type_attaquant=="terre":
            if type_defenseur=="terre" or type_defenseur=="normal":
                return power_attaquant
            elif type_defenseur=="eau":
                return power_attaquant*2
            elif type_defenseur=="feu":
                return power_attaquant*0.5
        elif type_attaquant=="normal":
            if type_defenseur=="normal":
                return power_attaquant
            else:
                return power_attaquant*0.75
            
    def attaque(self):
        attaquant=self.pokemons[self.__attaquant]
        defenseur=self.pokemons[self.__defenseur]

        new_PV=defenseur.get_PV()
        new_PV-=self.calcul_type_attack_power(attaquant,defenseur)
        defenseur.set_PV(new_PV)
        
    def looser(self):
        if self.is_alive(1) and not self.is_alive(0):
            return self.pokemons[0].get_name()
        elif self.is_alive(0) and not self.is_alive(1):
            return self.pokemons[1].get_name()
        else:
            return False
        
    def play(self):
        self.attaque()
        if self.winner():
            return self.winner()
        if self.__attaquant==0:
            self.__attaquant=1
            self.__defenseur=0
        else:
            self.__attaquant=0
            self.__defenseur=1
        return False
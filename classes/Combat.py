from classes.Pokemon import Pokemon

class Combat:
    def __init__(self,pokemons):
        self.__pokemons=pokemons
        self.__attaquant=1
        self.__defenseur=0
        
    def is_alive(self,index):
        if self.__pokemons[index].get_PV()<=0:
            return False
        else:
            return True
    
    def winner_name(self):
        if self.is_alive(0) and not self.is_alive(1):
            return self.__pokemons[0].get_name()
        elif self.is_alive(1) and not self.is_alive(0):
            return self.__pokemons[1].get_name()
        else:
            return False
    
    def winner(self):
        if self.is_alive(0) and not self.is_alive(1):
            return self.__pokemons[0]
        elif self.is_alive(1) and not self.is_alive(0):
            return self.__pokemons[1]
        else:
            return False
        
    def calcul_type_attack_power(self,attaquant,defenseur,competence="4"):
        
        type_defenseur=defenseur.get_type()
        
        if defenseur.get_type2():
            type2_defenseur=defenseur.get_type2()
        else:
            type2_defenseur=False
            
        power_attaquant=attaquant.get_power_attack()
        
        if type_defenseur in attaquant.get_fort():
            if type2_defenseur:
                if type2_defenseur in attaquant.get_fort():
                    return power_attaquant*(4+attaquant.get_competences()[competence]/100)
                elif type2_defenseur in attaquant.get_faible():
                    return power_attaquant*(1+attaquant.get_competences()[competence]/100)
                else:
                    return power_attaquant*(2+attaquant.get_competences()[competence]/100)
            else:
                return power_attaquant*(2+attaquant.get_competences()[competence]/100)
        elif type_defenseur in attaquant.get_faible():
            if type2_defenseur:
                if type2_defenseur in attaquant.get_fort():
                    return power_attaquant*(1+attaquant.get_competences()[competence]/100)
                elif type2_defenseur in attaquant.get_faible():
                    return power_attaquant*(0.25+attaquant.get_competences()[competence]/100)
                else:
                    return power_attaquant*(2+attaquant.get_competences()[competence]/100)
            else:
                return power_attaquant*(0.5+attaquant.get_competences()[competence]/100)
        else:
            return power_attaquant*(1+attaquant.get_competences()[competence]/100)   
            
    def attaque(self,competence="4"):
        attaquant=self.__pokemons[self.__attaquant]
        defenseur=self.__pokemons[self.__defenseur]

        new_PV=defenseur.get_PV()
        new_PV-=self.calcul_type_attack_power(attaquant,defenseur,competence)-defenseur.get_defense()
        defenseur.set_PV(new_PV)
        
    def looser(self):
        if self.is_alive(1) and not self.is_alive(0):
            return self.__pokemons[0].get_name()
        elif self.is_alive(0) and not self.is_alive(1):
            return self.__pokemons[1].get_name()
        else:
            return False
        
    def play(self,competence):
        self.attaque(competence)
        if self.winner_name():
            return False
        self.__attaquant=0
        self.__defenseur=1
        self.attaque()
        self.__attaquant=1
        self.__defenseur=0
        return False

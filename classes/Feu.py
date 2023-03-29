from classes.Pokemon import Pokemon

class Feu(Pokemon):
    def __init__(self,name="feu",niveau=4,PV=10,puissance_attaque=7,defense=2):
        super().__init__(name,niveau,PV,puissance_attaque,defense,"feu")
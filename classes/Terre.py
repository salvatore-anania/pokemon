from classes.Pokemon import Pokemon
class Terre(Pokemon):
    def __init__(self,name="terre",niveau=4,PV=120,puissance_attaque=2,defense=7):
        super().__init__(name,niveau,PV,puissance_attaque,defense,"terre")
from classes.Pokemon import Pokemon

class Eau(Pokemon):
    def __init__(self,name="eau",niveau=4,PV=10,puissance_attaque=7,defense=2):
        super().__init__(name,niveau,PV,puissance_attaque,defense,"eau")
        
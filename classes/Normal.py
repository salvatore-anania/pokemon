from classes.Pokemon import Pokemon

class Normal(Pokemon):
    def __init__(self,name="normal",niveau=4,PV=100,puissance_attaque=5,defense=3):
        super().__init__(name,niveau,PV,puissance_attaque,defense,"normal")
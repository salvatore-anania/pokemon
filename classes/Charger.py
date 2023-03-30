from json import load,dumps

class Charger:
    def __init__(self) -> None:
        pass
    
    def lire_pokemon(self,user):
        with open("saves/data_user.json", "r") as affiche:
            test=load(affiche)
        return test[user]
                
    def lire_attaques(self,type1):
        with open("dictionnaires/attaques.json", "r") as affiche:
            test=load(affiche)
        return test[type1]
    
    def lire_types(self,type1):
        with open("dictionnaires/types.json", "r") as affiche:
            test=load(affiche)
        return test[type1]
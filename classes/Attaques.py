from classes.Charger import Charger


class Attaques():
    
    def __init__(self,type1):
        self.__attaques=[]
        count=0
        for attaque_name,attaque_value in Charger().lire_attaques(type1).items():
            if count==0:
                self.__attaques.append((attaque_name,attaque_value,(271,393)))
            elif count==1:
                self.__attaques.append((attaque_name,attaque_value,(552,393)))
            elif count==2:
                self.__attaques.append((attaque_name,attaque_value,(271,485)))
            else:
                self.__attaques.append((attaque_name,attaque_value,(552,485)))
            count+=1
    
    def get_attaques(self):
        return self.__attaques
    
    
    
    

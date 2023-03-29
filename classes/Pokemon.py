class Pokemon:
    def __init__(self,name="",niveau=4,PV=100,puissance_attaque=5,defense=0,type_poke=""):
        self.__name=name
        self.__point_de_vie=PV
        self.__niveau=niveau
        self.__puissance_attaque=puissance_attaque
        self.__defense=defense
        self.__type=type_poke
        
        
    def get_name(self):
        return self.__name
    
    def get_PV(self):
        return self.__point_de_vie
    
    def get_niveau(self):
        return self.__niveau
    
    def get_power_attack(self):
        return self.__puissance_attaque
    
    def get_defense(self):
        return self.__defense
    
    def get_type(self):
        return self.__type
    
    def set_name(self,name):
        self.__name=name
    
    def set_PV(self,PV):
        if PV<0:
            self.__point_de_vie=0
        else:
            self.__point_de_vie=PV
    
    def set_niveau(self,niveau):
        self.__niveau=niveau
    
    def set_power_attack(self,power_attack):
        self.__puissance_attaque=power_attack
    
    def set_defense(self,defense):
        self.__defense=defense
        
    def affiche_infos(self):
        return f"Nom : {self.get_name()}  Niveau : {self.get_niveau()},PV : {self.get_PV()} defense : {self.get_defense()} attaque : {self.get_power_attack()}"
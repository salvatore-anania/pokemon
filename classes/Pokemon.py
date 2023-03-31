class Pokemon:
    def __init__(self,name,niveau,PV,puissance_attaque,defense,vie_max,XP=0):
        self.__name=name
        self.__vie_max=vie_max
        self.__point_de_vie=PV
        self.__niveau=niveau
        self.__puissance_attaque=puissance_attaque
        self.__defense=defense
        self.__experience=XP
        
    def get_name(self):
        return self.__name
    
    def get_vie_max(self):
        return self.__vie_max
    
    def get_PV(self):
        return self.__point_de_vie
    
    def get_XP(self):
        return self.__experience
    
    def get_niveau(self):
        return self.__niveau
    
    def get_power_attack(self):
        return self.__puissance_attaque
    
    def get_defense(self):
        return self.__defense

    def is_alive(self):
        if self.__point_de_vie >0:
            return True
        else:
            return False
    
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
        
    def exper(self):
        self.__experience+=10
    
    def soin(self):
        self.__point_de_vie=self.__vie_max
        
    def evolution(self):
        if self.__experience==20:
            self.__puissance_attaque+=5
            self.__defense+=2
            self.__vie_max+=10
            self.__niveau+=1
            self.__experience=0
        
    def affiche_infos(self):
        return f"Nom : {self.get_name()}  Niveau : {self.get_niveau()} PV : {self.get_PV()}, attaque : {self.get_power_attack()} defense : {self.get_defense()}"
      
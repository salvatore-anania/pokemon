from classes.Pokemon import Pokemon
from classes.Attaques import Attaques
from classes.Charger import Charger
import json


class Type(Pokemon):
    
    def __init__(self,name="generique",niveau=1,type1="normal",type2=False,PV=False,XP=0):
        self.__type1=type1
        self.__type2=type2
        self.__type_info=Charger().lire_types(self.__type1)
        if not PV:
            PV=self.__type_info["PV"]
        self.__attaques=Attaques(type1)
        super().__init__(name,niveau,PV,self.__type_info["attaque"]+5*niveau,self.__type_info["defense"]+niveau*2,self.__type_info["PV"]+niveau*10,XP)

    def get_image(self):
        return self.__type_info["image"]
    
    def get_fort(self):
        return self.__type_info["fort"]
    
    def get_faible(self):
        return self.__type_info["faible"]
    
    def get_type(self):
        return self.__type1
    
    def get_type2(self):
        return self.__type2
    
    def get_competences(self):
        return self.__type_info["competences"]
    
    def get_attaques(self):
        return self.__attaques.get_attaques()
    
    def get_save(self):
        return (self.get_name(),self.get_niveau(),self.__type1,self.__type2,self.get_PV(),self.get_XP())

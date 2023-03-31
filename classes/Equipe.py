from classes.Type import Type


class Equipe(Type):
    
    def __init__(self):
        self.__pokemons=[]
        
    def get_equipe(self):
        return self.__pokemons
    
    def add_pokemon(self,pokemon):
        if len(self.__pokemons)<7:
            self.__pokemons.append(pokemon)
        else:
            return "equipe pleine"
        
    def complete(self):
        if len(self.__pokemons)==6:
            return True
        else:
            return False
        
    def get_save(self):
        equipe_save=[]
        for pokemon in self.__pokemons:
            equipe_save.append(pokemon.get_save())
        return equipe_save
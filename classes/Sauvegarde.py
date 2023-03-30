from json import load,dumps

class Sauvegarde:
    def __init__(self) -> None:
        pass
    
    def save(self,user,pokemon=""):
        try:
            open("saves/data_user.json", "x")
        except:
            nothing=0
        ecrire=open("saves/data_user.json", "r+")
        try:
            donnes=load(ecrire)
        except:
            ecrire.write("{\""+user+"\":\"0\"}")
        else:
            if not(user in donnes.keys()):
                donnes[user] = pokemon
                ecrire.seek(0)
                ecrire.truncate(0)
                ecrire.write(dumps(donnes))
                ecrire.close()
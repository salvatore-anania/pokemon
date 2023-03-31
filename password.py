import re
import hashlib
import time
import json
from random import *
from tkinter import * 
from tkinter.messagebox import *

def test_user(user):
    list=lire()
    user_exist=user in list.keys()
    if user_exist:
        return user
    else:
        return False
        
def test_password(password):
    
    list=lire()
    one_special=re.search('[!@#$%\^&\*]',password)==None
    one_upper= re.search('[A-Z]',password)==None
    one_lower= re.search('[a-z]',password)==None
    one_number=re.search('\d',password)==None
    password_exist=encrypt(password) in list.values()
    if len(password)<8 or password_exist or one_upper or one_lower or one_special or one_number:
        showinfo("ERREUR !", "Mot de passe invalide !")
        return False
    else:
        return encrypt(password)
    
def create():
    password=password_get.get()
    verified_password=test_password(password)
    if verified_password:
        showinfo("VALIDE !", "Utilisateur enregistré !")
        save(user.get(),encrypt(password))

def test_login():
    user_exist=test_user(user.get())
    password=password_get.get()
    list=lire()
    if user_exist and password:
        if user_exist=="admin" and list[user_exist] == encrypt(password):
            admin()
        elif list[user_exist] == encrypt(password):
            connexion()
        else :
            showinfo("ERREUR !", "Mauvais mot de passe !")
            return False
    else:
        showinfo("ERREUR !", "Utilisateur inexistant!")
        return False
            
def encrypt(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def lire():
    with open("data.json", "r+") as affiche:
        test=json.load(affiche)
    return test

def affiche():
    test=lire()
    affichage=""
    count=0
    for i,j in test.items():
        count+=1
        if count<3:
            affichage+= "<<"+i+">>:<<"+j+">>"+"\t\t"
        else:
            affichage+= "<<"+i+">>:<<"+j+">>"+"\n\n"
            count=0
    showinfo("Affichage des mots de passe",affichage)

def save(user, crypte):
    ecrire=open("data.json", "r+")
    donnes=json.load(ecrire)
    donnes[user] = crypte
    ecrire.seek(0)
    ecrire.truncate(0)
    ecrire.write(json.dumps(donnes))
    ecrire.close()
    
def delete(user):
    ecrire=open("data.json", "r+")
    donnes=json.load(ecrire)
    del donnes[user]
    ecrire.seek(0)
    ecrire.truncate(0)
    ecrire.write(json.dumps(donnes))
    ecrire.close()
    showinfo("Utilisateur supprimer","Utilisateur supprimé !")
    admin_change_user.delete(0,END)
    admin()
    
def modifier_password(passord_to_modify):
    password=test_password(passord_to_modify)
    if password:
        save(user.get(), password)
        showinfo("Modification valide","Modification du mot de passe effectué !")
    password_get.delete(0,END)
    password_modifier.delete(0,END)
    admin_password_modifier.delete(0,END)
    
def save_user(user, user_change):
    ecrire=open("data.json", "r+")
    donnes=json.load(ecrire)
    donnes[user_change] = donnes[user]
    del donnes[user]
    ecrire.seek(0)
    ecrire.truncate(0)
    ecrire.write(json.dumps(donnes))
    ecrire.close()
    
def modifier_user_admin(user_to_change,new_user_name):
    if test_user(new_user_name)==False:
        save_user(user_to_change,new_user_name)
        showinfo("Modification valide","Modification de l'utilisateur effectué !")
        admin_change_user.delete(0,END)
        admin_change_user.insert(0,new_user_name)
    else:
        showinfo("Modification impossible","Utilisateur déjà existant !")

def modifier_user(user_to_change,new_user_name):
    if test_user(new_user_name)==False:
        save_user(user_to_change,new_user_name)
        showinfo("Modification valide","Modification de l'utilisateur effectué !")
        user.delete(0,END)
        user.insert(0,new_user_name)
    else:
        showinfo("Modification impossible","Utilisateur déjà existant !")
        
def modifier_admin_password(passord_to_modify):
    password=test_password(passord_to_modify)
    if password:
        save(admin_change_user.get(), password)
        showinfo("Modification valide","Modification du mot de passe effectué !")
        change_password.delete(0,END)

def generate():
    seed(time.time())
    mdp=[]
    for lower in range(5):
        mdp+=chr(randint(97,122))
    for upper in range(5):
        mdp+=chr(randint(65,90))
    for special in range(5):
        my_list=[33,35,36,37,38,42,64,94]
        mdp+=chr(choice(my_list))
    for number in range(5):
        mdp+=str(randint(0,100))
    shuffle(mdp)
    generated = ''.join(mdp)
    password_get.delete(0,END)
    password_get.insert(0,generated)
    
def log_out():
    Frame_connected.pack_forget()
    Frame_admin.pack_forget()
    Frame_change.pack_forget()
    
    Frame_connexion.pack()
    user.delete(0,END)
    password_get.delete(0,END)
    
def connexion():
    Frame_connexion.pack_forget()
    Frame_admin.pack_forget()
    Frame_change.pack_forget()
    
    
    Frame_connected.pack(padx=30, pady=30)
    Frame_user_connected.pack( padx=30, pady=30)
    label_name.pack( padx=5, pady=5)
    change_name.insert(0,user.get())
    change_name.pack( padx=5, pady=5)
    valider_name.pack( padx=5, pady=5)
    password_label.pack(padx=5, pady=5)
    password_modifier.pack(padx=5, pady=5)
    connect.pack(padx=5, pady=5)
    deconnect.pack(padx=5, pady=5)
    
def admin():
    Frame_connexion.pack_forget()
    Frame_connected.pack_forget()
    Frame_change.pack_forget()
    
    Frame_admin.pack(padx=30, pady=30)
    list_password.pack(side = TOP,padx=5, pady=5)
    Frame_admin_connected.pack( padx=30, pady=30)
    test.pack(side = TOP,padx=5, pady=5)
    admin_connected_label.config(font=("Arial", 20),text=user.get())
    admin_connected_label.pack(side = TOP,padx=5, pady=5) 
    
    change_user.pack(side = TOP,padx=5, pady=5)
    admin_change_user.pack(side = TOP,padx=5, pady=5)
    change_user_button.pack(side = TOP,padx=5, pady=5)
    
    admin_password_label.pack(side = TOP,padx=5, pady=5)
    admin_password_modifier.pack(padx=5, pady=5)
    
    admin_deconnect.pack(side=BOTTOM,padx=5, pady=5)
    admin_connect.pack(side=BOTTOM,padx=5, pady=5)

def change():
    if test_user(admin_change_user.get()):
        Frame_connexion.pack_forget()
        Frame_admin.pack_forget()
        Frame_admin_connected.pack_forget()
        
        
        Frame_change.pack(padx=30, pady=30)
        Frame_user_change.pack( padx=30, pady=30)
        
        change_username.insert(0,admin_change_user.get())
        change_user_label.pack( padx=5, pady=5)
        change_username.pack( padx=5, pady=5)
        valider_user.pack( padx=5, pady=5)
        
        change_password_label.pack(padx=5, pady=5)
        change_password.pack(padx=5, pady=5)
        
        to_delete.pack(side=BOTTOM,padx=5, pady=5)
        valider_password.pack(side=BOTTOM,padx=5, pady=5)
        go_back.pack(side=BOTTOM,padx=5, pady=5)
        
    else:
        showinfo("Modification impossible","Utilisateur inexistant !")
        admin()
        
def retour():
    change_username.delete(0,END)
    test_login()

fenetre = Tk()
fenetre.title("Password")
fenetre.configure(bg='grey')

Frame_connexion= Frame(fenetre,bg='grey')


#agencement de la frame connexion

Frame_user = Frame(Frame_connexion, borderwidth=2, relief=GROOVE)
Frame_user.pack( padx=30, pady=30)
Label(Frame_user, font=("Arial", 20),text="Utilisateur :").pack(side = TOP,padx=5, pady=5)
user = Entry(Frame_user,font=("Arial", 20), width=30)
user.pack(side = TOP,padx=5, pady=5)
password_label=Label(Frame_user, font=("Arial", 20),text="Mot de passe :")
password_label.pack(padx=5, pady=5)
password_get = Entry(Frame_user,font=("Arial", 20), width=30)
password_get.pack(padx=5, pady=5)
genere=Button(Frame_user, font=("Arial", 20),text="Generer un mot de passe", bg="grey" , command=generate)
genere.pack(padx=5, pady=5)
connect=Button(Frame_user, font=("Arial", 20),text="Connexion", bg="grey" , command=test_login)
connect.pack(side=BOTTOM,padx=5, pady=5)
creation=Button(Frame_user, font=("Arial", 20),text="Créer le compte.", bg="green",command=create)
creation.pack(side = BOTTOM, padx=5, pady=5)
Frame_connexion.pack()

Button(fenetre, font=("Arial", 20),text="Quitter", bg="red" , command=fenetre.quit).pack(side=BOTTOM,padx=5, pady=5)

Frame_connected= Frame(fenetre,bg='grey')

#agencement de la frame connected
Frame_user_connected = Frame(Frame_connected, borderwidth=2, relief=GROOVE)
label_name=Label(Frame_user_connected, font=("Arial", 20),text="Nom d'utilisateur :")
change_name = Entry(Frame_user_connected,font=("Arial", 20), width=30)
valider_name=Button(Frame_user_connected, font=("Arial", 20),text="Changer de nom", bg="grey" , command=lambda: modifier_user( user.get() , change_name.get()))

password_label=Label(Frame_user_connected, font=("Arial", 20),text="Modifier mot de passe :")
password_modifier = Entry(Frame_user_connected, font=("Arial", 20),width=30)

connect=Button(Frame_user_connected, font=("Arial", 20),text="Changer le mot de passe", bg="grey" , command=lambda: modifier_password(password_modifier.get()))
deconnect=Button(Frame_user_connected, font=("Arial", 20),text="Deconnexion", bg="red" , command=log_out)

Frame_admin= Frame(fenetre,bg='grey')
#agencement de la frame admin
list_password=Button(Frame_admin, font=("Arial", 20),text="Afficher les mots de passe", command=affiche)
Frame_admin_connected = Frame(Frame_admin, borderwidth=2, relief=GROOVE)
test=Label(Frame_admin_connected, font=("Arial", 20),text="Nom d'utilisateur :")
admin_connected_label=Label(Frame_admin_connected, font=("Arial", 20),text="")

change_user=Label(Frame_admin_connected, font=("Arial", 20),text="Modifier un utilisateur :")
admin_change_user = Entry(Frame_admin_connected,font=("Arial", 20), width=30)
change_user_button=Button(Frame_admin_connected, font=("Arial", 20),text="Modifier l'utilisateur", bg="grey" , command=change)

admin_password_label=Label(Frame_admin_connected, font=("Arial", 20),text="Modifier mot de passe administrateur :")
admin_password_modifier = Entry(Frame_admin_connected,font=("Arial", 20), width=30)
admin_deconnect= Button(Frame_admin_connected, font=("Arial", 20),text="Deconnexion", bg="red" , command=log_out)
admin_connect= Button(Frame_admin_connected, font=("Arial", 20),text="Modifier mot de passe administrateur", bg="grey" , command=lambda: modifier_password(admin_password_modifier.get()))


Frame_change= Frame(fenetre,bg='grey')

#agencement de la frame change
Frame_user_change = Frame(Frame_change, borderwidth=2, relief=GROOVE)

change_user_label= Label(Frame_user_change, font=("Arial", 20),text="Changer le nom d'utilisateur :")
change_username = Entry(Frame_user_change,font=("Arial", 20), width=30)
valider_user=Button(Frame_user_change, font=("Arial", 20),text="Changer le nom d'utilisateur", bg="grey" , command=lambda: modifier_user_admin( admin_change_user.get() , change_username.get()))

change_password_label=Label(Frame_user_change, font=("Arial", 20),text="Modifier le mot de passe:")
change_password = Entry(Frame_user_change,font=("Arial", 20), width=30)

valider_password=Button(Frame_user_change, font=("Arial", 20),text="Modifier le mot de passe", bg="grey" , command=lambda: modifier_admin_password(change_password.get()))
to_delete=Button(Frame_user_change, font=("Arial", 20),text="supprimer", bg="grey" , command= lambda: delete( admin_change_user.get()))
go_back=Button(Frame_user_change, font=("Arial", 20),text="Retour", bg="red" , command= retour)
fenetre.mainloop()

from tkinter import *


ma_fenetre = Tk()
ma_fenetre.geometry("1000x670")
ma_fenetre.resizable(False,False)
ma_fenetre.config(bg="white")




# PARTIE 1 DU TABLEAU 

label = Label(ma_fenetre, text="DOMOTIC logiciel", font=("Helvetica", 20,"bold"),bg="white")
label.place(x=20,y=10)


group1 = Frame(ma_fenetre,relief="solid",width=350, height=500,bg="black")
group1.grid(row=1, column=0, padx=10, pady=60)


Canvas(group1,bg="white", width=350,height=550).grid(row=0,column=0,padx=0,pady=0)

# INTRODUCTION DES ELEMENTS DU TABLEAU 1

# Label(group1,text="Domotique",font = ("Vani",12,"bold"),bg="white").place(x=20,y=20)
Label(group1,text="Système de réglage", font=("Helvetica",18,"bold"),bg="white").place(x=20,y=30)

Canvas(group1,bg="black",width=300,height=1).place(x=20,y=80)

# CHAMBRE

Label(group1,text="Chambre",font=("Helvetica",18),bg="white").place(x=20, y=105)
Label(group1,text="Eclairage/ température chambre",font=("Vani",10),bg="white").place(x=20, y=136)
boutonChambre = Button(group1,text="Allumer",font=("Vanu",10),width=12)
boutonChambre.place(x=230,y=105)

bouton = Button(group1,text="température",font=("Helvetica",10,'bold'),width=12,command=ma_fenetre.quit())
bouton.place(x=230,y=135)

# choix_froid = Radiobutton(group1, text="froid", width=3,bg="white",
# variable=sv_categorie, value="froid",
# command=lambda: print(sv_categorie.get()))
# choix_froid.place(x=230,y=135)

# choix_chaud = Radiobutton(group1, text="chaud", width=3,bg="white",
# variable=sv_categorie, value="chaud",
# command=lambda: print(sv_categorie.get()))
# choix_chaud.place(x=285,y=135)


# SALON
Label(group1,text="Salon",font=("Helvetica",18),bg="white").place(x=20, y=180)
Label(group1,text="Eclairage et température salon",font=("Vani",10),bg="white").place(x=20, y=210)
boutonChambre = Button(group1,text="Allumer",font=("Vanu",10),width=12)
boutonChambre.place(x=230,y=180)

bouton = Button(group1,text="température",font=("Helvetica",10,'bold'),width=12,command=ma_fenetre.quit())
bouton.place(x=230,y=210)

# choix_froid = Radiobutton(group1, text="froid", width=3,bg="white",
# variable=sv_categorie, value="froid",
# command=lambda: print(sv_categorie.get()))
# choix_froid.place(x=230,y=210)

# choix_chaud = Radiobutton(group1, text="chaud", width=3,bg="white",
# variable=sv_categorie, value="chaud",
# command=lambda: print(sv_categorie.get()))
# choix_chaud.place(x=285,y=210)

# DOUCHE

Label(group1,text="Douche",font=("Helvetica",18),bg="white").place(x=20, y=255)
Label(group1,text="Eclairage et température douche",font=("Vani",10),bg="white").place(x=20, y=285)
boutonChambre = Button(group1,text="Allumer",font=("Vanu",10),width=12)
boutonChambre.place(x=230,y=255)

bouton = Button(group1,text="température",font=("Helvetica",10,'bold'),width=12,command=ma_fenetre.quit())
bouton.place(x=230,y=285)

# choix_froid = Radiobutton(group1, text="froid", width=3,bg="white",
# variable=sv_categorie, value="froid",
# command=lambda: print(sv_categorie.get()))
# choix_froid.place(x=230,y=285)

# choix_chaud = Radiobutton(group1, text="chaud", width=3,bg="white",
# variable=sv_categorie, value="chaud",
# command=lambda: print(sv_categorie.get()))
# choix_chaud.place(x=285,y=285)

# CUISINE
Label(group1,text="Cuisine",font=("Helvetica",18),bg="white").place(x=20, y=330)
Label(group1,text="Eclairage et température cuisine",font=("Vani",10),bg="white").place(x=20, y=360)
boutonChambre = Button(group1,text="Allumer",font=("Vanu",10),width=12)
boutonChambre.place(x=230,y=330)

bouton = Button(group1,text="température",font=("Helvetica",10,'bold'),width=12,command=ma_fenetre.quit())
bouton.place(x=230,y=360)

# choix_froid = Radiobutton(group1, text="froid", width=3,bg="white",
# variable=sv_categorie, value="froid",
# command=lambda: print(sv_categorie.get()))
# choix_froid.place(x=230,y=360)

# choix_chaud = Radiobutton(group1, text="chaud", width=3,bg="white",
# variable=sv_categorie, value="chaud",
# command=lambda: print(sv_categorie.get()))
# choix_chaud.place(x=285,y=360)

# # JARDIN
Label(group1,text="Jardin",font=("Helvetica",18),bg="white").place(x=20, y=412)
Label(group1,text="Eclairage et température jardin",font=("Vani",10),bg="white").place(x=20, y=440)
boutonChambre = Button(group1,text="Allumer",font=("Vani",10),width=12)
boutonChambre.place(x=230,y=410)

bouton = Button(group1,text="température",font=("Helvetica",10,'bold'),width=12,command=ma_fenetre.quit())
bouton.place(x=230,y=440)

# choix_froid = Radiobutton(group1, text="froid", width=3,bg="white",
# variable=sv_categorie, value="froid",
# command=lambda: print(sv_categorie.get()))
# choix_froid.place(x=230,y=440)

# choix_chaud = Radiobutton(group1, text="chaud", width=3,bg="white",
# variable=sv_categorie, value="chaud",
# command=lambda: print(sv_categorie.get()))
# choix_chaud.place(x=285,y=440)

# TEXT DE FIN DU GROUPE 1
Label(group1,text = "Cette application a été construite pour \n vous permettre de mieux gérer l'ambiance de votre maison", font=("Helvetica",10),bg="white").place(x = 5, y=500)




# PARTIE 2 DU TABLEAU

group2 = Frame(ma_fenetre,width=600,height=400)
group2.place(x=385, y=60)
canvagroup2 = Canvas(group2,bg="#EDEDED", width=600,height=400)
canvagroup2.grid(row=0,column=0,padx=0)

titreGroup2 = Frame(group2,width=350,height=70,bg="#EDEDED")
Label(titreGroup2,text= "Maison", font=("Helvetica",22,"bold")).place(x=190, y=20)
canvaTitre = Canvas(titreGroup2,width=40)
photoTitre = PhotoImage(file = 'img/Vector.png')
item = canvaTitre.create_image(20,40,image = photoTitre)
titreGroup2.place(x=40,y=20)
canvaTitre.place(x=300,y=0)

# canevas1 = Canvas(group2, width=100, height=100, bg="white")
# Canvas(canevas1,bg="black",width=100, height=100).grid(row=0,column=0,padx=1)
# photo = PhotoImage(file='img/shower_svgrepo.com.png')
# item = canevas1.create_image(50, 50, image=photo)
# canevas1.place(x=10,y=10)


frame = Frame(group2, width=100, height=108, bg="white", highlightbackground="black", highlightthickness=2)
canevas1 = Canvas(frame, width=92, height=100, bg = "white")
photo1 = PhotoImage(file='img/bedroom-hotel_svgrepo.com.png')
item = canevas1.create_image(50, 50, image=photo1)
canevas1.place(x=0,y=0)
frame.place(x=80,y=100)

frame = Frame(group2, width=100, height=108, bg="white", highlightbackground="black", highlightthickness=2)
canevas2 = Canvas(frame, width=92, height=100, bg = "white")
photo2 = PhotoImage(file='img/living-room-sofa_svgrepo.com.png')
item = canevas2.create_image(50, 50, image=photo2)
canevas2.place(x=0,y=0)
frame.place(x=255,y=100)


frame = Frame(group2, width=100, height=108, bg="white", highlightbackground="black", highlightthickness=2)
canevas3 = Canvas(frame, width=92, height=100, bg = "white")
photo3 = PhotoImage(file='img/shower_svgrepo.com.png')
item = canevas3.create_image(50, 50, image=photo3)
canevas3.place(x=0,y=0)
frame.place(x=430,y=100)

frame = Frame(group2, width=100, height=108, bg="white", highlightbackground="black", highlightthickness=2)
canevas4 = Canvas(frame, width=92, height=100, bg = "white")
photo4 = PhotoImage(file='img/kitchen-room_svgrepo.com.png')
item = canevas4.create_image(50, 50, image=photo4)
canevas4.place(x=0,y=0)
frame.place(x=80,y=250)

frame = Frame(group2, width=100, height=108, bg="white", highlightbackground="black", highlightthickness=2)
canevas5 = Canvas(frame, width=92, height=100, bg = "white")
photo5 = PhotoImage(file='img/garden-planting-flower_svgrepo.com.png')
item = canevas5.create_image(50, 50, image=photo5)
canevas5.place(x=0,y=0)
frame.place(x=255,y=250)




# PARTIE 3 DU TABLEAU 

group3 = Frame(ma_fenetre)
group3.place(x=385, y=490)
canvagroup3 = Canvas(group3,bg="#A0A0A0", width=600,height=130)
canvagroup3.grid(row=0,column=0,padx=0)

frame = Frame(group3, width=180, height=108, bg="white", highlightbackground="black", highlightthickness=2)
canevas6 = Canvas(frame, width=170, height=100, bg = "white")
photo6 = PhotoImage(file='img/garden-planting-flower_svgrepo.com.png')
item = canevas6.create_image(50, 50, image=photo6)
canevas6.place(x=0,y=0)
frame.place(x=20,y=10)

frame = Frame(group3, width=100, height=108, bg="white", highlightbackground="black", highlightthickness=2)
canevas7 = Canvas(frame, width=92, height=100, bg = "white")
photo7 = PhotoImage(file='img/garden-planting-flower_svgrepo.com.png')
item = canevas7.create_image(50, 50, image=photo7)
canevas7.place(x=0,y=0)
frame.place(x=255,y=250)

frame = Frame(group3, width=100, height=108, bg="white", highlightbackground="black", highlightthickness=2)
canevas8 = Canvas(frame, width=92, height=100, bg = "white")
photo8 = PhotoImage(file='img/garden-planting-flower_svgrepo.com.png')
item = canevas8.create_image(50, 50, image=photo8)
canevas8.place(x=0,y=0)
frame.place(x=255,y=250)

ma_fenetre.mainloop() 


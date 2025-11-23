from tkinter import *
from fonction import *

ma_fenetre = Tk()
ma_fenetre.geometry("1000x670")
ma_fenetre.resizable(False,False)
ma_fenetre.config(bg="white")


Na = IntVar()



# PARTIE 1 DU TABLEAU 

label = Label(ma_fenetre, text="DOMOTIC logiciel", font=("Helvetica", 20,"bold"),bg="white")
label.place(x=20,y=10)


group1 = Frame(ma_fenetre,relief="solid",width=350, height=560,highlightthickness=1,highlightbackground="black",bg="white")
group1.place(x = 20, y = 60)

# INTRODUCTION DES ELEMENTS DU TABLEAU 1

#TITRE SYSTEME DE REGLAGE
Label(group1,text="Système de réglage", font=("Helvetica",18,"bold"),bg="white").place(x=20,y=30)

Canvas(group1,bg="black",width=310,height=1).place(x=20,y=80)

frameCanvas = Frame(group1,width=335,height=400,bg="#f2e9e7")
frameCanvas.place(x=0,y=95)

canvas = Canvas(frameCanvas,bg="gray",height=370,width=320)
canvas.pack(padx=2,side=LEFT,fill=BOTH)

scrollbar = Scrollbar(frameCanvas,orient=VERTICAL,width=15,command=canvas.yview)
scrollbar.pack(side=RIGHT,fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)

frame_list = Frame(canvas, bg="gray")

canvas_window = canvas.create_window((0, 0), window=frame_list, anchor="nw")

def update_frame_width(event):
    canvas.itemconfig(canvas_window, width=event.width)

canvas.bind("<Configure>", update_frame_width)

monCreation = Creation() 
ajout = Button(group1,text="+", font=("Helvetica",13,'bold'),width=4,command=lambda: monCreation.appelLabel(frame_list,frame_list2,group3))
ajout.place(relx=0.8,y=30)

        
        

# Mettre à jour le scrollregion
def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame_list.bind("<Configure>", update_scrollregion)




# TEXT DE FIN DU GROUPE 1
Label(group1,text = "Cette application a été construite pour \n vous permettre de mieux gérer l'ambiance de votre maison", font=("Helvetica",10),bg="white").place(x = 1, y=500)








# PARTIE 2 DU TABLEAU

# INTERFACE
group2 = Frame(ma_fenetre,width=600,height=400)
group2.place(x=385, y=60)

frameCanvas2 = Frame(group2,width=335,height=40)
frameCanvas2.place(x=0,y=0)

canvasGroup2 = Canvas(frameCanvas2,height=400,width=560)
canvasGroup2.pack(padx=10,side=LEFT,fill=BOTH)

scrollbarGroup2 = Scrollbar(frameCanvas2,orient=VERTICAL,width=15,command=canvasGroup2.yview)
scrollbarGroup2.pack(side=RIGHT,fill=Y)

canvasGroup2.configure(yscrollcommand=scrollbarGroup2.set)

frame_list2 = Frame(canvasGroup2)

canvas_window = canvasGroup2.create_window((0, 0), window=frame_list2, anchor="nw")

def update_frame_width(event):
    canvasGroup2.itemconfig(canvas_window, width=event.width)

canvasGroup2.bind("<Configure>", update_frame_width)

# Mettre à jour le scrollregion
def update_scrollregion(event):
    canvasGroup2.configure(scrollregion=canvasGroup2.bbox("all"))

frame_list2.bind("<Configure>", update_scrollregion)
#TITRE DU TABLEAU 








# PARTIE 3 DU TABLEAU 

#CORPS 
group3 = Frame(ma_fenetre)
group3.place(x=385, y=490)
canvagroup3 = Canvas(group3,bg="#A0A0A0", width=600,height=130)
canvagroup3.grid(row=0,column=0,padx=0)
    
labelAjt = Label(group3,text="Ajouter des éléments \npour pouvoir intéragir \navec vos piècces",font=("Helvetica",18,"bold"),bg="#A0A0A0",fg="white")
labelAjt.place(x=190, y= 20)



#PARTIE 






ma_fenetre.mainloop() 


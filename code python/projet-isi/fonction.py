from tkinter import *

class Creation:
    def __init__(self):
        self.etat_global = False
        self.tableauCanvas = []
        self.tableauButton = []
        self.photo1 = PhotoImage(file='img/saturn_svgrepo.com.png')
        self.photo2 = PhotoImage(file='img/Vectorlampe.png')

    def appelLabel(self, fene, fene2, group3):
        fenetre = Toplevel()
        fenetre.title("Réglage de la température")
        fenetre.geometry("400x150")
        fenetre.resizable(False, False)
        fenetre.config(bg="white")

        self.alignementY = 100

        label = Label(fenetre, text="Donnez un nom a votre pièce", font=("Helvetica", 13, "bold"))
        label.place(relx=0.2, rely=0.1)

        labelEntry = Entry(fenetre, font=("Helvetica", 12), highlightbackground="black", highlightthickness=1)
        labelEntry.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.3, anchor=CENTER)

        bouton = Button(fenetre, text="ok", command=lambda: self.ajt(fene, fene2, labelEntry, group3))
        bouton.place(x=310, y=63)

        boutonQuit = Button(fenetre, text="Quitter", width=20, command=lambda: self.quitter(fenetre))
        boutonQuit.place(relx=0.5, rely=0.8, anchor=CENTER)

        fenetre.mainloop()

    def ajt(self, fene, fene2, labelEntry, group3):
        valeur = labelEntry.get()
        if valeur.strip():
            # Création d'un cadre pour chaque ligne
            ligne = Frame(fene, bg="white")
            ligne.pack(fill=X, padx=3, pady=5)  # fill=X pour étendre la ligne horizontalement

            # Label Contenant les éléments (aligné à gauche)
            Label(ligne, text=valeur, font=("Helvetica", 18), bg="white").pack(side=TOP, padx=5)
            Label(ligne, text=f"Eclairage/ température {valeur}", font=("Vani", 10), bg="white").pack(side=TOP, anchor="center", pady=2)

            # Création du Canvas
            ligne2 = Frame(fene2, bg="white")
            ligne2.pack(fill=X, padx=3, pady=5)
            frame = Frame(ligne2, width=100, height=10, bg="white", highlightbackground="black", highlightthickness=2)
            canevas1 = Canvas(frame, width=92, height=20)

            labelTitre = Label(ligne2, text=f"{valeur}", font=("Helvetica", 20, "bold"), bg="white")

            label_figure = Label(frame, text=f"{valeur[0].upper()}", font=("Helvetica", 20, "bold"), bg="white", width=0, height=0)
            label_deg = Label(frame, text="°C", font=("Helvetica", 12, "bold"), bg="white")

            boutonSupp = Button(ligne, text="supprimer", font=("Helvetica", 10, "bold"), width=12, command=lambda: self.suppression_element(ligne, ligne2,self.tableauButton,self.tableauCanvas))

            boutonCouleur = Bouton()  # Création de l'objet Bouton pour changer la couleur
            boutonAllumer = Button(ligne, text="Allumer", font=("Vanu", 10, "bold"), width=12, command=lambda: boutonCouleur.changer_couleur(canevas1, boutonAllumer))
            boutonAllumer.pack(side=LEFT, pady=10)
            
            

            appeltemp = Temperature()
            bouton = Button(ligne, text="Température", font=("Helvetica", 10, "bold"), width=12, command=lambda: appeltemp.changer_temperature(label_deg))
            bouton.pack(side=LEFT)

            # Placement des widgets
            self.boutonAmbiance(group3)

            label_deg.pack(padx=0, pady=10)
            label_figure.pack(padx=0, pady=0)
            canevas1.pack(padx=4)
            frame.pack(padx=4, side=LEFT)
            labelTitre.pack(padx=20, side=LEFT)
            boutonSupp.pack(side=LEFT)

            self.tableauCanvas.append(canevas1)
            self.tableauButton.append(boutonAllumer)

    def boutonAmbiance(self, group3):
        
        
        boutonLumiere = Button(group3, width=150, height=80, bg="white", text="lumière", compound="top", image=self.photo2, bd=4, command=lambda: self.changer_couleur_tous(self.tableauCanvas, self.tableauButton))
        boutonLumiere.place(x=50, y=20)

        Label(group3, text="Allumer toutes les lumières", font=("Helvetica", 19, "bold"), bg="#A0A0A0", fg="white").place(x=210, y= 5,relheight=0.9,relwidth=0.6)

    def quitter(self,fenetre):
        fenetre.destroy()
        
        
    def suppression_element(self, ligne, ligne2,tableauCanvas,tableauButton):
        ligne.destroy()
        ligne2.destroy()
        
        def increSupp(self,tableauCanvas,tableauButton):
            for i in range(0,len(tableauCanvas)):
                for j in range(0,len(tableauButton)):
                    del tableauCanvas[i]
                    del tableauButton[j]
            
        return increSupp
        
        
    
    
        

    def changer_couleur_tous(self, tableauCanvas, tableauButton):
        self.etat_global = not self.etat_global
        for canvas, bouton in zip(tableauCanvas, tableauButton):
            if canvas.winfo_exists():  
                if self.etat_global:
                    canvas.config(bg="yellow")
                    bouton.config(text="Éteindre")
                else:
                    canvas.config(bg="white")
                    bouton.config(text="Allumer")

                
                
class Bouton:
    def __init__(self):
        self.etat = False   

    def changer_couleur(self, canvas, text):
        self.etat = not self.etat
        
        if self.etat:
            canvas.config(bg="yellow")
            text.config(text="Éteindre")
        else:
            canvas.config(bg="white")
            text.config(text="Allumer")
    

class Temperature:
    def __init__(self):
        self.etat = False
        self.labelAmbiance = None
        
        
        
    def changer_temperature(self,labelchange):
        
        root = Toplevel()
        root.title("Réglage de la température")
        root.geometry("400x150")
        root.resizable(False,False)
        root.config(bg = "white")
        newFrame = Frame(root,width=200,height=100,bg="white")
        self.valeur = IntVar()
        modif = Scale(newFrame, from_=0, to=28, orient=HORIZONTAL,variable=self.valeur)
        modif.pack(pady=10)
        newFrame.pack(padx=10,pady=5)
        modif.pack(padx=5,pady=2)
        
        label = Label(newFrame, text="Réglage de la température", font=("Helvetica", 14))
        label.pack(pady=10)
        bouton_valider = Button(newFrame, text="Valider", command=lambda: self.affiche(root,labelchange))
        bouton_valider.pack(pady=10)
        root.mainloop()
        
        
    def affiche(self,root,labelchange):
        iv = self.valeur.get()
        labelchange.config(text =f"{iv}°C")
        root.destroy()

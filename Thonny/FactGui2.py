from tkinter import *
from tkinter.messagebox import *

# création d'une première fenêtre
window = Tk()
# personnalisation de la fenêtre
# changer le titre
window.title("Calcul Factorielle")
# changer la taille
window.geometry("480x360")
window.minsize(480, 360)
# message afficher (label)
label_title = Label(window, text="Entrez un nombre entier")
label_title.pack()


def calculate():
    fact = 1
    N = input.get()
    try:
        N = int(N)
    except ValueError:
        showerror("ATTENTION", "La valeur que vous avez entré est invalide veuillez inscrire un nombre entier")

    if N == 0:
        showinfo("Résultat du calcul", f"La factorielle de {N} est {fact}")
    elif N < 0:
        showerror("ATTENTION", "Vous ne pouvez pas inscrire de valeurs négatives, veuillez relancer le programme")
    else:
        for i in range(1, N + 1):
            fact = fact * i
        showinfo("Résultat du calcul", f"La factorielle de {N} est {fact}")


value = StringVar()
input = Entry(window, textvariable=value, width=30)
input.pack()

calculate_button = Button(window, text="Calculer", command=calculate)
calculate_button.pack()

# afficher
window.mainloop()
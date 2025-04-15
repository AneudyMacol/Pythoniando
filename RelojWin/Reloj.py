import tkinter as tk
from time import strftime

class RelojDePared:
    def __init__(self, root):
        self.root = root
        self.root.title("Reloj de Pared")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        self.label_hora = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
        self.label_hora.pack(expand=True)

        self.actualizar_hora()

    def actualizar_hora(self):
        hora_actual = strftime("%H:%M:%S")
        self.label_hora.config(text=hora_actual)
        self.root.after(1000, self.actualizar_hora)

if __name__ == "__main__":
    root = tk.Tk()
    reloj = RelojDePared(root)
    root.mainloop()
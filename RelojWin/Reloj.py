import tkinter as tk
from time import strftime

class RelojDePared:
    def __init__(self, root):
        self.root = root
        self.root.title("Reloj de Pared")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        # Centralizar la ventana
        self.centralizar_ventana(400, 400)

        self.label_hora = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
        self.label_hora.pack(expand=True)

        self.actualizar_hora()

    def centralizar_ventana(self, ancho, alto):
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (alto_pantalla // 2) - (alto // 2)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")

    def actualizar_hora(self):
        hora_actual = strftime("%H:%M:%S")
        self.label_hora.config(text=hora_actual)
        self.root.after(1000, self.actualizar_hora)

if __name__ == "__main__":
    root = tk.Tk()
    reloj = RelojDePared(root)
    root.mainloop()
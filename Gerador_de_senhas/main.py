from tkinter import *
from random import choice
import random, string
root = Tk()
root.geometry("310x210")
root.configure(background="#000000")




class Gerador_De_Senhar:
    def __init__(self, master=None):
        self.conteiner1 = Frame(master,bg="#5C4033")
        self.conteiner1["pady"]=9
        self.conteiner1["padx"]=10
        self.conteiner1.pack()

        self.conteiner2 = Frame(master)
        self.conteiner2.pack()

        self.conteiner3 = Frame(master,bg="#000000")
        self.conteiner3.pack()

        self.titulo = Label(self.conteiner1,text="Gerador de Senhas", background="#5C4033", fg="#FFFFFF",padx=70)
        self.titulo["font"]="Arial", "20", "bold"
        self.titulo.pack()

        self.resposta =Label(self.conteiner2, text="--",background="#FFFFFF",fg="#000000",padx=145)
        self.resposta["font"] = "Arial", "20", "bold"
        self.resposta.pack()

        self.gerar = Button(self.conteiner3, text="GERAR")
        self.gerar["font"]="Arial", "15", "bold"
        self.gerar["command"]= self.Gerar_Senha
        self.gerar.pack(pady=35)

    def Gerar_Senha(self):
        senha = ""
        tamanho = 12
        caracteres = string.ascii_letters + string.digits + string.punctuation
        c=0
        while c != tamanho:
            senha += choice(caracteres)
            c+=1
            if c == 12:
                self.resposta["text"] = senha

Gerador_De_Senhar(root)
root.mainloop()
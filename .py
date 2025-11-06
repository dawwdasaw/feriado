import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Selecione o arquivo", filetypes=[("PDF", "*.PDF"), ("All files", "*.*")])
    if file_path:
        
        process_file(file_path)

def ler_pdf(file_path):
    p = 'a'
   


def Exemplo():
    root = tk.Tk()
    root.title("Quando é feriado")
    root.geometry('200x200')
    root.resizable(False, False)
    
    test = tk.Button(root, text="Selecione o arquivo", command=open_file_dialog) 
    test.pack()
    
    root.mainloop()

Exemplo()
import webbrowser
from tkinter import *
import tkinter as tk
from tkinter import ttk
from os.path import exists


#checks if the file has been created to determine whether to create or update the index.html file
def createHTML(self):
    fileName = 'index.html'
    if not exists('index.html'):
        f = open(fileName, "x")
    f = open(fileName, 'w')
    f.write("<html><body><h1>" + self.txt_content.get() + "</h1></body></html>")
    f.close()
    webbrowser.open_new_tab(fileName)

#creates an ugly but functional GUI
def loadGUI(self):
    self.lbl_header = tk.Label(self.master, text='Enter HTML Content')
    self.lbl_header.grid(row=0, column=0, columnspan=2, padx=30, pady=30)

    self.txt_content = tk.Entry(self.master, text='')
    self.txt_content.grid(row=1, column=0, columnspan=2)

    self.btn_update = tk.Button(self.master, width=10, height=5, text='Update', command=lambda: createHTML(self))
    self.btn_update.grid(row=2, column=2)

#generates a parent window that the GUI loads in
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500, 300)
        self.master.maxsize(500, 300)
        
        loadGUI(self)
        
#main method
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

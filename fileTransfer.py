import shutil, os, sys, time
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog

#syncs source files to destination
def sync(self):
    source = self.txt_src.get() + '/'
    destination = self.txt_dst.get() + '/'
    working = os.listdir(source)
    backup = os.listdir(destination)
    for i in working:
        if i not in backup:
            shutil.copy(source+i, destination)
        else:
           if os.stat(source+i).st_mtime > os.stat(destination+i).st_mtime:
             shutil.copy(source+i, destination)

#gets user input for source directory and updates text field
def updateSrc(self):
    source = tk.filedialog.askdirectory();
    self.txt_src.delete(0, END)
    self.txt_src.insert(0, source)

#gets user input for destination directory and updates text field
def updateDst(self):
    destination = tk.filedialog.askdirectory();
    self.txt_dst.delete(0, END)
    self.txt_dst.insert(0, destination)
         
#creates a GUI for selecting a source and destination directory to sync
def loadGUI(self):
    self.lbl_src = tk.Label(self.master, text='Source Directory', font=(25))
    self.lbl_src.grid(row=0, column=0, padx=(0,0), pady=(0,0), sticky=NW)
    self.lbl_dst = tk.Label(self.master, text='Destination Directory', font=(25))
    self.lbl_dst.grid(row=2, column=0, padx=(0,0), pady=(20,0), sticky=NW)

    self.txt_src = tk.Entry(self.master, width=65, text='')
    self.txt_src.grid(row=1, column=0, padx=(10,0), pady=(10,0), sticky=NW)
    self.txt_dst = tk.Entry(self.master, width=65, text='')
    self.txt_dst.grid(row=3, column=0, padx=(10,0), pady=(10,0), sticky=NW)

    self.btn_src = tk.Button(self.master, width=5, height=1, text='...', command=lambda: updateSrc(self))
    self.btn_src.grid(row=1, column=1, padx=(40,0), pady=(5,0), sticky=NW)
    self.btn_dst = tk.Button(self.master, width=5, height=1, text='...', command=lambda: updateDst(self))
    self.btn_dst.grid(row=3, column=1, padx=(40,0), pady=(5,0), sticky=NW)
    self.btn_update = tk.Button(self.master, width=12, height=2, text='Update', command=lambda: sync(self))
    self.btn_update.grid(row=4, column=1, padx=(0,0), pady=(27,0), sticky=NW)
    

#generates a parent window that the GUI loads in
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500, 200)
        self.master.maxsize(500, 200)
        self.master.title("File Transfer")
        self.master.configure(bg="#F0F0F0")
        loadGUI(self)
        
#main method
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

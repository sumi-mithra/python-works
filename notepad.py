from Tkinter import *
#import Tkinter as tk
from tkFileDialog import *

from ScrolledText import ScrolledText


class Notepad(ScrolledText):

     #filename=None 
 
     def newFile(self,event=None): 
        global filename
        filename="untitle"
        
        text=self.delete(0.0,END)

     def saveFile(self,event=None):
        global filename
        text=self.get(0.0,END)
        f=self.open(filename,'w')
        f.write(text)
        f.close()
    
     def saveAs(self,event=None):
        f=asksaveasfile(mode='w',defaultextension='.txt')
        text=self.get(0.0,END)
        try:
            f.write(text.rstrip())
        except:
            showerror(title="oops",message="unable to save file")

     def exit():
        root.destroy()
	
     def openFile(self,event=None):
        f=askopenfile(mode='r')
        t=f.read()
        text=self.delete(0.0,END)
        text=self.insert(0.0,t)
        
     def cut(self, event=None):
        self.copy()
        self.delete("sel.first", "sel.last")

     def copy(self, event=None):
        self.clipboard_clear()
        text = self.get("sel.first", "sel.last")
        self.clipboard_append(text)

     def paste(self, event=None):
        text = self.selection_get(selection='CLIPBOARD')
        self.insert('insert', text)





root=Tk()
#root.title("my python")
#root.minsize(width=400,height=400)
#root.maxsize(width=400,height=400)
#text=Text(root,width=400,height=400)
#text.pack()

root.title(' My Editor')
root.minsize(width=100, height=100)
root.geometry('800x500+350+150') #Height, Width, X, Y coordinates of the program

    #NotePad
notepad = Notepad(root, width=1000, height=100) 
    #Height and width of notepad
notepad.pack()

menubar=Menu(root)
filemenu=Menu(menubar)
filemenu.add_command(label="New",command=notepad.newFile)
filemenu.add_command(label="Open",command=notepad.openFile)
filemenu.add_command(label="Save",command=notepad.saveFile)
filemenu.add_command(label="SaveAs",command=notepad.saveAs)

filemenu.add_separator()
filemenu.add_command(label="quit",command=exit)
menubar.add_cascade(label="FILE",menu=filemenu)

editmenu=Menu(menubar)
editmenu.add_command(label="cut",command = notepad.cut)
editmenu.add_command(label="copy",command = notepad.copy)
editmenu.add_command(label="paste",command = notepad.paste)
menubar.add_cascade(label="EDIT",menu=editmenu)
menubar.add_cascade(label="FORMAT",menu=editmenu)
menubar.add_cascade(label="HELP",menu=editmenu)
root.config(menu=menubar)
root.mainloop()

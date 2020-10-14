from tkinter import Menu, messagebox as msg, filedialog, Tk
from nltk  import tokenize
from analyze import showcharacters, showcharactersex

class TextAnalyzer():
    def __init__(self,master):
        self.master = master
        self.master.title("TextAnalyzer")
        self.master.geometry("250x200")
        self.master.resizable(False,False)
        self.filename = ""
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Insert File", accelerator= 'Ctrl+O', command = self.insert_txt)
        self.file_menu.add_command(label="Close File", accelerator = 'Ctrl+F4', command = self.closefile)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)

        self.show_menu = Menu(self.menu, tearoff = 0)
        self.show_menu.add_command(label= "Show Number of characters", command = self.showcharacters)
        self.show_menu.add_command(label= "Show Number of words", command =self.shownumberofwords)
        self.menu.add_cascade(label="Show", menu=self.show_menu)


        self.about_menu = Menu(self.menu, tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event: self.aboutmenu())

    def showcharacters(self):
        if not ".txt" in self.filename:
            msg.showerror("ERROR", "NO TXT IMPORTED")
        else:
            msg.showinfo("Characters(including spaces):",showcharacters(self.line))

    def showcharactersex(self):
        if not ".txt" in self.filename:
            msg.showerror("ERROR", "NO TXT IMPORTED")
        else:
            msg.showinfo("Characters(exincluding spaces):",showcharactersex(self.line))

    
    def shownumberofwords(self):
        if not ".txt" in self.filename:
            msg.showerror("ERROR", "NO TXT IMPORTED")
        else:
            msg.showinfo("Words:",tokenize.word_tokenize(self.line))
    
    def closefile(self):
        if not ".txt" in self.filename:
            msg.showerror("ERROR", "NO TXT TO CLOSE")
        else:
            self.filename = ""
            msg.showinfo("SUSSESS", "YOUR TXT FILE HAS SUCCESFULLY CLOSED")

    def insert_txt(self):
        if self.filename == "":
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select txt file",
                                                       filetypes=(("txt files", "*.txt"),
                                                                  ("all files", "*.*")))
            if not ".txt" in self.filename:
                self.filename = ""
                msg.showerror("ERROR", "NO TXT IMPORTED")
            else:
                file  = open(str(self.filename), "r")
                self.line = file.read()
                msg.showinfo("SUCCESS", "TXT FILE ADDED SUCCESSFULLY")
        else:
            msg.showerror("ERROR", " A TXT FILE IS ALREADY OPEN")
    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        pass
    
    def aboutmenu(self):
        pass

        

def main():
    root=Tk()
    TextAnalyzer(root)
    root.mainloop()
    
if __name__=='__main__':
    main()
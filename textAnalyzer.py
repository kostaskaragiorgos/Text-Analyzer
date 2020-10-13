from tkinter import Menu, messagebox as msg, filedialog, Tk

class TextAnalyzer():
    def __init__(self,master):
        self.master = master
        self.master.title("TextAnalyzer")
        self.master.geometry("250x200")
        self.master.resizable(False,False)
        self.filename = ""
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event: self.aboutmenu())
    
    def insert_txt(self):
        if self.filename == "":
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select txt file",
                                                       filetypes=(("txt files", "*.txt"),
                                                                  ("all files", "*.*")))
            if not ".txt" in self.filename:
                self.filename = ""
                msg.showerror("ERROR", "NO TXT IMPORTED")
            else:
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
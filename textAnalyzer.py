""" text Analyzer """
from tkinter import Menu, messagebox as msg, filedialog, Tk
import csv
from nltk  import tokenize
from analyze import showcharacters, showcharactersex


def helpmenu():
    """ help menu function """
    msg.showinfo("Help", "Use the file menu to insert, close  a file and to save the analysis. \nUse the show menu to show the analysis results")

def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "Version 1.0")

class TextAnalyzer():
    """ Text Analyzer class """
    def __init__(self, master):
        self.master = master
        self.master.title("TextAnalyzer")
        self.master.geometry("250x200")
        self.master.resizable(False, False)
        self.filename = ""
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert File", accelerator='Ctrl+O',
                                   command=self.insert_txt)
        self.file_menu.add_command(label="Close File", accelerator='Ctrl+F4',
                                   command=self.closefile)
        self.file_menu.add_command(label="Save as", accelerator='Ctrl+S', command=self.saveas)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)

        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Show Number of characters(including spaces)", accelerator='Ctrl+R', command=self.showcharacters)
        self.show_menu.add_command(label="Show Number of words", accelerator='Alt+R', command=self.shownumberofwords)
        self.show_menu.add_command(label="Show Number of characters(excluding spaces)", accelerator='Ctrl+U', command=self.showcharactersex)
        self.menu.add_cascade(label="Show", menu=self.show_menu)

        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)

        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Control-o>', lambda event: self.insert_txt())
        self.master.bind('<Control-F4>', lambda event: self.closefile())
        self.master.bind('<Control-s>', lambda event: self.saveas())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-r>', lambda event: self.showcharacters())
        self.master.bind('<Alt-r>', lambda event: self.shownumberofwords())
        self.master.bind('<Control-u>', lambda event: self.showcharactersex())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
    def saveas(self):
        """ saves the analysis """
        if self.filename == "":
            msg.showerror("ERROR", "NO TXT FILE")
        else:
            self.filenamesave = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                             filetypes=(("csv files", "*.csv"),
                                                                        ("all files", "*.*")))
            if self.filenamesave is None or self.filenamesave == "":
                msg.showerror("ERROR", "NO FILE SAVED")
            else:
                with open(str(self.filenamesave)+'.csv', 'a+') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(["Number of words", str(len(tokenize.word_tokenize(self.line)))])
                    thewriter.writerow(["Characters(including spaces)", str(showcharacters(self.line))])
                    thewriter.writerow(["Characters(exincluding spaces)", str(showcharactersex(self.line))])
                msg.showinfo("SUCCESS", "CSV FILE SAVED SUCCESSFULLY")


    def showcharacters(self):
        """ shows the number of characters including spaces """
        if not ".txt" in self.filename:
            msg.showerror("ERROR", "NO TXT IMPORTED")
        else:
            msg.showinfo("Characters(including spaces):", showcharacters(self.line))

    def showcharactersex(self):
        """ shows the number of characters excluding spaces """
        if not ".txt" in self.filename:
            msg.showerror("ERROR", "NO TXT IMPORTED")
        else:
            msg.showinfo("Characters(excluding spaces):", showcharactersex(self.line))

    
    def shownumberofwords(self):
        """ shows the number of words """
        if not ".txt" in self.filename:
            msg.showerror("ERROR", "NO TXT IMPORTED")
        else:
            msg.showinfo("Words:", len(tokenize.word_tokenize(self.line)))
    
    def closefile(self):
        """ closes the file """
        if not ".txt" in self.filename:
            msg.showerror("ERROR", "NO TXT TO CLOSE")
        else:
            self.filename = ""
            msg.showinfo("SUSSESS", "YOUR TXT FILE HAS SUCCESFULLY CLOSED")

    def insert_txt(self):
        """ inserts a  .txt file """
        if self.filename == "":
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select txt file",
                                                       filetypes=(("txt files", "*.txt"),
                                                                  ("all files", "*.*")))
            if not ".txt" in self.filename:
                self.filename = ""
                msg.showerror("ERROR", "NO TXT IMPORTED")
            else:
                file = open(str(self.filename), "r")
                self.line = file.read()
                msg.showinfo("SUCCESS", "TXT FILE ADDED SUCCESSFULLY")
        else:
            msg.showerror("ERROR", " A TXT FILE IS ALREADY OPEN")
    
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    

        

def main():
    """ main function """
    root = Tk()
    TextAnalyzer(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()

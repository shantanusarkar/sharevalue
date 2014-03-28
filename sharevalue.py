from Tkinter import *
import tkMessageBox
import urllib2

class App():

    def __init__(self,master):
        frame = Frame(master)
        frame.pack

        self.entrytext = StringVar()
        Label(root, text="Enter NASDAQ value :",width=20).grid(row=0,column=0)
        Entry(root, textvariable=self.entrytext, width=20).grid(row=0,column=1)
        Button(root, text="Check Share Value",width=15, command=self.share).grid(row=1,column=0)
        Button(root, text="Exit", fg="red", command=frame.quit).grid(row=1,column=1)


    def share(self):
        global a
        self.a=self.entrytext.get()
        try:
            x = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s='+self.a+'&f=l1')
            value = float(x.read())
            if value == 0.00:
                tkMessageBox.showerror("Error","NASDAQ code invalid")
            else:
                tkMessageBox.showinfo("Result","The current sharevalue for %s is %f" % (self.a,value))
        except:
             tkMessageBox.showwarning("Warning","failed to open the finance.yahoo.com url. Check your internet connection.")

root = Tk()

app = App(root)
root.mainloop()

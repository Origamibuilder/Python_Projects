
from tkinter import *
 
class Temperatures(Frame):
    '''temperature conversion app'''
 
    def __init__(self,master):
        '''Temperatures(master) -> new temperature conversion window'''
        Frame.__init__(self,master)
        self.grid()
        # set up control variables
        # (tkinter uses DoubleVar() for floats)
        self.fahr = DoubleVar()
        self.cels = DoubleVar()
        # initialize values to freezing point of water
        self.fahr.set(32.0)
        self.cels.set(0.0)
        # set up widgets
        Label(self,text="Fahrenheit").grid(row=0,column=0)
        Label(self,text="Celsius").grid(row=0,column=1)
        Entry(self,textvariable=self.fahr).grid(row=1,column=0)
        Entry(self,textvariable=self.cels).grid(row=1,column=1)
        Button(self,text=">>>>>",command=self.fahr_to_cels).grid(row=2,column=0)
        Button(self,text="<<<<<",command=self.cels_to_fahr).grid(row=2,column=1)
 
    def fahr_to_cels(self):
        self.cels.set((5 * (self.fahr.get() - 32)) / 9)

    def cels_to_fahr(self):
        self.fahr.set(((9 /5) * self.cels.get()) + 32)
 
root = Tk()
root.title('Temperature Conversion')
temps = Temperatures(root)
temps.mainloop()

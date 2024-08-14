# Python Class 3962
# Lesson 7 Problem 3
# Author: origamibuilder (521817)


from tkinter import *

class cps_calculator(Frame):

    def __init__(self, master, time):
        
        
        Frame.__init__(self, master)

        self.inital_time = time

        self.time = time

        self.clicks = 0

    
        
        self.grid()

        self.start_button = Button(self, text = 'Click to start! ', font = ('Arial', 100), padx = 100, pady = 100, command = self.start_test)

        self.start_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.start_button.config(state = NORMAL)

        self.time_label = Label(master, text = f"Time left: Not Started", font = ('Arial', 50), padx = 50, pady=20)

        self.time_label.grid(row = 1, column = 0, padx=10, pady=10)

        self.click_label = Label(master, text = f'{self.clicks}', font = ('Arial', 50), padx = 50, pady=50)

        self.click_label.grid(row = 2, column = 0, padx = 10, pady = 10)

        

    def start_test(self):

        self.start_button.grid_forget()

        self.clicks = 1

        self.click_label['text'] = '1'

        self.Button = Button(self, text = f'Click me!', font = ('Arial', 100), padx = 100, pady=100, command = self.increment)

        self.Button.grid(row = 0, column = 0, padx=10, pady=10)

        self.update_timer()

    def increment(self):
        self.clicks += 1

        self.click_label.config(text = f"{self.clicks}")

    def update_timer(self):
        
        if self.time > 0:
            
            self.time_label.config(text = f"Time left: {self.time}")

            self.time -= 1

            self.master.after(1000, self.update_timer)
        else:

            self.time_label.config(text = f"Time left: 0")
            
            self.output_cps()
        

    def output_cps(self):
        self.Button.config(state = DISABLED)
        self.Button.config(font = ('Arial', 20))
        cps = self.clicks / self.inital_time
        cps = round(cps, 2)
        self.Button['text'] = f"Time's up! Your final cps was {cps}!"
        print(f"\nTime's up! Your final cps was {cps}!")

        
        
        
        
        
        

root = Tk()

root.title('Cps Test!')

length = ''

while not length.isdigit() or not int(length) > 0:
        length = input('What would you like for your cps test length to be (seconds)? ')

length = int(length)

print('Click the button once and continue to start! ')

hwf = cps_calculator(root, length)
hwf.mainloop()        
#

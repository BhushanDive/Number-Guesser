import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import random

class Game:

    def __init__(self):
        self.counter = 0
        self.root = ttk.Window(themename='darkly')
        self.root.title('Guess The Number')

        ### Declarations
            ### Window 1 Labels
        self.title_label = ttk.Label(self.root,text="Guess the Number!",font=('Cascadia Mono',24))
        
        self.Num1_label = ttk.Label(self.root,text="Enter the first Number", font=('Cascadia Mono',16))
        self.Num1_Entry = ttk.Entry(self.root)

        self.Num2_label = ttk.Label(self.root,text="Enter the Second Number", font=('Cascadia Mono',16))
        self.Num2_Entry = ttk.Entry(self.root)

        self.play_btn = ttk.Button(self.root, text="PLAY",bootstyle=SUCCESS, command=self.submit)
            
            ### Window 2 Labels
        self.range_label = ttk.Label(self.root,text="",font=('Cascadia Mono',24))
        self.guess_label = ttk.Label(self.root,text="Take a guess",font=('Cascadia Mono',16))
        self.guess_entry = ttk.Entry(self.root)
        self.hint_label = ttk.Label(self.root,text="",font=('Cascadia Mono',14))
        self.answer_label = ttk.Label(self.root,text="",font=('Cascadia Mono',14))

        self.back_btn = ttk.Button(self.root, text="BACK",bootstyle=DANGER, command=self.back)
        self.guess_btn = ttk.Button(self.root, text="GUESS",bootstyle=INFO, command=self.validate_guess)

        ### Layout Structuring for Window 1
        self.title_label.grid(row=0,column=0,columnspan=5,padx=10,pady=20)

        self.Num1_label.grid(row=1, column=0,sticky=W,padx=10,pady=20)
        self.Num1_Entry.grid(row=1,column=1,sticky=E,padx=10,pady=20)

        self.Num2_label.grid(row=2, column=0,sticky=W,padx=10,pady=20)
        self.Num2_Entry.grid(row=2,column=1,sticky=E,padx=10,pady=20)
        
        self.play_btn.grid(row=3,column=0,columnspan=2,pady=10)
        self.root.mainloop()

    ### Utility Functions
    def submit(self):
        self.get_entry_value()
        self.validate_inputs()
        self.clear_entry_value()
        self.hint_label.config(text="")
        self.answer_label.config(text="")
    
    def clear_entry_value(self):
        self.Num1_Entry.delete(0,ttk.END)
        self.Num2_Entry.delete(0,ttk.END)

    def get_entry_value(self):
        self.num1 = self.Num1_Entry.get()
        self.num2 = self.Num2_Entry.get()
    
    def back(self):
        self.guess_entry.delete(0,ttk.END)
        self.counter = 0
        self.forget_second_window()
        self.draw_first_window()

    ### Drawing First Window 
    def draw_first_window(self):
        self.Num1_label.grid(row=1, column=0,sticky=W,padx=10,pady=20)
        self.Num1_Entry.grid(row=1,column=1,sticky=E,padx=10,pady=20)

        self.Num2_label.grid(row=2, column=0,sticky=W,padx=10,pady=20)
        self.Num2_Entry.grid(row=2,column=1,sticky=E,padx=10,pady=20)
        
        self.play_btn.grid(row=3,column=0,columnspan=2,pady=10)
    
    ### Erase the First Window
    def forget_first_window(self):
        self.Num1_label.grid_forget()
        self.Num1_Entry.grid_forget()

        self.Num2_label.grid_forget()
        self.Num2_Entry.grid_forget()
        self.play_btn.grid_forget()
    
    ### Erase the Second Window 
    def forget_second_window(self):
        self.range_label.grid_forget()
        self.guess_label.grid_forget()
        self.guess_entry.grid_forget()
        self.hint_label.grid_forget()
        self.answer_label.grid_forget()

        self.back_btn.grid_forget()
        self.guess_btn.grid_forget()

    ### Drawing Second Window
    def draw_second_window(self):
        self.range_label.config(text=f"Range is {self.num1} to {self.num2}")
        self.range_label.grid(row=1,column=0,columnspan=2,padx=10,pady=20)
        self.guess_label.grid(row=2,column=0,sticky=W,padx=10,pady=20)
        self.guess_entry.grid(row=2,column=1,sticky=E,padx=10,pady=20)
        self.hint_label.grid(row=3,column=0,columnspan=2)
        self.answer_label.grid(row=4,column=0,columnspan=2)

        self.back_btn.grid(row=5,column=0,sticky=W,padx=10,pady=20)
        self.guess_btn.grid(row=5,column=1,sticky=E,padx=10,pady=20)

    ### Validating range 
    def validate_inputs(self):
        try:
            self.num1 = int(self.num1)
            self.num2 = int(self.num2)
            if self.num1 > self.num2:
                messagebox.showerror("Error !","Invalid Range !")
            elif self.num1 == self.num2:
                messagebox.showerror("Error !","A valid Range is needed")
            else:
                self.mystery_num = random.randint(self.num1,self.num2)
                self.forget_first_window()
                self.draw_second_window()
        except:
            messagebox.showerror("Error !","Either of the two inputs is not numeric.")
            messagebox.showerror("Error !","Please enter numbers !")
    
    ### Validate Guessed Number
    def validate_guess(self):
        try:
            self.guess = int(self.guess_entry.get())
            self.guess_entry.delete(0,ttk.END)
            self.counter += 1
            if self.guess > self.mystery_num:
                self.hint_label.config(text="Number is Too High")
            elif self.guess < self.mystery_num:
                self.hint_label.config(text="Number is Too Low")
            
            if self.guess == self.mystery_num:
                self.hint_label.config(text="You guessed it right !")
                self.answer_label.config(text=f"It took you {self.counter} tries")
        except:
            messagebox.showerror("Error !","Please enter numbers !")



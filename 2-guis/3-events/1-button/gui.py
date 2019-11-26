from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # set window properties
        self.title("TICKETS")
        self.configure(bg="#ccc", padx=20, pady=20)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_ticket_entry()
        self.__add_buy_button()
        self._buy_button_clicked (self, event)

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure( bg="#eee", 
                                    padx=20, 
                                    pady=20)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(   bg="#eee",
                                        font="Arial 14",
                                        text="ENTRANCE TICKETS")

    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, sticky=W)
        self.instruction_label.configure(   bg="#eee",
                                            text="How many tickets are needed?")

    def __add_ticket_entry(self):
        self.ticket_entry = Entry(self.outer_frame)
        self.ticket_entry.grid(row=2, column=0, sticky=W)
        self.ticket_entry.configure(width=20)
    #event

    def __add_buy_button(self):
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0)
        self.buy_button.configure(text="Submit")
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)                                       text="Submit")
    
    def _buy_button_clicked (self, event):
        messagebox.showinfo("Purchased!", "You have purchased the tickets!")
    
    def __buy_button_clicked(self, event):
        num_tickets = int(self.tickets_entry.get())
        if (num_tickets == 1):
            messagebox.showinfo("Purchased", "You have purchased 1 ticket.")
        elif (num_tickets > 1):
            messagebox.showinfo("Purchased", "You have purchased {} tickets".format(num_tickets))
        else:
            messagebox.showerror("Error", "You have entered an invalid number of tickets!")



       
        

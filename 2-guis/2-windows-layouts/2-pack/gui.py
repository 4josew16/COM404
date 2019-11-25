from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # set window properties
        self.title("Newsletter")
        self.configure(bg="#ccc", padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_email_frame()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_subscribe_button()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.pack(fill=X)
        self.outer_frame.configure( bg="#00ffff", 
                                    padx=10, 
                                    pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.pack(fill=X)
        self.heading_label.configure(   bg="#eee",
                                        font="Arial 18",
                                        text="RECEIVE OUR NEWSLETTER")

    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.pack(fill=X)
        self.instruction_label.configure(   bg="#eee",
                                            text="Please enter your email below to receiver our newsletter")

    def __add_email_frame(self):
        self.email_frame = Frame(self.outer_frame)
        self.email_frame.pack(fill=X)

    def __add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side=LEFT)
        self.email_label.configure( padx = 20,
                                    pady=20,
                                    text="Email:")

    def __add_email_entry(self):
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=LEFT)
        self.email_entry.configure(width=40)

    def __add_subscribe_button(self):
        self.subscribe_button = Button(self.outer_frame)
        self.subscribe_button.pack(fill=X)
        self.subscribe_button.configure(bg="white",
                                        text="Subscribe")
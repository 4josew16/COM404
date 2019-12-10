from tkinter import *



class Gui(Tk):

    def __init__(self):
        super().__init__()

    #load resources
        self.tick_image = PhotoImage(file="C:/Users/Wendy/Documents/GitHub/tick2.gif")
        
     # set window properties
        self.configure(bg="#ffe8e8", padx=10, pady=10)

    # add components
       
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_amount_entry()
        self.__add_clear_button()
        self.__add_convert_button()
        self.__add_label_frame()
        self.__add_message_label()
        self.__add_tick_image_label()

    
    # create heading label
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=4)
        self.heading_label.configure(bg="#ffe8e8", font="Arial 18", text="Currency Converter", padx=10, pady=10)
    
    # create instruction label
    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0, sticky=W)
        self.instruction_label.configure(bg="#ffe8e8", text="Amount", padx=10, pady=10)
        
    # create amount entry
    def __add_amount_entry(self):
        self.amount_entry = Entry()
        self.amount_entry.grid(row=2, column=0, columnspan=2, sticky=W, padx=10, pady=10)
        self.amount_entry.configure(width=40)

    # create buttons
    def __add_clear_button(self):
        self.clear_button = Button()
        self.clear_button.grid(row=3, column=0, sticky=E, padx=10, pady=10)
        self.clear_button.configure(text="Clear", command=self.amount_entry)
        self.clear_button.bind("<ButtonRelease-1>", self.__clear_button_clicked)
    
    def __clear_button_clicked(self, event): # to clear use command see function above and function below
        self.amount_entry.delete(0,END)
        self.message_label.configure(bg="#fffbce", width=40, text = "System Message Displayed Here")
      
    def __add_convert_button(self):
        self.convert_button = Button()
        self.convert_button.grid(row=3, column=1, sticky=W, padx=10, pady=10)
        self.convert_button.configure(text="Convert")
        self.convert_button.bind("<ButtonRelease-1>", self.__convert_button_clicked)
    
     # create event 
    def __convert_button_clicked(self, event): # do not add this def to the initialiser
        self.message_label.configure(text="Converting") # this will bypass the previous message

    # create system message label frame for message entry 
    def __add_label_frame(self):
        self.label_frame = LabelFrame()
        self.label_frame.grid(row=4, column=0, columnspan=2, sticky=W, padx=20, pady=20)
        self.label_frame.configure(width=40, bg="#fffbce")

    # create system message label
    def __add_message_label(self):
        self.message_label = Label(self.label_frame)
        self.message_label.grid(row=4, column=0, columnspan=2, sticky=W, padx=10, pady=10)
        self.message_label.configure(bg="#fffbce", width=40, text = "System Message Displayed Here")
    
    # define tick image 
    def __add_tick_image_label(self):
        self.tick_image_label = Label()
        self.tick_image_label.grid(row=2, column=0, columnspan=2, rowspan=2, sticky=W, padx=5, pady=5)
        self.tick_image_label.configure(image=self.tick_image)
      
    def __change_value(self,event):
        amount_entry = self.amount_entry.get()
        if amount_entry =='':
            self.tick_image_label.configure(image=self.tick_image)
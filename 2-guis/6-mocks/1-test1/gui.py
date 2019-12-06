from tkinter import *

class Gui(Tk):

  # initialise window
  def __init__(self):
    super().__init__()

  # add window components 
    self.title ("Newsletter")
    self.configure (bg="#eee", height=200, width=360, padx=10, pady=10)

  # add components 
    self.__add_outer_frame()
    self.__add_heading_label()
    self.__add_instruction_label()
    self.__add_email_label()
    

  # create outer frame 

  def __add_outer_frame (self):
    self.outer_frame = Frame()
    self.outer_frame.place(x=10, y=10,)
    
    
  #create heading label
  
  def __add_heading_label (self):
    self.heading_label = Label(self.outer_frame)
    self.heading_label.pack(fill=X)
    self.heading_label.configure(text="RECEIVE OUR NEWSLETTER", padx=10, pady=10)
  
  # create instructional label 

  def __add_instruction_label (self):
    self.instruction_label = Label (self.outer_frame)
    self.instruction_label.pack(fill=X)   
    self.instruction_label.configure(justify=LEFT,
                                     text = "Please enter your email below to receive our newsletter.",
                                     padx=10, pady=10)
  
  def __add_email_label (self):
    self.email_label = Label (self.outer_frame)
    self.email_label.place(x=10, y=102)
    self.email_label.pack(padx=10, pady=10)
    self.email_label.configure(text="Email")








from gui import Gui
    
gui = Gui()
gui.mainloop() 
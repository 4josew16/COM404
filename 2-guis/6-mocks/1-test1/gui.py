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
    self.__add_email_frame()
    self.__add_email_label()
    self.__add_entry_label()
  
    

  # create outer frame 

  def __add_outer_frame (self):
    self.outer_frame = Frame()
    self.outer_frame.pack(fill=X)
    self.outer_frame.configure(padx=10, pady=10)
    
    
  #create heading label
  
  def __add_heading_label (self):
    self.heading_label = Label(self.outer_frame)
    self.heading_label.pack(fill=X)
    self.heading_label.configure(font = "Arial 14", text="RECEIVE OUR NEWSLETTER", padx=10, pady=10)
  
  # create instructional label 

  def __add_instruction_label (self):
    self.instruction_label = Label (self.outer_frame)
    self.instruction_label.pack(fill=X)   
    self.instruction_label.configure(text = "Please enter your email below to receive our newsletter.", justify=LEFT,
                                     padx=10, pady=10)

  # create a frame for the email label 

  def __add_email_frame(self):
    self.email_frame = Frame(self.outer_frame)
    self.email_frame.configure(padx=10, pady=10)                                   
  
  # create email label 
  
  def __add_email_label (self):
    self.email_label = Label (self.email_frame)
    self.email_label.pack(side=LEFT)
    self.email_label.configure(padx=10, pady=10, text="Email")
  
  # create entry label 

  def __add_entry_label (self):
    self.entry_label = Entry (self.email_frame)
    self.entry_label.pack (side=LEFT)
    self.entry_label.configure(bd=2, font ="#f00", width =30)
  
 









from gui import Gui
    
gui = Gui()
gui.mainloop() 
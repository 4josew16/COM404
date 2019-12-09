from tkinter import *
from tkinter import messagebox

class part_b(Tk):

  # initialise window
  def __init__(self):
    super().__init__()

 
  # load resources 
    self.default_email_image = PhotoImage(file="C:/Users/Wendy/Documents/GitHub/default.gif")
    self.filled_email_image = PhotoImage(file="C:/Users/Wendy/Documents/GitHub/filled.gif")
    self.empty_email_image = PhotoImage(file="C:/Users/Wendy/Documents/GitHub/empty.gif")

  # add window components 
    self.title ("Newsletter")
    self.configure (bg="#eee", padx=10, pady=10)

  # add components 
    self.__add_outer_frame()
    self.__add_heading_label()
    self.__add_instruction_label()
    self.__add_email_frame()
    self.__add_email_label()
    self.__add_entry_label()
    self.__add_default_email_image_label()
    self.__filled_email_image()
    self.__empty_email_image()
    self.__add_subscribe_button()
  

      
  # create outer frame 
  def __add_outer_frame (self):
    self.outer_frame = Frame()
    self.outer_frame.pack(fill=X)
    self.outer_frame.configure(padx=10, pady=10)
    
  # create heading label
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
    self.email_frame.pack(fill=X)
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
    self.entry_label.bind("<KeyRelease>", self.__change_email_entry)  
  
  # create email image label function  
  def __add_default_email_image_label(self):
    self.default_email_image_label = Label (self.email_frame)
    self.default_email_image_label.pack (side=RIGHT)
    self.default_email_image_label.configure (image=self.default_email_image, padx=10)
  
  # create filled image label function
  def __filled_email_image (self):
    self.filled_email_image_label = Label (self.email_frame)
    self.filled_email_image_label.pack (side=RIGHT)
    self.filled_email_image_label.configure (image=self.filled_email_image, padx=10)
   
# create empty image label function
  def __empty_email_image (self):
    self.empty_email_image_label = Label (self.email_frame)
    self.empty_email_image_label.pack (side=RIGHT)
    self.empty_email_image_label.configure (image=self.empty_email_image, padx=10)
  

  # create subscribe button 
  def __add_subscribe_button(self):
    self.subscribe_button = Button (self.outer_frame)
    self.subscribe_button.pack (fill=X)
    self.subscribe_button.configure (bg="#fee", text = "Subscribe")
    self.subscribe_button.bind("<ButtonRelease-1>", self.__subscribe_button_clicked)
  
  #create event for changing email entries 
  def __change_email_entry(self, event):
    entry_label = self.entry_label.get()
    if entry_label =='':
      self.default_email_image.configure(image = self.filled_email_image)
    if entry_label!='':
      self.default_email_image.configure(image= self.empty_email_image)
      
 # create an event 

  def __subscribe_button_clicked(self, event): # do not add this def to the initialiser
    messagebox.showinfo("Newsletter", "Purchased")

from part_b import part_b
    
gui = part_b()
gui.mainloop() 
  

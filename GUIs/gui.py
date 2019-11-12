from tkinter import *

class Gui(Tk):

  # initialise window
  def __init__(self):
    super().__init__()

    # set window attributes
    self.title("Newsletter")
    self.configure(bg="#00ffff",
                   height=200, 
                   width=400)

    self.add_heading_label()
    self.add_second_label()
    self.add_third_label()
    self.add_email_entry()
    self.add_button()
   

    # add window components by
    # ...creating an object of the component stored in an attribute
    # ...setting the attributes of the component using the attribute
    # ...assigning any event handlers to the component

  # handle events
  # (callback functions to handle events will go here)
  
    # add window components by
    # ...creating an object of the component stored in an attribute  
  def add_heading_label(self):
    self.heading_label = Label()
    self.heading_label.place(x=40, y=30)
    
    # ...setting the attributes of the component using the attribute
    self.heading_label.configure(bg="#00ffff",font="Arial 16",
                                 text="RECEIVE OUR NEWSLETTER.")
                                 
  def add_second_label(self):
    self.second_label = Label()
    self.second_label.place(x=35, y=80)
    self.second_label.configure(bg="#00ffff",font="Arial 10",
                                 text="Please enter your email below to receive our newsletter.")
  
  def add_third_label(self):
    self.third_label = Label()
    self.third_label.place(x=40, y=120)
    self.third_label.configure(bg="#00ffff",font="Arial 10",
                                 text="Email")
  
  def add_email_entry(self):
    self.email_entry = Entry()
    self.email_entry.place(x=100, y=120)
    self.email_entry.configure(width = 40)

  def add_button(self):
    self.button = Button()
    self.button.place (x=150, y=160)
    self.button.configure(font = "Arial 10", text="Subscribe", width=10)
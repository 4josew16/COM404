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
    self.addemailNewsletter()
    self.add_email_frame()
    self.addEmail()
    self.addemailBox()
    self.addsubscribeButton()

  def add_heading_label(self):
      #create
    self.heading_label = Label()
    self.heading_label.pack()
    
    # style
    self.heading_label.configure(font="Arial 16",
                                 text="RECEIVE OUR NEWSLETTER.")
                                 
  def addemailNewsletter (self):
      #create
      self.emailNewsletter = Label()
      self.emailNewsletter.pack()
      
      #style
      self.emailNewsletter.configure(font="Arial 11",
                                     text = "Please enter your email address below to receive our newsletter")
  def addEmail (self):
      #create 
      self.Email=Label(self.email_frame)
      self.Email.pack(side=LEFT)

      #style
      self.Email.configure(font="Arial 11",
                            text="Email:")
  def addemailBox(self):
      #create
      self.emailBox = Entry(self.email_frame)
      self.emailBox.pack(side=RIGHT)
      self.emailBox.configure(width=30)
  
  def addsubscribeButton(self):
      self.addsubscribeButton=Button()
      self.addsubscribeButton.pack()
      self.addsubscribeButton.configure(width=45)
      self.addsubscribeButton.configure(font="Arial 11",
                                        text="Subscribe")

  def add_email_frame(self):
      self.email_frame=Frame()
      self.email_frame.pack()

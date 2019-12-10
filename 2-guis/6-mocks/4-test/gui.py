from tkinter import *

from tkinter import messagebox



class Gui(Tk):







    def __init__(self):

        super().__init__()

        self.grey_image = PhotoImage(file = "C:/Users/aaaa/Desktop/Apprenticeship docs/Python/GUI/grey.gif")

        self.green_image = PhotoImage(file = "C:/Users/aaaa/Desktop/Apprenticeship docs/Python/GUI/green.gif")

        self.red_image = PhotoImage(file = "C:/Users/aaaa/Desktop/Apprenticeship docs/Python/GUI/red.gif")



        # set window properties

        self.title("Newsletter")

        self.configure(bg="#ccc", padx=10, pady=10)



        # add components

        self.__add_outer_frame()

        self.__add_heading_label()

        self.__add_instruction_label()

        self.__add_email_label()

        self.__add_email_entry()

        self.__add_subscribe_button()

        self.__add_grey_image_label()

        #self.__add_option_box()

       # self.__add_red_image_label()



    def __add_outer_frame(self):

        self.outer_frame = Frame()

        self.outer_frame.grid(row=0, column=0)

        self.outer_frame.configure( bg="#eee", 

                                    padx=10, 

                                    pady=10)



    def __add_heading_label(self):

        self.heading_label = Label(self.outer_frame)

        self.heading_label.grid(row=0, column=0, columnspan=2)

        self.heading_label.configure(   bg="#eee",

                                        font="Arial 14",

                                        text="RECEIVE OUR NEWSLETTER")



    def __add_instruction_label(self):

        self.instruction_label = Label(self.outer_frame)

        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)

        self.instruction_label.configure(   bg="#eee",

                                            text="Please enter your email below to receiver our newsletter")



    def __add_email_label(self):

        self.email_label = Label(self.outer_frame)

        self.email_label.grid(row=2, column=0, sticky=E)

        self.email_label.configure( pady=20,

                                    text="Email:")



    def __add_email_entry(self):

        self.email_entry = Entry(self.outer_frame)

        self.email_entry.grid(row=2, column=1, sticky=W)

        self.email_entry.configure(width=40)

        self.email_entry.bind("<KeyRelease>",self.__add_email_entry_switch)





    def __add_grey_image_label(self):

        self.grey_image_label = Label(self.outer_frame)

        self.grey_image_label.grid(row=2, column=2, sticky=E)

        self.grey_image_label.configure(image=self.grey_image, height=20,

                                             width=20)



    #def __add_green_image_label(self):

    #    self.green_image_label = Label(self.outer_frame)

    #    self.green_image_label.grid(row=2, column=2, sticky=E)

    #    self.green_image_label.configure(image=self.green_image, height=20,

    #                                         width=20)



    #def __add_red_image_label(self):

    #   self.red_image_label = Label(self.outer_frame)

    #   self.red_image_label.grid(row=2, column=2, sticky=E)

    #   self.red_image_label.configure(image=self.red_image, height=20,

    #                                         width=20)   



    def __add_email_entry_switch(self,event):

        email_entry = self.email_entry.get()



        if email_entry == '':

            self.grey_image_label.configure(image=self.red_image, height=20,

                                             width=20)

        if email_entry != '':

            self.grey_image_label.configure(image=self.green_image, height=20,

                                             width=20)





    def __add_subscribe_button(self):

        self.subscribe_button = Button(self.outer_frame)

        self.subscribe_button.grid(row=5, column=0, columnspan=2, sticky=N+E+S+W)

        self.subscribe_button.configure(bg="#fcc",

                                        text="Subscribe")

        self.subscribe_button.bind("<ButtonRelease-1>", self.__subscribe_clicked)



    def __subscribe_clicked(self, event):

        messagebox.showinfo("Newsletter","Subscribed!")
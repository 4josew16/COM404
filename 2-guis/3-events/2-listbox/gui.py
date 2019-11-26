from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_lyric_frame()
        self.__add_lyric_entry()
        self.__add_button()
        self.__add_lyrics_label()
        self.__add_second_lyric_frame()


    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure( bg="yellow", 
                                    padx=20, 
                                    pady=20)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(   bg="white",
                                        font="Arial 18",
                                        text="Song Maker")

    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, sticky=W)
        self.instruction_label.configure(   bg="#eee",
                                            text="Lyric to add:")

    def __add_lyric_frame(self):
        self.lyric_frame = Frame(self.outer_frame)
        self.lyric_frame.grid(row=2, column=0)
        

    def __add_lyric_entry(self):
        self.email_entry = Entry(self.lyric_frame)
        self.email_entry.pack(side=LEFT)
        self.email_entry.configure(width=40)

    def __add_button(self):
        self.add_button = Button(self.outer_frame)
        self.add_button.pack(side=RIGHT)
        self.add_button.configure(bg="white",
                                        text="Add")
    
    def __add_lyrics_label(self):
        self.add_lyrics_label = Label(self.outer_frame)
        self.add_lyrics_label.grid(row=3, column=0, sticky=W)
        self.add_lyrics_label.configure(bg="#eee",
                                            text="Lyrics:")
    
    def __add_second_lyric_frame(self):
        self.second_lyric_frame = Frame(self.outer_frame)
        self.second_lyric_frame.grid(row=4, column=0, sticky=W)
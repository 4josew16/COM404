from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball_image = PhotoImage(file = "C:/Users/Wendy/Documents/GitHub/Ball.gif")
        
        # set window attributes
        self.configure(height=300,
                       width=300)

        # set animation attributes
        self.ball_x_pos = 20
        self.ball_y_pos = 20
        self.ball_x_change = 2
        self.ball_y_change = 2
        
        # add components
        self.add_ball_image_label() 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        self.ball_x_pos = self.ball_x_pos + self.ball_x_change
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        if self.ball_x_pos >150:
            self.ball_x_change = -2
        if self.ball_y_pos >150:
            self.ball_y_change = -2

        if self.ball_x_pos <0:
            self.ball_x_change = 2
        if self.ball_y_pos <0:
            self.ball_y_change = 2   
        self.after(100, self.tick)

       

    # the ball image
    def add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.ball_image)
    

     
# the object - this could be included in the main but needs to have the import 
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop()
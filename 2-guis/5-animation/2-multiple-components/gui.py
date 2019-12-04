from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.red_ball_image = PhotoImage(file = "C:/Users/Wendy/Documents/GitHub/Redball.gif")
        self.blue_ball_image = PhotoImage(file = "C:/Users/Wendy/Documents/GitHub/Blueball.gif")
        
        # set window attributes
        self.configure(height=300,
                       width=300)

        # set animation attributes
        self.red_ball_x_pos = 200
        self.red_ball_y_pos = 200
        self.red_ball_x_change = 1
        self.red_ball_y_change = 1

        self.blue_ball_y_pos = 200
        self.blue_ball_x_pos = 200
        self.blue_ball_y_change = 1
        self.blue_ball_x_change = 1
        
        # add components
        self.add_ball_image_label() 
       
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        self.red_ball_x_pos = self.red_ball_x_pos + self.red_ball_x_change
        self.red_ball_y_pos = self.red_ball_y_pos + self.red_ball_y_change
        self.red_ball_image_label.place(x=self.red_ball_x_pos, 
                                    y=self.red_ball_y_pos)

        self.blue_ball_x_pos = self.blue_ball_x_pos + self.blue_ball_x_change
        self.blue_ball_y_pos = self.blue_ball_y_pos + self.blue_ball_y_change
        self.blue_ball_image_label.place(x=self.blue_ball_x_pos, 
                                    y=self.blue_ball_y_pos)

        if self.red_ball_x_pos >150:
            self.red_ball_x_change = -2
        if self.red_ball_y_pos >150:
            self.red_ball_y_change = -2

        if self.red_ball_x_pos <0:
            self.red_ball_x_change = 2
        if self.red_ball_y_pos <0:
            self.red_ball_y_change = 2   
        
        
        if self.blue_ball_x_pos >150:
            self.blue_ball_x_change = -2
        if self.blue_ball_y_pos >150:
            self.blue_ball_y_change = -2

        if self.blue_ball_x_pos <0:
            self.blue_ball_x_change = 2
        if self.blue_ball_y_pos <0:
            self.blue_ball_y_change = 2   

        
        self.after(100, self.tick)

       

    # the ball image
    def add_ball_image_label(self):
        self.red_ball_image_label = Label()
        self.red_ball_image_label.place(x=self.red_ball_x_pos,
                                    y=self.red_ball_y_pos)
        self.red_ball_image_label.configure(image=self.red_ball_image)

        self.blue_ball_image_label = Label()
        self.blue_ball_image_label.place(x=self.blue_ball_x_pos,
                                    y=self.blue_ball_y_pos)
        self.blue_ball_image_label.configure(image=self.blue_ball_image)
    

     
# the object - this could be included in the main but needs to have the import 
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop()
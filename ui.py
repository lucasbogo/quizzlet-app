from tkinter import *  # Import everyrhing from TKinter Module



THEME_COLOR = "#375362"

class QuizInterface:
    
    # This is called everytime we create a new object from this class
    def __init__(self):
        # Property window set as a new object from the TK class
        self.window = Tk()
        # Change aspects of the window
        self.window.title("Quizzler")
        
        
        # Set program to run. TK Inter wowrks by running this endless loop It is constantly checking for updates in the UI.
        self.window.mainloop()
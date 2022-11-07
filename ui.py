from curses import window
from tkinter import *  # Import everyrhing from TKinter Module



THEME_COLOR = "#375362"

class QuizInterface:
    
    # This is called everytime we create a new object from this class
    def __init__(self):
        # Property window set as a new object from the TK class
        self.window = Tk()
        # Change aspects of the window
        self.window.title("Quiz App for Programming Patterns Discipline")
        # Call config method to change window's padding and add 20 pixels of padding in all four sides
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        # Score label. This is where user's score will be placed after calculation
        self.score_label = Label(text="Score: 0", fg="White", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        # Canvas created straight from the Canvas class. This is where the questions will be placed
        self.canvas = Canvas(width=300, height=250, bg="White")
        # Question text. Has a single attribute called text. 150 is half of 300, 125 is half of 250. This prevents tuple index out of range
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            text="Some Question Text", 
            fill=THEME_COLOR,
            font=("Arial", 20, "italic") 
        )
        # Set canva's size
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, )
        
        # Create buttons created form the Button class utilizing downloaded images for true 
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0) # column 0 specifies left position
        
        # Create buttons created form the Button class utilizing downloaded images for false 
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1) # column 1 specifies Right position
        
        
        # Set program to run. TK Inter works by running this endless loop It is constantly checking for updates in the UI.
        self.window.mainloop()
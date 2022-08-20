"""CS 108 - Final Project

Pictionary Game View

@author: Ben Elpidius (bee6)
@date: fall, 2021
@Project Used: Simple Draw
"""

from guizero import App, Text, PushButton, TextBox, Box, ButtonGroup, Drawing, Combo, Window, question
from pictionary import File, Leaderboard, Line, Squiggle, Rectangle, Ellipse
import random


class PictionaryGame:
    """This class provides the GUI for the Pictionary Game."""

    def __init__(self, app):
        """Creates the GUI which includes a canvas and user interactions such as figures and buttons. """

        #Pop-up when opening
        self.name = question("Name", "What is your name")
        
        #Pop-up when closing
        app.when_closed = self.when_closed

        #App
        app.title = 'Pictionary'
        app.font = 'Times New Romans'
        app.text_size = 12
        unit = 800
        control_unit = 150
        app.width = unit
        app.height = unit + control_unit
        
        #Gui Box
        gui_box = Box(app, width=unit, height=unit + control_unit, border=True)
            
        #Word Box
        word_box = Box(gui_box, width='fill', align='top', border=True)
        self.word = Text(word_box, text='Welcome to Pictionary! Please Press New Word to Generate a Random Word to Draw', align='top')
        
        #Timer Box
        timer_box = Box(word_box, height='fill', align='right', border=True)
        self.timer = Text(timer_box, text='120')

        #Options Box
        options_box = Box(gui_box, height='fill', align='right', border=True,)
        self.option = Text(options_box, text='Options', align='top')
        self.leaderboard = PushButton(options_box, text='Leaderboard', command=self.leaderboard)
        self.difficulty_level = Combo(options_box, options=['Easy', 'Medium', 'Hard'])
        self.new_word_button = PushButton(options_box, text='New Word', command=self.generate_new_word)
        self.hide_button = PushButton(options_box, text='Hide Word', command=self.hide)
        self.show_button = PushButton(options_box, text='Show Word', command=self.show)
        self.start_timer_button = PushButton(options_box, text='Start Timer', command=self.start_timer)
        self.reset_button = PushButton(options_box, text='Reset Timer', command=self.reset_timer)
        self.clear_canvas_button = PushButton(options_box, text='Clear Canvas', command=self.clear_canvas)
        self.quit_pictionary_button = PushButton(options_box, text='Quit', align='bottom', command=self.when_closed)

        #Drawing Box
        drawing_box = Box(gui_box, width='fill', height='fill', align='top', border=True)
        self.drawing = Drawing(drawing_box, width=800, height=700)
        self.drawing.bg = "white"

        #Buttons Box. Taken from Simple Draw.
        buttons_box = Box(gui_box, width='fill', border=True)
        self.figure_choice = ButtonGroup(
            buttons_box, ['line', 'rectangle', 'ellipse', 'free draw'], selected='line',
            horizontal=True
        )        
        self.color_choice = ButtonGroup(
            buttons_box, ['black', 'red', 'green', 'blue'], selected='black',
            horizontal = True
        )
        self.fill_choice = ButtonGroup(
            buttons_box, ['unfilled', 'filled'], selected='unfilled',
            horizontal=True
        )
        
        #Guessing Box
        guessing_box = Box(gui_box, width='fill', align='bottom', border=True)
        self.guess_answer = Text(guessing_box, text='Welcome to Pictionary!', align='bottom')
        self.guess = TextBox(guessing_box, width='fill', align='left')
        #self.hint = PushButton(guessing_box, text='Hint', align='right')
        self.guess_button = PushButton(guessing_box, text='Guess', align='right', command=self.check)
        
        #Number of correct answers
        self.correct_count = 0
        
        #Number of Guesses
        self.guesses = 0
        
        #Canvas Interaction. Taken from Simple Draw.
        self.drawing.when_left_button_pressed = self.process_mouse_press
        self.drawing.when_mouse_dragged = self.process_mouse_motion
        self.drawing.when_left_button_released = self.process_mouse_release
        
        #'Enter' key to guessing
        self.guess.when_key_pressed = self.enter_keyboard
        
        #Reads File 
        self.file = File()
        
        #Create the list of model objects, which starts empty,
        #and refresh the drawing canvas (to whitewash it). Taken from Simple Draw.
        self.figures = []
        self.draw_figures()

        #Temporary coordinates used by the drawing methods. Taken from Simple Draw.
        self.saved_x = None
        self.saved_y = None
        
    def process_mouse_press(self, event):
        """ Starts a new figure where the user presses the mouse based on the
        mode settings. Taken from Simple Draw.
        """
        self.saved_x = event.x
        self.saved_y = event.y
        self.temporary_figure = \
            self.create_figure(event, self.fill_choice.value=='filled',
                               self.color_choice.value)
        self.temporary_figure.render(self.drawing)

    def process_mouse_motion(self, event):
        """ Displays a temporary version of the figure and erase the previous
        temporary version. Taken from Simple Draw.
        """
        if self.figure_choice.value == 'free draw':
            # Squiggles are special in that they don't have temporary versions.
            self.temporary_figure.add_point((event.x, event.y))
            self.temporary_figure.render(self.drawing)
        else:
            # Erase the previous version by redrawing it in white.
            self.temporary_figure.set_color('White')
            self.temporary_figure.render(self.drawing)
            self.temporary_figure = \
                self.create_figure(event, self.fill_choice.value=='filled',
                                   self.color_choice.value)
            self.temporary_figure.render(self.drawing)

    def process_mouse_release(self, event):
        """ Create and save the final version of the figure. Taken from Simple Draw."""
        if self.figure_choice.value == 'free draw':
            self.temporary_figure.add_point((event.x, event.y))
            self.figures.append(self.temporary_figure)
        else:
            self.figures.append(
                self.create_figure(event,
                                   self.fill_choice.value=='filled',
                                   self.color_choice.value))
        self.draw_figures()

    def create_figure(self, event, filled, color):
        """ Creates a figure based on the given mode settings -
        The figure can be either temporary or permanent. The calls to the
        constructors for closed figures must convert upper-left and lower-right
        points into upper-left point and dimensions for the constructors. Taken from Simple Draw.
       """
        if self.figure_choice.value == 'line':
            return Line((self.saved_x, self.saved_y), (event.x, event.y),
                        color=color)
        elif self.figure_choice.value == 'rectangle':
            return Rectangle((self.saved_x, self.saved_y),
                             (event.x - self.saved_x, event.y - self.saved_y),
                             filled=filled, color=color)
        elif self.figure_choice.value == 'ellipse':
            return Ellipse((self.saved_x, self.saved_y),
                           (event.x - self.saved_x, event.y - self.saved_y),
                           filled=filled, color=color)
        elif self.figure_choice.value == 'free draw':
            return Squiggle((self.saved_x, self.saved_y), color=color)
    
    def draw_figures(self):
        """ Redraw all the stored figures on a fresh background. Taken from Simple Draw."""
        self.drawing.rectangle(0, 0,
                               self.drawing.width, self.drawing.height,
                               color='white')
        for figure in self.figures:
            figure.render(self.drawing)
             
        
    def enter_keyboard(self, event):
        """ Checks the guess with the answer when user hits enter key. """
        if event.key == '\r':
            self.check()
            
    def generate_new_word(self):
        """ Generates a new word when user hits new word button. """
        #From easy file
        if self.difficulty_level.value == 'Easy':
            self.word.value = str(random.choice(self.file.easy))
            self.guess_button.enable()
            
        #From medium file
        elif self.difficulty_level.value == 'Medium':
            self.word.value = str(random.choice(self.file.medium))
            self.guess_button.enable()
        
        #From hard file
        elif self.difficulty_level.value == 'Hard':
            self.word.value = str(random.choice(self.file.hard))
            self.guess_button.enable()
        
    def check(self):
        """ Checks the guess with the answer. """
        if self.guess.value == '':
            self.guess_answer.value = 'Welcome to Pictionary!'
        elif self.word.value.lower() == self.guess.value.lower():
            self.correct_count += 1
            self.guesses += 1
            self.guess_answer.value = 'You are correct! The answer is' + ' ' + self.word.value.lower() + '.' + 'You got' + ' ' + str(self.correct_count) + ' ' + 'correct.'
            self.guess_button.disable()
        else:
            self.guess_answer.value = 'You are incorrect! Please try harder.'
            self.guesses += 1

    def countdown(self):
        """ Counts down the timer by 1 second. """
        self.timer.value = int(self.timer.value) - 1
        if self.timer.value == '-1':
            self.timer.cancel(self.countdown)
            self.timer.value = '120'
            self.start_timer_button.enable()
            
    def start_timer(self):
        """ Starts the timer when user hits the start timer button. """
        self.timer.repeat(1000, self.countdown) 
        self.start_timer_button.disable()
        
    def reset_timer(self):
        """ Resets the timer to 120 when user hits the reset timer button. """
        self.timer.cancel(self.countdown)
        self.timer.value = '120'
        self.start_timer_button.enable()
    
    def clear_canvas(self):
        """ Clears the canvas when user hits the clear button. """
        self.drawing.clear()
        self.figures.clear()
        
    def hide(self):
        """ Hides the answer of the word when user hits the hide button. """
        self.word.hide()
    
    def show(self):
        """ Shows the answer of the word when user hits the show button. """
        self.word.show()
        
    def when_closed(self):
        """ Pop-ups when user tries to close the app and appends their name and counts to a file. """
        app.yesno("Quit", "Do you want to quit?")
        if self.guesses > 0:
            leaderboard = open('leaderboard.txt', 'a+')
            leaderboard.write(str(self.name) + ',' + str(self.guesses) + ',' + str(self.correct_count) + '\n')
            leaderboard.close()
            app.destroy()
        else:
            app.destroy()
        
    def leaderboard(self):
        """ Shows the top five all time leaderboard in a new window. """
        window = Window(app, title='Leaderboard', height=500, width=500)
        leaderboard_box = Box(window, width='fill', height='fill', border=True)
        self.board = Text(leaderboard_box, text='All Time Leaderboard')
        self.line = Text(leaderboard_box, text='-'*60)
        
        self.leader = Leaderboard()
        
        if len(self.leader.leaderboard) == 0:
            Text(leaderboard_box, text='No one has played yet.')
            
        elif len(self.leader.leaderboard) == 1:
            first = self.leader.leaderboard[0]
            self.first_place = Text(leaderboard_box, text='First Place-' + str(first))
            
        elif len(self.leader.leaderboard) == 2: 
            first = self.leader.leaderboard[0]
            second = self.leader.leaderboard[1]
            
            if first.corrects < second.corrects:
                self.first_place = Text(leaderboard_box, text='First Place-' + str(second))
                self.second_place = Text(leaderboard_box, text='Second Place-' + str(first))
            elif first.corrects > second.corrects:      
                self.first_place = Text(leaderboard_box, text='First Place-' + str(first))
                self.second_place = Text(leaderboard_box, text='Second Place-' + str(second))  
        
        else: 
            first = self.leader.leaderboard[0]
            second = self.leader.leaderboard[0]
            third = self.leader.leaderboard[0]
            
            for player in self.leader.leaderboard:
                if player.corrects > first.corrects:  
                    first = player
            self.leader.leaderboard.remove(first)
            
            for player in self.leader.leaderboard:
                if player.corrects > second.corrects:
                    second = player
            self.leader.leaderboard.remove(second)
            
            for player in self.leader.leaderboard:
                if player.corrects > third.corrects:
                    third = player
                    
            self.first_place = Text(leaderboard_box, text='First Place | ' + str(first))
            self.second_place = Text(leaderboard_box, text='Second Place | ' + str(second))
            self.third_place = Text(leaderboard_box, text='Third Place | ' + str(third))
            
            self.leader.leaderboard.append(first)
            self.leader.leaderboard.append(second)

app = App()
PictionaryGame(app)
app.display()
"""This file contains all the functions responsible for user interactions and information display
based on our safest flight algorithm and graph data type.

All UI windows are shown using Tkinter library.

"""
# Contributor: Alex
from tkinter import *
from PIL import ImageTk, Image

# Create the main window
WINDOW_COLOUR = '#93BFCF'
WINDOW_FONT_SIZE = ('Helvetica', 14)
TEXT_COLOUR = 'black'
root = Tk()
root.title('Post Covid-19: Where to Travel?')
root.config(bg=WINDOW_COLOUR)

# Zoom out the window to the fullscreen size
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

# Create text asking for user's name
name_label = Label(root, text="What's your name?", font=WINDOW_FONT_SIZE, bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
name_label.place(x=600, y=375)

# Create text asking for user's current location
curr_locat_label = Label(root, text="What's your current country?",
                         font=WINDOW_FONT_SIZE, bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
curr_locat_label.place(x=600, y=450)

# Create text asking for user's destination location
dest_locat_label = Label(root, text="What country do you plan to visit?", font=WINDOW_FONT_SIZE,
                         bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
dest_locat_label.place(x=600, y=525)

# Create a name entry box
name_entry = Entry(root, width=30, borderwidth=2)
name_entry.place(x=600, y=400)
user_answer = name_entry.get()

# Create a current location entry box
curr_entry = Entry(root, width=30, borderwidth=2)
curr_entry.place(x=600, y=475)

# Create a destination location entry box
dest_entry = Entry(root, width=30, borderwidth=2)
dest_entry.place(x=600, y=550)

# Create an introduction text
welcome_label = Label(root, text='Welcome!', font=('Helvetica', 20), bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
welcome_label.place(x=700, y=210)

intro_label = Label(root, text="Let's help you find the safest post-pandemic flight across the globe",
                    font=WINDOW_FONT_SIZE, bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
intro_label.place(x=540, y=250)


def display_direct_flight():
    """Display onto a new tkinter window a safety graph of the destination country, and text explaning that
    the system has found a direct flight between the user's current country and their destination country

    """


def display_layover_countries():
    """Display onto a new tkinter window the graphs of the top three safest layover countries based on
    the user's input of current country and destination country.

    Also, display text explaning that the system has found top three safest layover countries,
    and display a ranking from safest to least safe with a bold highlight on the safest layover country.

    """


def display_no_result():
    """Display onto a new tkinter window an image and text presenting no result found based on
    the user's input of current country and destination country.

    """
    result_root = Toplevel()
    result_root.title('No flight in database')
    result_root.config(bg=WINDOW_COLOUR)
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    result_root.geometry("%dx%d" % (w, h))

    # Load and resize image
    image = Image.open('image/error.png')
    resized = image.resize((300, 300), resample=Image.LANCZOS)
    new_image = ImageTk.PhotoImage(resized)

    # Display image
    image_label = Label(result_root, image=new_image, bg=WINDOW_COLOUR)
    image_label.pack(pady=(200, 0))

    # Display no-result text
    no_result_label = Label(result_root, text="NO RESULT FOUND", font=('Helvetica', 20, 'bold'), bg=WINDOW_COLOUR,
                            fg=TEXT_COLOUR)
    no_result_label.pack(pady=(50, 10))

    # Display apology and suggestion text
    apology_label = Label(result_root, text="We're sorry but we can't find any flight for your destination",
                          font=WINDOW_FONT_SIZE, bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    apology_label.pack()

    suggest_label = Label(result_root, text="Please try searching again",
                          font=WINDOW_FONT_SIZE, bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    suggest_label.pack()

    result_root.mainloop()


def check_inputs():
    """Check the user's input after the 'Submit' button is clicked and display the corresponding responses.
        Note: For simplicity, 'CC' is short for 'current country', and 'DC' is short for 'destination country'

        - If the input for CC and DC are empty, ask the user to input again
        - If either the input for CC or DC is empty, ask the user to input the missing parameter.
        - If either the input for CC or DC is not in the database, ask the user to try again.

        Otherwise, proceed to the next window accordingly to three conditions:
        - Direct flight:
        - Top layover countries:
        - No result founded:

        *TO BE FINISHED!!!*

    """
    curr_location_ans = curr_entry.get()
    dest_location_ans = dest_entry.get()
    database_countries = ['Canada', 'Vietnam']

    if not curr_location_ans and not dest_location_ans:
        print('Please enter your information')

    elif not curr_location_ans:
        print('Please enter your current country')

    elif not dest_location_ans:
        print('Please enter your destination country')

    elif curr_location_ans not in database_countries:
        print('Sorry, your current country is not in our database. Please try again')

    elif dest_location_ans not in database_countries:
        print('Sorry, your destination country is not in our database. Please try again')

    else:
        print('Successfully submitted')
        # Case 1: Show direct flight
        display_direct_flight()

        # Case 2: Show top 3 layover countries and highlight the safest one
        display_layover_countries()

        # Case 3: No direct flight and no layover countries
        display_no_result()


# Create a submit button
sub_button = Button(root, text='Submit', font=WINDOW_FONT_SIZE, bg=WINDOW_COLOUR, fg='black',
                    command=check_inputs, borderwidth=0)
sub_button.place(x=700, y=600)

root.mainloop()

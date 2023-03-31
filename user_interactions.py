"""This file contains all the functions responsible for user interactions and information display
based on our safest flight algorithm and graph data type.

All UI windows are shown using Tkinter library.

Note: For simplicity, in all the docstrings, 'CC' is short for 'current country',
and 'DC' is short for 'destination country'

"""
# Contributor: Alex
from tkinter import *
from tkinter import messagebox

import numpy
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import display_plots
from display_plots import plot_map
from flights import *

# Create the main window
WINDOW_COLOUR = '#E4DCCF'
WINDOW_FONT_SIZE = ('Helvetica', 18)
TEXT_COLOUR = 'black'
root = Tk()
root.title('Post Covid-19: Where to Travel?')
root.config(bg=WINDOW_COLOUR)

# Zoom out the window to the fullscreen size
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

# Create text asking for user's name
name_label = Label(root, text="What's your name?", font=('Helvetica', 16), bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
name_label.place(x=600, y=375)

# Create text asking for user's current location
curr_locat_label = Label(root, text="What's your current country?",
                         font=('Helvetica', 16), bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
curr_locat_label.place(x=600, y=450)

# Create text asking for user's destination location
dest_locat_label = Label(root, text="What country do you plan to visit?", font=('Helvetica', 16),
                         bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
dest_locat_label.place(x=600, y=525)

# Create a name entry box
name_entry = Entry(root, width=30, borderwidth=2)
name_entry.place(x=600, y=400)

# Create a current location entry box
curr_entry = Entry(root, width=30, borderwidth=0)
curr_entry.place(x=600, y=475)

# Create a destination location entry box
dest_entry = Entry(root, width=30, borderwidth=2)
dest_entry.place(x=600, y=550)

# Create an introduction text
welcome_label = Label(root, text='Welcome!', font=('Helvetica', 30), bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
welcome_label.place(x=680, y=170)

intro_label = Label(root, text="Let's help you find the safest post-pandemic international flight across the globe",
                    font=WINDOW_FONT_SIZE, bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
intro_label.place(x=425, y=250)

view_map_label = Label(root, text="Click here to view our Safety Choropleth map for reference",
                       font=('Helvetica', 16, 'italic', 'underline'), bg=WINDOW_COLOUR, fg=TEXT_COLOUR, cursor='hand2')
view_map_label.place(x=550, y=280)
view_map_label.bind('<Button-1>', lambda x: plot_map('data/sample_data_map.csv'))


def display_direct_flight():
    """Display onto a new tkinter window a safety graph of the destination country, and text explaning that
    the system has found a direct flight between the user's current country and their destination country

    """
    result_root = Toplevel()
    result_root.title('Direct flight')
    result_root.config(bg=WINDOW_COLOUR)
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    result_root.geometry("%dx%d" % (w, h))

    # User's name
    user_name = name_entry.get()
    # dest_country = dest_entry.get().upper()
    # flight_network = Flights()
    # dest_vertex = flight_network.countries[dest_country]
    dest_name = 'ITALY'
    dest_index = '1.0'

    # Display text on the right-hand side of the screen
    communicate_label1 = Label(result_root,
                               text=f"Hi {user_name}, we found you a direct flight to your destination",
                               font=WINDOW_FONT_SIZE, bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    communicate_label1.pack(pady=(100, 5))

    communicate_label2 = Label(result_root, text=f"Your destination {dest_name} has a danger index of {dest_index}.",
                               font=('Helvetica', 18), bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    communicate_label2.pack(pady=5)

    # Display graph on the left-hand side of the screen

def plot_graph():
    # the figure that will contain the plot
    fig = Figure(figsize=(5, 5), dpi=100)

    # List of squares
    y = [i ** 2 for i in range(101)]

    # Adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.plot(y)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


    data = (20, 35, 30, 35, 27)

    ind = numpy.arange(5)  # the x locations for the groups
    w = .5

    rects1 = ax.bar(ind, data, width)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


def plot_graph_sample():
    display_plots.plot_bar_graph('data/country-danger-index.csv', ['ITALY', 'POLAND' 'UNITED STATES'])


def display_layover_countries(top3_flights: list[tuple]):
    """Display onto a new tkinter window the graphs of the top three safest layover countries based on
    the user's input of current country and destination country.

    Also, display text explaning that the system has found top three safest layover countries,
    and display a ranking from safest to least safe with a bold highlight on the safest layover country.

    """
    # user's name
    user_name = name_entry.get()

    first, second, third = top3_flights

    result_root = Toplevel()
    result_root.title('Top 3 layover countries')
    result_root.config(bg=WINDOW_COLOUR)
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    result_root.geometry("%dx%d" % (w, h))

    # Display communication text
    communicate_label1 = Label(result_root,
                               text=f"Hi {user_name}, we found you the top three safest layover countries for your "
                                    f"destination", font=('Helvetica', 18), bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    communicate_label1.pack(pady=(75, 5))
    communicate_label2 = Label(result_root, text=f"Your best choice is {first[0]} with the danger index of {first[1]}.",
                               font=('Helvetica', 18), bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    communicate_label2.pack(pady=5)

    index_frame = Frame(result_root)
    index_frame.place(x=450, y=700)

    index_def_label = Label(result_root, text='danger index: the average of infection rate per 1000 people '
                                              'and death rate per 100 recorded cases',
                            font=('Helvetica', 14, 'italic'), bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    index_def_label.place(x=450, y=800)

    # Display 1st country, bold and with the text '(recommended)' below the country name
    first_label = Label(result_root, text='1. ' + first[0], font=('Helvetica', 20, 'bold'),
                        bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    first_label.place(x=175, y=200)
    recomended_label = Label(result_root, text='(recommended)', font=('Helvetica', 14, 'italic'),
                             bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    recomended_label.place(x=175, y=225)

    # Display 2nd country
    second_label = Label(result_root, text='2. ' + second[0], font=('Helvetica', 20),
                         bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    second_label.place(x=670, y=200)

    # Display 3rd country
    third_label = Label(result_root, text='3. ' + third[0], font=('Helvetica', 20),
                        bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    third_label.place(x=1175, y=200)

    # Display three graphs corresponding to three layover countries
    plot_graph_sample()


def display_no_result():
    """Display onto a new tkinter window an image and text presenting no result found based on
    the user's input of current country and destination country.

    """
    result_root = Toplevel()
    result_root.title('No flight')
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


def error_message(box_empty: bool = False, both_incorrect: bool = False, same_location: bool = False):
    """Display a message box if

    :param box_empty:
    :return:
    """
    if not box_empty:
        if both_incorrect:
            messagebox.showinfo('Error', 'Sorry, both inputs are not in our database. Please try again')
        else:
            if same_location:
                messagebox.showinfo('Error', 'Sorry, two inputs can not be the same. Please try again')
            else:
                messagebox.showinfo('Error', 'Sorry, one of your inputs is not in our database.\nPlease try '
                                             'again')

    else:  # If box is empty
        messagebox.showinfo('Error', 'Sorry, your input is incomplete. Please try again')


def display_results(source_country: str, dest_country: str):
    """

    :param source_country:
    :param dest_country:
    :return:
    """
    # A complete graph of flights
    flight_network = Flights()  # For testing purpose only
    # generate_complete_flight_network() # Return a complete graph of flights from the database

    # Two objects of source country and destination country
    source_vertex = flight_network.countries[source_country]
    dest_vertex = flight_network.countries[dest_country]

    # Check for a direct flight
    check_direct_flight = flight_network.adjacent(source_country, dest_country)

    if check_direct_flight:  # Direct flight
        display_direct_flight()

    elif source_vertex.check_connected(dest_country, set()):  # Case 2: Two countries are connected
        possible_flights = source_vertex.find_flights(dest_vertex, set())
        # For testing purpose, ('ITALY', 3.0), ('POLAND', 2.0), ('UNITED STATES', 1.0)]

        top3_flights = compute_stats.compute_safest_neighbour(possible_flights)

        display_layover_countries(top3_flights)

    else:
        display_no_result()


def check_inputs():
    """Check the user's input after the 'Submit' button is clicked and display the corresponding responses.
        Note: For simplicity, 'CC' is short for 'current country', and 'DC' is short for 'destination country'

        - If the input for CC and DC are empty, ask the user to input again
        - If either the input for CC or DC is empty, ask the user to input the missing parameter.
        - If either the input for CC or DC is not in the database, ask the user to try again.
        - If the input for CC and DC are the same, ask the user to try again.

        Otherwise, call display_results which proceeds to the next window accordingly to one of these conditions:
        - Direct flight: The vertices reprensenting two input countries are adjacent in the graph.
        - Top layover flights: The vertices representing two input countries are connected in the graph
        - No result founded: The vertices representing two input countries are not connected in the graph

    """
    curr_location = curr_entry.get().upper()
    dest_location = dest_entry.get().upper()
    database_countries = ['CANADA', 'FRANCE', 'GERMANY']  # For testing purposes

    if not curr_location or not dest_location:  # Input is empty
        error_message(True)

    elif curr_location not in database_countries and dest_location not in database_countries:  # Input's not in database
        error_message(False, True)

    elif curr_location not in database_countries or dest_location not in database_countries:
        error_message()

    elif curr_location == dest_location:  # Both inputs are the same
        error_message(False, False, True)

    else:
        # display_results(curr_location, dest_location)
        display_layover_countries([('ITALY', 1.0), ('POLAND', 2.0), ('UNITED STATES', 3.0)])
        # display_direct_flight()


# Create a submit button
sub_button = Button(root, text='Submit', font=WINDOW_FONT_SIZE, bg=WINDOW_COLOUR, fg='black',
                    command=check_inputs, borderwidth=0)
sub_button.place(x=700, y=600)

root.mainloop()

"""This file contains all the functions responsible for user interactions and information display
based on our safest flight algorithm and graph data type.

All UI windows are shown using Tkinter library.

Note: For simplicity, in all the docstrings, 'CC' is short for 'current country',
and 'DC' is short for 'destination country'

"""
# Contributor: Alex
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import pandas as pd
from display_plots import plot_map

from flights import *
from generate_graph import *

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
view_map_label.bind('<Button-1>', lambda x: plot_map('...'))


def display_direct_flight(flights: list[tuple]):
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
    country = [tup[0] for tup in flights]
    danger_index = [tup[1] for tup in flights]

    # Display text on the right-hand side of the screen
    communicate_label1 = Label(result_root,
                               text=f"Hi {user_name}, we found you a direct flight to your destination",
                               font=('Helvetica', 20), bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    communicate_label1.pack(pady=(100, 10))

    communicate_label2 = Label(result_root, text=f"Your current country {country[0]} has a danger index of {danger_index[0]}.",
                               font=('Helvetica', 18), bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    communicate_label2.pack(pady=5)
    communicate_label3 = Label(result_root, text=f"Your destination {country[1]} has a danger index of {danger_index[1]}.",
                               font=('Helvetica', 18), bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    communicate_label3.pack(pady=5)
    index_def_label = Label(result_root, text='danger index: the average of infection rate per 1000 people '
                                              'and death rate per 100 recorded cases',
                            font=('Helvetica', 15, 'italic'), bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    index_def_label.place(x=450, y=810)

    # Display graph on the left-hand side of the screen
    data = {'Country': country,
            'Danger Index': danger_index}
    df = pd.DataFrame(data)

    fig = plt.Figure(figsize=(12, 5), dpi=100)
    ax = fig.add_subplot(111)

    bar = FigureCanvasTkAgg(fig, result_root)
    bar.get_tk_widget().place(x=150, y=265)
    df.plot.bar(x='Country', y='Danger Index', legend=True, ax=ax)

    ax.set_title('Danger index of your current country, and your destination country')
    ax.set_xticklabels(country, rotation=0)


def display_layover_countries(flights: list[tuple]):
    """Display onto a new tkinter window the graphs of the danger index of the source country,
    the top three safest layover countries, and the destination country based onthe user's input.

    Also, display text explaning that the system has found top three safest layover countries,
    and display a ranking of top three safest layover countries with an emphasis on the safest country.

    """
    # user's name
    user_name = name_entry.get()

    first, second, third = flights[1], flights[2], flights[3]
    country = [tup[0] for tup in flights]
    danger_index = [tup[1] for tup in flights]

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
                            font=('Helvetica', 15, 'italic'), bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    index_def_label.place(x=450, y=810)

    # Display 1st country, bold and with the text '(recommended)' below the country name
    first_label = Label(result_root, text='1. ' + first[0], font=('Helvetica', 20, 'bold'),
                        bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    first_label.place(x=325, y=190)
    recomended_label = Label(result_root, text='(recommended)', font=('Helvetica', 14, 'bold', 'italic'),
                             bg=WINDOW_COLOUR, fg='blue')
    recomended_label.place(x=325, y=215)

    # Display 2nd country
    second_label = Label(result_root, text='2. ' + second[0], font=('Helvetica', 20),
                         bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    second_label.pack(pady=(50, 10))

    # Display 3rd country
    third_label = Label(result_root, text='3. ' + third[0], font=('Helvetica', 20),
                        bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
    third_label.place(x=1050, y=190)

    # Display three graphs corresponding to three layover countries
    data = {'Country': country,
            'Danger Index': danger_index}
    df = pd.DataFrame(data)

    fig = plt.Figure(figsize=(12, 5), dpi=100)
    ax = fig.add_subplot(111)

    bar = FigureCanvasTkAgg(fig, result_root)
    bar.get_tk_widget().place(x=150, y=265)
    # df = df[['Country', 'Danger Index']].groupby('Country')
    # df.plot(kind='bar', legend=True, ax=ax)

    df.plot.bar(x='Country', y='Danger Index', legend=True, ax=ax)

    ax.set_title('Danger index of your current country, top three safest layover countries '
                 'and your destination country')
    ax.set_xticklabels(country, rotation=0)


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
    """Display an error message box when users' input to the system is invalid.

        - If box_empty is True, that means users do not enter the expected input but still click submit.
        - If both incorrect is True, that means both of users' inputs are not in the database.
        - If same_location is True, that means users enter the same country for the current country, and
        destination country.

        In all invalid cases, the system briefly explains what information is missing/incorrect, and request users
        to try again.

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
    # Generate a complete graph of flights from the database
    flight_network = generate_flight_network() # For testing purpose only

    # Two objects of source country and destination country
    source_vertex = flight_network.countries[source_country]
    dest_vertex = flight_network.countries[dest_country]

    # Check for a direct flight
    check_direct_flight = flight_network.adjacent(source_country, dest_country)

    # Compute danger_index for source country and destination country
    source_index_tup = compute_safest_neighbour({source_vertex})
    dest_index_tup = compute_safest_neighbour({dest_vertex})

    if check_direct_flight:  # Direct flight
        flights = []
        flights.extend(source_index_tup)
        flights.extend(dest_index_tup)
        display_direct_flight(flights)

    elif source_vertex.check_connected(dest_country, set()):  # Case 2: Two countries are connected
        possible_flights = source_vertex.find_flights(dest_vertex, set())
        # For testing purpose, ('ITALY', 3.0), ('POLAND', 2.0), ('UNITED STATES', 1.0)]

        flights = compute_safest_neighbour(possible_flights)

        flights.insert(0, source_index_tup[0])
        flights.extend(dest_index_tup)

        display_layover_countries(flights)

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
        # display_layover_countries([('FRANCE', 2.0), ('ITALY', 1.0), ('POLAND', ), ('UNITED STATES', 3.0), ('GERMANY',4.5)])
        display_direct_flight([('FRANCE', 2.0), ('ITALY', 1.0)])


# Create a submit button
sub_button = Button(root, text='Submit', font=WINDOW_FONT_SIZE, bg=WINDOW_COLOUR, fg='black',
                    command=check_inputs, borderwidth=0)
sub_button.place(x=700, y=600)

root.mainloop()

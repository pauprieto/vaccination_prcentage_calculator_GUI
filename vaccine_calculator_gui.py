from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Vaccine GUI')
root.minsize(700, 200)
root.geometry('600x200+500+250')

def percentage_calculation(*args):
    """
    Calculates the percentage of people vaccinated in a specific city

    Arguments:
        population -- The current population number of city
        vaccinated -- The number of city population that are currently vaccinated

    Returns the current vaccination rate percentage with two decimal places. If error occurs triggers error message.
    """
    try:
        if get(population) < 0:
            population.set(0)
            error_invalid_input()
        elif get(vaccinated) < 0:
            vaccinated.set(0)
            error_invalid_input()
        elif get(vaccinated) > get(population):
            vaccinated.set(0)
            error_exceeds_pop()
        elif get(vaccinated) == 0 and get(population) == 0:
            percentage.set('0.00%')
        elif get(population) > 0 and get(vaccinated) > 0:
            percentage.set('{:.2f}%'.format(float(get(vaccinated) / get(population) * 100)))
    except TclError:
        #  Error handling of invalid char input (i.e., non integer)
        error_invalid_input()

def on_click(*args):
    """
    Function to increase number of vaccinated population by 1
    """
    vaccinated.set(get(vaccinated) + 1)
    percentage_calculation()

def get(var):
    try:
        return int(var.get())
    except:
        var.set(0)
        error_invalid_input()
        return 0

def error_invalid_input():
    """
    Error handling of negative numbers and non integer numbers
    """
    population.set(0)
    vaccinated.set(0)
    messagebox.showerror('Error', 'This is NOT a positive number. \n\n Please click "OK" and try again.')

def error_exceeds_pop():
    """
     Error handling for vaccinated number exceeding population number
    """
    messagebox.showerror('Error', 'The number of people vaccinated cannot exceed the population number. \n \n' 
                                  'Please click "OK" and try again.')

def exit_program(*args):
    """
    Popup message to confirm if user wants to quit the program when pressing Escape key
    """
    close = messagebox.askyesno('Quit confirmation', 'Are you sure you want to exit the program?')
    if close == 1:
        root.destroy()
    else:
        return

# Callable Variables
population = StringVar(value=0)
vaccinated = StringVar(value=0)
percentage = StringVar()
percentage.set('{:.2f}%'.format(float(0)))

# Define all widgets
frame = ttk.Frame(root, padding='25 25 25 25', cursor='hand2', style='TFrame')
# Left column
population_label = ttk.Label(frame, text='Population:', style='TLabel')
vaccinated_label = ttk.Label(frame, text='Number vaccinated:', style='TLabel')
vaccination_rate_label = ttk.Label(frame, text='Vaccination rate:', style='TLabel')
# Center column
percentage_label = ttk.Label(frame, textvariable=percentage, style='TLabel')
population_entry = ttk.Entry(frame, textvariable=population, style='TEntry')
vaccinated_entry = ttk.Entry(frame, textvariable=vaccinated, style='TEntry')
# All buttons
add_button = ttk.Button(frame, text='+', width=10, style='TButton', command=on_click)
enter_button = ttk.Button(frame, text='Enter', width=20, style='enter.TButton', command=percentage_calculation)
exit_button = ttk.Button(frame, text='Exit', width=20, style='exit.TButton', command=root.quit)

# Responsiveness of window resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.grid(column=0, row=0, sticky=(N, E, W, S))
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)

# Place widgets in window
population_label.grid(column=0, row=0, sticky=E)
vaccinated_label.grid(column=0, row=1, sticky=E)
vaccination_rate_label.grid(column=0, row=2, sticky=E)

population_entry.grid(column=1, columnspan=2, row=0, sticky=(E, W))
vaccinated_entry.grid(column=1, columnspan=2, row=1, sticky=(E, W))
percentage_label.grid(column=1, columnspan=2, row=2, sticky=W)

add_button.grid(column=3, row=1, sticky=W)
enter_button.grid(column=1, row=3)
exit_button.grid(column=2, row=3)

# Define padding for all widgets
for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=5)

# Add styling and theme
style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame',
                background='#F8FAFD',
                fieldbackground='F8FAFD'
                )

style.configure('TLabel',
                foreground='#1C1C1C',
                background='#F8FAFD'
                )

style.configure('TEntry',
                foreground='#1C1C1C',
                background='#F8FAFD'
                )

style.configure('TButton',
                foreground='#1C1C1C',
                background='#FFFFFF',
                font='helvetica 10'
                )

style.map('TButton',
          foreground=[('active', '#4A403A')],
          background=[('active', '#E0E0F8')]
          )

# Program key bindings
root.bind('<Return>', percentage_calculation)  # Calculate entry with 'Enter' key
add_button.bind('<Key-plus>', on_click)  # Add 1 using the '+' key when focus is on add_button
enter_button.bind('<Key-plus>', on_click)  # Add 1 using '+' key when focus is on enter_button
exit_button.bind('<Key-plus>', on_click)  # Add 1 using '+' key when focus is on exit_button
add_button.bind('<Return>', on_click)  # Add 1 using the 'Enter' key when focus is on add_button
root.bind('<Escape>', exit_program)  # Exit program selection with the 'Esc' key
exit_button.bind('<Return>', exit_program)  # Exit program selection with the 'Enter' key when focus is on exit_button

root.mainloop()

from tkinter import *
from backend import Database

database = Database()

#function that does an action when an item in the listbox is selected
def get_selected_row(event):
    try:
        global selected_row
        inventory_index = inventory.curselection()[0]
        selected_row = inventory.get(inventory_index)
        book_title_entry.delete(0, END)
        book_title_entry.insert(END, selected_row[1])
        book_author_entry.delete(0, END)
        book_author_entry.insert(END, selected_row[2])
        book_year_entry.delete(0, END)
        book_year_entry.insert(END, selected_row[3])
        book_ISBN_entry.delete(0, END)
        book_ISBN_entry.insert(END, selected_row[4])
    except IndexError:
        pass

def view_command():
    inventory.delete(0, END)
    for row in database.view():
        inventory.insert(END, row)

def search_command():
    inventory.delete(0, END)
    for row in database.search(book_title_entry.get(), book_author_entry.get(), book_year_entry.get(), book_ISBN_entry.get()):
        inventory.insert(END, row)

def add_command():
    database.insert(book_title_entry.get(), book_author_entry.get(), book_year_entry.get(), book_ISBN_entry.get())
    inventory.delete(0, END)
    #inventory.insert(END, (book_title_entry.get(), book_author_entry.get(), book_year_entry.get(), book_ISBN_entry.get()))
    for row in database.view():
        inventory.insert(END, row)

def delete_command():
    database.delete(selected_row[0])
    inventory.delete(0, END)
    for row in database.view():
        inventory.insert(END, row)

def update_command():
    database.update(selected_row[0], book_title_entry.get(), book_author_entry.get(), book_year_entry.get(), book_ISBN_entry.get())
    inventory.delete(0, END)
    for row in database.view():
        inventory.insert(END, row)


window = Tk()
window.title("Rusyn Book Store Database")

#Tkinter labels for buttons
book_title = Label(window, text = "Title")
book_title.grid(row = 0, column = 0)

book_author = Label(window, text = "Author")
book_author.grid(row = 0, column = 2)

book_year = Label(window, text = "Year")
book_year.grid(row = 1, column = 0)

book_ISBN = Label(window, text = "ISBN")
book_ISBN.grid(row = 1, column = 2)

book_title_text = StringVar
book_title_entry = Entry(window, textvariable = book_title_text)
book_title_entry.grid(row = 0, column = 1)

book_author_text = StringVar
book_author_entry = Entry(window, textvariable = book_author_text)
book_author_entry.grid(row = 0, column = 3)

book_year_text = StringVar
book_year_entry = Entry(window, textvariable = book_year_text)
book_year_entry.grid(row = 1, column = 1)

book_ISBN_text = StringVar
book_ISBN_entry = Entry(window, textvariable = book_ISBN_text)
book_ISBN_entry.grid(row = 1, column = 3)

#Bookstore inventory list box
inventory = Listbox(window, height = 6, width = 35)
inventory.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

#Scrollbar
scroll_bar = Scrollbar(window)
scroll_bar.grid(row = 2, column = 2, rowspan=6)

inventory.configure(yscrollcommand = scroll_bar.set)
scroll_bar.configure(command = inventory.yview)

#Event that happens when you select an item in the listbox, binds to a function
inventory.bind('<<ListboxSelect>>', get_selected_row)


view_all = Button(window, text = "View all", width = 12, command = view_command)
view_all.grid(row = 2, column = 3)

search_entry = Button(window, text = "Search entry", width = 12, command = search_command)
search_entry.grid(row = 3, column = 3)

add_entry = Button(window, text = "Add entry", width = 12, command = add_command)
add_entry.grid(row = 4, column = 3)

updated_selected = Button(window, text = "Update selected", width = 12, command = update_command)
updated_selected.grid(row = 5, column = 3)

delete_selected = Button(window, text = "Delete selected", width = 12, command = delete_command)
delete_selected.grid(row = 6, column = 3)

close = Button(window, text = "Close", width = 12, command = window.destroy)
close.grid(row = 7, column = 3)

window.mainloop()
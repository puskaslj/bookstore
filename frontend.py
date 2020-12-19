from tkinter import *
from backend import Database

database = Database("books.db")

class Window(object):

    def __init__(self, window):
    
        self.window = window

        self.window.title("Rusyn Book Store Database")

        #Tkinter labels for buttons
        book_title = Label(window, text = "Title")
        book_title.grid(row = 0, column = 0)

        book_author = Label(window, text = "Author")
        book_author.grid(row = 0, column = 2)

        book_year = Label(window, text = "Year")
        book_year.grid(row = 1, column = 0)

        book_ISBN = Label(window, text = "ISBN")
        book_ISBN.grid(row = 1, column = 2)

        self.book_title_text = StringVar
        self.book_title_entry = Entry(window, textvariable = self.book_title_text)
        self.book_title_entry.grid(row = 0, column = 1)

        self.book_author_text = StringVar
        self.book_author_entry = Entry(window, textvariable = self.book_author_text)
        self.book_author_entry.grid(row = 0, column = 3)

        self.book_year_text = StringVar
        self.book_year_entry = Entry(window, textvariable = self.book_year_text)
        self.book_year_entry.grid(row = 1, column = 1)

        self.book_ISBN_text = StringVar
        self.book_ISBN_entry = Entry(window, textvariable = self.book_ISBN_text)
        self.book_ISBN_entry.grid(row = 1, column = 3)

        #Bookstore inventory list box
        self.inventory = Listbox(window, height = 6, width = 35)
        self.inventory.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

        #Scrollbar
        scroll_bar = Scrollbar(window)
        scroll_bar.grid(row = 2, column = 2, rowspan=6)

        self.inventory.configure(yscrollcommand = scroll_bar.set)
        scroll_bar.configure(command = self.inventory.yview)

        #Event that happens when you select an item in the listbox, binds to a function
        self.inventory.bind('<<ListboxSelect>>', self.get_selected_row)


        view_all = Button(window, text = "View all", width = 12, command = self.view_command)
        view_all.grid(row = 2, column = 3)

        search_entry = Button(window, text = "Search entry", width = 12, command = self.search_command)
        search_entry.grid(row = 3, column = 3)

        add_entry = Button(window, text = "Add entry", width = 12, command = self.add_command)
        add_entry.grid(row = 4, column = 3)

        updated_selected = Button(window, text = "Update selected", width = 12, command = self.update_command)
        updated_selected.grid(row = 5, column = 3)

        delete_selected = Button(window, text = "Delete selected", width = 12, command = self.delete_command)
        delete_selected.grid(row = 6, column = 3)

        close = Button(window, text = "Close", width = 12, command = window.destroy)
        close.grid(row = 7, column = 3)

    def get_selected_row(self, event):
        try:
            global selected_row
            inventory_index = self.inventory.curselection()[0]
            self.selected_row = self.inventory.get(inventory_index)
            self.book_title_entry.delete(0, END)
            self.book_title_entry.insert(END, self.selected_row[1])
            self.book_author_entry.delete(0, END)
            self.book_author_entry.insert(END, self.selected_row[2])
            self.book_year_entry.delete(0, END)
            self.book_year_entry.insert(END, self.selected_row[3])
            self.book_ISBN_entry.delete(0, END)
            self.book_ISBN_entry.insert(END, self.selected_row[4])
        except IndexError:
            pass

    def view_command(self):
        self.inventory.delete(0, END)
        for row in database.view():
            self.inventory.insert(END, row)

    def search_command(self):
        self.inventory.delete(0, END)
        for row in database.search(self.book_title_entry.get(), self.book_author_entry.get(), self.book_year_entry.get(), self.book_ISBN_entry.get()):
            self.inventory.insert(END, row)

    def add_command(self):
        database.insert(self.book_title_entry.get(), self.book_author_entry.get(), self.book_year_entry.get(), self.book_ISBN_entry.get())
        self.inventory.delete(0, END)
        #inventory.insert(END, (book_title_entry.get(), book_author_entry.get(), book_year_entry.get(), book_ISBN_entry.get()))
        for row in database.view():
            self.inventory.insert(END, row)

    def delete_command(self):
        database.delete(self.selected_row[0])
        self.inventory.delete(0, END)
        for row in database.view():
            self.inventory.insert(END, row)

    def update_command(self):
        database.update(self.selected_row[0], self.book_title_entry.get(), self.book_author_entry.get(), self.book_year_entry.get(), self.book_ISBN_entry.get())
        self.inventory.delete(0, END)
        for row in database.view():
            self.inventory.insert(END, row)

window = Tk()
Window(window)
window.mainloop()
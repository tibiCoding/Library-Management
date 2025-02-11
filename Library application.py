import os.path
import tkinter as tk
from tkinter import messagebox, simpledialog

# Read the library file
def read_library(filename):
    books = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                book = (int(parts[0]), parts[1], parts[2], parts[3], int(parts[4]))
                books.append(book)
    return books

# Save the library file
def save_library():
    with open(filename, "w") as file:
        for book in books:
            line = f"{book[0]},{book[1]},{book[2]},{book[3]},{book[4]}\n"
            file.write(line)
    messagebox.showinfo("Success", "Library saved.")

# Add a book
def add_book():
    title = simpledialog.askstring("Input", "Book title:")
    author = simpledialog.askstring("Input", "Author:")
    genre = simpledialog.askstring("Input", "Genre:")
    year = simpledialog.askinteger("Input", "Year of publication:")
    if title and author and genre and year:
        new_id = max([book[0] for book in books], default=0) + 1
        books.append((new_id, title, author, genre, year))
        update_book_list()
    else:
        messagebox.showerror("Error", "All fields must be filled!")

# Search for a book
def search_book():
    search_term = simpledialog.askstring("Search", "Enter a title or author:")
    if search_term:
        results = [book for book in books if search_term.lower() in book[1].lower() or search_term.lower() in book[2].lower()]
        listbox.delete(0, tk.END)
        if results:
            for book in results:
                listbox.insert(tk.END, f"{book[0]}: {book[1]} by {book[2]} ({book[3]}, {book[4]})")
        else:
            messagebox.showinfo("Result", "No books found with that search term.")

# Remove a book
def remove_book():
    selection = listbox.curselection()
    if selection:
        book_id = int(listbox.get(selection[0]).split(":")[0])
        global books
        books = [book for book in books if book[0] != book_id]
        update_book_list()
    else:
        messagebox.showerror("Error", "Select a book to remove.")

# Show all books
def show_all_books():
    listbox.delete(0, tk.END)
    if books:
        for book in books:
            listbox.insert(tk.END, f"{book[0]}: {book[1]} by {book[2]} ({book[3]}, {book[4]})")
    else:
        messagebox.showinfo("Library", "No books in the library.")

# Update the book list display
def update_book_list():
    listbox.delete(0, tk.END)
    for book in books:
        listbox.insert(tk.END, f"{book[0]}: {book[1]} by {book[2]} ({book[3]}, {book[4]})")

# Close the application
def close_app():
    root.quit()

# Initialize the Tkinter window
root = tk.Tk()
root.title("Library Management")
root.geometry("500x400")

# File name for storage
filename = "library.txt"
books = read_library(filename)

# Create menu bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save", command=save_library)
file_menu.add_command(label="Close", command=close_app)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Book list
listbox = tk.Listbox(root, width=60, height=15)
listbox.pack(pady=10)
update_book_list()

# Buttons
btn_add = tk.Button(root, text="Add Book", command=add_book)
btn_add.pack(fill=tk.X)

btn_search = tk.Button(root, text="Search Book", command=search_book)
btn_search.pack(fill=tk.X)

btn_remove = tk.Button(root, text="Remove Book", command=remove_book)
btn_remove.pack(fill=tk.X)

btn_show_all = tk.Button(root, text="Show All Books", command=show_all_books)
btn_show_all.pack(fill=tk.X)

btn_save = tk.Button(root, text="Save", command=save_library)
btn_save.pack(fill=tk.X)

btn_close = tk.Button(root, text="Close", command=close_app)
btn_close.pack(fill=tk.X)

root.mainloop()

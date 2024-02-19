# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 22:27:06 2024

@author: bbilg
"""
import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel
from tkinter.font import Font
from library import Library
from book import Book



class LibraryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.library = Library()
        self.bold_font = Font(family="Helvetica", size=10, weight="bold") 
        self.show_menu()
    def show_menu(self):
        tk.Label(self.master, text="***MENU***", font=self.bold_font).pack()
        tk.Button(self.master, text="1) List Books", command=self.open_list_books_window, font=self.bold_font).pack(fill=tk.X)
        tk.Button(self.master, text="2) Add Book", command=self.open_add_book_window, font=self.bold_font).pack(fill=tk.X)
        tk.Button(self.master, text="3) Remove Book", command=self.open_remove_book_window, font=self.bold_font).pack(fill=tk.X)
        tk.Button(self.master, text="4) To exit, enter 4 or Q", command=self.master.quit, font=self.bold_font).pack(fill=tk.X)
        
       
    def open_add_book_window(self):
        def add_book():
            name = name_var.get()
            author = author_var.get()
            release_date = release_date_var.get()
            pages = pages_var.get()
            if name and author and release_date and pages:
                book = Book(name, author, release_date, pages)
                self.library.add_book(book)
                messagebox.showinfo("Success", "Book added successfully")
                add_book_window.destroy()

        add_book_window = Toplevel(self.master)
        add_book_window.title("Add Book")

        tk.Label(add_book_window, text="Book Name:").grid(row=0, column=0)
        name_var = tk.StringVar()
        tk.Entry(add_book_window, textvariable=name_var).grid(row=0, column=1)

        tk.Label(add_book_window, text="Author:").grid(row=1, column=0)
        author_var = tk.StringVar()
        tk.Entry(add_book_window, textvariable=author_var).grid(row=1, column=1)

        tk.Label(add_book_window, text="Release Date:").grid(row=2, column=0)
        release_date_var = tk.StringVar()
        tk.Entry(add_book_window, textvariable=release_date_var).grid(row=2, column=1)

        tk.Label(add_book_window, text="Pages:").grid(row=3, column=0)
        pages_var = tk.StringVar()
        tk.Entry(add_book_window, textvariable=pages_var).grid(row=3, column=1)

        tk.Button(add_book_window, text="Submit", command=add_book).grid(row=4, column=0, columnspan=2)

    def open_list_books_window(self):
        list_books_window = Toplevel(self.master)
        list_books_window.title("List Books")
        lb = tk.Listbox(list_books_window)
        lb.pack(fill=tk.BOTH, expand=True)
        for book in self.library.books:
            lb.insert(tk.END, str(book))

    def open_remove_book_window(self):
        book_name = simpledialog.askstring("Remove Book", "Enter the book name:", parent=self.master)
        if book_name:
            result = self.library.remove_book(book_name)
            if result:
                messagebox.showinfo("Success", "The  book is removed successfully")
            else:
                messagebox.showerror("Error", "The book is not found")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
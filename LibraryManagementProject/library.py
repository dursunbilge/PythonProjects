# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:07:47 2024

@author: bbilg
#library.py
"""


from filemanager import FileManager

class Library:
    def __init__(self, filename='books.txt'):
        self.filename = filename
        self.books = FileManager.read_books(self.filename)

    def list_books(self):
        if not self.books:
            print("No books found.")
        for book in self.books:
            print(book)

    def add_book(self, book):
        self.books.append(book)
        FileManager.write_books(self.filename, self.books)

    def remove_book(self, book_name):
        self.books = [book for book in self.books if book.name != book_name]
        FileManager.write_books(self.filename, self.books)
        
    def __del__(self):
       
        try:
            self.file.close()
        except AttributeError:
            # File was not opened or already closed
            pass    
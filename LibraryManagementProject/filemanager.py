# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:07:11 2024

@author: bbilg
#filemanager.py
"""


from book import Book

class FileManager:
    @staticmethod
    def read_books(filename):
        books = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    if line.strip():
                        name, author, release_date, pages = line.strip().split(", ")
                        books.append(Book(name, author, release_date, pages))
        except FileNotFoundError:
            open(filename, 'w').close()
        return books

    @staticmethod
    def write_books(filename, books):
        with open(filename, 'w') as file:
            for book in books:
                file.write(str(book) + '\n')
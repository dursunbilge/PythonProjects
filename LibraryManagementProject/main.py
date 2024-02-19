# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:08:10 2024

@author: bbilg
"""
#main.py

from library import Library
from book import Book

def main():
    lib = Library()
    while True:
        choice = choose()

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            name = input("Enter the book name: ")
            author = input("Enter the author name: ")
            release_date = input("Enter the release date: ")
            pages = input("Enter the number of pages: ")
            lib.add_book(Book(name, author, release_date, pages))
        elif choice == "3":
            lib.remove_book(input("Please enter the name of the book you want to remove: "))
        elif choice == "4" or choice == "Q":
            print("Exiting program...")
            break
def choose():
    while True:
        print("***MENU***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) To exit enter 4 or Q")
        choice = input("Please enter your choice: ")

        if choice in ["1", "2", "3", "4", "Q"]:
            return choice
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
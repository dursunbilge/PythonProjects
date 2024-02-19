# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:06:46 2024

@author: bbilg
#book.py
"""

class Book:
    def __init__(self, name, author, release_date, pages):
        self.name = name
        self.author = author
        self.release_date = release_date
        self.pages = pages

    def __str__(self):
        return f"{self.name}, {self.author}, {self.release_date}, {self.pages}"
  
"Library Management Project" is my first  project that I created using object-oriented programming techniques in Python. It aims to provide basic library functions such as listing, adding, and removing books through a user-friendly interface. Here are the main Features of the Project:

book.py: Contains the Book class, which holds information for a book. Each book object stores the name of the book, name of the  author, release date, and number of pages of the book.

library.py: Defines the Library class that manages the books in the library. This class includes functions to list books, add a new book, and remove books. It interacts with the FileManager class to read and write book information from and to a file.

filemanager.py: Contains the FileManager class, which manages file operations. This class offers static methods to read the book list from a file and write the updated list back to the file.

main.py: Provides a menu for users to interact with the library system through the console. Users can perform operations such as listing books, adding books, and removing books via the given menu in console-based interface.

maingui.py: Contains the Graphical User Interface (GUI) version of the system. Developed using the Tkinter library, this graphical interface allows users to list, add, and remove books. It also provides a more user-friendly interface, making operations easier to perform.

To sum up, the resulted Library Management Project  is a system that allows users to manage a book list in a library, featuring both a console-based and a graphical user interface. It follows object-oriented programming principles to define classes and methods for managing books and library operations. A separate class (FileManager) is used for file operations, enhancing the modularity and readability of the code. Users can choose to interact with the system either via the console-based interface or the graphical interface.

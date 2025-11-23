# Library Management System

## Project Overview
This project is a simple Library Management System made in Python. It helps a librarian to keep track of books, issue them to students, and calculate fines if they return the book late. It uses a CSV file to save data so we don't lose it when we close the program.

## Features
* **Add Books:** You can add new books to the library database.
* **Issue Books:** Mark a book as borrowed and save the due date.
* **Return Books:** Return a book and automatically calculate the fine based on days overdue.
* **View All Books:** See a list of all books and their status.
* **Data Saving:** All data is saved in a file called `library.csv`.

## Technologies Used
* Python
* CSV (for file handling)
* VS Code (as code editor)

## How to Install and Run
1. Download all the python files (`main.py`, `book_operations.py`, `fine_calculator.py`, `file_manager.py`).
2. Put them all in one folder.
3. Open the folder in VS Code or Terminal.
4. Run the command: python main.py
5. The menu will appear on the screen.

How to Test
You can test the features by selecting the numbers in the menu:

* **Option 1 (Show):** Select `1` to see if the list of books prints correctly. If the file is empty, it should show nothing or just the header.
* **Option 2 (Add):** Select `2` to add a book. Enter a dummy ID (e.g., `101`) and Title. Then use Option 1 to check if it saved.
* **Option 3 (Issue):** Select `3`. Enter the ID of the book you just added. Enter a due date (e.g., `20/10/2023`).
* **Option 4 (Return):** Select `4`. Enter the ID `101` and a return date.
    * *Test No Fine:* Enter a date before the due date.
    * *Test Fine:* Enter a date after the due date to see if the math works.
* **Option 5 (Exit):** Select `5` to close the program safely.

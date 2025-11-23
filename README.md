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
3. Open the folder in VS Code with python extensions installed or Terminal.
4. Run the command: python main.py
5. The menu will appear on the screen.

# OR

1. **Open VS Code** on your computer with python extensions installed.
2. Press `Ctrl + Shift + P` on your keyboard to open the command palette.
3. Type `Git: Clone` and press Enter.
4. Paste the repository link: **[PASTE YOUR GITHUB REPO LINK HERE]**
5. Select a folder to save it in and click "Open".
6. Once the folder is open, click on `main.py` file on the left side.
7. Open the Terminal (`Ctrl + ~`) and type:

## How to Test
You can test the features by selecting the numbers in the menu:

* **Option 1 (Show):** Select `1` to see if the list of books prints correctly. If the file is empty, it should show nothing or just the header.
* **Option 2 (Add):** Select `2` to add a book. Enter a dummy ID (e.g., `101`) and Title. Then use Option 1 to check if it saved.
* **Option 3 (Issue):** Select `3`. Enter the ID of the book you just added. Enter a due date (e.g., `20/10/2023`).
* **Option 4 (Return):** Select `4`. Enter the ID `101` and a return date.
    * *Test No Fine:* Enter a date before the due date.
    * *Test Fine:* Enter a date after the due date to see if the math works.
* **Option 5 (Exit):** Select `5` to close the program safely.

## Step-by-Step Testing
Please test the project in this order to see the features working:

**Step 1: Issue a Book**
* Run the program
* Choose **Option 3 (Issue)**
* Enter Book ID: `1` (or any ID from the list)
* Enter Due Date: `01/01/2023` (Enter an old date)
* The system will say "Done" and save it

**Step 2: Return the Book**
* Now, Choose **Option 4 (Return)**.
* Enter Book ID: `1`.
* Enter Return Date: `20/01/2025`
* Enter Fine Per Day: `5`.
* The system will calculate overdue days and show total fine amount.

**Step 3: Check Test Cases**
You can try these specific inputs to check error handling:
* **Test Case 1 (Wrong Date):** Try to Issue a book and type date as `hello`. The system should say "wrong date format" and ask you to try again.
* **Test Case 2 (Wrong Choice):** Type in the menu `99` or `abc`. The system should say "Invalid choice".
* **Test Case 3 (Already Issued):** Try to Issue Book `1` again *before* returning it. The system should say "Already issued".

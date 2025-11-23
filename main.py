# main.py
import files
import book_mgr

def main():
    print("LIBRARY SYSTEM")
    
    # load books at start
    books = files.load_data()
    
    while True:
        print("\n1. Show")
        print("2. Add")
        print("3. Issue")
        print("4. Return")
        print("5. Exit")
        
        try:
            x = int(input("Choice: "))
        except:
            print("Please enter a number.")
            continue
        
        if x == 1:
            print("\nList of Books:")
            for b in books:
                print(b)
        elif x == 2:
            book_mgr.add_b(books)
        elif x == 3:
            book_mgr.issue_b(books)
        elif x == 4:
            book_mgr.return_b(books)
        elif x == 5:
            print("Bye.")
            break
        else:
            print("Invalid choice.")

# run program
main()

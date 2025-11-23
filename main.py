import file_manager
import book_operations

def main():
    print("LIBRARY SYSTEM")
    
    books=file_manager.load_data()
    
    while True:
        print("\n1. Show")
        print("2. Add")
        print("3. Issue")
        print("4. Return")
        print("5. Exit")
        
        try:
            x=int(input("Choice (1-5): "))
        except:
            print("numbers only pls")
            continue
        
        if x==1:
            print("\nList of Books:")
            for b in books:
                print(b)
        elif x==2:
            book_operations.add_b(books)
        elif x==3:
            book_operations.issue_b(books)
        elif x==4:
            book_operations.return_b(books)
        elif x==5:
            print("Bye.")
            break
        else:
            print("Invalid choice.")

main()

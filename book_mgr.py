# book_mgr.py
import files
import my_dates

# b_list is the list of books
def add_b(b_list):
    id = input("Enter Book ID: ")
    name = input("Enter Title: ")
    
    # 0=id, 1=name, 2=borrowed?, 3=date
    new_book = [id, name, "No", ""]
    b_list.append(new_book)
    
    files.save_data(b_list)
    print("Added.")

def issue_b(b_list):
    id = input("Enter ID: ")
    
    flag = 0
    for b in b_list:
        if b[0] == id:
            flag = 1
            if b[2] == "Yes":
                print("Already issued.")
            else:
                d = input("Enter Due Date (Format DD/MM/YYYY): ")
                
                try:
                    # manual check for date format
                    # just testing if split works
                    p = d.split('/')
                    t_d = int(p[0])
                    t_m = int(p[1])
                    t_y = int(p[2])
                    
                    # if code reaches here, date is ok
                    b[2] = "Yes"
                    b[3] = d
                    files.save_data(b_list)
                    print("Done.")
                    
                except:
                    print("Error: Date format wrong! Try again.")
                    print("----------------")
                    # call function again
                    issue_b(b_list)
                    return
            break
            
    if flag == 0:
        print("Not found.")

def return_b(b_list):
    id = input("Enter ID: ")
    
    flag = 0
    for b in b_list:
        if b[0] == id:
            flag = 1
            if b[2] == "No":
                print("Book is here only.")
            else:
                d_ret = input("Return Date (Format DD/MM/YYYY): ")
                d_due = b[3]
                
                try:
                    # calc fine
                    diff = my_dates.get_overdue(d_ret, d_due)
                    
                    if diff > 0:
                        fine = diff * 5
                        print("Late by", diff, "days.")
                        print("Fine is", fine)
                    else:
                        print("No fine.")
                    
                    # reset book
                    b[2] = "No"
                    b[3] = ""
                    files.save_data(b_list)
                    
                except:
                    print("Error: Date typed wrong. Try again.")
                    print("----------------")
                    # restart process
                    return_b(b_list)
                    return
            break
            
    if flag == 0:
        print("Not found.")

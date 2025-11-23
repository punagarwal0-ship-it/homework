# book_operations.py
import file_manager
import fine_calculator

def add_b(b_list):
    id=input("Enter Book ID (e.g. 101): ")
    name=input("Enter Title (e.g. Python Basics): ")
    
    new_book=[id, name, "No", ""]
    b_list.append(new_book)
    
    file_manager.save_data(b_list)
    print("Added.")

def issue_b(b_list):
    id=input("Enter ID (e.g. 101): ")
    
    found=0
    for b in b_list:
        if b[0]==id:
            found=1
            if b[2]=="Yes":
                print("Already issued.")
            else:
                d=input("Enter Due Date (e.g. 25/12/2023): ")
                
                try:
                    p=d.split('/')
                    d_test=int(p[0])
                    m_test=int(p[1])
                    y_test=int(p[2])
                    
                    b[2]="Yes"
                    b[3]=d
                    file_manager.save_data(b_list)
                    print("Done.")
                    
                except:
                    print("wrong date format.. try again")
                    print("----------------")
                    issue_b(b_list)
                    return
            break
            
    if found==0:
        print("Not found.")

def return_b(b_list):
    id=input("Enter ID (e.g. 101): ")
    
    found=0
    for b in b_list:
        if b[0]==id:
            found=1
            if b[2]=="No":
                print("Book is here only.")
            else:
                d_ret=input("Return Date (e.g. 30/12/2023): ")
                cost=input("Enter Fine Per Day (e.g. 5): ")
                
                d_due=b[3]
                
                try:
                    diff=fine_calculator.get_overdue(d_ret, d_due)
                    
                    if diff>0:
                        val=int(cost)
                        fine=diff*val
                        print("Late by", diff, "days.")
                        print("Fine is", fine)
                    else:
                        print("No fine.")
                    
                    b[2]="No"
                    b[3]=""
                    file_manager.save_data(b_list)
                    
                except:
                    print("something went wrong. check inputs")
                    print("----------------")
                    return_b(b_list)
                    return
            break
            
    if found==0:
        print("Not found.")

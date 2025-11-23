# fine_calculator.py

def leap(y):
    if(y%400==0):
        return True
    elif(y%4==0 and y%100!=0):
        return True
    else:
        return False

def m_len(m, y):
    lst=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if m==2:
        if leap(y):
            return 29
    
    return lst[m-1]

def count_days(d, m, y):
    total=0
    
    for y1 in range(1, y):
        if leap(y1):
            total=total+366
        else:
            total=total+365

    for m1 in range(1, m):
        total=total+m_len(m1, y)
    
    total=total+d
    return total

def get_overdue(d_ret, d_due):
    p1=d_ret.split('/')
    d1=int(p1[0])
    m1=int(p1[1])
    y1=int(p1[2])

    p2=d_due.split('/')
    d2=int(p2[0])
    m2=int(p2[1])
    y2=int(p2[2])

    days1=count_days(d1, m1, y1)
    days2=count_days(d2, m2, y2)
    
    ans=days1-days2
    return ans

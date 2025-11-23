
import csv

FNAME="library.csv"

def load_data():
    data=[]
    
    try:
        f=open(FNAME, 'r')
        r=csv.reader(f)
        for row in r:
            if len(row)>0:
                data.append(row)
        f.close()
    except:
        pass
        
    return data

def save_data(lst):
    f=open(FNAME, 'w')
    w=csv.writer(f)
    w.writerows(lst)
    f.close()

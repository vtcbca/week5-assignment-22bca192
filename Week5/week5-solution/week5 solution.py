attribute=['sid','sname','city','monum']
records=[[1,'om','surat',1234567890],
          [2,'sai','vyra',1122334455],
          [3,'ram','bajipura',1233214567],
         [4,'radha','vadodra',9087654321],
         [5,'gopal','bombay',1233567890]]
li=[]
for i in range(2):
    sid=int(input("\nEnter stusdent id:"))
    sname=input("\nEnter the student name:")
    city=input("\nEnter the student city name:")
    monum=int(input("\nEnter the student mobile number:"))
    l=[sid,sname,city,monum]
    li.append(l)

              
import csv 
with open('student.csv','w',newline='') as w:
    file=csv.writer(w)
    file.writerow(attribute)
    file.writerows(li)
    file.writerows(records)

import csv
with open('student.csv','r',newline='') as r:
    csvreader=csv.reader(r)
    for row in csvreader:
        print(row)
    
              
              

              
              
              
              
              
    
    

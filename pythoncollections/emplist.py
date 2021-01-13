employees=[[1001,"ajay","qa",1981,2003],
           [1002,"vijay","developer",1992,2008],
           [1003,"arun","pa",1989,2010],
           [1004,"amal","developer",2009,2014],
           [1004,"vimal","developer",1987,1989]
           ]

#print all emp desig
for emp in employees:
    print(emp[2])

#print all emp desig=developer
for emp in employees:
    if(emp[2]=="developer"):
        print(emp[1])

#print all emp those who are wrking in 1980's
for emp in employees:
    if((emp[3]>1980)&(emp[3]<2000)):
        print("employees working in 1980's",  emp[1])




#print all emp details whose exp > 9 yrs
diff=0
for emp in employees:
    diff=emp[4]-emp[3]
    #print(diff)
    if(diff>9):
        print("employees having more than 9 yrs",emp[1])

lst=[1,2,3,4,6]
low=0
upp=len(lst)-1
elmnt=7
while(low<upp):
    total=lst[low]+lst[upp]
    if(elmnt<total):
        upp-=1
    elif(elmnt>total):
        low+=1
    elif(elmnt==total):
        print(lst[low],",",lst[upp])
        break
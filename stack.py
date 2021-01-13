size=int(input("enter the size of stack"))
stk=[]

top=0
n=1
def push(element):

    global top
    if(top>=size):
        print("stack is full")
    else:
        stk.insert(top,element)
        print("element pushed")
        top+=1

def pop():
    global top
    if(top<0):
        print("stack is empty")
    else:
        print(stk[top-1],"popped")
        top-=1

def display():
    global top
    for i in range(0,top):
        print(stk[i])

while(n!=0):
    option=int(input("enter operation u want to perform 1)push 2)pop 3)display"))
    if(option==1):
        elemnt=input()
        push(elemnt)
    elif(option==2):
        pop()
    elif option==3:
        display()
    else:
        print("invalid option")
    n=int(input("enter do u want to continue press 0 for exit"))

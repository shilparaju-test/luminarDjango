from tkinter import *
root=Tk()
root.title("main window")#change the title of the window
label1=Label(root,text="name")
label2=Label(root,text="emailaddress")
label3=Label(root,text="password")
label1.pack()
label2.pack()
label3.pack()
entry1=Entry(root)
entry2=Entry(root)
entry3=Entry(root)
entry1.pack()
entry2.pack()
entry3.pack()
root.mainloop()
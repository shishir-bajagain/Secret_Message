import secret_msg as msg
from tkinter import * #type: ignore


root = Tk()
root.geometry("600x550")
root.config(bg="black")

Text1 = Label(root,text="HELLO AGENT!!!",bg="black",fg="RED",font=("New Times Romania",20,"bold","underline"),relief=RAISED,border = 0)
Text1.place(x=190,y=0)

def clearInput(event):
    if Input.get()== " Enter Your Secret Message":
        Input.delete(0,END)


Input = Entry(root,bg="orange",fg="Green",font=("New Times Romania",20,"bold"),border=0,width = 25)
Input.place(x=120,y=70)
Input.insert(0, " Enter Your Secret Message")
Input.bind("<FocusIn>",clearInput)
# Input.bind("<FocusOut>", restore_default)

Display = Label(root,text="Your Output is...",padx=70, pady=70,relief=RAISED, bg ="grey", fg ="RED",font=("New Times Romania",20,"bold"))
Display.place(x=130,y=250)

def display(string):
    Display = Label(root,text="Your Output is...",padx=70, pady=70,relief=RAISED, bg ="grey", fg ="RED",font=("New Times Romania",20,"bold"))
    Display.destroy()
    Display = Label(root,text=string,padx=70, pady=100,relief=RAISED, bg ="grey", fg ="RED",font=("New Times Romania",20,"bold"))
    Display.place(x=130,y=250)

def Code():
    msg_code = msg.verify(1,Input.get()) 
    display(msg_code)

def De_Code():
    msg_decode = msg.verify(2,Input.get()) 
    display(msg_decode)

ButtonCode = Button(root, text="CODE",padx=70,pady=2,font=("New Romania Times", 15, "bold"), relief= RAISED, cursor="circle",command=Code)
ButtonCode.place(x=50,y=150)

ButtonDecode = Button(root, text="DECODE",padx=70,pady=2,font=("New Romania Times", 15, "bold"), relief= RAISED, cursor="circle", command=De_Code)
ButtonDecode.place(x=300,y=150)

root.mainloop()
import tkinter as tk


win = tk.Tk()
win.configure(background="Navy blue")
win.title("Remove Duplicate Text")
win.geometry('810x420')
win.resizable(0,0)


def submit(event):
    # Remove String Program
    val = txt2.get()
    val = val.lower()
    output=''
    for ch in val:
        if ch not in output:
            output=output+ch
    print(output)              

    #Print result of Remove string in Text field
    Msg = tk.Text(win,borderwidth=5,width=26,height=10,bg="white",fg="black",font=('times',15,'bold'))
    Msg.place(x=300,y=225)
    Msg.place(x=300,y=225)
    Msg.insert(tk.END,output)

# Widget for This Application
label = tk.Label(win,text="Duplicate Character Remover",width=22,height=2,fg="white",bg="black",font=('times',15,'bold'))
label.place(x=305,y=10)

label1 = tk.Label(win,text="Enter Your Text ",width=19,height=1,bg="yellow",fg="black",font=('times',15,'bold'))
label1.place(x=318,y=140)

txt2 = tk.Entry(win,borderwidth=5,width=26,bg="white",fg="black",font=('times',15,'bold'))
txt2.place(x=300,y=170)

# submit button 
button = tk.Button(win, text="SUBMIT",borderwidth=3,width=10,bg="black",fg="white")
button.pack()
button.place(x=590,y=170)

# For Using SubmitButton Click Left Key Of Mouse
button.bind('<Button-1>',submit)
# for using Enter Key To see Result
win.bind("<Return>", submit)

win.mainloop()

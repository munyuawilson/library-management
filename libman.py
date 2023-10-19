from tkinter import *



root=Tk()
root.title("E-Lib")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.configure(bg="#06414b")


root.geometry(f"{screen_width}x{screen_height}")
    
    
def button_click():
    pass
    







email_var=StringVar()

email_label=Label(text="Enter Email Address:",bg="#06414b")

email_entry = Entry(root,textvariable = email_var,bg="#06414b", font=('calibre',10,'normal'),)


button = Button(root, text="Send",bg="white",fg="black" ,command=button_click)



# Place the name_entry widget at the center
email_label.place(relx=0.5, rely=0.6, anchor=CENTER)
email_entry.place(relx=0.5, rely=0.7, anchor=CENTER)
button.place(relx=0.5, rely=0.8, anchor=CENTER)










root.mainloop()

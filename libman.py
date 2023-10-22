from tkinter import *

import send_email

root=Tk()
root.title("E-Lib")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.configure(bg="#06414b")
root.geometry(f"{screen_width}x{screen_height}")


number_var=IntVar()
email_var=StringVar()
random_number=send_email.random_number
print(random_number)   
 #function for send button   
def button_click():
    email=email_var.get().lower()
    if 's.karu.ac.ke' in email:
        send_code_function()
        send_email.send(recipient_email=email)
    else:
        pass
    

def send_button_click():
    code=number_var.get()
    if code==random_number:
        #Give a pop up of two hours
        #Give two hours
        #Minimize the app window
        print("you are in!")




def send_code_function():
    number_label=Label(text="Enter code:",bg="#06414b")
    

    code_entry = Entry(root,textvariable = number_var,bg="#06414b", font=('calibre',10,'normal'),)


    submit_code = Button(root, text="Confirm",bg="white",fg="black" ,command=send_button_click)
    
    number_label.place(relx=0.3, rely=0.6, anchor=CENTER)
    code_entry.place(relx=0.5, rely=0.6, anchor=CENTER)
    submit_code.place(relx=0.6, rely=0.6, anchor=CENTER)
    
    
    
#creation email label on screen
def email_label_function():

    email_label=Label(text="Enter School Email Address:",bg="#06414b")

    email_entry = Entry(root,textvariable = email_var,bg="#06414b", font=('calibre',10,'normal'),)


    button = Button(root, text="Send",bg="white",fg="black" ,command=button_click)



    # Place the name_entry widget at the center
    email_label.place(relx=0.3, rely=0.5, anchor=CENTER)
    email_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
    button.place(relx=0.6, rely=0.5, anchor=CENTER)







email_label_function()


root.mainloop()

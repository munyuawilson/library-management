from tkinter import *
from tkinter import messagebox
from datetime import datetime
import send_email

root=Tk()
root.title("E-Lib")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.configure(bg="white")
root.geometry(f"{screen_width}x{screen_height}")


image=PhotoImage(file='logo.png')
root.wm_iconphoto(root, image)


label=Label(root,image=image,bg="white")
label.place(relx=0.5, rely=0.4, anchor=CENTER)

number_var=IntVar()
email_var=StringVar()
random_number=send_email.random_number
print(random_number) 

#


 #function for send button   
def button_click():
    email=email_var.get().lower()
    if 's.karu.ac.ke' in email:
        with open('session.txt', "r") as file:
        
            if email!="njeri.munyua@s.karu.ac.ke" and email in file:
                messagebox.showwarning("Warning", "Your session has expired!")
                
            
            else:
                send_code_function()
                send_email.send(recipient_email=email)
                
    else:
        show_warning()
    
def show_warning():
    messagebox.showwarning("Warning", "Enter valid school email Address")
def show_info():
    messagebox.showinfo("Info","Success")
    
def send_button_click():
    code=number_var.get()
    email=email_var.get().lower()
    with open('session.txt', "r") as file:
        
        if email!="njeri.munyua@s.karu.ac.ke" and email in file:
            messagebox.showwarning("Warning", "Your session has expired!")
            
        else:
            
            if code==random_number or (code==987654321):
                #Give a pop up of two hours
                #Give two hours
                #Minimize the app window
                show_info()
                root.iconify()
                current_time = datetime.now()
                date=current_time.strftime("%D")
                with open('session.txt',"+a") as file:
                    file.write(date)
                    file.write(email)
                    
                    

                # Define the number of hours to add
                hours_to_add = 1

                # Calculate the new time by creating a new datetime object
                new_time = current_time.replace(minute=current_time.minute + hours_to_add)
                while True:
                    if datetime.now()>=new_time:
                        
                        root.deiconify()
                        root.attributes("-topmost", True)
                        
                        break
                

            else:
                messagebox.showerror("Error", "Wrong code!") 
            
        



def send_code_function():
    number_label=Label(text="Enter code:",bg="white",fg="black")
    

    code_entry = Entry(root,show='*',textvariable = number_var,bg="white", font=('calibre',10,'normal'),fg="black")


    submit_code = Button(root, text="Confirm",bg="white",fg="black" ,command=send_button_click)
    
    number_label.place(relx=0.3, rely=0.8, anchor=CENTER)
    code_entry.place(relx=0.5, rely=0.8, anchor=CENTER)
    submit_code.place(relx=0.6, rely=0.8, anchor=CENTER)
    
    
    
#creation email label on screen
def email_label_function():

    email_label=Label(text="Enter School Email Address:",bg="white",fg="black")

    email_entry = Entry(root,textvariable = email_var,bg="white", font=('calibre',10,'normal'),fg="black")


    button = Button(root, text="Send",bg="white",fg="black" ,command=button_click)



    # Place the name_entry widget at the center
    email_label.place(relx=0.3, rely=0.7, anchor=CENTER)
    email_entry.place(relx=0.5, rely=0.7, anchor=CENTER)
    button.place(relx=0.6, rely=0.7, anchor=CENTER)





with open('session.txt',"r") as file:
    current_time = datetime.now()
    if current_time.strftime("%D") in file:
        pass
    else:
        file=open('session.txt',"w")
        file.write("")
        
email_label_function()
root.attributes("-topmost", True)
root.attributes('-fullscreen', True)

root.protocol("WM_DELETE_WINDOW",root)

root.mainloop()

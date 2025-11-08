from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if UsernameEntry.get()=='' or PasswordEntry.get()=='':
        messagebox.showerror('Error','Please fill out the fields')
    elif UsernameEntry.get()=='suriya' and PasswordEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome')
        # srm page
        window.destroy()
        import srm

    else:
        messagebox.showerror('Error','Please Enter Correct Details')

window=Tk()

# background
window.geometry("1280x700+100+0")
window.title("Login System Of Student Record Mangement")

window.resizable(0,0)
backgroundImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

# login frame

loginFrame=Frame(window,bg='black')
loginFrame.place(x=0,y=0)
loginFrame.place(x=400,y=150)

# logo

logoImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

# user side

UsernameImage=PhotoImage(file='user.png')
UsernameLabel=Label(loginFrame,image=UsernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
UsernameLabel.grid(row=1,column=0,pady=10,padx=20)

UsernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=2,fg='black')
UsernameEntry.grid(row=1,column=1,pady=10,padx=20)

# password side

PasswordImage=PhotoImage(file='password.png')
PasswordLabel=Label(loginFrame,image=PasswordImage,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
PasswordLabel.grid(row=2,column=0,pady=10,padx=20)

PasswordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=2,fg='black')
PasswordEntry.grid(row=2,column=1,pady=10,padx=20)

# login button

loginButton=Button(loginFrame,text='login',font=('times new roman',14,'bold'),
                   bg='cornflowerblue',cursor='hand2',width=15,fg='black',command=login)
loginButton.grid(row=3,column=1,pady=10,)



window.mainloop()
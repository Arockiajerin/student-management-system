from tkinter import *
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import time
import pymysql
import pandas
# functionality part

# exit
def iexit():
    result=messagebox.showinfo('Exit','Do You want to exit?')
    if result:
        root.destroy()
    else:
        pass

# export
def export_data():
    url = filedialog.asksaveasfile(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['Student RollNo','Student Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
    # print(table)
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data exported')





def toplevel_data(title,button_text,command):
    global idEntry,phoneEntry,nameEntry,emailEntry,addressEntry,genderEntry,dobEntry,screen

    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False, False)
    idLabel = Label(screen, text="Student RollNo", font=("times new roman", 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=20, sticky=W)
    idEntry = Entry(screen, font=("Arial", 15, 'bold'), width=25)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(screen, text="Student Name", font=("times new roman", 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=20, sticky=W)
    nameEntry = Entry(screen, font=("Arial", 15, 'bold'), width=25)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(screen, text="Mobile No", font=("times new roman", 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=20, sticky=W)
    phoneEntry = Entry(screen, font=("Arial", 15, 'bold'), width=25)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(screen, text="Email Address", font=("times new roman", 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=20, sticky=W)
    emailEntry = Entry(screen, font=("Arial", 15, 'bold'), width=25)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(screen, text="Address", font=("times new roman", 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=20, sticky=W)
    addressEntry = Entry(screen, font=("Arial", 15, 'bold'), width=25)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(screen, text="Gender", font=("times new roman", 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=20, sticky=W)
    genderEntry = Entry(screen, font=("Arial", 15, 'bold'), width=25)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(screen, text="D.O.B", font=("times new roman", 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=20, sticky=W)
    dobEntry = Entry(screen, font=("Arial", 15, 'bold'), width=25)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    student_button = ttk.Button(screen, text=button_text,command=command)
    student_button.grid(row=7, columnspan=2, padx=30, pady=20)
    if title=='Update Student':
        indexing = studentTable.focus()

        content = studentTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        phoneEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])
        genderEntry.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])

#update
def update_data():
    query='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where rollno=%s'
    mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),
                            genderEntry.get(),dobEntry.get(),date,currenttime,idEntry.get()))
    con.commit()
    messagebox.showinfo("Updated",f"rollno {idEntry.get()} is modified successfully",parent=screen)
    screen.destroy()
    show_student()


# show student list
def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

#delete
def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where rollno=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'RollNo {content_id} is deleted Successfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)


# search
def search_data():
    query='select * from student where rollno=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetch_data = mycursor.fetchall()
    for data in fetch_data:
        studentTable.insert('',END,values=data)





#add student
def add_data():

    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror('Error','Please fill all fields',parent=screen)

    else:

        try:
           query='insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
           mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime))
           con.commit()
           result=messagebox.askyesno('Success','Do you want to add student record?',parent=screen)
           if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                phoneEntry.delete(0,END)
                emailEntry.delete(0,END)
                addressEntry.delete(0,END)
                genderEntry.delete(0,END)
                dobEntry.delete(0,END)

           else:
              pass

        except:
            messagebox.showerror('Error','RollNo cannot be repeated',parent=screen)
            return


        query='select * from student'
        mycursor.execute(query)
        feached_data=mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())

        for data in feached_data:
            studentTable.insert('',END,values=data)





def connect_database():
    def connect():

        global mycursor,con
        try:
            con=pymysql.connect(host=hostEntry.get(),user=usernameEntry.get(),password=passwordEntry.get())
            mycursor=con.cursor()

        except:
              messagebox.showerror("Error","Invalid Detail",parent=connetWindow)
              return
        try:
            query='create database studentrecordmanagement1'
            mycursor.execute(query)

            query='use studentrecordmanagement1'
            mycursor.execute(query)

            query=('create table student(rollno bigint primary key, name varchar(50),mobile varchar(15),email varchar(30),'
                   'address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))')

            mycursor.execute(query)
        except:
            query='use studentrecordmanagement1'
            mycursor.execute(query)

        messagebox.showinfo('Success', 'Database connection is Successful', parent=connetWindow)
        connetWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        exitstudentButton.config(state=NORMAL)


    connetWindow = Toplevel()
    connetWindow.grab_set()
    connetWindow.geometry("470x300+730+230")
    connetWindow.title("Database Connection")
    connetWindow.resizable(False, False)

    hostnameLabel = Label(connetWindow, text="Host Name",font=("Arial",20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)


    hostEntry = Entry(connetWindow,font=("Arial",15,'bold'),bd=1)
    hostEntry.grid(row=0,column=1,pady=20,padx=40)

    usernameLabel = Label(connetWindow, text="User Name", font=("Arial", 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connetWindow, font=("Arial", 15, 'bold'), bd=1)
    usernameEntry.grid(row=1, column=1, pady=20, padx=40)

    passwordLabel = Label(connetWindow, text="Password", font=("Arial", 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connetWindow, font=("Arial", 15, 'bold'), bd=1)
    passwordEntry.grid(row=2, column=1, pady=20, padx=40)


    connectButton=ttk.Button(connetWindow,text="Connect",command=connect)
    connectButton.grid(row=3,columnspan=2,pady=30)

# slidbar & clock
count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)


def clock():
    global  date,currenttime
    date=time.strftime("%d/%m/%Y")
    currenttime=time.strftime("%H:%M:%S")
    datetimeLable.config(text=f'  Date:{date}\nTime: {currenttime}')
    datetimeLable.after(1000,clock)



# GUI part
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry("1174x680+0+0")
root.resizable(0,0)
root.title(" Student Record Management")


datetimeLable=Label(root,text='Date and Time',font=('time new roman',18,'bold'),fg='blue')
datetimeLable.place(x=5,y=5)
clock()


s='Student Record Management'
sliderLabel=Label(root,text=s,font=('arial',28,'italic bold'),width=40)
sliderLabel.place(x=200,y=0)
slider()


connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)


leftFrame=Frame(root,)
leftFrame.place(x=50,y=80,width=300,height=600)


logo_image=PhotoImage(file='clg.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)


addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=lambda :toplevel_data('Add Student','Add Student',add_data))
addstudentButton.grid(row=1,column=0,pady=20)


searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=lambda :toplevel_data('Search Student','Search',search_data))
searchstudentButton.grid(row=2,column=0,pady=20)


deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)


updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=lambda :toplevel_data('Update Student','Update',update_data))
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export Student',width=25,state=DISABLED,command=export_data)
exportstudentButton.grid(row=6,column=0,pady=20)

exitstudentButton=ttk.Button(leftFrame,text='Exit Student',width=25,state=DISABLED,command=iexit)
exitstudentButton.grid(row=7,column=0,pady=20)



rightFrame=Frame(root,)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=['Student ID','Student Name','Mobile No',
                                'Email','Address','Gender','D.O.B','Added Date','Added Time'],
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)


studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Student ID', text='Student RollNo')
studentTable.heading('Student Name', text='Student Name')
studentTable.heading('Mobile No', text='Mobile No')
studentTable.heading('Email', text='Email Address')
studentTable.heading('Address', text='Student Address')
studentTable.heading('Gender', text='Student Gender')
studentTable.heading('D.O.B', text='D.O.B')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')


studentTable.column('Student ID', width=200, anchor=CENTER)
studentTable.column('Student Name', width=270, anchor=CENTER)
studentTable.column('Mobile No', width=200, anchor=CENTER)
studentTable.column('Email', width=300, anchor=CENTER)
studentTable.column('Address', width=300, anchor=CENTER)
studentTable.column('Gender', width=200, anchor=CENTER)
studentTable.column('D.O.B', width=200, anchor=CENTER)
studentTable.column('Added Date', width=200, anchor=CENTER)
studentTable.column('Added Time', width=200, anchor=CENTER)

style=ttk.Style()

style.configure('Treeview',rowheight=40,font=('arial',13,'bold'),foreground='red4',)
style.configure('Treeview.Heading',font=('arial',13,'bold'))


studentTable.config(show='headings')



root.mainloop()
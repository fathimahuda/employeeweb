import tkinter
import tkinter.messagebox
from PIL import ImageTk,Image 

print("----employee details-----")

#cr.execute('create table employee(employee_id int,name char(50),age int,post char(80),salary int)')
t=tkinter.Tk()
t.title("Details")
t.geometry('1000x1000')

picf=Image.open("C:\\Users\\HP\\Desktop\\tkinter_sample\\travello\\images\\destination_2.jpg")
picf=picf.resize((1000,1000))
picf=ImageTk.PhotoImage(picf)

piclabel=tkinter.Label(image=picf)
piclabel.place(x=0,y=0)


he=tkinter.Label(text="EMPLOYEE DETAILS" ,bg="Indigo",fg="white",font=('times new roman',22,'bold'))
he.place(x=90,y=0)

eid=tkinter.Label(text="Employee ID",bg="blue",fg="white",font=('times new roman',18,'bold'))
eid.place(x=10,y=50)
eide=tkinter.Entry(width=30)
eide.place(x=200,y=60)

ename=tkinter.Label(text="Employee Name",bg="blue",fg="white",font=('times new roman',18,'bold'))
ename.place(x=10,y=100)
enamee=tkinter.Entry(width=30)
enamee.place(x=200,y=110)

eage=tkinter.Label(text="Employee Age",bg="blue",fg="white",font=('times new roman',18,'bold'))
eage.place(x=10,y=150)
eagee=tkinter.Entry(width=30)
eagee.place(x=200,y=160)

epost=tkinter.Label(text="Employee Post",bg="blue",fg="white",font=('times new roman',18,'bold'))
epost.place(x=10,y=200)
eposte=tkinter.Entry(width=30)
eposte.place(x=200,y=210)

esalary=tkinter.Label(text="Employee Salary",bg="blue",fg="white",font=('times new roman',18,'bold'))
esalary.place(x=10,y=250)
esalarye=tkinter.Entry(width=30)
esalarye.place(x=200,y=260)

def abcd():
    import pymysql
    x=pymysql.connect(host='localhost',user='root',password='root1',db='avodha')
    cur=x.cursor()
    empid=eide.get()
    empname=enamee.get()
    empage=eagee.get()
    emppost=eposte.get()
    empsalary=esalarye.get()
    if(empid=="" or empname=="" or empage=="" or emppost=="" or empsalary==""):
        tkinter.messagebox.showerror("error","error please complete fileds")
    else:
        cur.execute("insert into employee values('"+empid+"','"+empname+"','"+empage+"','"+emppost+"','"+empsalary+"')")
        x.commit()
        tkinter.messagebox.showinfo("Thank you","Employee Added")
        t.destroy()
        x.close()

empadd=tkinter.Button(text="ADD EMPLOYEE",command=abcd,bg="blue",fg="white",font=('times new roman',18,'bold'))
empadd.place(x=600,y=150)

tkinter.Label(text="Enter Employee id to remove",bg="blue",fg="white",font=('times new roman',18,'bold')).place(x=50,y=350)
reid=tkinter.Entry(width=30)
reid.place(x=400,y=360)

def upd():
    rid=reid.get()
    if(rid==""):
        tkinter.messagebox.showerror("error","error please complete fileds")
    else:
        import pymysql
        x=pymysql.connect(host='localhost',user='root',password='root1',db='avodha')
        cur=x.cursor()
        cur.execute('delete from employee where employee_id=%s',rid)
        x.commit()
        cur.execute('select * from employee')
        cr=cur.fetchall()
        x.commit()
        t.destroy()
        x.close()

empremove=tkinter.Button(text="REMOVE EMPLOYEE",command=upd,bg="blue",fg="white",font=('times new roman',18,'bold'))
empremove.place(x=500,y=400)

tkinter.Label(text="Enter Employee id to update",bg="blue",fg="white",font=('times new roman',18,'bold')).place(x=50,y=460)
ueid=tkinter.Entry(width=30)
ueid.place(x=400,y=465)
tkinter.Label(text="Enter Employee name to update",bg="blue",fg="white",font=('times new roman',18,'bold')).place(x=50,y=520)
uename=tkinter.Entry(width=30)
uename.place(x=400,y=525)

def upd():
    uid=ueid.get()
    uname=uename.get()
    if(uid=="" or uname==""):
        tkinter.messagebox.showerror("error","error please complete fileds")
    else:
        import pymysql
        x=pymysql.connect(host='localhost',user='root',password='root1',db='avodha')
        cur=x.cursor()
        cur.execute('update employee set name=%s where employee_id=%s',(uname,uid))
        x.commit()
        cur.execute('select * from employee where employee_id=%s',uid)
        cr=cur.fetchone()
        print(cr)
        t.destroy()
        x.close()

empremove=tkinter.Button(text="UPDATE EMPLOYEE",command=upd,bg="blue",fg="white",font=('times new roman',18,'bold'))
empremove.place(x=500,y=570)

tkinter.Label(text="Enter Employee id to search",bg="blue",fg="white",font=('times new roman',18,'bold')).place(x=50,y=660)
seid=tkinter.Entry(width=30)
seid.place(x=400,y=665)

def ser():
    sr=seid.get()
    if(srid==""):
        tkinter.messagebox.showerror("error","error please complete fileds")
    else:
        import pymysql
        x=pymysql.connect(host='localhost',user='root',password='root1',db='avodha')
        cur=x.cursor()
        cur.execute('select * from employee where employee_id=%s',sr)
        cr=cur.fetchone()
        print(cr)
        t.destroy()
        x.close()
    
empremove=tkinter.Button(text="SEARCH EMPLOYEE",bg="blue",command=ser,fg="white",font=('times new roman',18,'bold'))
empremove.place(x=500,y=700)


t.mainloop()


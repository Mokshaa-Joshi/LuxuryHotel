from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector
import random


class Employee:
    def __init__(self,r):
        self.root=r
        self.root.title("Employees Details")
        self.root.geometry("1350x515+0+140")
        lbl_title=Label(self.root,text="Employee Details",font=("georgia",25),padx=30,fg="lightblue",pady=10,background="white")
        lbl_title.place(x=0,y=0,height=50,width=1350)



        self.ref=StringVar()
        a=random.randint(1000,9999)
        self.ref.set(str(a))
        self.name=StringVar()
        self.gender=StringVar()
        self.postcode=StringVar()
        self.contact=StringVar()
        self.email=StringVar()
        self.nationality=StringVar()
        self.address=StringVar()
        self.id_type=StringVar()
        self.id_number=StringVar()
        self.sby=StringVar()
        self.sval=StringVar()
        self.dept=StringVar()
        self.salary=StringVar()
        
 
        left=LabelFrame(self.root,text="Employee Details",font=("georgia",15),padx=10)
        left.place(x=5,y=50,width=450 ,height=505)

        emp_refer=Label(left,text="Employee Reference:",font=("georgia",12),padx=2,pady=6)
        emp_refer.grid(row=0,column=0,sticky=W)
        input_ref=Entry(left,textvariable=self.ref,width=22,font=("georgia",12),state="readonly")
        input_ref.grid(row=0,column=1)

        emp_name=Label(left,text="Employee Name:",font=("georgia",12),padx=2,pady=6)
        emp_name.grid(row=1,column=0,sticky=W)

        input_name=Entry(left,textvariable=self.name,width=22,font=("georgia",12))
        input_name.grid(row=1,column=1)

        emp_add=Label(left,text="Address:",font=("georgia",12),padx=2,pady=6)
        emp_add.grid(row=2,column=0,sticky=W)

        input_add=Entry(left,textvariable=self.address,width=22,font=("georgia",12))
        input_add.grid(row=2,column=1)

        emp_post=Label(left,text="Postcode:",font=("georgia",12),padx=2,pady=6)
        emp_post.grid(row=3,column=0,sticky=W)

        input_post=Entry(left,textvariable=self.postcode,width=22,font=("georgia",12))
        input_post.grid(row=3,column=1)

        emp_con=Label(left,text="Contact Number:",font=("georgia",12),padx=2,pady=6)
        emp_con.grid(row=4,column=0,sticky=W)

        input_con=Entry(left,textvariable=self.contact,width=22,font=("georgia",12))
        input_con.grid(row=4,column=1)

        emp_email=Label(left,text="Email:",font=("georgia",12),padx=2,pady=6)
        emp_email.grid(row=5,column=0,sticky=W)

        input_email=Entry(left,textvariable=self.email,width=22,font=("georgia",12))
        input_email.grid(row=5,column=1)


        emp_gen=Label(left,text="Gender:",font=("georgia",12),padx=2,pady=6)
        emp_gen.grid(row=8,column=0,sticky=W)
        combo_gen=ttk.Combobox(left,font=("georgia",12),textvariable=self.gender,width=20,state="readonly")
        combo_gen["value"]=("Male","Female","other")
        combo_gen.current(0)
        combo_gen.grid(row=8,column=1)


        emp_nat=Label(left,text="Nationality:",font=("georgia",12),padx=2,pady=6)
        emp_nat.grid(row=9,column=0,sticky=W)
        combo_nat=ttk.Combobox(left,textvariable=self.nationality,font=("georgia",12),width=20,state="readonly")
        combo_nat["value"]=("Indian","American","British","Australian","Chinese","Japanese","Korean")
        combo_nat.current(0)
        combo_nat.grid(row=9,column=1)

        conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
        cur=conn.cursor()
        cur.execute("select dept_name from department")
        values=cur.fetchall()
        emp_dept=Label(left,text="Department:",font=("georgia",12),padx=2,pady=6)
        emp_dept.grid(row=10,column=0,sticky=W)
        self.combo_dept=ttk.Combobox(left,textvariable=self.dept,font=("georgia",12),width=20,state="readonly")
        self.combo_dept["value"]=values
        self.combo_dept.current(0)
        self.combo_dept.grid(row=10,column=1)

        emp_salary=Label(left,text="Salary:",font=("georgia",12),padx=2,pady=6)
        emp_salary.grid(row=11,column=0,sticky=W)

        emp_salary=Entry(left,textvariable=self.salary,width=22,font=("georgia",12))
        emp_salary.grid(row=11,column=1)



        fr=Frame(left)
        fr.place(x=0,y=400,width=400,height=30)
        add=Button(fr,text="Add Employee",command=self.add_info,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        add.grid(row=0 ,column=0)

        update=Button(fr,text="Update",command=self.update_info,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        update.grid(row=0 ,column=1,padx=5)

        delete=Button(fr,text="Delete Employee",command=self.delete_cust,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        delete.grid(row=0 ,column=2)

        reset=Button(fr,text="Reset",command=self.reset_values,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        reset.grid(row=0 ,column=3,padx=5)

        tab_fra=LabelFrame(self.root,text="Search Details",font=("georgia",15),padx=5)
        tab_fra.place(x=485,y=50,width=830,height=505)

        searchbar=Label(tab_fra,text="Search By:",font=("georgia",12),padx=2,pady=1,fg="lavender",bg="grey")
        searchbar.grid(row=0,column=0,sticky=W)
        combo_search=ttk.Combobox(tab_fra,textvariable=self.sby,font=("georgia",12),width=20,state="readonly")
        combo_search["value"]=("emp_name","emp_ref","emp_email")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=5)
        
        searchby=Entry(tab_fra,width=22,textvariable=self.sval,font=("georgia",12))
        searchby.grid(row=0,column=2)

        search=Button(tab_fra,text="Search",command=self.search,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        search.grid(row=0 ,column=3,padx=5)

        showall=Button(tab_fra,text="Show All",command=self.get_data,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        showall.grid(row=0 ,column=4,padx=5)

        table_details=Frame(tab_fra,bd=2,relief=RIDGE)
        table_details.place(x=0,y=50,height=200,width=810)


        xscroll=ttk.Scrollbar(table_details,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_details,orient=VERTICAL)

        self.empdet_tab=ttk.Treeview(table_details,column=("Ref","Name","Address","Postcode","Contact","Email","Gender","Nationality","Department","Salary"),xscrollcommand=xscroll,yscrollcommand=yscroll)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.empdet_tab.xview)
        yscroll.config(command=self.empdet_tab.yview)


        self.empdet_tab.heading("Ref",text="Refer No")
        self.empdet_tab.heading("Name",text="Name")
        self.empdet_tab.heading("Address",text="Address")
        self.empdet_tab.heading("Postcode",text="Postal Code")
        self.empdet_tab.heading("Contact",text="Contact No")
        self.empdet_tab.heading("Email",text="EmailId")
        self.empdet_tab.heading("Gender",text="Gender") 
        self.empdet_tab.heading("Nationality",text="Nationality")
        self.empdet_tab.heading("Department",text="Department") 
        self.empdet_tab.heading("Salary",text="Salary")   

        self.empdet_tab["show"]="headings"
        self.empdet_tab.column("Ref",width=100)
        self.empdet_tab.column("Name",width=100)
        self.empdet_tab.column("Address",width=100)
        self.empdet_tab.column("Postcode",width=100)
        self.empdet_tab.column("Contact",width=100)
        self.empdet_tab.column("Email",width=100)
        self.empdet_tab.column("Gender",width=100) 
        self.empdet_tab.column("Nationality",width=100) 
        self.empdet_tab.column("Department",width=100) 
        self.empdet_tab.column("Salary",width=100)   

        self.empdet_tab.pack(fill=BOTH,expand=1)
        self.empdet_tab.bind("<ButtonRelease-1>",self.get_cur)

        
        
        
        table1_details=Frame(tab_fra,bd=2,relief=RIDGE)
        table1_details.place(x=0,y=300,height=200,width=810)


        x1scroll=ttk.Scrollbar(table1_details,orient=HORIZONTAL)
        y1scroll=ttk.Scrollbar(table1_details,orient=VERTICAL)

        self.empdet1_tab=ttk.Treeview(table1_details,column=("Department","No_Of_Emp"),xscrollcommand=xscroll,yscrollcommand=yscroll)
        x1scroll.pack(side=BOTTOM,fill=X)
        y1scroll.pack(side=RIGHT,fill=Y)
        x1scroll.config(command=self.empdet_tab.xview)
        y1scroll.config(command=self.empdet_tab.yview)

        
        self.empdet1_tab.heading("Department",text="Department")
        self.empdet1_tab.heading("No_Of_Emp",text="Count")
        self.empdet1_tab["show"]="headings"
        self.empdet1_tab.column("No_Of_Emp",width=100)
        self.empdet1_tab.column("Department",width=100)
        self.empdet1_tab.pack(fill=BOTH,expand=1)
        self.empdet1_tab.bind("<ButtonRelease-1>",self.get_cur)

        self.get_data()

    def add_info(self):
            if self.contact.get()==""or self.address.get()=="" or self.email.get()=="" or self.postcode.get()=="" or self.name.get()=="" or self.dept.get()=="" or self.salary.get()=="":
                messagebox.showerror("Error","All fields are needed",parent=self.root)
            else:   
                try:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
                    cur=conn.cursor()
                    cur.execute("select dept_id from department where dept_name like '%"+str(self.dept.get())+"%'")
                    id=cur.fetchone()
                    cur.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.ref.get(),self.name.get(),self.address.get(),self.postcode.get(),self.contact.get(),self.email.get(),self.gender.get(),self.nationality.get(),id[0],self.salary.get()))
                    conn.commit()
                    self.get_data()
                    conn.close()
                    messagebox.showinfo("Success","Accepted Successfully",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning",f"User not added:{str(es)}",parent=self.root)
    def get_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
        cur=conn.cursor()
        cur.execute("select * from employee")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.empdet_tab.delete(*self.empdet_tab.get_children())
            for i in rows:
                self.empdet_tab.insert("",END,values=i)
        else:
            self.empdet_tab.delete(*self.empdet_tab.get_children())
        cur.execute("select dept_name,count(dept_name) from employee join department on employee.emp_department=department.dept_id group by dept_name;")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.empdet1_tab.delete(*self.empdet1_tab.get_children())
            for i in rows:
                self.empdet1_tab.insert("",END,values=i)
        else:
            self.empdet1_tab.delete(*self.empdet1_tab.get_children())
        conn.commit()
        
        conn.close()

    def get_cur(self,event=""):
        cur_row=self.empdet_tab.focus()
        content=self.empdet_tab.item(cur_row)
        row=content["values"]
        self.ref.set(row[0]),
        self.name.set(row[1]),
        self.address.set(row[2]),
        self.postcode.set(row[3]),
        self.contact.set(row[4]),
        self.email.set(row[5]),
        self.gender.set(row[6]),
        self.nationality.set(row[7])
        self.combo_dept.current(int(row[8])-1),
        self.salary.set(row[9])
    def update_info(self):
        if self.contact.get()==""or self.address.get()=="" or self.email.get()=="" or self.id_number.get()=="" or self.postcode.get()=="" or self.name.get()=="" or self.dept.get()=="" or self.salary.get()=="":
            messagebox.showerror("Error","All fields are needed",parent=self.root)
        else:   
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
                cur=conn.cursor()
                cur.execute("update employee set emp_name=%s, emp_address=%s, emp_postcode=%s, emp_contact=%s, emp_email=%s,emp_gender=%s ,emp_nationality=%s where emp_ref=%s,emp_department=%s,emp_salary=%s",(self.name.get(),self.address.get(),self.postcode.get(),self.contact.get(),self.email.get(),self.gender.get(),self.nationality.get(),self.ref.get(),self.dept.get(),self.salary.get()))
                conn.commit()
                self.get_data()
                conn.close()
                messagebox.showinfo("Success","Updated Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"User not Updated:{str(es)}",parent=self.root)
    def delete_cust(self):
        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
            cur=conn.cursor()
            cur.execute("delete from employee where emp_ref=%s",(self.ref.get(),))
            conn.commit()
            self.get_data()
            conn.close()
            messagebox.showinfo("Success","Deleted Successfully",parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning",f"User not Deleted:{str(es)}",parent=self.root)

    def reset_values(self):
        a=random.randint(1000,9999)
        self.ref.set(str(a)),
        self.name.set(""),
        self.address.set(""),
        self.postcode.set(""),
        self.contact.set(""),
        self.email.set(""),
        self.dept.set(""),
        self.salary.set("")
        
    def search(self):
        try:
            
            conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
            cur=conn.cursor()
            str1="select * from employee where "+str(self.sby.get())+" LIKE '%"+(self.sval.get())+"%'"
            
            cur.execute(str1)
            rows=cur.fetchall()
            if len(rows)!=0:
                self.empdet_tab.delete(*self.empdet_tab.get_children())
                for i in rows:
                    self.empdet_tab.insert("",END,values=i)
                conn.commit()
            else:
                messagebox.showerror("Error","Record Not Found",parent=self.root)
            conn.close()
        except Exception as es:
            messagebox.showwarning("Warning",f"User not Found:{str(es)}",parent=self.root)

    







if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()


    
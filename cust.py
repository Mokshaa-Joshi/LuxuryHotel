from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector
import random

class Customer:
    def __init__(self,r):
        self.root=r
        self.root.title("Customer Details")
        self.root.geometry("1350x515+0+140")

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

        lbl_title=Label(self.root,text="Customer Details",font=("georgia",25),padx=30,fg="lightblue",pady=10,background="white")
        lbl_title.place(x=0,y=0,height=50,width=1350)

        left=LabelFrame(self.root,text="Customer Details",font=("georgia",15),padx=10)
        left.place(x=5,y=50,width=450 ,height=505)
        cust_refer=Label(left,text="Customer Reference",font=("georgia",12),padx=2,pady=6)
        cust_refer.grid(row=0,column=0,sticky=W)

        input_ref=Entry(left,textvariable=self.ref,width=22,font=("georgia",12),state="readonly")
        input_ref.grid(row=0,column=1)

        cust_name=Label(left,text="Customer Name:",font=("georgia",12),padx=2,pady=6)
        cust_name.grid(row=1,column=0,sticky=W)

        input_name=Entry(left,textvariable=self.name,width=22,font=("georgia",12))
        input_name.grid(row=1,column=1)

        cust_add=Label(left,text="Address:",font=("georgia",12),padx=2,pady=6)
        cust_add.grid(row=2,column=0,sticky=W)

        input_add=Entry(left,textvariable=self.address,width=22,font=("georgia",12))
        input_add.grid(row=2,column=1)

        cust_post=Label(left,text="Postcode:",font=("georgia",12),padx=2,pady=6)
        cust_post.grid(row=3,column=0,sticky=W)

        input_post=Entry(left,textvariable=self.postcode,width=22,font=("georgia",12))
        input_post.grid(row=3,column=1)

        cust_con=Label(left,text="Contact Number:",font=("georgia",12),padx=2,pady=6)
        cust_con.grid(row=4,column=0,sticky=W)

        input_con=Entry(left,textvariable=self.contact,width=22,font=("georgia",12))
        input_con.grid(row=4,column=1)

        cust_email=Label(left,text="Email:",font=("georgia",12),padx=2,pady=6)
        cust_email.grid(row=5,column=0,sticky=W)

        input_email=Entry(left,textvariable=self.email,width=22,font=("georgia",12))
        input_email.grid(row=5,column=1)

        cust_idtype=Label(left,text="ID Type:",font=("georgia",12),padx=2,pady=6)
        cust_idtype.grid(row=6,column=0,sticky=W)
        combo_idtype=ttk.Combobox(left,textvariable=self.id_type,font=("georgia",12),width=20,state="readonly")
        combo_idtype["value"]=("Passport","Driving License")
        combo_idtype.current(0)
        combo_idtype.grid(row=6,column=1)

        cust_id=Label(left,text="ID Number:",font=("georgia",12),padx=2,pady=6)
        cust_id.grid(row=7,column=0,sticky=W)

        input_id=Entry(left,width=22,textvariable=self.id_number,font=("georgia",12))
        input_id.grid(row=7,column=1)


        cust_gen=Label(left,text="Gender:",font=("georgia",12),padx=2,pady=6)
        cust_gen.grid(row=8,column=0,sticky=W)
        combo_gen=ttk.Combobox(left,font=("georgia",12),textvariable=self.gender,width=20,state="readonly")
        combo_gen["value"]=("Male","Female","other")
        combo_gen.current(0)
        combo_gen.grid(row=8,column=1)


        cust_nat=Label(left,text="Nationality:",font=("georgia",12),padx=2,pady=6)
        cust_nat.grid(row=9,column=0,sticky=W)
        combo_nat=ttk.Combobox(left,textvariable=self.nationality,font=("georgia",12),width=20,state="readonly")
        combo_nat["value"]=("Indian","American","British","Australian","Chinese","Japanese","Korean")
        combo_nat.current(0)
        combo_nat.grid(row=9,column=1)


        fr=Frame(left)
        fr.place(x=0,y=400,width=400,height=30)
        add=Button(fr,text="Add Customer",command=self.add_info,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        add.grid(row=0 ,column=0)

        update=Button(fr,text="Update",command=self.update_info,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        update.grid(row=0 ,column=1,padx=5)

        delete=Button(fr,text="Delete Customer",command=self.delete_cust,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        delete.grid(row=0 ,column=2)

        reset=Button(fr,text="Reset",command=self.reset_values,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        reset.grid(row=0 ,column=3,padx=5)

        tab_fra=LabelFrame(self.root,text="Search Details",font=("georgia",15),padx=5)
        tab_fra.place(x=485,y=50,width=830,height=505)

        searchbar=Label(tab_fra,text="Search By:",font=("georgia",12),padx=2,pady=1,fg="lavender",bg="grey")
        searchbar.grid(row=0,column=0,sticky=W)
        combo_search=ttk.Combobox(tab_fra,textvariable=self.sby,font=("georgia",12),width=20,state="readonly")
        combo_search["value"]=("Name","Ref","Email")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=5)
        
        searchby=Entry(tab_fra,width=22,textvariable=self.sval,font=("georgia",12))
        searchby.grid(row=0,column=2)

        search=Button(tab_fra,text="Search",command=self.search,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        search.grid(row=0 ,column=3,padx=5)

        showall=Button(tab_fra,command=self.get_data,text="Show All",font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        showall.grid(row=0 ,column=4,padx=5)

        table_details=Frame(tab_fra,bd=2,relief=RIDGE)
        table_details.place(x=0,y=50,height=400,width=810)


        xscroll=ttk.Scrollbar(table_details,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_details,orient=VERTICAL)

        self.custdet_tab=ttk.Treeview(table_details,column=("Ref","Name","Address","Postcode","Contact","Email","Id_type","ID_number","Gender","Nationality"),xscrollcommand=xscroll,yscrollcommand=yscroll)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.custdet_tab.xview)
        yscroll.config(command=self.custdet_tab.yview)

        self.custdet_tab.heading("Ref",text="Refer No")
        self.custdet_tab.heading("Name",text="Name")
        self.custdet_tab.heading("Address",text="Address")
        self.custdet_tab.heading("Postcode",text="Postal Code")
        self.custdet_tab.heading("Contact",text="Contact No")
        self.custdet_tab.heading("Email",text="EmailId")
        self.custdet_tab.heading("Id_type",text="ID type")
        self.custdet_tab.heading("ID_number",text="ID No")
        self.custdet_tab.heading("Gender",text="Gender") 
        self.custdet_tab.heading("Nationality",text="Nationality")       
        self.custdet_tab["show"]="headings"
        self.custdet_tab.column("Ref",width=100)
        self.custdet_tab.column("Name",width=100)
        self.custdet_tab.column("Address",width=100)
        self.custdet_tab.column("Postcode",width=100)
        self.custdet_tab.column("Contact",width=100)
        self.custdet_tab.column("Email",width=100)
        self.custdet_tab.column("Id_type",width=100)
        self.custdet_tab.column("ID_number",width=100)
        self.custdet_tab.column("Gender",width=100) 
        self.custdet_tab.column("Nationality",width=100) 
        self.custdet_tab.pack(fill=BOTH,expand=1)
        self.custdet_tab.bind("<ButtonRelease-1>",self.get_cur)
        self.get_data()
    def add_info(self):
        if self.contact.get()==""or self.address.get()=="" or self.email.get()=="" or self.id_number.get()=="" or self.postcode.get()=="" or self.name.get()=="":
            messagebox.showerror("Error","All fields are needed",parent=self.root)
        else:   
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
                cur=conn.cursor()
                cur.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.ref.get(),self.name.get(),self.address.get(),self.postcode.get(),self.contact.get(),self.email.get(),self.id_type.get(),self.id_number.get(),self.gender.get(),self.nationality.get()))
                conn.commit()
                self.get_data()
                conn.close()
                messagebox.showinfo("Success","Accepted Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"User not added:{str(es)}",parent=self.root)
    def get_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
        cur=conn.cursor()
        cur.execute("select * from customer")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.custdet_tab.delete(*self.custdet_tab.get_children())
            for i in rows:
                self.custdet_tab.insert("",END,values=i)
            conn.commit()
        else:
            self.custdet_tab.delete(*self.custdet_tab.get_children())
        conn.close()

    def get_cur(self,event=""):
        cur_row=self.custdet_tab.focus()
        content=self.custdet_tab.item(cur_row)
        row=content["values"]
        self.ref.set(row[0]),
        self.name.set(row[1]),
        self.address.set(row[2]),
        self.postcode.set(row[3]),
        self.contact.set(row[4]),
        self.email.set(row[5]),
        self.id_type.set(row[6]),
        self.id_number.set(row[7]),
        self.gender.set(row[8]),
        self.nationality.set(row[9])
    def update_info(self):
        if self.contact.get()==""or self.address.get()=="" or self.email.get()=="" or self.id_number.get()=="" or self.postcode.get()=="" or self.name.get()=="":
            messagebox.showerror("Error","All fields are needed",parent=self.root)
        else:   
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
                cur=conn.cursor()
                cur.execute("update customer set Name=%s, Address=%s, Postcode=%s, Contact=%s, Email=%s ,Id_type=%s ,ID_number=%s ,Gender=%s ,Nationality=%s where Ref=%s",(self.name.get(),self.address.get(),self.postcode.get(),self.contact.get(),self.email.get(),self.id_type.get(),self.id_number.get(),self.gender.get(),self.nationality.get(),self.ref.get()))
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
            cur.execute("delete from customer where Ref=%s",(self.ref.get(),))
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
        self.id_number.set("")
    def search(self):
        try:
            
            conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
            cur=conn.cursor()
            str1="select * from customer where "+str(self.sby.get())+" LIKE '%"+(self.sval.get())+"%'"
            
            cur.execute(str1)
            rows=cur.fetchall()
            if len(rows)!=0:
                self.custdet_tab.delete(*self.custdet_tab.get_children())
                for i in rows:
                    self.custdet_tab.insert("",END,values=i)
                conn.commit()
            else:
                messagebox.showerror("Error","Record Not Found",parent=self.root)
            conn.close()
        except Exception as es:
            messagebox.showwarning("Warning",f"User not Found:{str(es)}",parent=self.root)

        
if __name__=="__main__":
    root=Tk()
    obj=Customer(root)
    root.mainloop()
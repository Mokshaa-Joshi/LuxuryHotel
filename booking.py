from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector
import random
from datetime import date as date_n
from PIL import Image,ImageTk 
class Booking:
    def __init__(self,r):
        self.root=r
        self.root.title("Booking Details")
        self.root.geometry("1375x515+0+140")
        self.custref=StringVar()
        self.custname=StringVar()
        self.gender=StringVar()
        self.postcode=StringVar()
        self.contact=StringVar()
        self.email=StringVar()
        self.roomtype=StringVar()
        self.roomno=StringVar()
        self.checkin=StringVar()
        self.checkout=StringVar()
        self.meal=StringVar()
        self.paidtax=IntVar()
        self.subtotal=IntVar()
        self.total=IntVar()
        self.ndays=IntVar()
        self.bookingid=IntVar()
        img1=Image.open(r"C:\Users\admin\Desktop\hotel\images\room.jpg")
        img1=img1.resize((350,250),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=950,y=60,width=350,height=190)
        lbl_title=Label(self.root,text="Room Booking",font=("georgia",25),padx=30,fg="lightblue",pady=10,background="white")
        lbl_title.place(x=0,y=0,height=50,width=1350)
        right=LabelFrame(self.root,text="Customer Details",font=("georgia",15),padx=10)
        right.place(x=490,y=50,width=400,height=200)
        cust_name=Label(right,text="Customer Name:",font=("georgia",12),padx=2,pady=6)
        cust_name.grid(row=0,column=0,sticky=W)
        cust_name1=Entry(right,textvariable=self.custname,font=("georgia",12),state="readonly")
        cust_name1.grid(row=0,column=1,sticky=W)
        cust_gender=Label(right,text="Gender:",font=("georgia",12),padx=2,pady=6)
        cust_gender.grid(row=1,column=0,sticky=W)
        cust_gender1=Entry(right,textvariable=self.gender,font=("georgia",12),state="readonly")
        cust_gender1.grid(row=1,column=1,sticky=W)
        cust_post=Label(right,text="Postcode:",font=("georgia",12),padx=2,pady=6)
        cust_post.grid(row=2,column=0,sticky=W)
        cust_post1=Entry(right,textvariable=self.postcode,font=("georgia",12),state="readonly")
        cust_post1.grid(row=2,column=1,sticky=W)
        cust_contact=Label(right,text="Contact No.:",font=("georgia",12),padx=2,pady=6)
        cust_contact.grid(row=3,column=0,sticky=W)
        cust_contact1=Entry(right,textvariable=self.contact,font=("georgia",12),state="readonly")
        cust_contact1.grid(row=3,column=1,sticky=W)
        cust_email=Label(right,text="Email:",font=("georgia",12),padx=2,pady=6)
        cust_email.grid(row=4,column=0,sticky=W)
        cust_email1=Entry(right,textvariable=self.email,font=("georgia",12),state="readonly")
        cust_email1.grid(row=4,column=1,sticky=W)
        left=LabelFrame(self.root,text="Room Details",font=("georgia",15),padx=10)
        left.place(x=5,y=50,width=480 ,height=505)
        cust_ref=Label(left,text="Customer Reference Number",font=("georgia",12),padx=2,pady=6)
        cust_ref.grid(row=0,column=0,sticky=W)

        input_custref=Entry(left,width=10,textvariable=self.custref,font=("georgia",12))
        input_custref.grid(row=0,column=1,sticky=W)
        fetch_data=Button(left,command=self.fetch_cust_data,text="Fetch Details",font=("georgia",9),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        fetch_data.grid(row=0,column=1,sticky=E)
        checkin=Label(left,text="Check in date:",font=("georgia",12),padx=2,pady=6)
        checkin.grid(row=1,column=0,sticky=W)

        input_check_in=Entry(left,textvariable=self.checkin,width=22,font=("georgia",12))
        input_check_in.grid(row=1,column=1)

        check_out =Label(left,text="Checkout:",font=("georgia",12),padx=2,pady=6)
        check_out.grid(row=2,column=0,sticky=W)

        input_check_out=Entry(left,textvariable=self.checkout,width=22,font=("georgia",12))
        input_check_out.grid(row=2,column=1)

        conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
        cur=conn.cursor(buffered=True)
        cur.execute("select distinct room_type from room")
        rows=cur.fetchall()
        roomtype=Label(left,text="Room Type:",font=("georgia",12),padx=2,pady=6)
        roomtype.grid(row=4,column=0,sticky=W)
        roomtype=ttk.Combobox(left,textvariable=self.roomtype,font=("georgia",12),width=8,state="readonly")
        roomtype["value"]=rows
        roomtype.current(0)
        roomtype.grid(row=4,column=1,sticky=W)
        check_ava=Button(left,command=self.check_available,text="Available rooms",font=("georgia",9),width=11,fg="lavender",bg="grey",bd=0,pady=5)
        check_ava.grid(row=4,column=1,sticky=E)
        
        ava=Label(left,text="Available Room:",font=("georgia",12),padx=2,pady=6)
        ava.grid(row=5,column=0,sticky=W)
        
        self.input_ava=ttk.Combobox(left,textvariable=self.roomno,width=10,font=("georgia",12))
        

        lbl_meal=Label(left,text="Meal:",font=("georgia",12),padx=2,pady=6)
        lbl_meal.grid(row=6,column=0,sticky=W)

        input_meal=ttk.Combobox(left,textvariable=self.meal,width=20,font=("georgia",12))
        input_meal["value"]=("Breakfast","Lunch","Dinner","Lunch and Dinner","Breakfast and Dinner","Breakfast,Lunch,Dinner")
        input_meal.current(0)
        input_meal.grid(row=6,column=1)

        ptax=Label(left,text="Paid Tax:",font=("georgia",12),padx=2,pady=6)
        ptax.grid(row=7,column=0,sticky=W)

        input_ptax=Entry(left,width=22,textvariable=self.paidtax,font=("georgia",12),state="readonly")
        input_ptax.grid(row=7,column=1)


        stot=Label(left,text="Sub Total:",font=("georgia",12),padx=2,pady=6)
        stot.grid(row=8,column=0,sticky=W)

        input_stot=Entry(left,width=22,textvariable=self.subtotal,font=("georgia",12),state="readonly")
        input_stot.grid(row=8,column=1)

        tot=Label(left,text="Total Cost:",font=("georgia",12),padx=2,pady=6)
        tot.grid(row=9,column=0,sticky=W)

        input_tot=Entry(left,width=22,textvariable=self.total,font=("georgia",12),state="readonly")
        input_tot.grid(row=9,column=1)

        
        fr=Frame(left)
        fr.place(x=0,y=300,width=400,height=150)
        billgen=Button(fr,text="Generate Bill",command=self.gen_bill, font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        billgen.grid(row=0,column=0,pady=20)
        add=Button(fr,text="Add Booking",command=self.add_booking,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        add.grid(row=1 ,column=0)


        delete=Button(fr,text="Delete Booking",command=self.delete_book,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        delete.grid(row=1 ,column=1,padx=5)

        reset=Button(fr,text="Reset",command=self.reset_values,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        reset.grid(row=1 ,column=2)
        tab_fra=LabelFrame(self.root,text="Room Details",font=("georgia",15),padx=5)
        tab_fra.place(x=490,y=255,width=830,height=305)
        table_details=Frame(tab_fra,bd=2,relief=RIDGE)
        table_details.place(x=0,y=0,height=290,width=810)


        xscroll=ttk.Scrollbar(table_details,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_details,orient=VERTICAL)

        self.bookdet_tab=ttk.Treeview(table_details,column=("idbooking","ref_cust","check_in","check_out","room_no","meal","no_of_days"),xscrollcommand=xscroll,yscrollcommand=yscroll)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.bookdet_tab.xview)
        yscroll.config(command=self.bookdet_tab.yview)

        self.bookdet_tab.heading("idbooking",text="Booking ID")
        self.bookdet_tab.heading("ref_cust",text="Customer Reference")
        self.bookdet_tab.heading("check_in",text="Check In")
        self.bookdet_tab.heading("check_out",text="Check out")
        self.bookdet_tab.heading("room_no",text="Room No")
        self.bookdet_tab.heading("meal",text="Meal")
        self.bookdet_tab.heading("no_of_days",text="No of days")     
        self.bookdet_tab["show"]="headings"
        self.bookdet_tab.pack(fill=BOTH,expand=1)
        self.get_data()
        self.bookdet_tab.bind("<ButtonRelease-1>",self.get_cur)
    def gen_bill(self):
        if self.custref.get()==""or self.meal.get()=="" or self.checkin.get()=="" or self.checkout.get()=="" or self.roomno.get()=="" or self.roomtype.get()=="":
            messagebox.showerror("Error","All fields are needed",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
            cur=conn.cursor(buffered=True)
            cur.execute("select price from room where room_no=%s",(self.roomno.get(),))
            pr=cur.fetchone()
            
            c_in=str(self.checkin.get()).split("-")
            c_out=str(self.checkout.get()).split("-")
            x=date_n(int(c_out[0]),int(c_out[1]),int(c_out[2]))-date_n(int(c_in[0]),int(c_in[1]),int(c_in[2]))
            self.ndays=x.days
            print(self.ndays)
            t=self.ndays*int(pr[0])
            paid_tax=int(t)*5/100
            self.paidtax.set(paid_tax)
            mealtype=self.meal.get()
            if mealtype=="Breakfast":
                self.subtotal.set(t+200)
            elif mealtype=="Lunch":
                self.subtotal.set(t+300)
            elif mealtype=="Dinner":
                self.subtotal.set(t+400)
            elif mealtype=="Lunch and Dinner":
                self.subtotal.set(t+600)
            elif mealtype=="Breakfast and Dinner":
                self.subtotal.set(t+500)
            elif mealtype=="Breakfast,Lunch,Dinner":
                self.subtotal.set(t+800)
            self.total.set(paid_tax+(self.subtotal.get()))
            conn.commit()
            conn.close()
    def get_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
        cur=conn.cursor(buffered=True)
        cur.execute("select * from booking")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.bookdet_tab.delete(*self.bookdet_tab.get_children())
            for i in rows:
                self.bookdet_tab.insert("",END,values=i)
            conn.commit()
        else:
            self.bookdet_tab.delete(*self.bookdet_tab.get_children())
        conn.close()
    def add_booking(self):
        if self.custref.get()==""or self.meal.get()=="" or self.checkin.get()=="" or self.checkout.get()=="" or self.roomno.get()=="" or self.roomtype.get()=="":
            messagebox.showerror("Error","All fields are needed",parent=self.root)
        else:   
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
                cur=conn.cursor(buffered=True)
                cur.execute("insert into booking(ref_cust,check_in,check_out,room_no,meal) values(%s,%s,%s,%s,%s)",(self.custref.get(),self.checkin.get(),self.checkout.get(),self.roomno.get(),self.meal.get()))
                cur.execute("update booking set no_of_days=datediff(check_out,check_in)")
                cur.execute("select idbooking from booking where room_no=%s",(self.roomno.get(),))
                id=cur.fetchone()
                a=random.randint(1000,9999)
                cur.execute("insert into invoice values(%s,%s,%s,%s,%s,%s)",(str(a),str(self.subtotal.get()),str(self.paidtax.get()),str(self.total.get()),self.custref.get(),id[0]))
                conn.commit()
                self.get_data()
                conn.close()
                messagebox.showinfo("Success","Accepted Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Booking not added:{str(es)}",parent=self.root)

    def check_available(self):
        if self.roomtype!="":
            conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
            cur=conn.cursor(buffered=True)
            cur.execute("select room_no from room where room_type like '%"+str(self.roomtype.get())+"%' and room_no not in (select room_no from booking where check_out between %s and %s)",(self.checkin.get(),self.checkout.get()))
            room=cur.fetchall()
            self.input_ava["value"]=room
            if(len(room)!=0):
                self.input_ava.current(0)
            else:
                self.input_ava["value"]=("",)
                self.input_ava.current(0)
            self.input_ava.grid(row=5,column=1)
            conn.commit()
            conn.close()
    def get_cur(self,event=""):
        cur_row=self.bookdet_tab.focus()
        content=self.bookdet_tab.item(cur_row)
        row=content["values"]
        self.bookingid.set(row[0]),
        self.custref.set(row[1]),
        self.checkin.set(row[2]),
        self.checkout.set(row[3]),
        self.roomno.set(row[4]),
        self.meal.set(row[5]),
        conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
        cur=conn.cursor(buffered=True)
        cur.execute("select room_type from room where room_no="+str(self.roomno.get()))
        l=cur.fetchone()
        self.roomtype.set(l)
    def fetch_cust_data(self):
        
        conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
        cur=conn.cursor(buffered=True)
        cur.execute("select * from customer where Ref="+str(self.custref.get()))
        rows=cur.fetchall()
        if len(rows)!=0:
            row=rows[0]
            self.custname.set(row[1]),
            self.gender.set(row[8]),
            self.postcode.set(row[3]),
            self.contact.set(row[4]),
            self.email.set(row[5]),
            print(rows)
            conn.commit()
        else:
            messagebox.showerror("Error","No Record Found",parent=self.root)
        conn.close()
    def reset_values(self):
        self.custref.set(""),
        self.checkin.set(""),
        self.checkout.set(""),
       
    def delete_book(self):
        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
            cur=conn.cursor(buffered=True)
            cur.execute("delete from invoice where booking_no=%s",(str(self.bookingid.get()),))
            cur.execute("delete from booking where idbooking=%s",(str(self.bookingid.get()),))
            conn.commit()
            self.get_data()
            conn.close()
            messagebox.showinfo("Success","Deleted Successfully",parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning",f"User not Deleted:{str(es)}",parent=self.root)
if __name__=="__main__":
    root=Tk()
    obj=Booking(root)
    root.mainloop()
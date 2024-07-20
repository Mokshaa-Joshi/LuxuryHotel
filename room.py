from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector
import random
from PIL import Image,ImageTk 
class Room:
    def __init__(self,r):
        self.root=r
        self.root.title("Room Details")
        self.root.geometry("1350x515+0+140")
        self.roomno=StringVar()
        self.roomtype=StringVar()
        self.rprice=StringVar()
        lbl_title=Label(self.root,text="Room Details",font=("georgia",25),padx=30,fg="lightblue",pady=10,background="white")
        lbl_title.place(x=0,y=0,height=50,width=1350)

        left=LabelFrame(self.root,text="Room Details",font=("georgia",15),padx=10)
        left.place(x=5,y=50,width=450 ,height=505)
        cust_refer=Label(left,text="Room Number",font=("georgia",12),padx=2,pady=6)
        cust_refer.grid(row=0,column=0,sticky=W)

        input_ref=Entry(left,width=22,textvariable=self.roomno,font=("georgia",12))
        input_ref.grid(row=0,column=1)

        cust_name=Label(left,text="Price:",font=("georgia",12),padx=2,pady=6)
        cust_name.grid(row=1,column=0,sticky=W)

        input_name=Entry(left,width=22,textvariable=self.rprice,font=("georgia",12))
        input_name.grid(row=1,column=1)
        cust_gen=Label(left,text="Type:",font=("georgia",12),padx=2,pady=6)
        cust_gen.grid(row=2,column=0,sticky=W)
        combo_gen=ttk.Combobox(left,textvariable=self.roomtype,font=("georgia",12),width=20,state="readonly")
        combo_gen["value"]=("Single","Double","Deluxe","Luxury","Apartment")
        combo_gen.current(0)
        combo_gen.grid(row=2,column=1)
         
        fr=Frame(left)
        fr.place(x=0,y=400,width=400,height=30)
        add=Button(fr,text="Add Room",command=self.add_info,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        add.grid(row=0 ,column=0)

        update=Button(fr,text="Update",command=self.update_info,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        update.grid(row=0 ,column=1,padx=5)

        delete=Button(fr,text="Delete Room",command=self.delete_room,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        delete.grid(row=0 ,column=2)

        reset=Button(fr,text="Reset",command=self.reset_values,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        reset.grid(row=0 ,column=3,padx=5)
        tab_fra=LabelFrame(self.root,text="Room Details",font=("georgia",15),padx=5)
        tab_fra.place(x=490,y=50,width=830,height=305)
        table_details=Frame(tab_fra,bd=2,relief=RIDGE)
        table_details.place(x=0,y=0,height=290,width=810)
        xscroll=ttk.Scrollbar(table_details,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_details,orient=VERTICAL)

        self.roomdet_tab=ttk.Treeview(table_details,column=("Room_no","room_type","price"),xscrollcommand=xscroll,yscrollcommand=yscroll)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.roomdet_tab.xview)
        yscroll.config(command=self.roomdet_tab.yview)

        self.roomdet_tab.heading("Room_no",text="Room No")
        self.roomdet_tab.heading("room_type",text="Room Type")
        self.roomdet_tab.heading("price",text="Price")    
        self.roomdet_tab["show"]="headings"
        self.roomdet_tab.pack(fill=BOTH,expand=1)
        self.roomdet_tab.bind("<ButtonRelease-1>",self.get_cur)
        self.get_data()
    def get_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
        cur=conn.cursor()
        cur.execute("select * from room")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.roomdet_tab.delete(*self.roomdet_tab.get_children())
            for i in rows:
                self.roomdet_tab.insert("",END,values=i)
        
            conn.commit()
        else:
            self.roomdet_tab.delete(*self.roomdet_tab.get_children())
        conn.close()
    def reset_values(self):
        self.roomno.set(""),
        self.roomtype.set(""),
        self.rprice.set(""),
    def get_cur(self,event=""):
        cur_row=self.roomdet_tab.focus()
        content=self.roomdet_tab.item(cur_row)
        row=content["values"]
        self.roomno.set(row[0]),
        self.roomtype.set(row[1]),
        self.rprice.set(row[2])
    def add_info(self):
        if self.roomno.get()==""or self.roomtype.get()=="" or self.rprice.get()=="" :
            messagebox.showerror("Error","All fields are needed",parent=self.root)
        else:   
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
                cur=conn.cursor()
                cur.execute("insert into room values(%s,%s,%s)",(self.roomno.get(),self.roomtype.get(),self.rprice.get()))
                conn.commit()
                self.get_data()
                conn.close()
                messagebox.showinfo("Success","Accepted Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Room not added:{str(es)}",parent=self.root)
    def delete_room(self):
        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
            cur=conn.cursor()
            cur.execute("delete from room where room_no=%s",(self.roomno.get(),))
            conn.commit()
            self.get_data()
            conn.close()
            messagebox.showinfo("Success","Deleted Successfully",parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning",f"User not Deleted:{str(es)}",parent=self.root)

    
    def update_info(self):
        if self.roomno.get()==""or self.roomtype.get()=="" or self.rprice.get()=="":
            messagebox.showerror("Error","All fields are needed",parent=self.root)
        else:   
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
                cur=conn.cursor()
                cur.execute("update room set  room_type=%s, price=%s where room_no=%s",(self.roomtype.get(),self.rprice.get(),self.roomno.get()))
                conn.commit()
                self.get_data()
                conn.close()
                messagebox.showinfo("Success","Updated Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"User not Updated:{str(es)}",parent=self.root)
if __name__=="__main__":
    root=Tk()
    obj=Room(root)
    root.mainloop()
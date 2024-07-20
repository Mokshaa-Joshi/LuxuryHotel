from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector
import random

class Invoice:
    def __init__(self,r):
        self.root=r
        self.root.title("Invoice Details")
        self.root.geometry("1350x515+0+140")
        lbl_title=Label(self.root,text="Invoice Details",font=("georgia",25),padx=30,fg="lightblue",pady=10,background="white")
        lbl_title.place(x=0,y=0,height=50,width=1350)
        tab_fra=LabelFrame(self.root,text="Search Details",font=("georgia",15),padx=5)
        tab_fra.place(x=0,y=50,width=1330,height=505)

        self.sval=StringVar()
        self.sby=StringVar()
        


        searchbar=Label(tab_fra,text="Search By:",font=("georgia",12),padx=2,pady=1,fg="lavender",bg="grey")
        searchbar.grid(row=0,column=0,sticky=W)
        combo_search=ttk.Combobox(tab_fra,textvariable=self.sby,font=("georgia",12),width=20,state="readonly")
        combo_search["value"]=("idinvoice","cust_ref","booking_no")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=5)
        
        searchby=Entry(tab_fra,width=22,textvariable=self.sval,font=("georgia",12))
        searchby.grid(row=0,column=2)

        search=Button(tab_fra,text="Search",command=self.search,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        search.grid(row=0 ,column=3,padx=5)

        showall=Button(tab_fra,text="Show All",command=self.get_data,font=("georgia",10),fg="lavender",bg="grey",bd=0,padx=5,pady=5)
        showall.grid(row=0 ,column=4,padx=5)

        table_details=Frame(tab_fra,bd=2,relief=RIDGE)
        table_details.place(x=0,y=50,height=500,width=1250)


        xscroll=ttk.Scrollbar(table_details,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_details,orient=VERTICAL)

        self.invoicedet_tab=ttk.Treeview(table_details,column=("Invoice_id","Subtotal","Tax","Total_Cost","Cust_ref","Booking_no"),xscrollcommand=xscroll,yscrollcommand=yscroll)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.invoicedet_tab.xview)
        yscroll.config(command=self.invoicedet_tab.yview)


        self.invoicedet_tab.heading("Invoice_id",text="Invoice_id")
        self.invoicedet_tab.heading("Subtotal",text="Subtotal")
        self.invoicedet_tab.heading("Tax",text="Tax")
        self.invoicedet_tab.heading("Total_Cost",text="Total_Cost ")
        self.invoicedet_tab.heading("Cust_ref",text="Cust_ref")
        self.invoicedet_tab.heading("Booking_no",text="Booking_no")
           

        self.invoicedet_tab["show"]="headings"
        self.invoicedet_tab.column("Invoice_id",width=100)
        self.invoicedet_tab.column("Subtotal",width=100)
        self.invoicedet_tab.column("Tax",width=100)
        self.invoicedet_tab.column("Total_Cost",width=100)
        self.invoicedet_tab.column("Cust_ref",width=100)
        self.invoicedet_tab.column("Booking_no",width=100)
           

        self.invoicedet_tab.pack(fill=BOTH,expand=1)
        #self.invoicedet_tab.bind("<ButtonRelease-1>",self.get_cur)
        self.get_data()

    def get_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
        cur=conn.cursor()
        cur.execute("select * from invoice")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.invoicedet_tab.delete(*self.invoicedet_tab.get_children())
            for i in rows:
                self.invoicedet_tab.insert("",END,values=i)
        else:
            self.invoicedet_tab.delete(*self.invoicedet_tab.get_children())
        
        conn.commit()
        conn.close()
    def search(self):
        try:
            
            conn=mysql.connector.connect(host="localhost",user="root",password="Unnati@2003",database="hotel_management_system",auth_plugin='mysql_native_password')
            cur=conn.cursor()
            str1="select * from invoice where "+str(self.sby.get())+" LIKE '%"+(self.sval.get())+"%'"
            
            cur.execute(str1)
            rows=cur.fetchall()
            if len(rows)!=0:
                self.invoicedet_tab.delete(*self.invoicedet_tab.get_children())
                for i in rows:
                    self.invoicedet_tab.insert("",END,values=i)
                conn.commit()
            else:
                messagebox.showerror("Error","Record Not Found",parent=self.root)
            conn.close()
        except Exception as es:
            messagebox.showwarning("Warning",f"User not Found:{str(es)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=Invoice(root)
    root.mainloop()



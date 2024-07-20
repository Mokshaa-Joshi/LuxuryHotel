from tkinter import *
from PIL import Image,ImageTk 
from cust import Customer
from booking import Booking
from room import Room
from employee import Employee
from invoice import Invoice
class HotelManagementSystem:

    def __init__(self,r):
        self.root=r
        self.root.title("Hotel Management System")
        self.root.geometry("1920x1080+0+0")
        

        lbl_title=Label(self.root,text="Eden Resorts",font=("georgia",50),fg="lightblue",background="black")
        lbl_title.place(x=0,y=0,height=80,width=1300)

        main_frame=Frame(self.root)
        main_frame.place(x=0,y=100,width=1920,height=830)

        main_background=Image.open(r"C:\Users\admin\Desktop\hotel\images\main1.jpg")
        main_background=main_background.resize((1550,790),Image.ANTIALIAS)
        self.main_back=ImageTk.PhotoImage(main_background)
        lbl_main_back=Label(main_frame,image=self.main_back)
        lbl_main_back.place(x=0,y=0,width=1550,height=790)



        btn=Frame(self.root,bg='lavender')
        btn.place(x=0,y=80,width=1500,height=40) 
        cust=Button(btn,text="Customer Details",command=self.customer_details,font=("georgia",15) ,width=15,padx=16 ,bd=0,pady=5,bg="lavender",fg="grey")
        cust.grid(row=0,column=0)

        booking=Button(btn,text="Booking Details",command=self.booking_details,font=("georgia",15) ,width=15,padx=22.5 ,bd=0,pady=5,bg="lavender",fg="grey")
        booking.grid(row=0,column=1)

        invoice=Button(btn,text="Invoice",command=self.invoice_det,font=("georgia",15) ,width=15,padx=62.5 ,bd=0,pady=5,bg="lavender",fg="grey")
        invoice.grid(row=0,column=2)

        room=Button(btn,text="Room Details",font=("georgia",15),command=self.room_details,width=15 ,padx=32.5,pady=5 ,bd=0,bg="lavender",fg="grey")
        room.grid(row=0,column=3)

        emp=Button(btn,text="Employee Details",font=("georgia",15),command=self.emp_det,width=15 ,padx=20.5,pady=5 ,bd=0,bg="lavender",fg="grey")
        emp.grid(row=0,column=4)

    def emp_det(self):
        self.new_window=Toplevel(self.root)
        self.app=Employee(self.new_window) 

    def customer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Customer(self.new_window)
    def booking_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Booking(self.new_window)
    def room_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Room(self.new_window)
    def invoice_det(self):
        self.new_window=Toplevel(self.root)
        self.app=Invoice(self.new_window)
if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

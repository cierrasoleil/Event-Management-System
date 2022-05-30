from random import randint
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector
import random
from tkinter import messagebox

class EventBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Booking Tab")
        self.root.geometry("1130x480+225+220")

        #VARIABLES
        self.var_contact=StringVar()
        self.var_datebooked=StringVar()
        self.var_edate=StringVar()
        self.var_etype=StringVar()
        self.var_seats=StringVar()
        self.var_meal=StringVar()

        #TITLE
        lbl_title=Label(self.root, text="BOOK AN EVENT ", font=("times new roman", 18, "bold"), bg="hot pink",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #LOGO
        img2=Image.open(r"C:\Users\user\Desktop\python\AOOP VERY FINAL\IMAGES\LOGO.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=90,height=50)

        img3=Image.open(r"C:\Users\user\Desktop\python\AOOP VERY FINAL\IMAGES\LOGO.png")
        img3=img3.resize((500,175),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=740,y=55,width=370,height=190)

        #LABEL FRAME
        labelframeleft=LabelFrame(self.root, text="Event Booking Details", font=("times new roman", 13, "bold"),bd=2,relief=RIDGE, padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #LABELS AND ENTRY
        #CUST CELL
        lbl_cust_contact=Label(labelframeleft, text = "Customer's Cell No.",font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact=ttk.Entry(labelframeleft, width=20,textvariable=self.var_contact , font=("times new roman", 12))
        enty_contact.grid(row=0, column=1,sticky=W)

        #FETCH DATA BTN
        btnfetch=Button(labelframeleft,command=self.Fetch_contact ,text="Collect Data",font = ("times new roman", 11, "bold"), bg="hot pink",fg="white", width =10)
        btnfetch.place(x=310, y = 1)

        #DATE BOOKED
        DBooked=Label(labelframeleft, text = "Date Booked", font=("times new roman", 12, "bold"), padx=2, pady=6)
        DBooked.grid(row=1, column=0, sticky=W)

        txtDBooked=ttk.Entry(labelframeleft, width=29,textvariable=self.var_datebooked ,font=("times new roman", 12))
        txtDBooked.grid(row=1, column=1)

        #EVENT DATE
        EBooked=Label(labelframeleft, text = "Event Date", font=("times new roman", 12, "bold"), padx=2, pady=6)
        EBooked.grid(row=2, column=0, sticky=W)

        txtEBooked=ttk.Entry(labelframeleft, width=29,textvariable=self.var_edate ,font=("times new roman", 12))
        txtEBooked.grid(row=2, column=1)

        #EVENT TYPE
        etype=Label(labelframeleft, text = "Event Type", font=("times new roman", 12, "bold"), padx=2, pady=6)
        etype.grid(row=3, column=0, sticky=W)

        combo_etype=ttk.Combobox(labelframeleft, width=27,textvariable=self.var_etype ,font=("times new roman", 12))
        combo_etype["value"]=("","Birthday","Anniversary", "Wedding", "Showers", "Holiday", "Party", "Others")
        combo_etype.current(0)
        combo_etype.grid(row=3, column=1)

        #BOOKED SEAT
        SBooked=Label(labelframeleft, text = "Seats Booked", font=("times new roman", 12, "bold"), padx=2, pady=6)
        SBooked.grid(row=4, column=0, sticky=W)

        txtSBooked=ttk.Entry(labelframeleft, width=29,textvariable=self.var_seats ,font=("times new roman", 12))
        txtSBooked.grid(row=4, column=1)

        #MEAL PAX
        meal=Label(labelframeleft, text = "Set Meal Pax", font=("times new roman", 12, "bold"), padx=2, pady=6)
        meal.grid(row=5, column=0, sticky=W)

        txtmeal=ttk.Entry(labelframeleft, width=29,textvariable=self.var_meal ,font=("times new roman", 12))
        txtmeal.grid(row=5, column=1)

        #BUTTONS
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=350, width=410, height=45)

        btnadd=Button(btn_frame, text="Add",command=self.add_data,font = ("Lora", 11, "bold"), bg="hot pink",fg="white", width =10)
        btnadd.grid(row=0, column=0, padx=1)

        btnud=Button(btn_frame, text="Update",command=self.update,font = ("Lora", 11, "bold"), bg="hot pink",fg="white", width =10)
        btnud.grid(row=0, column=1, padx=1)

        btndel=Button(btn_frame, text="Delete",command=self.cdelete,font = ("Lora", 11, "bold"), bg="hot pink",fg="white", width =10)
        btndel.grid(row=0, column=2, padx=1)

        btnres=Button(btn_frame, text="Reset",command=self.reset,font = ("Lora", 11, "bold"), bg="hot pink",fg="white", width =10)
        btnres.grid(row=0, column=3, padx=1)

        #SHOW TABLE
        TABLE_F=LabelFrame(self.root, text="Event Details", font=("times new roman", 12, "bold"),bd=2,relief=RIDGE, padx=2)
        TABLE_F.place(x=435,y=250,width=700,height=300)

        deets_table=Frame(TABLE_F, bd=2, relief=RIDGE)
        deets_table.place(x=0, y=2, width=680, height=200)

        scroll_x=ttk.Scrollbar(deets_table, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(deets_table, orient=VERTICAL)

        self.book_table=ttk.Treeview(deets_table, column=("Contact", "DB", "ED", "ET", "SB", "MP"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill = Y)

        scroll_x.config(command=self.book_table.xview)
        scroll_y.config(command=self.book_table.yview)

        self.book_table.heading("Contact", text="Cell No.")
        self.book_table.heading("DB", text="Date Booked")
        self.book_table.heading("ED", text="Event Date")
        self.book_table.heading("ET", text="Event Type")
        self.book_table.heading("SB", text="Seats Booked")
        self.book_table.heading("MP", text="Set Meal")
        
        self.book_table["show"]="headings"

        self.book_table.column("Contact", width=100)
        self.book_table.column("DB", width=100)
        self.book_table.column("ED", width=100)
        self.book_table.column("ET", width=100)
        self.book_table.column("SB", width=100)
        self.book_table.column("MP", width=100)
    

        self.book_table.pack(fill=BOTH, expand =1)
        self.book_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get()==""or self.var_datebooked.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert Into Book Values(%s, %s, %s, %s, %s, %s)",(
                                                                                    self.var_contact.get(),
                                                                                    self.var_datebooked.get(),
                                                                                    self.var_edate.get(),
                                                                                    self.var_etype.get(),
                                                                                    self.var_seats.get(),
                                                                                    self.var_meal.get()
                                                                                   ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Event Booked Sucesfully.", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", "Something went wrong: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row= self.book_table.focus()
        content=self.book_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_datebooked.set(row[1])
        self.var_edate.set(row[2])
        self.var_etype.set(row[3])
        self.var_seats.set(row[4])
        self.var_meal.set(row[5])

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error", "Please enter valid mobile number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
            my_cursor=conn.cursor()
            my_cursor.execute("update book set DB=%s, ED=%s, ET=%s, SB=%s, MP=%s where contact=%s",( 
                                                                                    self.var_datebooked.get(),
                                                                                    self.var_edate.get(),
                                                                                    self.var_etype.get(),
                                                                                    self.var_seats.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_contact.get()
                                                                                 ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Event Details has been updated", parent=self.root)

    def cdelete(self):
        cdelete=messagebox.askyesno("Event Management System", "Do you want to delete this information?", parent=self.root)
        if cdelete>0:
            conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
            my_cursor=conn.cursor()
            query="Delete from book where contact= %s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)

        else:
            if not cdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
                    
    def reset(self):
        self.var_contact.set("")
        self.var_datebooked.set("")
        self.var_edate.set("")
        self.var_etype.set("")
        self.var_seats.set("")
        self.var_meal.set("")


        #FETCH DATA
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from book")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                
            self.book_table.delete(*self.book_table.get_children())
            for i in rows:
                self.book_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    #INFOS IN COLLECTING DATA
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error!", "Please Enter Valid Contact Number.", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
            my_cursor=conn.cursor()
            query=("Select Name from customer where Mobile = %s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error!", "Number not found.", parent=self.root)
            else:
                conn.commit()
                conn.close()

                #NAME
                showDataFrame=Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=440, y=55, width= 300, height=190)
                lblName= Label(showDataFrame, text="Name:", font=("lora", 11, "bold"))
                lblName.place(x=0, y=0)
                lbl=Label (showDataFrame, text="\n".join(row), font=("lora", 11))
                lbl.place(x=70, y=0)

                #GENDER
                conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
                my_cursor=conn.cursor()
                query=("Select Sex from customer where Mobile = %s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblSex= Label(showDataFrame, text="Sex:", font=("lora", 11, "bold"))
                lblSex.place(x=0, y=30)
                lbl=Label (showDataFrame, text="\n".join(row), font=("lora", 11))
                lbl.place(x=70, y=30)

                #EMAIL
                conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
                my_cursor=conn.cursor()
                query=("Select Email from customer where Mobile = %s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblemail= Label(showDataFrame, text="Email:", font=("lora", 11, "bold"))
                lblemail.place(x=0, y=60)
                lbl=Label (showDataFrame, text="\n".join(row), font=("lora", 11))
                lbl.place(x=70, y=60)

                #NATIONALITY
                conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
                my_cursor=conn.cursor()
                query=("Select Nationality from customer where Mobile = %s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblntl= Label(showDataFrame, text="Nationality:", font=("lora", 11, "bold"))
                lblntl.place(x=0, y=90)
                lbl=Label (showDataFrame, text="\n".join(row), font=("lora", 11))
                lbl.place(x=100, y=90)

                #ADDRESS
                conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
                my_cursor=conn.cursor()
                query=("Select Address from customer where Mobile = %s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lbladdr= Label(showDataFrame, text="Address:", font=("lora", 11, "bold"))
                lbladdr.place(x=0, y=120)
                lbl=Label (showDataFrame, text="\n".join(row), font=("lora", 11))
                lbl.place(x=70, y=120)

                #ZIP
                conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
                my_cursor=conn.cursor()
                query=("Select ZIP from customer where Mobile = %s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblzip= Label(showDataFrame, text="ZIP Code:", font=("lora", 11, "bold"))
                lblzip.place(x=0, y=150)
                lbl=Label (showDataFrame, text="\n".join(row), font=("lora", 11))
                lbl.place(x=70, y=150)

    def total(self):
        inDate=self.var_datebooked.get()
        outDate=self.var_edate.get()
        inDate=datetime.strftime(inDate, "%d/%m/%Y")
        outDate=datetime.strftime(outDate, "%d/%m/%Y")
        self.var_

if __name__ == "__main__":
    root = Tk()
    obj = EventBooking(root)
    root.mainloop()
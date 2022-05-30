from random import randint
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Tab")
        self.root.geometry("1130x480+225+220")

        #VARIABLE
        self.var_ref=StringVar()
        x=random.randint(0, 999)
        self.var_ref.set(str(x))

        self.var_name=StringVar()
        self.var_sex=StringVar()
        self.var_ntnl=StringVar()
        self.var_email=StringVar()
        self.var_mobile=StringVar()
        self.var_add=StringVar()
        self.var_zip=StringVar()

        #TITLE
        lbl_title=Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="hot pink",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #LOGO
        img2=Image.open(r"C:\Users\user\Desktop\python\AOOP VERY FINAL\IMAGES\LOGO.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=90,height=50)

        #LABEL FRAME
        labelframeleft=LabelFrame(self.root, text="Customer Details", font=("times new roman", 12, "bold"),bd=2,relief=RIDGE, padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #LABELS AND ENTRY
        #CUST REF
        lbl_cust_ref=Label(labelframeleft, text = "Customer Reference", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref, width=29, font=("times new roman", 13), state="readonly")
        enty_ref.grid(row=0, column=1)

        #CUST NAME
        cname=Label(labelframeleft, text = "Customer Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_name, width=29, font=("times new roman", 13))
        txtcname.grid(row=1, column=1)

        #GENDER
        gender=Label(labelframeleft, text = "Sex", font=("times new roman", 12, "bold"), padx=2, pady=6)
        gender.grid(row=2, column=0, sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_sex, width=27, font=("times new roman", 13), state="readonly")
        combo_gender["value"]=("","Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=2, column=1)

        #NATIONALITY
        ntl=Label(labelframeleft, text = "Nationality", font=("times new roman", 12, "bold"), padx=2, pady=6)
        ntl.grid(row=3, column=0, sticky=W)

        combo_ntl=ttk.Combobox(labelframeleft,textvariable=self.var_ntnl, width=27, font=("times new roman", 13), state="readonly")
        combo_ntl["value"]=("","Filipino", "American", "Japanese", "South Korean", "Other")
        combo_ntl.current(0)
        combo_ntl.grid(row=3, column=1)

        #EMAIL ADDRESS
        emailadd=Label(labelframeleft, text = "Email Address", font=("times new roman", 12, "bold"), padx=2, pady=6)
        emailadd.grid(row=4, column=0, sticky=W)
        txtemailadd=ttk.Entry(labelframeleft,textvariable=self.var_email, width=29, font=("times new roman", 13))
        txtemailadd.grid(row=4, column=1)

        #MOBILE NUMBER
        mnum=Label(labelframeleft, text = "Mobile Number", font=("times new roman", 12, "bold"), padx=2, pady=6)
        mnum.grid(row=5, column=0, sticky=W)
        txtmnum=ttk.Entry(labelframeleft,textvariable=self.var_mobile, width=29, font=("times new roman", 13))
        txtmnum.grid(row=5, column=1)

        #ADDRESS
        addr=Label(labelframeleft, text = "Permanent Address", font=("times new roman", 12, "bold"), padx=2, pady=6)
        addr.grid(row=6, column=0, sticky=W)
        txtaddr=ttk.Entry(labelframeleft,textvariable=self.var_add, width=29, font=("times new roman", 13))
        txtaddr.grid(row=6, column=1)

        #ZIP CODE
        pcode=Label(labelframeleft, text = "ZIP Code", font=("times new roman", 12, "bold"), padx=2, pady=6)
        pcode.grid(row=7, column=0, sticky=W)
        txtpcode=ttk.Entry(labelframeleft,textvariable=self.var_zip, width=29, font=("times new roman", 13))
        txtpcode.grid(row=7, column=1)

        #BUTTONS
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=350, width=410, height=45)

        btnadd=Button(btn_frame, text="Add",command=self.add_data ,font = ("Lora", 11, "bold"), bg="hot pink",fg="white", width =10)
        btnadd.grid(row=0, column=0, padx=1)

        btnud=Button(btn_frame, text="Update",command=self.update ,font = ("Lora", 11, "bold"), bg="hot pink",fg="white", width =10)
        btnud.grid(row=0, column=1, padx=1)

        btndel=Button(btn_frame, text="Delete",command=self.cdelete ,font = ("Lora", 11, "bold"), bg="hot pink",fg="white", width =10)
        btndel.grid(row=0, column=2, padx=1)

        btnres=Button(btn_frame, text="Reset",command=self.reset ,font = ("Lora", 11, "bold"), bg="hot pink",fg="white", width =10)
        btnres.grid(row=0, column=3, padx=1)

        #LABEL FRAME 2 & SEARCH SYSTEM
        TABLE_F=LabelFrame(self.root, text="View Details", font=("times new roman", 12, "bold"),bd=2,relief=RIDGE, padx=2)
        TABLE_F.place(x=435,y=50,width=700,height=490)

        
        #SHOW DATA
        deets_table=Frame(TABLE_F, bd=2, relief=RIDGE)
        deets_table.place(x=0, y=10, width=680, height=400)

        scroll_x=ttk.Scrollbar(deets_table, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(deets_table, orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(deets_table, column=("Ref", "Name", "Sex", "Nationality", "Email",
                                             "Mobile", "Address", "ZIP"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill = Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Ref", text="Reference No.")
        self.Cust_Details_Table.heading("Name", text="Name")
        self.Cust_Details_Table.heading("Sex", text="Sex")
        self.Cust_Details_Table.heading("Nationality", text="Nationality")
        self.Cust_Details_Table.heading("Email", text="Email Address")
        self.Cust_Details_Table.heading("Mobile", text="Mobile Number")
        self.Cust_Details_Table.heading("Address", text="Address")
        self.Cust_Details_Table.heading("ZIP", text="ZIP Code")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("Ref", width=100)
        self.Cust_Details_Table.column("Name", width=100)
        self.Cust_Details_Table.column("Sex", width=100)
        self.Cust_Details_Table.column("Nationality", width=100)
        self.Cust_Details_Table.column("Email", width=100)
        self.Cust_Details_Table.column("Mobile", width=100)
        self.Cust_Details_Table.column("Address", width=100)
        self.Cust_Details_Table.column("ZIP", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand =1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()==""or self.var_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert Into Customer Values(%s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                    self.var_ref.get(),
                                                                                    self.var_name.get(),
                                                                                    self.var_sex.get(),
                                                                                    self.var_ntnl.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_add.get(),
                                                                                    self.var_zip.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", "Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row= self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_sex.set(row[2]),
        self.var_ntnl.set(row[3]),
        self.var_email.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_add.set(row[6]),
        self.var_zip.set(row[7])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error", "Please enter valid mobile number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s, Sex=%s, Nationality=%s, Email=%s, Mobile=%s, Address=%s, ZIP=%s where Ref=%s ",(
                                                                                                                                   
                                                                                                                                    self.var_name.get(),
                                                                                                                                    self.var_sex.get(),
                                                                                                                                    self.var_ntnl.get(),
                                                                                                                                    self.var_email.get(),
                                                                                                                                    self.var_mobile.get(),
                                                                                                                                    self.var_add.get(),
                                                                                                                                    self.var_zip.get(),
                                                                                                                                     self.var_ref.get()
                                                                                                                         ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details has been updated", parent=self.root)

    def cdelete(self):
        cdelete=messagebox.askyesno("Event Management System", "Do you want to delete this information?", parent=self.root)
        if cdelete>0:
            conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
            my_cursor=conn.cursor()
            query="Delete from Customer where Ref= %s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)

        else:
            if not cdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_ref.set(""),
        self.var_name.set(""),
        self.var_sex.set(""),
        self.var_ntnl.set(""),
        self.var_email.set(""),
        self.var_mobile.set(""),
        self.var_add.set(""),
        self.var_zip.set("")

        x=random.randint(0, 999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost", username="root", password = "zyrah", database= "management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where " +str(self.search_var.get())+" LIKE ' % " + str(self.txt_search.get())+" % ' ")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values = i)
            conn.commit()
        conn.close()



if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
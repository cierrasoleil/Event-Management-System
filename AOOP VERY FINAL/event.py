from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win
from booking import EventBooking


class EventManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management System")
        self.root.geometry("1400x685+0+0")

        #BANNER
        img1=Image.open(r"C:\Users\user\Desktop\python\AOOP VERY FINAL\IMAGES\IMAGEA.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1600,height=140)

        #LOGO
        img2=Image.open(r"C:\Users\user\Desktop\python\AOOP VERY FINAL\IMAGES\LOGO.png")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #TITLE BAR
        lbl_title=Label(self.root, text="EVENT MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="light pink",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1500,height=50)

        #FRAME
        main_frame=Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        #Menu
        lbl_menu=Label(main_frame, text="MENU", font=("lora", 35, "bold"), bg="light pink",fg="white",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #Btn
        btn_frame=Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0,  y=75, width=250, height=200)

        cust_btn=Button(btn_frame,text="CUSTOMER", command=self.cust_details, width =22, font=("times new roman", 15, "bold"), bg="light pink",fg="white",bd=0, cursor ="hand2")
        cust_btn.grid(row=0, column=0, pady=2)

        event_btn=Button(btn_frame,text="EVENTS",command=self.eventbooking ,width =22, font=("times new roman", 15, "bold"), bg="light pink",fg="white",bd=0, cursor ="hand2")
        event_btn.grid(row=1, column=0, pady=2)

        #RIGHT MAIN
        img3=Image.open(r"C:\Users\user\Desktop\python\AOOP VERY FINAL\IMAGES\IMAGEA.png")
        img3=img3.resize((1200,530),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1200,height=530)

        #LOWER LEFT
        img4=Image.open(r"C:\Users\user\Desktop\python\AOOP VERY FINAL\IMAGES\MAIN1.jpg")
        img4=img4.resize((230,180),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=160,width=230,height=180)

        img5=Image.open(r"C:\Users\user\Desktop\python\AOOP VERY FINAL\IMAGES\MAIN2.jpg")
        img5=img5.resize((230,170),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=340,width=230,height=170)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def eventbooking(self):
        self.new_window=Toplevel(self.root)
        self.app = EventBooking(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = EventManagementSystem(root)
    root.mainloop()
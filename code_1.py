from tkinter import *
from PIL import Image, ImageTk
from customer import cust_window
from room import roombooking
from details import deatilsroom

class Hotelmanagementsystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital management system")
        self.root.geometry('1550x800+0+0')
        img1 = Image.open(r"C:\Users\kanak\Downloads\hotel management\hotel1.png")
        img1 = img1.resize((1550, 140))

        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=1550, height=140)
        img2 = Image.open(r"C:\Users\kanak\Downloads\hotel management\logohotel.png")
        img2 = img2.resize((230, 140))

        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=230, height=140)
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)
        cust_bnt=Button(btn_frame,text="CUSTOMER",command=self.cust_detail,width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, relief=RIDGE,cursor="hand1")
        cust_bnt.grid(row=0,column=0,pady=1)
        
        room_bnt=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, relief=RIDGE,cursor="hand1")
        room_bnt.grid(row=1,column=0,pady=1)
        detail_bnt=Button(btn_frame,text="DETAIL",command=self.details_room,width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, relief=RIDGE,cursor="hand1")
        detail_bnt.grid(row=2,column=0,pady=1)
        report_bnt=Button(btn_frame,text="REPORT",width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, relief=RIDGE,cursor="hand1")
        report_bnt.grid(row=3,column=0,pady=1)
        logout_bnt=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, relief=RIDGE,cursor="hand1")
        logout_bnt.grid(row=4,column=0,pady=1)
        img3 = Image.open(r"C:\Users\kanak\Downloads\hotel management\slide3.jpg")
        img3 = img3.resize((1310, 590))

        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=225, y=0, width=1310, height=590)

        img4 = Image.open(r"C:\Users\kanak\Downloads\hotel management\myh.jpg")
        img4 = img4.resize((230, 210))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(r"C:\Users\kanak\Downloads\hotel management\khana.jpg")
        img5 = img5.resize((230, 150))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg5 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=420, width=230, height=190)
    def cust_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_window(self.new_window)


    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=deatilsroom(self.new_window)
        



        


        


if __name__ == "__main__":
    root = Tk()
    obj = Hotelmanagementsystem(root)
    root.mainloop()

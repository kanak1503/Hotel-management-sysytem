from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime

class roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("customer window")
        self.root.geometry('1298x550+230+220')
        #variable
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        #title

        lbl_title = Label(self.root, text="ROOM BOOKING", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)
        img1 = Image.open(r"C:\Users\kanak\Downloads\hotel management\logohotel.png")
        img1 = img1.resize((100, 40))

        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(root, image=self.photoimg1, bd=0, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=100, height=40)



        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Deatils",font=("times new roman", 10, "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("times new roman", 13, "bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        check_in_date=Label(labelframeleft,text="Check in Date",font=("times new roman", 10, "bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("times new roman", 13, "bold"))
        txtcheck_in_date.grid(row=1,column=1)

        lbl_check_out=Label(labelframeleft,text="Check out date",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)
        txt_checkout=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("times new roman", 13, "bold"))
        txt_checkout.grid(row=2,column=1)

        lbl_roomtype=Label(labelframeleft,text="Room type",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=3,column=0,sticky=W)
        conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomype from details")
        row=my_cursor.fetchall()

        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("times new roman", 10, "bold"),width=27)
        combo_roomtype["value"]=row
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)

        lblroomavailable=Label(labelframeleft,text="Available room:",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lblroomavailable.grid(row=4,column=0,sticky=W)
        #txtroomavailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("times new roman", 13, "bold"))
        #txtroomavailable.grid(row=4,column=1)
        conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomno from details")
        rows=my_cursor.fetchall()

        
        combo_avaroom=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("times new roman", 10, "bold"),width=27)

        combo_avaroom["value"]=rows
        combo_avaroom.current(0)
        combo_avaroom.grid(row=4,column=1)

        lblmeal=Label(labelframeleft,text="Meal",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lblmeal.grid(row=5,column=0,sticky=W)
        txtmeal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_meal,font=("times new roman", 13, "bold"))
        txtmeal.grid(row=5,column=1)

        lblnoofdays=Label(labelframeleft,text="No. of days",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lblnoofdays.grid(row=6,column=0,sticky=W)
        txtnoofdays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_noofdays,font=("times new roman", 13, "bold"))
        txtnoofdays.grid(row=6,column=1)

        lblnoofdays=Label(labelframeleft,text="Paid tax",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lblnoofdays.grid(row=7,column=0,sticky=W)
        txtnoofdays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_paidtax,font=("times new roman", 13, "bold"))
        txtnoofdays.grid(row=7,column=1)

        lblnoofdays=Label(labelframeleft,text="Sub total",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lblnoofdays.grid(row=8,column=0,sticky=W)
        txtnoofdays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_actualtotal,font=("times new roman", 13, "bold"))
        txtnoofdays.grid(row=8,column=1)

        lbidnumber=Label(labelframeleft,text="Total cost",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbidnumber.grid(row=9,column=0,sticky=W)
        txtidnumber=ttk.Entry(labelframeleft,width=29,textvariable=self.var_total,font=("times new roman", 13, "bold"))
        txtidnumber.grid(row=9,column=1)

        #***********fetch button**************
        btnfetch=Button(labelframeleft,text="FETCH DATA",command=self.fetch_contact,font=("times new roman", 8, "bold"),bg="black",fg="gold",width=10)
        btnfetch.place(x=330,y=2)
        btnbill=Button(labelframeleft,text="BILL",command=self.total,font=("times new roman", 8, "bold"),bg="black",fg="gold",width=10)
        btnbill.grid(row=10,column=0,sticky=W)


        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        btnadd=Button(btn_frame,text="ADD",command=self.add_data,font=("times new roman", 13, "bold"),bg="black",fg="gold",width=8)
        btnadd.grid(row=0,column=0,padx=1)
        btndelete=Button(btn_frame,text="DELETE",command=self.mdelete,font=("times new roman", 13, "bold"),bg="black",fg="gold",width=8)
        btndelete.grid(row=0,column=2,padx=1)
        btnupdate=Button(btn_frame,text="UPDATE",command=self.update,font=("times new roman", 13, "bold"),bg="black",fg="gold",width=8)
        btnupdate.grid(row=0,column=1,padx=1)
        btnreset=Button(btn_frame,text="RESET",command=self.reset,font=("times new roman", 13, "bold"),bg="black",fg="gold",width=8)
        btnreset.grid(row=0,column=3,padx=1)
        #******************right side image******************
        img3 = Image.open(r"C:\Users\kanak\Downloads\hotel management\bed.jpg")
        img3 = img3.resize((520, 200))

        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3= Label(root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg3.place(x=750, y=55, width=520, height=200)


        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details",font=("times new roman", 10, "bold"),padx=2)
        table_frame.place(x=435,y=280,width=860,height=260)
        lbl_searchby=Label(table_frame,text="Search BY",font=("times new roman", 10, "bold"),bg="red",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=3)
        self.search_var=StringVar()

        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("times new roman", 10, "bold"),width=27,state="readonly")
        combo_search["value"]=("Contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1)
        self.txt_search=StringVar()
        textsearch=ttk.Entry(table_frame,textvariable=self.txt_search,width=29,font=("times new roman", 13, "bold"))
        textsearch.grid(row=0,column=2,padx=3)
        btnsearch=Button(table_frame,text="Search",font=("times new roman", 13, "bold"),bg="black",fg="gold",width=8)
        btnsearch.grid(row=0,column=3,padx=1)
        btnshowall=Button(table_frame,text="Show All",font=("times new roman", 13, "bold"),bg="black",fg="gold",width=8)
        btnshowall.grid(row=0,column=4,padx=1)


        # show data table
        detail_table=Frame(table_frame,bd=2,relief=RIDGE)
        detail_table.place(x=0,y=50,width=860,height=180)
        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)
        self.room_table = ttk.Treeview(detail_table, columns=("contact", "checkindate", "checkout", "roomtype", "roomavailable", "meal", "noofdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkindate", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="No. of Days")
        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkindate", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_contact.get(),
                                                                                                    self.var_checkin.get(),
                                                                                                    self.var_checkout.get(),
                                                                                                    self.var_roomtype.get(),
                                                                                                    self.var_roomavailable.get(),
                                                                                                    self.var_meal.get(),
                                                                                                    self.var_noofdays.get()
                                                                                                    ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)
    def get_cursor(self,event):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                
                                                                                                   self.var_checkin.get(),
                                                                                                    self.var_checkout.get(),
                                                                                                    self.var_roomtype.get(),
                                                                                                    self.var_roomavailable.get(),
                                                                                                    self.var_meal.get(),
                                                                                                    self.var_noofdays.get(),self.var_contact.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room detail has been updated successfully",parent=self.root)
    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management system","Do you want delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    def reset(self):
        #self.var_ref.set("")
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

        


       
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if(len(rows)!=0):
            self.room_table.delete(* self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
                conn.commit()
        conn.close()
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","please enter the contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row ==None:
                messagebox.showerror("Error","this number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=450,y=55,width=250,height=180)
                lblname=Label(showdataframe,text="Name:",font=("times new roman", 12, "bold"))
                lblname.place(x=0,y=0)
                lbl=Label(showdataframe,text=row,font=("times new roman", 13, "bold"))
                lbl.place(x=50,y=0)


                conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
                my_cursor=conn.cursor()
                query=("select gender from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblgender=Label(showdataframe,text="Gender:",font=("times new roman", 12, "bold"))
                lblgender.place(x=0,y=30)
                lbl2=Label(showdataframe,text=row,font=("times new roman", 13, "bold"))
                lbl2.place(x=50,y=30)

                conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
                my_cursor=conn.cursor()
                query=("select email from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblemail=Label(showdataframe,text="Email:",font=("times new roman", 12, "bold"))
                lblemail.place(x=0,y=60)
                lbl3=Label(showdataframe,text=row,font=("times new roman", 13, "bold"))
                lbl3.place(x=50,y=60)

                conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
                my_cursor=conn.cursor()
                query=("select nationality from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblnationality=Label(showdataframe,text="Nationality:",font=("times new roman", 12, "bold"))
                lblnationality.place(x=0,y=90)
                lbl4=Label(showdataframe,text=row,font=("times new roman", 13, "bold"))
                lbl4.place(x=50,y=90)

                conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lbladd=Label(showdataframe,text="Address:",font=("times new roman", 12, "bold"))
                lbladd.place(x=0,y=120)
                lbl5=Label(showdataframe,text=row,font=("times new roman", 13, "bold"))
                lbl5.place(x=60,y=120)
    def total(self):
        indate=self.var_checkin.get()
        outdate=self.var_checkout.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outdate-indate).days)


        #if(self.var_meal.get=="Breafast"):




                    





        




if __name__ == "__main__":
    root = Tk()
    obj = roombooking(root)
    root.mainloop()

from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime

class deatilsroom:
    def __init__(self, root):
        self.root = root
        self.root.title("customer window")
        self.root.geometry('1298x550+230+220')

        self.var_floor=StringVar()
        self.var_roomno=StringVar()
        self.var_roomtype=StringVar()
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)
        img1 = Image.open(r"C:\Users\kanak\Downloads\hotel management\logohotel.png")
        img1 = img1.resize((100, 40))

        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(root, image=self.photoimg1, bd=0, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=100, height=40)
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New room add",font=("times new roman", 10, "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=545,height=490)


        lbl_cust_floor=Label(labelframeleft,text=" Floor",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_cust_floor.grid(row=0,column=0,sticky=W)
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=29,font=("times new roman", 13, "bold"))
        entry_floor.grid(row=0,column=1)

        lbl_cust_roomno=Label(labelframeleft,text="Room No",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_cust_roomno.grid(row=1,column=0,sticky=W)
        entry_roomno=ttk.Entry(labelframeleft,textvariable=self.var_roomno,width=29,font=("times new roman", 13, "bold"))
        entry_roomno.grid(row=1,column=1)

        lbl_cust_roomtype=Label(labelframeleft,text="Room Type",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_cust_roomtype.grid(row=2,column=0,sticky=W)
        entry_roomtype=ttk.Entry(labelframeleft,textvariable=self.var_roomtype,width=29,font=("times new roman", 13, "bold"))
        entry_roomtype.grid(row=2,column=1)


        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)
        btnadd=Button(btn_frame,text="ADD",command=self.add_data,font=("times new roman", 13, "bold"),bg="black",fg="gold",width=8)
        btnadd.grid(row=0,column=0,padx=1)
        btndelete=Button(btn_frame,text="DELETE",command=self.mdelete,font=("times new roman", 13, "bold"),bg="black",fg="gold",width=8)
        btndelete.grid(row=0,column=2,padx=1)
        btnupdate=Button(btn_frame,text="UPDATE",command=self.update,font=("times new roman", 13, "bold"),bg="black",fg="gold",width=8)
        btnupdate.grid(row=0,column=1,padx=1)
        btnreset=Button(btn_frame,text="RESET",command=self.reset,font=("times new roman", 13, "bold"),bg="black",fg="gold",width=8)
        btnreset.grid(row=0,column=3,padx=1)

        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show room Details",font=("times new roman", 10, "bold"),padx=2)
        table_frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.room_table=ttk.Treeview(table_frame,columns=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)


        self.room_table.heading("floor", text="floor")
        self.room_table.heading("roomno", text="room no")
        self.room_table.heading("roomtype", text="room type")
        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)
        
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
         
        self.fetch_data()
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                                    self.var_floor.get(),
                                                                                                    self.var_roomno.get(),
                                                                                                    self.var_roomtype.get(),
                                                                                                    
                                                                                                    ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","room details added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s,roomype=%s where roomno=%s",(
                
                                                                                                   self.var_floor.get(),
                                                                                                    self.var_roomtype.get(),
                                                                                                    self.var_roomno.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room detail has been updated successfully",parent=self.root)
    def get_cursor(self,event):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if(len(rows)!=0):
            self.room_table.delete(* self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
                conn.commit()
        conn.close()
    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management system","Do you want delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
            my_cursor=conn.cursor()
            query="delete from details where roomno=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    def reset(self):
        #self.var_ref.set("")
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("")
        



if __name__ == "__main__":
    root = Tk()
    obj = deatilsroom(root)
    root.mainloop()

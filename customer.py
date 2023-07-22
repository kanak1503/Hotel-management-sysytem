from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
class cust_window:
    def __init__(self, root):
        self.root = root
        self.root.title("customer window")
        self.root.geometry('1298x550+230+220')
        # ===========variables================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_cust_name= StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_mother=StringVar()
        
        




        lbl_title = Label(self.root, text="ADD CUSTOMER DETAIL", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)
        img1 = Image.open(r"C:\Users\kanak\Downloads\hotel management\logohotel.png")
        img1 = img1.resize((100, 40))

        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(root, image=self.photoimg1, bd=0, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=100, height=40)


        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Deatils",font=("times new roman", 10, "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #labels and entry
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("times new roman", 13, "bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        #customer name
        lbl_cname=Label(labelframeleft,text="Customer Name",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_cname.grid(row=1,column=0,sticky=W)
        cname_ref=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("times new roman", 13, "bold"))
        cname_ref.grid(row=1,column=1)

        #mother name
        lbl_mname=Label(labelframeleft,text="Mother Name",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_mname.grid(row=2,column=0,sticky=W)
        mname_ref=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=29,font=("times new roman", 13, "bold"))
        mname_ref.grid(row=2,column=1)

        #gender comnox
        lbl_gender=Label(labelframeleft,text="Gender",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("times new roman", 10, "bold"),width=27)
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        
        combo_gender.grid(row=3,column=1)

      

        #postal
        lbl_post=Label(labelframeleft,text="postcode",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_post.grid(row=4,column=0,sticky=W)
        post_ref=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("times new roman", 13, "bold"))

        post_ref.grid(row=4,column=1)

        #mobile
        lbl_mobile=Label(labelframeleft,text="Mobile",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_mobile.grid(row=5,column=0,sticky=W)
        mobile_ref=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("times new roman", 13, "bold"))
        mobile_ref.grid(row=5,column=1)

        #email
        lbl_email=Label(labelframeleft,text="Email",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_email.grid(row=6,column=0,sticky=W)
        email_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_email,font=("times new roman", 13, "bold"))
        email_ref.grid(row=6,column=1)

        #nationality
        lbl_nationality=Label(labelframeleft,text="Nationality",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_nationality.grid(row=7,column=0,sticky=W)
        nationality_ref=ttk.Entry(labelframeleft,textvariable=self.var_nationality,width=29,font=("times new roman", 13, "bold"))
        nationality_ref.grid(row=7,column=1)

        #idproof type
        lbl_idprooftype=Label(labelframeleft,text="Id Proof Type",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_idprooftype.grid(row=8,column=0,sticky=W)
        idprooftype_ref=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,width=29,font=("times new roman", 13, "bold"))
        #idprooftype_ref.grid(row=8,column=1)
        idprooftype_ref["value"]=("Aadhar","Voter card","other")
        
        idprooftype_ref.grid(row=8,column=1)

        #idnumber
        lbl_idnumber=Label(labelframeleft,text="ID Number",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_idnumber.grid(row=9,column=0,sticky=W)
        idnumber_ref=ttk.Entry(labelframeleft,textvariable=self.var_idnumber,width=29,font=("times new roman", 13, "bold"))
        idnumber_ref.grid(row=9,column=1)

        #address
        lbl_address=Label(labelframeleft,text="Address",font=("times new roman", 10, "bold"),padx=2,pady=6)
        lbl_address.grid(row=10,column=0,sticky=W)
        post_ref=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("times new roman", 13, "bold"))
        post_ref.grid(row=10,column=1)
        

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


        #TABLE FRAME
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details",font=("times new roman", 10, "bold"),padx=2)
        table_frame.place(x=435,y=50,width=860,height=490)
        lbl_searchby=Label(table_frame,text="Search BY",font=("times new roman", 10, "bold"),bg="red",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=3)
        self.search_var=StringVar()

        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("times new roman", 10, "bold"),width=27,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1)
        self.txt_search=StringVar()
        textsearch=ttk.Entry(table_frame,textvariable=self.txt_search,width=29,font=("times new roman", 13, "bold"))
        textsearch.grid(row=0,column=2,padx=3)
        btnsearch=Button(table_frame,text="Search",command=self.search,font=("times new roman", 13, "bold"),bg="black",fg="gold",width=8)
        btnsearch.grid(row=0,column=3,padx=1)
        btnshowall=Button(table_frame,text="Show All",command=self.fetch_data,font=("times new roman", 13, "bold"),bg="black",fg="gold",width=8)
        btnshowall.grid(row=0,column=4,padx=1)

        # show data table
        detail_table=Frame(table_frame,bd=2,relief=RIDGE)
        detail_table.place(x=0,y=50,width=860,height=350)
        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)
        self.Cust_detail_table=ttk.Treeview(detail_table,columns=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Cust_detail_table.xview)
        scroll_y.config(command=self.Cust_detail_table.yview)

        self.Cust_detail_table.heading("ref",text="Refer NO")
        self.Cust_detail_table.heading("name",text="Name")
        self.Cust_detail_table.heading("mother",text="Mother Name")
        self.Cust_detail_table.heading("gender",text="gender")
        self.Cust_detail_table.heading("post",text="post")
        self.Cust_detail_table.heading("mobile",text="mobile")
        self.Cust_detail_table.heading("email",text="email")
        self.Cust_detail_table.heading("nationality",text="nationality")
        self.Cust_detail_table.heading("idproof",text="idproof")
        self.Cust_detail_table.heading("idnumber",text="idnumber")
        self.Cust_detail_table.heading("address",text="address")
        self.Cust_detail_table["show"]="headings"



        self.Cust_detail_table.column("ref",width=100)
        self.Cust_detail_table.column("name",width=100)
        self.Cust_detail_table.column("mother",width=100)
        self.Cust_detail_table.column("gender",width=100)
        self.Cust_detail_table.column("post",width=100)
        self.Cust_detail_table.column("mobile",width=100)
        self.Cust_detail_table.column("email",width=100)
        self.Cust_detail_table.column("nationality",width=100)
        self.Cust_detail_table.column("idproof",width=100)
        self.Cust_detail_table.column("idnumber",width=100)
        self.Cust_detail_table.column("address",width=100)
        self.Cust_detail_table.pack(fill=BOTH,expand=1)
        self.Cust_detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),
                                                                                                self.var_cust_name.get(),
                                                                                                self.var_mother.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_post.get(),
                                                                                                self.var_mobile.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_nationality.get(),
                                                                                                self.var_idproof.get(),
                                                                                                self.var_idnumber.get(),
                                                                                                self.var_address.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)
                 
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if(len(rows)!=0):
            self.Cust_detail_table.delete(* self.Cust_detail_table.get_children())
            for i in rows:
                self.Cust_detail_table.insert("",END,values=i)
                conn.commit()
        conn.close()
    def get_cursor(self,event):
        cursor_row=self.Cust_detail_table.focus()
        content=self.Cust_detail_table.item(cursor_row)
        row=content["values"]
        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_idproof.set(row[8])
        self.var_idnumber.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set name=%s,mother=%s,gender=%s,post=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s",(
                
                                                                                                self.var_cust_name.get(),
                                                                                                self.var_mother.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_post.get(),
                                                                                                self.var_mobile.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_nationality.get(),
                                                                                                self.var_idproof.get(),
                                                                                                self.var_idnumber.get(),
                                                                                                self.var_address.get(),self.var_ref.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer detail has been updated successfully",parent=self.root)
            
    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management system","Do you want delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    def reset(self):
        #self.var_ref.set("")
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        #self.var_nationality.set("")
        #self.var_idproof.set("")
        self.var_idnumber.set("")
        self.var_address.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="2024Cs@1098",database="management")
        my_cursor=conn.cursor()
        #my_cursor.execute("select*from customer where"+str(self.search_var.get()),+"Like '%"+str(self.txt_search.get())+"%'")
        my_cursor.execute("select * from customer where " + str(self.search_var.get()) + " Like '%" + str(self.txt_search.get()) + "%'")

        row=my_cursor.fetchall()
        if(len(row)!=0):
            self.Cust_detail_table.delete(* self.Cust_detail_table.get_children())
            for i in row:
                self.Cust_detail_table.insert("",END,values=i)
                conn.commit()
            conn.close()








            

    






            















if __name__ == "__main__":
    root = Tk()
    obj = cust_window(root)
    root.mainloop()

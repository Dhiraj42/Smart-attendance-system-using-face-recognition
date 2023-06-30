from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #=============variables=============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar() 
        self.var_dob=StringVar()
        self.var_email=StringVar() 
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_tg=StringVar()
        

        

         #for first image
        img=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image17.jfif")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=470,height=130)
        
        #for second image
        img1=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image18.jfif")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=460,y=0,width=500,height=130)

        #for third iamge
        img2=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image19.jfif")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=940,y=0,width=500,height=130)

         #background image
        img3=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image12.jpg")
        img3=img3.resize((1530,730),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM" , font=("times new roman",35,"bold") ,bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1250,height=600)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        left_frame.place(x=17,y=20,width=1500,height=600)

        # img_left=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image19.jfif")
        # img_left=img_left.resize((100,30),Image.ANTIALIAS)
        # self.photoimg_left=ImageTk.PhotoImage(img_left)

        # f_lbl=Label(left_frame,image=self.photoimg2)
        # f_lbl.place(x=0,y=0,width=600,height=100)

        #current coarse
        current_coarse_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_coarse_frame.place(x=0,y=0,width=700,height=120)

        #department 
        dep_label=Label(current_coarse_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_coarse_frame,textvariable=self.var_dep,font=("times new romen",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","IT","Mechanical","Instrumentation","Civil","CS","E&TC")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #COURSE
        course_label=Label(current_coarse_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        dep_combo=ttk.Combobox(current_coarse_frame,textvariable=self.var_course,font=("times new romen",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Course","First year","Second year","Third Year","Forth Year")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10)

        #YEAR
        year_label=Label(current_coarse_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_coarse_frame,textvariable=self.var_year,font=("times new romen",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Year","2019-20","2020-21","2021-22","2022-23")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #SEMESTER
        sem_label=Label(current_coarse_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_coarse_frame,textvariable=self.var_semester,font=("times new romen",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Semester","sem-1","sem-2","sem-3","sem-4","sem-4","sem-5","sem-6","sem-7","sem-8")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #CLASS STUDENT INFO
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=0,y=130,width=700,height=300)

        #studentid
        studentID_label=Label(class_student_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,sticky=W)

        stuID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=18,font=("times new roman",13,"bold"))
        stuID_entry.grid(row=0,column=1,padx=10,sticky=W)

        #Student name
        studentname_label=Label(class_student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,sticky=W)

        stuname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=24,font=("times new roman",13,"bold"))
        stuname_entry.grid(row=0,column=3,padx=10,sticky=W)

        #Student Devision
        division_label=Label(class_student_frame,text="Class Division",font=("times new roman",12,"bold"),bg="white")
        division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)


        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new romen",12,"bold"),width=16,state="readonly")
        div_combo["values"]=("Division","A","B","C","D","E","F","G","H","I","J")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll NO
        roll_label=Label(class_student_frame,text="Roll Number",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=24,font=("times new roman",13,"bold"))
        roll_entry.grid(row=1,column=3,padx=10,sticky=W)

        #GENDER
        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new romen",12,"bold"),width=16,state="readonly")
        gender_combo["values"]=("Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DATE OF BIRTH
        DOB_label=Label(class_student_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=24,font=("times new roman",13,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,sticky=W)

        #Email
        email_label=Label(class_student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=18,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,sticky=W)

        #Phone Number
        mob_label=Label(class_student_frame,text="Phone",font=("times new roman",12,"bold"),bg="white")
        mob_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        mob_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=24,font=("times new roman",13,"bold"))
        mob_entry.grid(row=3,column=3,padx=10,sticky=W)

        #Address
        Add_label=Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        Add_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Add_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=18,font=("times new roman",13,"bold"))
        Add_entry.grid(row=4,column=1,padx=10,sticky=W)

        #Gurdian name
        TG_label=Label(class_student_frame,text="TG",font=("times new roman",12,"bold"),bg="white")
        TG_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        TG_entry=ttk.Entry(class_student_frame,textvariable=self.var_tg,width=24,font=("times new roman",13,"bold"))
        TG_entry.grid(row=4,column=3,padx=10,sticky=W)

        # Radiobutton
        self.var_radio1=StringVar()
        radiobut1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo sample",value="Yes")
        radiobut1.grid(row=5,column=0)

        self.var_radio2=StringVar()
        radiobut2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="no photo sample",value="No")
        radiobut2.grid(row=5,column=2)

        #button frame
        butframe=Frame(class_student_frame,bd=2,relief=RIDGE)
        butframe.place(x=0,y=190,width=720,height=300)

        #SAVE BUTTON
        save_but=Button(butframe,text="Save",command=self.add_data,width=24,font=("times new roman",9,"bold"),bg="blue",fg="white")
        save_but.grid(row=0,column=0)

        #update
        up_but=Button(butframe,text="Update",command=self.update_data,width=24,font=("times new roman",9,"bold"),bg="blue",fg="white")
        up_but.grid(row=0,column=1)

        #delete
        del_but=Button(butframe,text="Delete",command=self.delete_data,width=24,font=("times new roman",9,"bold"),bg="blue",fg="white")
        del_but.grid(row=0,column=2)

        #RESET
        res_but=Button(butframe,text="Reset",command=self.reset_data,width=24,font=("times new roman",9,"bold"),bg="blue",fg="white")
        res_but.grid(row=0,column=3)

        #take a photo sample
        take_but=Button(butframe,text="Take Photo Sample",command=self.generate_dataset,width=24,font=("times new roman",9,"bold"),bg="blue",fg="white")
        take_but.grid(row=1,column=0)

        # #Update photo sample
        # Update_but=Button(butframe,text="Update Photo Sample",width=24,font=("times new roman",9,"bold"),bg="blue",fg="white")
        # Update_but.grid(row=1,column=1)


        




        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=700,y=20,width=530,height=900)

        #search System???<<>>>>>________
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=0,y=0,width=700,height=70)

        search_label=Label(search_frame,text="Search By:",width=8,font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new romen",12,"bold"),width=9,state="readonly")
        search_combo["values"]=("Select","Roll no.","Phone no.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        search_entry=ttk.Entry(search_frame,width=10,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W)

       #serach button
        search_but=Button(search_frame,text="Search",width=9,font=("times new roman",9,"bold"),bg="blue",fg="white")
        search_but.grid(row=0,column=3,padx=4)

        #show all
        showall_but=Button(search_frame,text="Show All",width=9,font=("times new roman",9,"bold"),bg="blue",fg="white")
        showall_but.grid(row=0,column=4,padx=4) 

        #TABEL FRAME
        tabel_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        tabel_frame.place(x=0,y=75,width=700,height=300)

        scroll_x=ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabel_frame,orient=VERTICAL)
        
        self.student_tabel=ttk.Treeview(tabel_frame,column=('dep','course','year','sem','id','name','div','roll','gender','dob','email','phone','add','tg','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_tabel.xview)
        scroll_y.config(command=self.student_tabel.yview)

        self.student_tabel.heading("dep",text="Department") 
        self.student_tabel.heading("course", text="Course")
        self.student_tabel.heading("year", text="Year")
        self.student_tabel.heading("sem", text="Semester")
        self.student_tabel.heading("id", text="StudentId")
        self.student_tabel.heading("name", text="Name")
        self.student_tabel.heading("roll", text="Roll")
        self.student_tabel.heading("gender", text="gender")
        self.student_tabel.heading("div", text="Division")
        self.student_tabel.heading("email", text="Email")
        self.student_tabel.heading("dob", text="DOB")
        self.student_tabel.heading("phone", text="Phone")
        self.student_tabel.heading("add",text="Address")
        self.student_tabel.heading("tg", text="TG")
        self.student_tabel.heading("photo", text="PhotoSampleStatus")
        self.student_tabel["show"]="headings"

        self.student_tabel.column("dep", width=100) 
        self.student_tabel.column("course", width=100)
        self.student_tabel.column("year", width=100) 
        self.student_tabel.column("sem", width=100)
        self.student_tabel.column("id", width=100) 
        self.student_tabel.column("name", width=100)
        self.student_tabel.column("roll", width=100)
        self.student_tabel.column("gender", width=100)
        self.student_tabel.column("div", width=100) 
        self.student_tabel.column("dob", width=100)
        self.student_tabel.column("email", width=100)
        self.student_tabel.column("phone", width=100) 
        self.student_tabel.column("add", width=100)
        self.student_tabel.column("tg", width=100)
        self.student_tabel.column("photo", width=150)

        self.student_tabel.pack(fill=BOTH,expand=1)
        self.student_tabel.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    #=================fuction declaration=============
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try: 
            # messagebox.showinfo("Success","Succesfully Enter Data")
                conn=mysql.connector.connect(host="localhost",username="root",password="Dhiraj@789",database="dhiraj")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into stdent values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_tg.get(),
                                                                                                self.var_radio1.get()

                                                                                                

                                                                                            
                                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   



# +======================================fetch data===================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Dhiraj@789",database="dhiraj")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from stdent")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in data:
                self.student_tabel.insert("",END,values=i)
            conn.commit()
        conn.close()

    #  ================get cursor==================
    def get_cursor(self,event=""):
        cursor_focus=self.student_tabel.focus()
        content=self.student_tabel.item(cursor_focus)
        data1=content["values"]

        self.var_dep.set(data1[0]),
        self.var_course.set(data1[1]),
        self.var_year.set(data1[2]),
        self.var_semester.set(data1[3]),
        self.var_std_id.set(data1[4]),
        self.var_std_name.set(data1[5]),
        self.var_div.set(data1[6]),
        self.var_roll.set(data1[7]),
        self.var_gender.set(data1[8]),
        self.var_dob.set(data1[9]),
        self.var_email.set(data1[10]),
        self.var_phone.set(data1[11]),
        self.var_address.set(data1[12]),
        self.var_tg.set(data1[13]),
        self.var_radio1.set(data1[14]),
        
# ================update fuction===========
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Dhiraj@789",database="dhiraj")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update stdent set dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Tg=%s,PhotoSample=%s where student_id=%s",(

                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_tg.get(),
                                                                                                                        self.var_radio1.get(), 
                                                                                                                        self.var_std_id.get()    
                                                                                                                    ))                                                         
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details Update Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

# ===============================delete function=========================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Dhiraj@789",database="dhiraj")
                    my_cursor=conn.cursor()
                    sql="delete from stdent where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)  

# ========================resete fuction===================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set=("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("select division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_tg.set("")
        self.var_radio1.set("")


# ================================?generate data set or take a photo sample=============
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Dhiraj@789",database="dhiraj")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from stdent")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update stdent set dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Tg=%s,PhotoSample=%s where student_id=%s",(

                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_tg.get(),
                                                                                                                        self.var_radio1.get(), 
                                                                                                                        self.var_std_id.get()==id+1
                                                                                                           ))
        
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                    

                    # ==================load prediend data on face frontals from opencv==========
                face_classfier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classfier.detectMultiScale(gray,1.3,5)
                        #scaling factor=1.3 
                        #minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                        
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==30:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed !!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)  


                                                                                               
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

###########variables##########
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
       





        #for first image
        img=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image11.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=770,height=150)
        
        #for second image
        img1=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image13.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=700,y=0,width=790,height=150)

        #background image
        img3=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image12.jpg")
        img3=img3.resize((1530,730),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM" , font=("times new roman",35,"bold") ,bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1500,height=600)

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Information",font=("times new roman",12,"bold"))
        left_frame.place(x=0,y=10,width=650,height=450)

        

        #label and entry
        #Attendanceid
        attendanceID_label=Label(left_frame,text="Attendance ID",font=("times new roman",12,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,sticky=W)

        attendanceID_entry=ttk.Entry(left_frame,width=18,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=8)

        #Roll
        roll_label=Label(left_frame,text="Roll No.:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W )

        roll_label_entry=ttk.Entry(left_frame,width=18,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        roll_label_entry.grid(row=0,column=3,pady=8)

        #Name
        name_label=Label(left_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_label=ttk.Entry(left_frame,width=18,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        name_label.grid(row=1,column=1,padx=10,pady=8)

        #Deaprtment
        department_label=Label(left_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,sticky=W)

        department=ttk.Entry(left_frame,width=18,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        department.grid(row=1,column=3,padx=10,pady=8)

       #time
        time_label=Label(left_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time=ttk.Entry(left_frame,width=18,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        time.grid(row=2,column=1,padx=10,pady=8)

        #Date
        date_label=Label(left_frame,text="Date",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,sticky=W)

        date=ttk.Entry(left_frame,width=18,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        date.grid(row=2,column=3,padx=10,pady=8)

        #attendance
        attendance_label=Label(left_frame,text="Attendance",font=("times new roman",12,"bold"),bg="white")
        attendance_label.grid(row=3,column=0,padx=10,sticky=W)

        self.atten_status=ttk.Combobox(left_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",13,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #button frame
        butframe=Frame(left_frame,bd=2,relief=RIDGE)
        butframe.place(x=0,y=300,width=720,height=300)

        #SAVE BUTTON
        save_but=Button(butframe,text="Import csv",command=self.importcsv,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        save_but.grid(row=0,column=0)

        #update
        up_but=Button(butframe,text="Export csv",command=self.exportcsv,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        up_but.grid(row=0,column=1)

        #delete
        del_but=Button(butframe,text="Update",width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        del_but.grid(row=0,column=2)

        #RESET
        res_but=Button(butframe,text="Reset",command=self.reset_data,width=21,font=("times new roman",9,"bold"),bg="blue",fg="white")
        res_but.grid(row=0,column=3)

        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=660,y=10,width=600,height=450)

        tableframe=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        tableframe.place(x=5,y=10,width=580,height=400)

        ####scroll bar table#####
        scroll_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableframe,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(tableframe,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No.")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Dapartment")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance ")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=80)
        self.AttendanceReportTable.column("name",width=80)
        self.AttendanceReportTable.column("department",width=80)
        self.AttendanceReportTable.column("time",width=80)
        self.AttendanceReportTable.column("date",width=80)
        self.AttendanceReportTable.column("attendance",width=80)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.getcursor)


        #########fetch data###########

    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import csv###
    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("csv file","*.csv"),("all file","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    #export csv##
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("csv file","*.csv"),("all file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data export","Your Data Exported succefully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 

    def getcursor(self,events=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"] 
        self.var_atten_id.set(rows[0])  
        self.var_atten_roll.set(rows[1])  
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()


            
import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from time import strftime
from datetime import datetime
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognization import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Detection:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1265x790+0+0")
        self.root.title("Face Recognition System")


        #for first image
        img=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image31.jpg")
        img=img.resize((700,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=470,height=130)
        
        #for second image
        img1=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image32.jpg")
        img1=img1.resize((480,170),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=460,y=0,width=480,height=130)

        #for third iamge
        img2=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image34.png")
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

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM" ,font=("times new roman",35,"bold") ,bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        #+===============TIme============


        def time():
            string = strftime("%I:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)

        # Create a Tkinter window or frame (title_lbl assumed to be defined)
        # ...

        lbl = Label(title_lbl, font=("times new roman", 14, "bold"), background="white", foreground="blue")
        lbl.place(x=0, y=0, width=110, height=50)
        time()


        #student button
        img4=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image24.png")
        img4=img4.resize((160,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=90,y=70,width=150,height=180)

        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",10,"bold") ,bg="darkblue",fg="white")
        b1_1.place(x=90,y=250,width=152,height=20)


        #Detect face buttom
        img5=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image25.jpg")
        img5=img5.resize((160,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=350,y=70,width=150,height=180)

        b1_1=Button(bg_img,text="FACE RECOGNITION",cursor="hand2",command=self.face_data,font=("times new roman",10,"bold") ,bg="darkblue",fg="white")
        b1_1.place(x=350,y=250,width=152,height=20)

        #FOR attenadance
        img6=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image26.jpg")
        img6=img6.resize((160,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=600,y=70,width=150,height=180)

        b1_1=Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance_data,font=("times new roman",10,"bold") ,bg="darkblue",fg="white")
        b1_1.place(x=600,y=250,width=152,height=20)


        #HELP
        img7=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image28.jpg")
        img7=img7.resize((160,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=900,y=70,width=150,height=180)

        b1_1=Button(bg_img,text="HELP",cursor="hand2",font=("times new roman",10,"bold") ,bg="darkblue",fg="white")
        b1_1.place(x=900,y=250,width=152,height=20)

        #TRAIN DATA
        img8=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image27.png")
        img8=img8.resize((160,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.traindata)
        b1.place(x=90,y=300,width=150,height=180)

        b1_1=Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.traindata,font=("times new roman",10,"bold") ,bg="darkblue",fg="white")
        b1_1.place(x=90,y=470,width=152,height=20)

        #PHOTOS
        img9=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image29.jpg")
        img9=img9.resize((160,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=350,y=300,width=150,height=180)

        b1_1=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",10,"bold") ,bg="darkblue",fg="white")
        b1_1.place(x=350,y=470,width=152,height=20)

        #DEVELOPER
        img10=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image30.jpg")
        img10=img10.resize((160,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=600,y=300,width=150,height=180)

        b1_1=Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer_data,font=("times new roman",10,"bold") ,bg="darkblue",fg="white")
        b1_1.place(x=600,y=470,width=152,height=20)

        #EXIT
        img11=Image.open(r"C:\Users\dhira\OneDrive\Desktop\face detection\images\image8.jfif")
        img11=img11.resize((150,180),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.isExit)
        b1.place(x=900,y=300,width=150,height=180)

        b1_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.isExit,font=("times new roman",10,"bold") ,bg="darkblue",fg="white")
        b1_1.place(x=900,y=470,width=152,height=20)

    def open_img(self):
        os.startfile("data")


        # #<<<<<<<<<<<<<>Funcion button>>>>>>>>>>>>>>>>>

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def traindata(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def isExit(self):
        self.isExit=tkinter.messagebox.askyesno("Face recognition system","Are you sure want to exit?")
        if self.isExit>0:
            self.root.destroy()
        else:
            return
        


    


    

if __name__ == "__main__":
    root=Tk()
    obj=Face_Detection(root)
    root.mainloop()




from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime 
import cv2
import os
import numpy as np





class Face_Recognition:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("Face Recognition System")

                title_lbl=Label(self.root,text="FACE RECOGNITION" , font=("times new roman",35,"bold") ,bg="white",fg="green")
                title_lbl.place(x=0,y=0,width=1300,height=45)

# ==================img no.1==============
                img_top=Image.open(r"images\image16.jpg")
                img_top=img_top.resize((600,600),Image.ANTIALIAS)
                self.photoimg_top=ImageTk.PhotoImage(img_top)

                f_lbl1=Label(self.root,image=self.photoimg_top)
                f_lbl1.place(x=0,y=50,width=600,height=600)

# ================img no.2==================
                img_top1=Image.open(r"images\image14.jpg")
                img_top1=img_top1.resize((750,600),Image.ANTIALIAS)
                self.photoimg_top1=ImageTk.PhotoImage(img_top1)

                f_lbl=Label(self.root,image=self.photoimg_top1)
                f_lbl.place(x=600,y=50,width=750,height=600)

# =================button======================
                b2_1=Button(f_lbl,text="FACE RECOGNITION",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold") ,bg="sky blue",fg="green")
                b2_1.place(x=250,y=500,width=250,height=30)

##==============ATTENDANCE======================  
        def mark_attendance(self, i, r, n, d):
                attendance_data = f"{i.strip('()')}{r.strip('()')}{n.strip('()')}{d.strip('()')}"
                now = datetime.now()
                dtString = now.strftime("%H:%M:%S")
                d1 = now.strftime("%d/%m/%Y")
                attendance_data += f"{dtString},{d1},present\n"

                with open("dhiraj.csv", "r+", newline="\n") as f:
                        myDataList = f.readlines()
                        name_list = [entry.split(",")[0:4] for entry in myDataList]

                        if attendance_data.split(",")[0:4] not in name_list:
                                f.write(attendance_data)


 
# ========================face recognition function================
        def face_recog(self):
                def draw_boundary(img,classiffier,scaleFactor,minNeighbors,color,text,clf):
                        gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        features=classiffier.detectMultiScale(gray_image,scaleFactor,minNeighbors) 

                        coord=[]

                        for (x,y,w,h) in features:
                                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                                id,predict1=clf.predict(gray_image[y:y+h,x:x+w])
                                confidence=int((100*(1-predict1/300)))

                                conn=mysql.connector.connect(host="localhost",username="root",password="Dhiraj@789",database="dhiraj")
                                my_cursor=conn.cursor()

                                my_cursor.execute("select Name from stdent where student_id="+str(id))
                                n = my_cursor.fetchone()
                                n = str(n)  # Convert to string

                                my_cursor.execute("select Roll from stdent where student_id="+str(id))
                                r = my_cursor.fetchone()
                                r = str(r)  # Convert to string

                                my_cursor.execute("select dep from stdent where student_id="+str(id))
                                d = my_cursor.fetchone()
                                d = str(d)  # Convert to string

                                my_cursor.execute("select student_id from stdent where student_id="+str(id))
                                i = my_cursor.fetchone()
                                i = str(i)  # Convert to string








                                if confidence>70:
                                        cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(170, 74, 68),3)
                                        cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(170, 74, 68),3)
                                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(170, 74, 68),3)
                                        cv2.putText(img,f"dep:{d}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(170, 74, 68),3)
                                        self.mark_attendance(i,r,n,d)

                                else:
                                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                                        cv2.putText(img,"unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                                coord=[x,y,w,h]
                        return coord

                def recognize(img,clf,faceCascade):
                        coord1=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                        return img

                faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                clf=cv2.face.LBPHFaceRecognizer_create()   
                clf.read("classifier.xml")   

                videocap=cv2.VideoCapture(0)

                while True:
                        ret,img=videocap.read()   
                        img=recognize(img,clf,faceCascade)
                        cv2.imshow("Welcome to face recognition",img)

                        if cv2.waitKey(1)==13:
                                break
                videocap.release()
                cv2.destroyAllWindows()


                    

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
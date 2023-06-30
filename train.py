from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
import cv2
import os
import numpy as np





class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET" , font=("times new roman",35,"bold") ,bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=45)

# ==================for image==================
        img_top=Image.open(r"images\image34.png")
        img_top=img_top.resize((1300,330),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1300,height=330)

# ======================train data Button==========
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold") ,bg="sky blue",fg="red")
        b1_1.place(x=0,y=380,width=1300,height=50)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  ##gray scale image
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Trainning",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

    #    ==========================train_classifier=============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Trainning Data set Completed!!!")



if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()

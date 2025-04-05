import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  
from help import Help
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from time import strftime
from chatbot import ChatBot
from datetime import datetime

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x900+0+0")
        self.root.title("Face Recognition System")

        # First Image
        img = Image.open(r"college_images\BestFacialRecognition.jpg")
        img = img.resize((426, 100))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=426, height=100)

        # Second Image
        img1 = Image.open(r"college_images\facialrecognition.png")
        img1 = img1.resize((426, 100))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=426, y=0, width=426, height=100)

        # Third Image
        img2 = Image.open(r"college_images\images.jpg")
        img2 = img2.resize((428, 100))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=852, y=0, width=428, height=100)

        # Background Image
        img3 = Image.open(r"college_images\background.jpeg")
        img3 = img3.resize((1280, 600))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1280, height=600)

        # Title Label
        title_lbl = Label(bg_img, text="FACIAL RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="#1a1a2e", fg="#e94560", anchor="w", padx=20)
        title_lbl.place(x=0, y=0, width=1280, height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font = ("times new roman", 17, "bold"), bg="#1a1a2e", fg="#ffffff")        
        lbl.place(x=1120, y=0, width=150, height=45)
        time()

        # Student Button
        img4 = Image.open(r"college_images\gettyimages-1022573162.jpg")
        img4 = img4.resize((190, 180))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=145, y=80, width=190, height=180)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=145, y=247, width=190, height=30)

        # Detect face Button
        img5 = Image.open(r"college_images\face_detector1.jpg")
        img5 = img5.resize((190, 180))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b1.place(x=400, y=80, width=190, height=180)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=400, y=247, width=190, height=30)

        # Attendance face Button
        img6 = Image.open(r"college_images\report.jpg")
        img6 = img6.resize((190, 180))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b1.place(x=655, y=80, width=190, height=180)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=655, y=247, width=190, height=30)

        # # Help face Button
        # img7 = Image.open(r"college_images\help.jpg")
        # img7 = img7.resize((190, 180))
        # self.photoimg7 = ImageTk.PhotoImage(img7)

        # b1 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.help_desk)
        # b1.place(x=910, y=80, width=190, height=180)

        # b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.help_desk, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        # b1_1.place(x=910, y=247, width=190, height=30)

        # Chatbot Button
        img7 = Image.open(r"college_images\chat.jpg")
        img7 = img7.resize((190, 180))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.chatBot)
        b1.place(x=910, y=80, width=190, height=180)

        b1_1 = Button(bg_img, text="ChatBot", cursor="hand2", command=self.chatBot, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=910, y=247, width=190, height=30)

        # Train face Button
        img8 = Image.open(r"college_images\Train.jpg")
        img8 = img8.resize((190, 180))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b1.place(x=145, y=340, width=190, height=180)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data,  font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=145, y=507, width=190, height=30)

        # Photos face Button
        img9 = Image.open(r"college_images\sample.jpg")
        img9 = img9.resize((190, 180))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x=400, y=340, width=190, height=180)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=400, y=507, width=190, height=30)

        # Developer face Button
        img10 = Image.open(r"college_images\Team-Management-Software-Development.jpg")
        img10 = img10.resize((190, 180))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.developer_data)
        b1.place(x=655, y=340, width=190, height=180)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=655, y=507, width=190, height=30)

        # Exit face Button
        img11 = Image.open(r"college_images\exit.jpg")
        img11 = img11.resize((190, 180))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b1.place(x=910, y=340, width=190, height=180)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=910, y=507, width=190, height=30)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = messagebox.askyesno("Face recognition!", "Are you sure exit this project?", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

        #---------Functionality Buttons---------
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    # def help_desk(self):
    #     self.new_window = Toplevel(self.root)
    #     self.app = Help(self.new_window)

    def chatBot(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
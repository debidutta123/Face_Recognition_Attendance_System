from tkinter import *
from PIL import Image, ImageTk  
from tkinter import messagebox
from datetime import datetime
import cv2
import mysql.connector

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x900+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION" , font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1280, height=45)

        img_top = Image.open(r"college_images\face_detector1.jpg")
        img_top = img_top.resize((550, 650))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=550, height=650)

        img_buttom = Image.open(r"college_images\facial_recognition_system_identification.jpg")
        img_buttom = img_buttom.resize((730, 650))
        self.photoimg_buttom = ImageTk.PhotoImage(img_buttom)

        f_lbl = Label(self.root, image=self.photoimg_buttom)
        f_lbl.place(x=550, y=50, width=730, height=650)

        # Buttons
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 16, "bold"), bg="green", fg="white")
        b1_1.place(x=270, y=572, width=180, height=35)

    #-------------------Attendance Functionality------------------
    def mark_attendance(self, i, r, n, d):
        with open("Attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])

            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    #-------------------Face Recognition Functionality------------------
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            conn = mysql.connector.connect(host="localhost", username="root", password="Debi@123", database="face_reconizer")
            my_cursor = conn.cursor()

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                my_cursor.execute("select Name from student where Student_id=%s", (id,))
                n = my_cursor.fetchone()
                n = n[0] if n else "Unknown"

                my_cursor.execute("select Roll from student where Student_id=%s", (id,))
                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown"

                my_cursor.execute("select Dep from student where Student_id=%s", (id,))
                d = my_cursor.fetchone()
                d = d[0] if d else "Unknown"

                my_cursor.execute("select Student_id from student where Student_id=%s", (id,))
                i = my_cursor.fetchone()
                i = i[0] if i else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                
                coord = [x, y, w, h]
            
            conn.close()
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition.", img)

            if cv2.waitKey(1) == 13:  # Enter key
                break
        video_cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result!", "Face Recognized Successfully.")

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

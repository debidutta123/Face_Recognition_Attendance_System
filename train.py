import os
from tkinter import *
from PIL import Image, ImageTk  
from tkinter import messagebox
import cv2
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x900+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET" , font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1280, height=45)

        img_top = Image.open(r"college_images\facialrecognition.png")
        img_top = img_top.resize((1280, 290))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1280, height=290)

        # Buttons
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 27, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=340, width=1280, height=60)

        img_buttom = Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img_buttom = img_buttom.resize((1280, 300))
        self.photoimg_buttom = ImageTk.PhotoImage(img_buttom)

        f_lbl = Label(self.root, image=self.photoimg_buttom)
        f_lbl.place(x=0, y=400, width=1280, height=300)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')   # convert to grayscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[-1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)
        
        #---------------Training the classifier and save------------------
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result!", "Training datasets completed successfully.")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
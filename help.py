from tkinter import *
from PIL import Image, ImageTk  

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x900+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="HELP DESK" , font=("times new roman", 35, "bold"), bg="white", fg="BLUE")
        title_lbl.place(x=0, y=0, width=1280, height=45)

        img_top = Image.open(r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top = img_top.resize((1280, 700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1280, height=700)

        dev_label = Label(f_lbl, text="Email: sdebidutta2024@gmail.com", font=("times new roman", 18, "bold"), fg="blue")
        dev_label.place(x=425, y=185)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
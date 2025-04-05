from tkinter import *
import webbrowser
from PIL import Image, ImageTk  

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x900+0+0")
        self.root.title("Developer Profile")
        self.root.configure(bg="#f5f5f5")
        
        self.create_widgets()
    
    def load_image(self, path, size):
        try:
            img = Image.open(path)
            img = img.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading image {path}: {e}")
            return None
        
    def open_linkedin(self):
            webbrowser.open("https://www.linkedin.com/in/debidutta-mahaprasad-sahoo-3ba508245?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")
    
    def create_widgets(self):
        title_lbl = Label(self.root, text="MEET THE DEVELOPER", font=("Helvetica", 35, "bold"), bg="#007acc", fg="white")
        title_lbl.place(x=0, y=0, width=1280, height=60)
        
        bg_image = self.load_image("college_images/dev.jpg", (1280, 700))
        if bg_image:
            bg_lbl = Label(self.root, image=bg_image)
            bg_lbl.image = bg_image
            bg_lbl.place(x=0, y=60, width=1280, height=700)
        
        main_frame = Frame(self.root, bg="#1e1e1e", bd=2, relief=RIDGE, highlightbackground="#ffdd57", highlightthickness=2)
        main_frame.place(x=830, y=100, width=420, height=550)
        
        profile_img = self.load_image("college_images/debidutta.jpg", (200, 200))
        if profile_img:
            profile_lbl = Label(main_frame, image=profile_img, bg="white")
            profile_lbl.image = profile_img
            profile_lbl.place(x=120, y=10, width=200, height=200)
        
        Label(main_frame, text="Hello! I'm Debidutta Sahoo.", font=("Helvetica", 20, "bold"), fg="#ffdd57", bg="#1e1e1e").place(x=30, y=220)
        Label(main_frame, text="Full Stack Developer", font=("Helvetica", 16, "italic"), fg="#ffffff", bg="#1e1e1e").place(x=90, y=255)
        
        desc = "Passionate about creating efficient and scalable applications. Skilled in Python, JavaScript, React, Node.js and more."
        Label(main_frame, text=desc, font=("Arial", 12), fg="#cccccc", bg="#1e1e1e", wraplength=380, justify="center").place(x=20, y=280)

        # Contact Button with LinkedIn Redirection & Hover Effect
        def on_enter(e):
            contact_btn.config(bg="#ffcc00", fg="#000000")
        def on_leave(e):
            contact_btn.config(bg="#1e1e1e", fg="#ffdd57")
        
        contact_btn = Button(main_frame, text="Get in Touch", font=("Poppins", 18, "bold"),
                             bg="#1e1e1e", fg="#ffdd57", bd=0, relief=RAISED, cursor="hand2",
                             activebackground="#ffcc00", activeforeground="#000000",
                             command=self.open_linkedin)
        contact_btn.bind("<Enter>", on_enter)
        contact_btn.bind("<Leave>", on_leave)
        contact_btn.place(x=120, y=345, width=160, height=45)
        
        footer_img = self.load_image("college_images/footer.jpg", (420, 155))
        if footer_img:
            footer_lbl = Label(main_frame, image=footer_img, bg="white")
            footer_lbl.image = footer_img
            footer_lbl.place(x=0, y=395, width=420, height=155)

        dev_label = Label(footer_lbl, text="Email: sdebidutta2024@gmail.com", font=("times new roman", 16, "bold"), fg="white", bg="#1e1e1e", bd=0)
        dev_label.place(x=73, y=120)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()

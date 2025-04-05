from time import strftime
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import bcrypt

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x750+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACIAL RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="#1a1a2e", fg="#e94560", anchor="w", padx=20)
        title_lbl.place(x=0, y=0, width=1280, height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font = ("times new roman", 17, "bold"), bg="#1a1a2e", fg="#ffffff")        
        lbl.place(x=1120, y=0, width=150, height=45)
        time()

        # ----------------Background Image----------------
        bg_img = Image.open(r"college_images\AI.jpeg").resize((1280, 655))
        self.photoimg = ImageTk.PhotoImage(bg_img)

        Label(self.root, image=self.photoimg).place(x=0, y=45, width=1280, height=655)

        # ----------------Login Frame----------------
        frame = Frame(self.root, bd=2, bg="black")
        frame.place(x=490, y=150, width=350, height=450)

        img1 = Image.open(r"college_images\LoginIconAppl.png")
        img1 = img1.resize((100, 100))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        img1_label = Label(self.root, image=self.photoimg1, bg="black", bd=0)
        img1_label.place(x=620, y=105, width=100, height=100)

        login_lbl = Label(frame, text="Get Started", font=("times new roman", 25, "bold"), bg="black", fg="white")
        login_lbl.place(x=90, y=55)

        # -----------------------Icon images------------------------
        img2 = Image.open(r"college_images\LoginIconAppl.png")
        img2 = img2.resize((25, 25))
        self.photoimg2 = ImageTk.PhotoImage(img2)
                
        password_icon_label = Label(frame, image=self.photoimg2, bg="black", bd=0)
        password_icon_label.place(x=35, y=117, width=25, height=25)
        
        img3 = Image.open(r"college_images\lock-512.png")
        img3 = img3.resize((25, 25))
        self.photoimg3 = ImageTk.PhotoImage(img3)
                
        username_icon_label = Label(frame, image=self.photoimg3, bg="black", bd=0)
        username_icon_label.place(x=35, y=207, width=25, height=25)

        # ----------------Labels & Entry Fields----------------
        Label(frame, text="Email:", font=("times new roman", 20, "bold"), bg="black", fg="white").place(x=65, y=110)
        self.email_entry = ttk.Entry(frame, font=("times new roman", 18, "bold"))
        self.email_entry.place(x=35, y=150, width=280)

        Label(frame, text="Password:", font=("times new roman", 20, "bold"), bg="black", fg="white").place(x=65, y=200)
        self.password_entry = ttk.Entry(frame, font=("times new roman", 18, "bold"), show="*")  # Hide password
        self.password_entry.place(x=35, y=240, width=280)

        # ----------------Buttons----------------
        Button(frame, text="Don't have an account? Sign Up", font=("times new roman", 13, "bold"), fg="white", bg="black", bd=0, activebackground="black", activeforeground="white", cursor="hand2", command=self.open_register).place(x=50, y=280) 

        Button(frame, text="Login", font=("times new roman", 25, "bold"), fg="white", bg="red", activebackground="darkred", command=self.login, cursor="hand2").place(x=75, y=350, width=200, height=50)

        Button(frame, text="Forgot Password?", font=("times new roman", 13, "bold"), bd=0, fg="white", bg="black", activebackground="black", activeforeground="white", cursor="hand2", command=self.forgot_password_window).place(x=95, y=405)

    def login(self):
        """Validate user credentials and allow login if correct."""
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Debi@123", database="face_reconizer")
            my_cursor = conn.cursor()

            # Fetch user data
            my_cursor.execute("SELECT pasword FROM register WHERE email=%s", (email,))
            user_data = my_cursor.fetchone()

            conn.close()

            if user_data:
                hashed_password = user_data[0].encode('utf-8')

                # Check if entered password matches stored hashed password
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    # messagebox.showinfo("Success", "Login Successful!", parent=self.root)
                    self.clear_fields()
                    self.open_main_system()
                else:
                    messagebox.showerror("Error", "Invalid Password!", parent=self.root)
            else:
                messagebox.showerror("Error", "User not found! Please register first.", parent=self.root)

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}", parent=self.root)

    def clear_fields(self):
        """Resets all input fields after successful registration."""
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def open_main_system(self):
        """Redirect to the main system after successful login."""
        from main import Face_Recognition_System
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition_System(self.new_window)

    def open_register(self):
        """Open the registration window."""
        try:
            from register import Register
            self.new_window = Toplevel(self.root)
            self.app = Register(self.new_window)
        except ImportError:
            messagebox.showerror("Error", "Registration module not found.")

    #-------------------Forgot Password------------------
    def forgot_password_window(self):
        if not self.email_entry.get():
            messagebox.showerror("Error!", "Please enter your email to reset password.", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Debi@123", database="face_reconizer")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE email=%s")
            value = (self.email_entry.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error!", "This email is not registered.", parent=self.root)
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("350x450+610+170")
                self.root2.config(bg="black")

                l = Label(self.root2, text="Forgot Password", font=("times new roman", 22, "bold"), bg="#1a1a2e", fg="#e94560")
                l.place(x=0, y=0, width=350, height=50)

                Label(self.root2, text="Security Question:", font=("times new roman", 20, "bold"), bg="black", fg="white").place(x=35, y=60)

                self.security_q_combo = ttk.Combobox(self.root2, font=("times new roman", 18, "bold"), state="readonly")
                self.security_q_combo["values"] = ("Select", "Your Birth Place", "Your Nick Name", "Your Favorite Teacher")
                self.security_q_combo.current(0)
                self.security_q_combo.place(x=35, y=100, width=280, height=30)

                Label(self.root2, text="Security Answer:", font=("times new roman", 20, "bold"), bg="black", fg="white").place(x=35, y=150)

                self.security_a = ttk.Entry(self.root2, font=("times new roman", 18, "bold"))
                self.security_a.place(x=35, y=190, width=280)

                Label(self.root2, text="New Password:", font=("times new roman", 20, "bold"), bg="black", fg="white").place(x=35, y=240)
                self.new_password_entry = ttk.Entry(self.root2, font=("times new roman", 18, "bold"), show="*") 
                self.new_password_entry.place(x=35, y=280, width=280)

                Button(self.root2, text="Reset", font=("times new roman", 25, "bold"), fg="white", bg="green", activebackground="darkgreen", command=self.reset_password, cursor="hand2").place(x=75, y=350, width=200, height=50)

    #-----------------Reset Password------------------
    def reset_password(self):
        """Reset the password after validation."""
        if self.security_q_combo.get() == "Select":
            messagebox.showerror("Error!", "Select Security Question is required!", parent=self.root2)
        elif self.security_a.get() == "":
            messagebox.showerror("Error!", "Enter your answer.", parent=self.root2)
        elif self.new_password_entry.get() == "":
            messagebox.showerror("Error!", "Enter your new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Debi@123", database="face_reconizer")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE email=%s AND security_q=%s AND security_a=%s")
            value = (self.email_entry.get(), self.security_q_combo.get(), self.security_a.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error!", "Security Question and Answer do not match.", parent=self.root2)
            else:
                hashed_password = bcrypt.hashpw(self.new_password_entry.get().encode('utf-8'), bcrypt.gensalt())
                update_query = ("UPDATE register SET pasword=%s WHERE email=%s")
                my_cursor.execute(update_query, (hashed_password, self.email_entry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success!", "Password reset successful. Please login!", parent=self.root2)
                self.root2.destroy()

if __name__ == "__main__":
    root = Tk()
    Login_Window(root)
    root.mainloop()

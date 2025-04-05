from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import bcrypt
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x750+0+0")
        self.root.title("Face Recognition System")

        # ---------------------Variables----------------------
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_q = StringVar()
        self.var_security_a = StringVar()
        self.var_password = StringVar()
        self.var_cpassword = StringVar()
        self.var_check = IntVar()

        # ------------Background image---------
        bg_img = Image.open("college_images/un.jpg").resize((1280, 700))
        self.photoimg = ImageTk.PhotoImage(bg_img)

        Label(self.root, image=self.photoimg).place(x=0, y=0, width=1280, height=700)

        # -----------------Left Image-----------------
        left_img = Image.open("college_images/register.jpg").resize((400, 500))
        self.left_photoimg = ImageTk.PhotoImage(left_img)

        Label(self.root, image=self.left_photoimg).place(x=100, y=100, width=400, height=500)

        # ---------------Frame-----------------
        frame = Frame(self.root, bd=2, bg="white")
        frame.place(x=500, y=100, width=680, height=500)

        Label(frame, text="REGISTER HERE", font=("times new roman", 25, "bold"), bg="white", fg="darkgreen").place(x=150, y=10)

        # ----------------Labels and Entries----------------
        fields = [("First Name:", self.var_fname, 35, 90), 
                  ("Last Name:", self.var_lname, 350, 90), 
                  ("Contact No:", self.var_contact, 35, 160), 
                  ("Email:", self.var_email, 350, 160),
                  ("Security Answer:", self.var_security_a, 350, 230), 
                  ("Password:", self.var_password, 35, 300),
                  ("Confirm Password:", self.var_cpassword, 350, 300)]
        
        for text, var, x, y in fields:
            Label(frame, text=text, font=("times new roman", 16, "bold"), bg="white").place(x=x, y=y)
            ttk.Entry(frame, textvariable=var, font=("times new roman", 16, "bold")).place(x=x, y=y + 30, width=300)

        # ----------------Security Question----------------
        Label(frame, text="Select Security Question:", font=("times new roman", 16, "bold"), bg="white").place(x=35, y=230)

        security_q_combo = ttk.Combobox(frame, textvariable=self.var_security_q, font=("times new roman", 15, "bold"), state="readonly")
        security_q_combo["values"] = ("Select", "Your Birth Place", "Your Nick Name", "Your Favorite Teacher")
        security_q_combo.current(0)
        security_q_combo.place(x=35, y=260, width=300, height=30)

        # -------------Check Button----------------
        Checkbutton(frame, variable=self.var_check, text="I agree to the terms and conditions.", font=("times new roman", 13, "bold"), onvalue=1, offvalue=0, bg="white").place(x=200, y=375)

        # ------------------Buttons-------------------
        Button(frame, text="Register Now", font=("times new roman", 14, "bold"), fg="white", bg="red", activebackground="darkred", cursor="hand2", command=self.register_data).place(x=60, y=420, width=200, height=50)

        Button(frame, text="Login Now", font=("times new roman", 14, "bold"), fg="white", bg="blue", activebackground="darkblue", cursor="hand2", command=self.login_now).place(x=380, y=420, width=200, height=50)

    # -----------------Function Declaration------------------
    def register_data(self):
        """Handles registration validation and database insertion."""
        if not all([self.var_fname.get(), self.var_lname.get(), self.var_contact.get(), self.var_email.get(),
                    self.var_security_q.get() != "Select", self.var_security_a.get(), self.var_password.get()]):
            messagebox.showerror("Error!", "All fields are required!", parent=self.root)
        elif self.var_password.get() != self.var_cpassword.get():
            messagebox.showerror("Error!", "Passwords do not match!", parent=self.root)
        elif not self.var_check.get():
            messagebox.showerror("Error!", "You must agree to the terms and conditions!", parent=self.root)
        else:
            self.save_to_database()

    def save_to_database(self):
        """Saves user registration data to the database."""
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Debi@123", database="face_reconizer")
            my_cursor = conn.cursor()

            # Check if the user already exists
            my_cursor.execute("SELECT * FROM register WHERE email=%s", (self.var_email.get(),))
            if my_cursor.fetchone():
                messagebox.showerror("Error!", "User already exists. Please login instead.", parent=self.root)
                conn.close()
                return

            # Hash password before storing
            hashed_password = bcrypt.hashpw(self.var_password.get().encode('utf-8'), bcrypt.gensalt())

            # Insert new user with hashed password
            my_cursor.execute(
                "INSERT INTO register (fname, lname, contact, email, security_q, security_a, pasword) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security_q.get(),
                    self.var_security_a.get(),
                    hashed_password.decode('utf-8')  # Store the hashed password as a string
                )
            )

            conn.commit()
            conn.close()
            messagebox.showinfo("Success!", "Registered Successfully.", parent=self.root)

            # Clear form after successful registration
            self.clear_fields()

        except mysql.connector.Error as e:
            messagebox.showerror("Error!", f"Database Error: {str(e)}.", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error!", f"Unexpected Error: {str(e)}.", parent=self.root)

    def clear_fields(self):
        """Resets all input fields after successful registration."""
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_security_q.set("Select")
        self.var_security_a.set("")
        self.var_password.set("")
        self.var_cpassword.set("")
        self.var_check.set(0)

    def login_now(self):
        from login import Login_Window
        self.root.withdraw()  
        login_win = Toplevel(self.root)
        Login_Window(login_win)

if __name__ == "__main__":
    root = Tk()
    Register(root)
    root.mainloop()
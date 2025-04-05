from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x900+0+0")
        self.root.title("Face Recognition System")

        #------------- Variables------------
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendnance = StringVar()

        # First Image
        img_top = Image.open(r"college_images\smart-attendance.jpg")
        img_top = img_top.resize((650, 170))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=650, height=170)

        # Second Image
        img1 = Image.open(r"college_images\iStock-182059956_18390_t12.jpg")
        img1 = img1.resize((650, 170))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=650, y=0, width=650, height=170)

        img3 = Image.open(r"college_images\background.jpeg")
        img3 = img3.resize((1280, 550))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Background Image
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=170, width=1280, height=550)

        title_lbl = Label(bg_img, text="ATTENDNANCE MANAGEMENT SYSTEM" , font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1280, height=40)

        # Main Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=7, y=45, width=1266, height=475)

        # left frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("times new roman", 12, "bold"))
        Left_frame.place(x=4, width=625, height=469)

        img_left = Image.open(r"college_images\face-recognition.png")
        img_left = img_left.resize((615, 150))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=2, width=616, height=150)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=155, width=612, height=285)

        # Attendance id
        attendanceId_label = Label(left_inside_frame, text="Attendance Id:", font=("times new roman", 11, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame, width=19, textvariable=self.var_atten_id,  font=("times new roman", 11, "bold"))  
        attendanceId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Roll No
        roll_label = Label(left_inside_frame, text="Roll No:", font=("times new roman", 11, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        atten_roll = ttk.Entry(left_inside_frame, width=19, textvariable=self.var_atten_roll, font=("times new roman", 11, "bold"))
        atten_roll.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Name
        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 11, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        atten_name = ttk.Entry(left_inside_frame, width=19, textvariable=self.var_atten_name, font=("times new roman", 11, "bold"))  
        atten_name.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Department
        dep_label = Label(left_inside_frame, text="Department:", font=("times new roman", 11, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        atten_dep = ttk.Entry(left_inside_frame, width=19, textvariable=self.var_atten_dep, font=("times new roman", 11, "bold"))
        atten_dep.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Time
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 11, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        atten_time = ttk.Entry(left_inside_frame, width=19, textvariable=self.var_atten_time, font=("times new roman", 11, "bold"))  
        atten_time.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # Date
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 11, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        atten_date = ttk.Entry(left_inside_frame, width=19, textvariable=self.var_atten_date, font=("times new roman", 11, "bold"))  
        atten_date.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Attendance
        attendance_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 11, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, width=17, textvariable=self.var_atten_attendnance, font=("times new roman", 11, "bold"), state="readonly")
        self.atten_status["values"] = ["Status", "Present", "Absent"]
        self.atten_status.grid(row=3, column=1, pady=5)
        self.atten_status.current(0)

        # Buttons Frame
        btn_frame = Frame(left_inside_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=3, y=170, width=600, height=70)

        import_btn = Button(btn_frame, text="Import Csv", command=self.importCsv,  width=30, font=("times new roman", 13, "bold"), bg="darkblue", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export Csv", command=self.exportCsv,  width=30, font=("times new roman", 13, "bold"), bg="darkblue", fg="white")
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", width=30, font=("times new roman", 13, "bold"), bg="darkblue", fg="white")
        update_btn.grid(row=1, column=0)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=30, font=("times new roman", 13, "bold"), bg="darkblue", fg="white")
        reset_btn.grid(row=1, column=1)

        # Right frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=635, width=625, height=469)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE) 
        table_frame.place(x=5, y=5, width=610, height=430) 

        #-----------------Scroll bar table-------------------
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance Id")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Nname")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name", width=150)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    #------------------Fetch Data--------------
    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)
    
    # Import csv
    def importCsv(self):
        global mydata
        mydata.clear()  # Clear the list before importing new data

        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(), 
            title="Open CSV", 
            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), 
            parent=self.root
        )

        if not fln:  # Check if the user selected a file
            messagebox.showwarning("Warning!", "No file selected!", parent=self.root)
            return

        try:
            with open(fln, newline="") as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    if i:  # Ensure no empty lines are added
                        mydata.append(i)
            
            if mydata:
                self.fetch_data(mydata)
                messagebox.showinfo("Success!", "CSV Data Imported Successfully!", parent=self.root)
            else:
                messagebox.showwarning("Warning!", "CSV file is empty!", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error!", f"Failed to load CSV file.\n{str(e)}", parent=self.root)

    # Export csv
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data!", "No data found to export.", parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(), 
                title="Open CSV", 
                filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), 
                parent=self.root
            )
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported!", "Your data exported to" + os.path.basename(fln) + "successfully.")
        except Exception as es:
            messagebox.showerror("Error!", f"Due to :{str(es)}", parent = self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']

        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendnance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("") 
        self.var_atten_roll.set("") 
        self.var_atten_name.set("") 
        self.var_atten_dep.set("") 
        self.var_atten_time.set("") 
        self.var_atten_date.set("") 
        self.var_atten_attendnance.set("") 

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
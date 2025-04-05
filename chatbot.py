from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x600+0+0")
        self.root.bind("<Return>", self.enter_func)
        self.root.title("Face Recognition System")

        main_frame = Frame(self.root, bd=3, bg="powder blue", width=590)
        main_frame.pack()

        img_chat = Image.open(r"college_images\chat.jpg")
        img_chat = img_chat.resize((200, 70))
        self.photoimg = ImageTk.PhotoImage(img_chat)

        img_chat_label = Label(main_frame, bd=2, relief=RAISED, anchor="nw", width=730, compound=LEFT, image=self.photoimg, text="CHAT ME", font=('arial', 25, "bold"), fg="green", bg="white")
        img_chat_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('arial', 14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, bd=3, bg="white", width=600)
        btn_frame.pack()

        label = Label(btn_frame, text="Type Something:", font=('arial', 12, "bold"), fg="green", bg="white")
        label.grid(row=0, column=0, padx=2, sticky=W)

        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame, width=40, textvariable=self.entry, font=('times new roman', 15, "bold"))
        self.entry1.grid(row=0, column=1, padx=2, sticky=W)

        self.send = Button(btn_frame, text="Send", command=self.send, font=("arial", 12, "bold"), width=8, bg="green", fg="white")
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear = Button(btn_frame, text="Clear Data", command=self.clear, font=("arial", 12, "bold"), width=10, bg="red", fg="white")
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ""
        self.label_1 = Label(btn_frame, text=self.msg, font=('arial', 12, "bold"), fg="red", bg="white")
        self.label_1.grid(row=1, column=1, padx=50, sticky=W)

    #-------------------Function Declaration-------------
    def enter_func(self, event):
        self.send.invoke()
        self.entry.set("")
        
    def clear(self):
        self.text.delete("1.0", END)
        self.entry.set("")
        
    def send(self):
        send = "\t\t\t\t" + "You: " + self.entry.get()
        self.text.insert(END, "\n" + send)
        self.text.yview(END)

        if (self.entry.get() == ""):
            self.msg = "Please, enter some input."
            self.label_1.config(text=self.msg, fg="red")
        
        else:
            self.msg = ""
            self.label_1.config(text=self.msg, fg="red")

        if (self.entry.get() == "Hello"):
            self.text.insert(END, "\n\n" + "Bot: Hi")

        elif (self.entry.get() == "Hi"):
            self.text.insert(END, "\n\n" + "Bot: Hello")        

        elif (self.entry.get() == "How are you?"):
            self.text.insert(END, "\n\n" + "Bot: Fine & you")  

        elif (self.entry.get() == "Fantastic"):
            self.text.insert(END, "\n\n" + "Bot: Nice to hear")

        elif (self.entry.get() == "Who created you?"):
            self.text.insert(END, "\n\n" + "Bot: Debidutta did with using python.")  

        elif (self.entry.get() == "What's your name?"):
            self.text.insert(END, "\n\n" + "Bot: Mr.Talkie")  

        elif (self.entry.get() == "Can you speak Odia?"):
            self.text.insert(END, "\n\n" + "Bot: I'm still learning it...")    

        elif (self.entry.get() == "What's machine learning?"):
            self.text.insert(END, "\n\n" + "Bot: Machine learning is a branch of \nartificial intelligence (AI) that enables \ncomputers to learn from data and \nimprove their performance over time \nwithout being explicitly programmed. \nInstead of following predefined rules, \nmachine learning algorithms identify \npatterns in data and use those patterns \nto make predictions or decisions.")   

        elif (self.entry.get() == "How does face recognition work?"):
            self.text.insert(END, "\n\n" + "Bot: Machine learning is a branch of \nartificial intelligence (AI) that enables \ncomputers to learn from data and \nimprove their performance over time \nwithout being explicitly programmed. \nInstead of following predefined rules, \nmachine learning algorithms identify \npatterns in data and use those patterns \nto make predictions or decisions.") 

        elif (self.entry.get() == "How does facial recognition work step by step?"):
            self.text.insert(END, "\n\n" + "Bot: Machine learning is a branch of \nartificial intelligence (AI) that enables \ncomputers to learn from data and \nimprove their performance over time \nwithout being explicitly programmed. \nInstead of following predefined rules, \nmachine learning algorithms identify \npatterns in data and use those patterns \nto make predictions or decisions.")

        elif (self.entry.get() == "How many countries use facial recognition?"):
            self.text.insert(END, "\n\n" + "Bot: Machine learning is a branch of \nartificial intelligence (AI) that enables \ncomputers to learn from data and \nimprove their performance over time \nwithout being explicitly programmed. \nInstead of following predefined rules, \nmachine learning algorithms identify \npatterns in data and use those patterns \nto make predictions or decisions.")   

        elif (self.entry.get() == "What's python programming?"):
            self.text.insert(END, "\n\n" + "Bot: Machine learning is a branch of \nartificial intelligence (AI) that enables \ncomputers to learn from data and \nimprove their performance over time \nwithout being explicitly programmed. \nInstead of following predefined rules, \nmachine learning algorithms identify \npatterns in data and use those patterns \nto make predictions or decisions.") 

        elif (self.entry.get() == "What's chatbot?"):
            self.text.insert(END, "\n\n" + "Bot: Machine learning is a branch of \nartificial intelligence (AI) that enables \ncomputers to learn from data and \nimprove their performance over time \nwithout being explicitly programmed. \nInstead of following predefined rules, \nmachine learning algorithms identify \npatterns in data and use those patterns \nto make predictions or decisions.")     

        elif (self.entry.get() == "Bye"):
            self.text.insert(END, "\n\n" + "Bot: Thank you for Chatting...") 

        else:
            self.text.insert(END, "\n\n" + "Bot: Sorry! I didn't get it.")        

if __name__ == "__main__":
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
'''Algorithm
1. make a classes with different object and use init method
2. making a button frame to open different pages
3. interconnecting each other with the help of buttons made in button frame
4. importing DbConnections from back_end.connection and importing Student from model.model_class to ren the registration and records page
5. importing Image Tk from PIL to add picture in tkinter
6. using linear search to search the name from the records
7. used exceptional handling to fetch and search the data ni records portion
8. importing ttk from tkinter to scroll make the combobox in registration page
9. importing messagebox from tkinter to display the message and warning when needed.
'''

from tkinter import *
from PIL import ImageTk, Image
from model.model_class import Student
from back_end.connection import DbConnection
from tkinter import messagebox
from tkinter import ttk
def linear_search(record, Name):
    for i in record:
        print(i)
        if i == Name:
            return True
    return False
class web_design():
    def __init__(self,image):
        self.wn=window
        self.wn.title('Web Design')
        self.wn.geometry('1500x700')
        self.wn.canvas = Canvas(self.wn, width=5000, height=1000)

def home():
    class Home():
        def __init__(self,image):
            self.wn = window
            self.wn.title("HOME PAGE")
            self.wn.geometry('1500x700')
            self.wn.canvas = Canvas(self.wn, width=5000, height=1000)

    window = Toplevel()
    Home(window)
    # ====================canvas in window=====================================
    canvas = Canvas(window, width=1565, height=1000)
    # ====================lbl_heading in window=====================================
    lbl_heading = Label(window, text='💝 𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓣𝓸: 💝', bd=5, bg="#4682B4", font=('arial', 30, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    lbl_heading = Label(window, text='🎀  𝒢𝑅𝒜𝐹𝐹𝐼𝒯𝐼 𝐿𝐸𝒜𝑅𝒩𝐼𝒩𝒢 𝒞𝐸𝒩𝒯𝐸𝑅  🎀  ', bd=5, bg="#4682B4",
                        font=('arial', 30, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    image = ImageTk.PhotoImage(Image.open("D:\\PycharmProjects\\my web page\\g3.jpg"))
    canvas.create_image(0, 0, anchor=NW, image=image)
    canvas.pack()
    window.mainloop()

def Registration():
    class Rose():
        def __init__(self, image):
            self.wn = window
            self.wn.title('Web Design')
            self.wn.geometry('1500x700')
            self.wn.canvas = Canvas(self.wn, width=5000, height=1000)

    def Redis():
        class Main_Interface():
            def __init__(self, root):
                self.wn = root
                self.wn.title('Sample Application')
                self.wn.geometry('400x550')
                self.wn.configure(bg='#FFD39B')

                heading = Label(self.wn, text='My Sample Appication', bd=5, bg="#FFD39B", font=('arial', 15, 'bold'))
                heading.pack(side=TOP, fill=X)

                lbl_heading = Label(self.wn, text='Please add 𝐂𝐢𝐭𝐢𝐳𝐞𝐧𝐬𝐡𝐢𝐩 𝐈𝐃 𝐍𝐮𝐦𝐛𝐞𝐫 in ID box ',
                                    bd=5,
                                    bg="#92C7C7", font=('arial', 15, 'bold'))
                lbl_heading.pack(side=TOP, fill=X)
                lbl_heading = Label(self.wn, text='Please write DOB in DD/MM/YY format ', bd=5, bg="red",
                                    font=('arial', 15, 'bold'))
                lbl_heading.pack(side=TOP, fill=X)

                # ==================making the object of connection===================================
                self.dbconnect = DbConnection()
                # ==================Frame in window===================================
                main_frame = Frame(self.wn, bg='#76EEC6')
                main_frame.place(x=30, y=107, width=330, height=360)

                btn_frame = Frame(self.wn, bg='#FF4040', bd=5)
                btn_frame.place(x=30, y=460, width=330, height=50)
                # ==================widget in main frame==================================
                lbl_ID = Label(main_frame, text='ID', font=('arial', 15, 'bold'), width=8, bg='#76EEC6')
                lbl_ID.grid(row=0, column=0, padx=10, pady=10)
                self.ent_ID = Entry(main_frame)
                self.ent_ID.grid(row=0, column=1, padx=10, pady=10)

                lbl_Name = Label(main_frame, text='Name', font=('arial', 15, 'bold'), width=8, bg='#76EEC6')
                lbl_Name.grid(row=1, column=0, padx=10, pady=10)
                self.ent_Name = Entry(main_frame)
                self.ent_Name.grid(row=1, column=1, padx=10, pady=10)

                lbl_Address = Label(main_frame, text='Address', font=('arial', 15, 'bold'), width=8, bg='#76EEC6')
                lbl_Address.grid(row=2, column=0, padx=10, pady=10)
                self.ent_Address = Entry(main_frame)
                self.ent_Address.grid(row=2, column=1, padx=10, pady=10)

                lbl_DOB = Label(main_frame, text='DOB', font=('arial', 15, 'bold'), width=8, bg='#76EEC6')
                lbl_DOB.grid(row=3, column=0, padx=10, pady=10)
                self.ent_DOB = Entry(main_frame)
                self.ent_DOB.grid(row=3, column=1, padx=10, pady=10)

                lbl_Gender = Label(main_frame, text="Gender", font=("arial", 15, 'bold'), width=8, bg='#76EEC6')
                lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
                self.combo_Gender = ttk.Combobox(main_frame, font=("times new roman", 13), width=12, state='readonly')
                self.combo_Gender['values'] = ("Male", "Female", "Other")
                self.combo_Gender.grid(row=4, column=1, padx=20, )

                lbl_Contact = Label(main_frame, text='Contacts', font=('arial', 15, 'bold'), width=8, bg='#76EEC6')
                lbl_Contact.grid(row=5, column=0, padx=10, pady=10)
                self.ent_Contact = Entry(main_frame)
                self.ent_Contact.grid(row=5, column=1, padx=10, pady=10)

                lbl_Email = Label(main_frame, text='Email', font=('arial', 15, 'bold'), width=8, bg='#76EEC6')
                lbl_Email.grid(row=6, column=0, padx=10, pady=10)
                self.ent_Email = Entry(main_frame)
                self.ent_Email.grid(row=6, column=1, padx=10, pady=10)

                # ==================buttons in button frame==================================
                btn_add = Button(btn_frame, text='Add', bg='#FF7256', font=('arial', 12, 'bold'), command=self.add)
                btn_add.pack(side=LEFT, padx=60, pady=5)

                btn_clear = Button(btn_frame, text='Clear', bg='#FF7256', font=('arial', 12, 'bold'),
                                   command=self.clear)
                btn_clear.pack(side=LEFT, padx=10, pady=5)

            # ==================Defining Add and Clear Button==================================
            def add(self):
                stu_ref = Student(self.ent_ID.get(), self.ent_Name.get(), self.ent_Address.get(), self.ent_DOB.get(),
                                  self.combo_Gender.get(), self.ent_Contact.get(), self.ent_Email.get())
                query = 'insert into learners values(%s,%s,%s,%s,%s,%s,%s);'
                values = (
                    int(stu_ref.get_ID()), stu_ref.get_Name(), stu_ref.get_Address(), stu_ref.get_DOB(),
                    stu_ref.get_Gender(),
                    stu_ref.get_Contact(), stu_ref.get_Email())
                self.dbconnect.insert(query, values)
                messagebox.showinfo("Success", "Data inserted sucessfully")

            def clear(self):
                self.ent_ID.delete(0, END)
                self.ent_Name.delete(0, END)
                self.ent_Address.delete(0, END)
                self.ent_DOB.delete(0, END)
                self.combo_Gender.delete(0, END)
                self.ent_Contact.delete(0, END)
                self.ent_Email.delete(0, END)

        root = Toplevel()
        Main_Interface(root)
    def records():
        class Window:
            def __init__(self, master):
                self.master = master
                self.master.title("Administration Login System")
                self.master.geometry('1350x750+0+0')
                self.master.config(bg='#4B0082')
                self.frame = Frame(self.master, bg='#4B0082')
                self.frame.pack()

                self.Username = StringVar()
                self.Password = StringVar()

                self.lblTitle = Label(self.frame, text='𝓛𝓔𝓐𝓡𝓝𝓔𝓡𝓢 𝓜𝓐𝓝𝓐𝓖𝓔𝓜𝓔𝓝𝓣 𝓢𝓨𝓢𝓣𝓔𝓜', font=('arial', 50, 'bold'),bg='#4B0082',fg='white')
                self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40,padx=10)
                # =========================================================================================================
                self.LoginFrame1 = LabelFrame(self.frame, width=1350, height=600, font=('arial', 20, 'bold'),relief='ridge', bg='#BA55D3', bd=20)
                self.LoginFrame1.grid(row=1, column=0,padx=300)
                self.LoginFrame2 = LabelFrame(self.frame, width=1350, height=600, font=('arial', 20, 'bold'),relief='ridge',bg='#BA55D3', bd=20)
                self.LoginFrame2.grid(row=2, column=0)
                self.LoginFrame3 = LabelFrame(self.frame, width=1350, height=600, font=('arial', 20, 'bold'),relief='ridge',bg='#483D8B', bd=20)
                self.LoginFrame3.grid(row=3, column=0,)

                # =================================Label and Entry=================================================================

                self.lblUsername = Label(self.LoginFrame1, text='Username', font=('arial', 20, 'bold'), bd=22,bg='#BA55D3',fg='Cornsilk')
                self.lblUsername.grid(row=0, column=0)
                self.txtUsername = Entry(self.LoginFrame1, font=('arial', 20, 'bold'), textvariable=self.Username)
                self.txtUsername.grid(row=0, column=1)

                self.lblPassword = Label(self.LoginFrame1, text='Password', font=('arial', 20, 'bold'), bd=22,bg='#BA55D3',fg='Cornsilk')
                self.lblPassword.grid(row=1, column=0)
                self.txtPassword = Entry(self.LoginFrame1, font=('arial', 20, 'bold'), show='*',textvariable=self.Password)
                self.txtPassword.grid(row=1, column=1)
                self.lblNote=Label(self.LoginFrame3,text='Please use Username=learners and Password=12345 to login',font=('arial',30, 'bold'),
                                         bg='#483D8B',fg='black')
                self.lblNote.grid(row=4, column=0)

                # =======================================Buttons========================================================================
                self.btnLogin = Button(self.LoginFrame2, text='Login', width=17, font=('arial', 20, 'bold'),
                                       command=self.Login_System)
                self.btnLogin.grid(row=3, column=0, pady=20, padx=0)

                self.btnReset = Button(self.LoginFrame2, text='Reset', width=17, font=('arial', 20, 'bold'),
                                       command=self.Reset)
                self.btnReset.grid(row=3, column=1, pady=20, padx=0)

                # =========================================Buttons====================

            def Login_System(self):
                u = (self.Username.get())
                p = (self.Password.get())

                if (u == str("learners") and p == str(12345)):
                    messagebox.showinfo("Login Success", "Login is successfull view records")
                    __call__ = self.records()

                else:
                    messagebox.showinfo("Login Error", "Invalid login details, Please! add valid details")
                    self.Username.set("")
                    self.Password.set("")
                    self.txtUsername.focus()

            def Reset(self):
                self.Username.set("")
                self.Password.set("")
                self.txtUsername.focus()

            def records(self):
                class Teacher():
                    def __init__(self, root):
                        self.root = root
                        self.root.title("Show Record")
                        self.root.geometry("1350x700+0+0")
                        self.root.configure(bg='sky blue')
                        title = Label(self.root, text='Records Of Learners', bd=10, relief=GROOVE,
                                      font=("times new roman", 40, 'bold'), bg='cyan')
                        title.pack(side=TOP, fill=X)

                        # ====================connection object=====================================
                        self.dbconnect = DbConnection()

                        self.ent_ID = StringVar()
                        self.ent_Name = StringVar()
                        self.ent_Address = StringVar()
                        self.ent_DOB = StringVar()
                        self.combo_Gender = StringVar()
                        self.ent_Contact = StringVar()
                        self.ent_Email = StringVar()

                        self.search_by = StringVar()
                        self.search_txt = StringVar()

                        # ====================Detail frame in window=====================================
                        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='magenta')
                        Detail_Frame.place(x=300, y=100, width=800, height=580)
                        # ====================Widget in Detail frame=====================================
                        lbl_search = Label(Detail_Frame, text="Search By Full Name", bg="magenta", fg="black",font=("times new roman", 20, 'bold'))
                        lbl_search.grid(row=0, column=0, pady=10, padx=5, sticky="w")
                        self.txt_Search = Entry(Detail_Frame, textvariable=self.search_txt, width=15,font=("times new roman", 14, 'bold'),
                                                bd=5,relief=GROOVE)
                        self.txt_Search.grid(row=0, column=2, pady=10, padx=5, sticky="w")
                        # ====================Buttons in Detail Frame=====================================
                        Searchbtn = Button(Detail_Frame, text='Search', width=15, pady=5,command=self.search_data).grid(row=0,column=3,
                                                                                                                        padx=1,pady=10)
                        Showallbtn = Button(Detail_Frame, text='Show All', width=15, pady=5,command=self.fetch_data).grid(row=0,column=4,
                                                                                                                          padx=1,pady=10)
                        upd_del = Button(Detail_Frame, text='Delete/Update', width=15, pady=5,command=self.upd_del).grid(row=0,column=5,
                                                                                                                         padx=1,pady=6)
                        # ====================Table frame in window=====================================
                        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg='magenta')
                        Table_Frame.place(x=10, y=70, width=760, height=500)

                        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
                        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
                        self.Test_Table = ttk.Treeview(Table_Frame,
                                                       columns=("ID", "Name", "Address", "DOB", "Gender", "Contact", "Email"),
                                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
                        scroll_x.pack(side=BOTTOM, fill=X)
                        scroll_y.pack(side=RIGHT, fill=Y)
                        scroll_x.config(command=self.Test_Table.xview)
                        scroll_y.config(command=self.Test_Table.yview)
                        self.Test_Table.heading("ID", text="ID")
                        self.Test_Table.heading("Name", text="Name")
                        self.Test_Table.heading("Address", text="Address")
                        self.Test_Table.heading("DOB", text="DOB")
                        self.Test_Table.heading("Gender", text="Gender")
                        self.Test_Table.heading("Contact", text="Contacts")
                        self.Test_Table.heading("Email", text="Email")
                        self.Test_Table['show'] = 'headings'
                        self.Test_Table.column("ID", width=100)
                        self.Test_Table.column("Name", width=100)
                        self.Test_Table.column("Address", width=100)
                        self.Test_Table.column("DOB", width=100)
                        self.Test_Table.column("Gender", width=100)
                        self.Test_Table.column("Contact", width=100)
                        self.Test_Table.column("Email", width=150)
                        self.Test_Table.pack(fill=BOTH, expand=1)
                        self.fetch_data()

                    def fetch_data(self):
                        query = "select * from learners;"
                        records = self.dbconnect.select(query)

                        if len(records) != 0:
                            self.Test_Table.delete(*self.Test_Table.get_children())
                            for row in records:
                                self.Test_Table.insert('', END, values=row)

                    def search_data(self):
                        if self.txt_Search.get() == "":
                            messagebox.showinfo("Error", "Searching information required")
                        else:
                            query = "select * from learners where Name=%s;"
                            values = (self.txt_Search.get(),)
                            records = self.dbconnect.search(query, values)
                            list = []
                            for row in records:
                                list.append(row[1])
                            if not linear_search(list, self.txt_Search.get()):
                                messagebox.showinfo("Error", "This Name doesnot exist")
                            elif len(records) != 0:
                                self.Test_Table.delete(*self.Test_Table.get_children())
                                for row in records:
                                    self.Test_Table.insert('', END, values=row)

                    def upd_del(self):
                        class Main_Interface():
                            def __init__(self, root):
                                self.wn = root
                                self.wn.title('Sample Application')
                                self.wn.geometry('400x550')
                                self.wn.configure(bg='#FFD39B')

                                heading = Label(self.wn, text='My Sample Appication', bd=5, bg="#FFD39B",
                                                font=('arial', 15, 'bold'))
                                heading.pack(side=TOP, fill=X)

                                lbl_heading = Label(self.wn,
                                                    text='Please add 𝐂𝐢𝐭𝐢𝐳𝐞𝐧𝐬𝐡𝐢𝐩 𝐈𝐃 𝐍𝐮𝐦𝐛𝐞𝐫 in ID box ',
                                                    bd=5,
                                                    bg="#92C7C7", font=('arial', 15, 'bold'))
                                lbl_heading.pack(side=TOP, fill=X)
                                lbl_heading = Label(self.wn, text='Please write DOB in DD/MM/YY format ', bd=5,
                                                    bg="red",
                                                    font=('arial', 15, 'bold'))
                                lbl_heading.pack(side=TOP, fill=X)

                                # ==================making the object of connection===================================
                                self.dbconnect = DbConnection()
                                # ==================Frame in window===================================
                                main_frame = Frame(self.wn, bg='#76EEC6')
                                main_frame.place(x=30, y=107, width=330, height=360)

                                btn_frame = Frame(self.wn, bg='#FF4040', bd=5)
                                btn_frame.place(x=30, y=460, width=330, height=50)
                                # ==================widget in main frame==================================
                                lbl_ID = Label(main_frame, text='ID', font=('arial', 15, 'bold'), width=8, bg='#76EEC6')
                                lbl_ID.grid(row=0, column=0, padx=10, pady=10)
                                self.ent_ID = Entry(main_frame)
                                self.ent_ID.grid(row=0, column=1, padx=10, pady=10)

                                lbl_Name = Label(main_frame, text='Name', font=('arial', 15, 'bold'), width=8,bg='#76EEC6')
                                lbl_Name.grid(row=1, column=0, padx=10, pady=10)
                                self.ent_Name = Entry(main_frame)
                                self.ent_Name.grid(row=1, column=1, padx=10, pady=10)

                                lbl_Address = Label(main_frame, text='Address', font=('arial', 15, 'bold'), width=8,bg='#76EEC6')
                                lbl_Address.grid(row=2, column=0, padx=10, pady=10)
                                self.ent_Address = Entry(main_frame)
                                self.ent_Address.grid(row=2, column=1, padx=10, pady=10)

                                lbl_DOB = Label(main_frame, text='DOB', font=('arial', 15, 'bold'), width=8,bg='#76EEC6')
                                lbl_DOB.grid(row=3, column=0, padx=10, pady=10)
                                self.ent_DOB = Entry(main_frame)
                                self.ent_DOB.grid(row=3, column=1, padx=10, pady=10)

                                lbl_Gender = Label(main_frame, text="Gender", font=("arial", 15, 'bold'), width=8,bg='#76EEC6')
                                lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
                                self.combo_Gender = ttk.Combobox(main_frame, font=("times new roman", 13), width=12,state='readonly')
                                self.combo_Gender['values'] = ("Male", "Female", "Other")
                                self.combo_Gender.grid(row=4, column=1, padx=20, )

                                lbl_Contact = Label(main_frame, text='Contacts', font=('arial', 15, 'bold'), width=8,bg='#76EEC6')
                                lbl_Contact.grid(row=5, column=0, padx=10, pady=10)
                                self.ent_Contact = Entry(main_frame)
                                self.ent_Contact.grid(row=5, column=1, padx=10, pady=10)

                                lbl_Email = Label(main_frame, text='Email', font=('arial', 15, 'bold'), width=8,bg='#76EEC6')
                                lbl_Email.grid(row=6, column=0, padx=10, pady=10)
                                self.ent_Email = Entry(main_frame)
                                self.ent_Email.grid(row=6, column=1, padx=10, pady=10)

                                # ==================buttons in button frame==================================
                                btn_update = Button(btn_frame, text='Update', bg='#FF7256', font=('arial', 12, 'bold'),command=self.update)
                                btn_update.pack(side=LEFT, padx=20, pady=5)

                                btn_delete = Button(btn_frame, text='Delete', bg='#FF7256', font=('arial', 12, 'bold'),command=self.delete)
                                btn_delete.pack(side=LEFT, padx=20, pady=5)

                                btn_clear = Button(btn_frame, text='Clear', bg='#FF7256', font=('arial', 12, 'bold'),command=self.clear)
                                btn_clear.pack(side=LEFT, padx=20, pady=5)

                            def update(self):
                                stu_ref = Student(self.ent_ID.get(), self.ent_Name.get(), self.ent_Address.get(),self.ent_DOB.get(),
                                                  self.combo_Gender.get(), self.ent_Contact.get(), self.ent_Email.get())
                                query = 'update learners set Name=%s,Address=%s,DOB=%s,Gender=%s,Contact=%s,Email=%s where ID=%s;'
                                values = (stu_ref.get_Name(), stu_ref.get_Address(), stu_ref.get_DOB(), stu_ref.get_Gender(),
                                          stu_ref.get_Contact(), stu_ref.get_Email(), int(stu_ref.get_ID()))
                                self.dbconnect.update(query, values)
                                messagebox.showinfo("Success", "Data updated sucessfully")

                            def clear(self):
                                self.ent_ID.delete(0, END)
                                self.ent_Name.delete(0, END)
                                self.ent_Address.delete(0, END)
                                self.ent_DOB.delete(0, END)
                                self.combo_Gender.delete(0, END)
                                self.ent_Contact.delete(0, END)
                                self.ent_Email.delete(0, END)

                            def delete(self):
                                stu_ref = Student(self.ent_ID.get(), self.ent_Name.get(), self.ent_Address.get(),
                                                  self.ent_DOB.get(),
                                                  self.combo_Gender.get(), self.ent_Contact.get(), self.ent_Email.get())
                                query = 'delete from learners where ID=%s;'
                                values = (int(stu_ref.get_ID()),)
                                self.dbconnect.delete(query, values)
                                messagebox.showinfo("Success", "Data deleted sucessfully")

                        root = Tk()
                        Main_Interface(root)

                root = Tk()
                Teacher(root)

        if __name__ == '__main__':
            root = Toplevel()
            Window(root)
    window = Toplevel()
    object=Rose(window)
    canvas = Canvas(window, width=1565, height=1000)
    lbl_heading = Label(window, text='🎀 𝓦𝓔𝓛𝓒𝓞𝓜𝓔 𝓣𝓞 𝓡𝓔𝓖𝓘𝓢𝓣𝓡𝓐𝓣𝓘𝓞𝓝 𝓐𝓝𝓓 𝓣𝓗𝓔 𝓡𝓔𝓒𝓞𝓡𝓓 𝓟𝓐𝓖𝓔 🎀', bd=5, bg="grey",font=('arial', 30, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    btn_frame = Frame(window, width=1565, bd=5, bg="black")
    btn_frame.place(y=200, x=500)
    btn_signup = Button(btn_frame, text='Registration Page',fg='white',font=('arial', 20, 'bold'), width=20, bg="black",
                        command=Redis)
    btn_signup.pack(side=TOP)
    btn_services = Button(btn_frame, text='Login to View Records',fg='white', font=('arial', 20, 'bold'), width=20, bg="black",
                          command=records)
    btn_services.pack(side=TOP, pady=5)
    image = ImageTk.PhotoImage(Image.open("D:\\PycharmProjects\\my web page\\as.jpg"))
    canvas.create_image(0, 0, anchor=NW, image=image)
    canvas.pack()
    window.mainloop()
def Services():
    class Home():
        def __init__(self,image):
            self.wn = window
            self.wn.title("OUR SERVICES")
            self.wn.geometry('1500x700')
            self.wn.canvas = Canvas(self.wn, width=5000, height=1000)

    window = Toplevel()
    Home(window)
    # ====================canvas in window=====================================
    canvas = Canvas(window, width=1565, height=1000)
    # ====================lbl_heading in window=====================================
    lbl_heading = Label(window, text='💝 𝓞𝓤𝓡 𝓢𝓔𝓡𝓥𝓘𝓒𝓔𝓢 💝', bd=5, bg="#4682B4", font=('arial', 50, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    lbl_heading = Label(window, text='🎀 𝓦𝓔 𝓟𝓡𝓞𝓥𝓘𝓓𝓔 𝓓𝓘𝓕𝓕𝓡𝓔𝓝𝓣 𝓜𝓐𝓣𝓔𝓡𝓘𝓐𝓛𝓢 𝓣𝓞 𝓗𝓔𝓛𝓟 𝓛𝓔𝓐𝓡𝓝𝓔𝓡𝓢 𝓣𝓞 𝓜𝓐𝓚𝓔 𝓖𝓡𝓐𝓕𝓕𝓘𝓣𝓘 🎀 ', bd=5,
                        bg="#4682B4",font=('arial',25, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    image = ImageTk.PhotoImage(Image.open("D:\\PycharmProjects\\my web page\\1.jpg"))
    canvas.create_image(0, 0, anchor=NW, image=image)
    canvas.pack()
    window.mainloop()
def Contact_Us():
    class Home():
        def __init__(self,image):
            self.wn = window
            self.wn.title("OUR SERVICES")
            self.wn.geometry('1500x700')
            self.wn.canvas = Canvas(self.wn, width=5000, height=1000)

    window = Toplevel()
    Home(window)
    # ====================canvas in window=====================================
    canvas = Canvas(window, width=1565, height=1000)
    # ====================lbl_heading in window=====================================
    lbl_heading = Label(window, text='💝 ✴𝓒𝓞𝓝𝓣𝓐𝓒𝓣 𝓤𝓢✴ 💝', bd=5, bg="#3BB9FF", font=('arial',30,'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    lbl_heading = Label(window, text='🌺 𝓒𝓞𝓝𝓣𝓐𝓒𝓣 𝓓𝓔𝓣𝓐𝓘𝓛𝓢 𝓕𝓞𝓡 𝓐𝓝𝓨 𝓠𝓤𝓔𝓡𝓘𝓔𝓢 🌺', bd=5, bg="#3BB9FF",font=('arial',25, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    image = ImageTk.PhotoImage(Image.open("D:\\PycharmProjects\\my web page\\12.jpg"))
    canvas.create_image(0, 0, anchor=NW, image=image)
    canvas.pack()
    window.mainloop()
window=Tk()
web_design(window)
canvas = Canvas(window, width=1565, height=1000)
lbl_heading = Label(window, text='🎀  𝒢𝑅𝒜𝐹𝐹𝐼𝒯𝐼 𝐿𝐸𝒜𝑅𝒩𝐼𝒩𝒢 𝒞𝐸𝒩𝒯𝐸𝑅  🎀 ', bd=5, bg="grey", font=('arial', 30, 'bold'))
lbl_heading.pack(side=TOP, fill=X)
lbl_heading = Label(window, text='𝒦𝒶𝓉𝒽𝓂𝒶𝓃𝒹𝓊,𝒩𝑒𝓅𝒶𝓁 ', bd=5, bg="grey", font=('arial', 24, 'bold'))
lbl_heading.pack(side=TOP, fill=X)
btn_frame = Frame(window, width=1565, bd=5, bg="grey", height=50)
btn_frame.place(y=100)
btn_home = Button(btn_frame, text='Home Page', font=('arial', 20, 'bold'), width=20, bg="grey",command=home)
btn_home.pack(side=LEFT)
btn_signup = Button(btn_frame, text='Registration Page', font=('arial', 20, 'bold'), width=20, bg="grey",command=Registration)
btn_signup.pack(side=LEFT)
btn_services = Button(btn_frame, text='Our Services', font=('arial', 20, 'bold'), width=20, bg="grey",command=Services)
btn_services.pack(side=RIGHT)
btn_ContactUs = Button(btn_frame, text='Contact Us', font=('arial', 20, 'bold'), width=20, bg="grey",command=Contact_Us)
btn_ContactUs.pack(side=RIGHT)
image = ImageTk.PhotoImage(Image.open("D:\\PycharmProjects\\my web page\\Capture.png"))
canvas.create_image(0,0, anchor=NW, image=image)
canvas.pack()
window.mainloop()



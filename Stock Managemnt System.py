'''
Importing Required Modules,
To Install Used Modules:
In CMD - 1. pip install tkinter
'''

from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

import tempfile
import win32api
import win32print

'''
Defining size of tkinter window------------------------------------------------------------
'''

root = Tk()
root.title("Stock Management System")

width = 1000
height = 520

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="SteelBlue")

'''
Defining Required Variables------------------------------------------------------------------
'''
USERNAME = StringVar()
PASSWORD = StringVar()
PRODUCT_NAME = StringVar()
PRODUCT_PRICE = IntVar()
PRODUCT_QTY = IntVar()
PRODUCT_ID = StringVar()
PRODUCT_NAME1 = StringVar()
PRODUCT_PRICE1 = IntVar()
PRODUCT_QTY1 = IntVar()
PRODUCT_ID1 = StringVar()
SEARCH = StringVar()

'''
Defining Required Function------------------------------------------------------------
'''
def Database():

    #Function For Database Connectivity

    global conn, cursor #Making conn,cursor a globle variable

    conn = sqlite3.connect("pythontut.db")#connecting to database

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY  NOT NULL, product_name TEXT, product_qty INTEGER, product_price INTEGER)")
#=====================================================================================================


def Exit():

    #Function To Get Pop Up A Exit Window

    result = tkMessageBox.askquestion('Stock Manegement System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

    else:
        tkMessageBox.showinfo('Return','You will now return to the application screen')

#=====================================================================================================


def ShowLoginForm():

    #Function For Creating A Login Window

    global loginform
    loginform = Toplevel()
    loginform.title("Stock Manegement System/Account Login")

    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))

    LoginForm()

#=====================================================================================================

def ShowLogForm():

    #Function For Creating A Signin Window

    global logform
    logform = Toplevel()
    logform.title("Stock Manegement System/Account SignUp")

    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    logform.resizable(0, 0)
    logform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LogForm()

#=====================================================================================================

def LoginForm():

    #Costumising login window

    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)

    lbl_text = Label(TopLoginForm, text="Administrator Login", font=('arial', 25), width=600)
    lbl_text.pack(fill=X)

    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)

    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=0)

    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=1)

    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)

    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 18), width=15)
    username.grid(row=0, column=1)

    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 18), width=15, show="*")
    password.grid(row=1, column=1)

    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)

#=====================================================================================================

def LogForm():

    #Costumising signin window

    global lbl_result
    TopLogForm = Frame(logform, width=600, height=100, bd=1, relief=SOLID)
    TopLogForm.pack(side=TOP, pady=20)

    lbl_text = Label(TopLogForm, text="Administrator Sign Up", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)

    MidLogForm = Frame(logform, width=600)
    MidLogForm.pack(side=TOP, pady=50)

    lbl_username = Label(MidLogForm, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=0)

    lbl_password = Label(MidLogForm, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=1)

    lbl_result = Label(MidLogForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)

    username = Entry(MidLogForm, textvariable=USERNAME, font=('arial', 18), width=15)
    username.grid(row=0, column=1)

    password = Entry(MidLogForm, textvariable=PASSWORD, font=('arial', 18), width=15, show="*")
    password.grid(row=1, column=1)

    btn_login = Button(MidLogForm, text="Register", font=('arial', 18), width=30 , command=Signin)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)

#=====================================================================================================

def Home():

    #Creating A After Login Home Window

    global Home
    Home = Tk()
    Home.title("Stock Manegement System/Home")

    width = 1024
    height = 520
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)

    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)

    lbl_display = Label(Title, text='''STOCK MANEGEMENT
SYSTEM''', font=('impact',45 ),fg = 'DarkBlue', bg = 'AliceBlue')
    lbl_display.pack()

    #Creating Menu Bar

    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)#1st File Menu
    filemenu2 = Menu(menubar, tearoff=0)#2nd File Menu

    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="About", command=About)
    filemenu.add_command(label="Exit", command=Exit)

    filemenu2.add_command(label="Add new", command=ShowAddNew)
    filemenu2.add_command(label="View", command=ShowView)

    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Stock", menu=filemenu2)

    Home.config(menu=menubar)
    Home.config(bg="SteelBlue")

    #----------------------------Creating Buttons-------------------------
    b22 = Button(Home,text = 'About',font=('Arial', 14),fg = 'DarkBlue', bg = 'AliceBlue', height = 3, width = 12, command=About)
    b22.pack(side = LEFT)

    b11 = Button(Home,text = 'Logout',font=('Arial', 14),fg = 'DarkBlue', bg = 'AliceBlue', height = 3, width = 12, command=Logout)
    b11.pack(side = RIGHT)

    b55 = Button(Home,text = 'Exit',font=('Arial', 18),fg = 'DarkBlue', bg = 'AliceBlue', height = 3, width = 12, command=Exit)
    b55.pack(side = BOTTOM)

    b33 = Button(Home,text = 'View',font=('Arial', 18),fg = 'DarkBlue', bg = 'AliceBlue', height = 3, width = 12, command=ShowView)
    b33.pack(side = BOTTOM)

    b44 = Button(Home,text = 'Add New',font=('Arial', 18),fg = 'DarkBlue', bg = 'AliceBlue', height = 3, width = 12, command=ShowAddNew)
    b44.pack(side = BOTTOM)

#=====================================================================================================

def ShowAddNew():

    #Creating Add New Item Window

    global addnewform
    addnewform = Toplevel()
    addnewform.title("Stock Manegement System/Add new")

    width = 600
    height = 500

    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()

#=====================================================================================================

def AddNewForm():

    #Costmising Add New Window

    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)

    lbl_text = Label(TopAddNew, text="Add New Product", font=('arial', 25), width=600)
    lbl_text.pack(fill=X)

    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)

    lbl_productid = Label(MidAddNew, text="Product ID:", font=('arial', 18), bd=10)
    lbl_productid.grid(row=0, sticky=W)

    lbl_productname = Label(MidAddNew, text="Product Name:", font=('arial', 18), bd=10)
    lbl_productname.grid(row=1, sticky=W)

    lbl_qty = Label(MidAddNew, text="Product Quantity:", font=('arial', 18), bd=10)
    lbl_qty.grid(row=2, sticky=W)

    lbl_price = Label(MidAddNew, text="Product Price:", font=('arial', 18), bd=10)
    lbl_price.grid(row=3, sticky=W)

    productid = Entry(MidAddNew, textvariable=PRODUCT_ID, font=('arial', 18), width=15)
    productid.grid(row=0, column=1)

    productname = Entry(MidAddNew, textvariable=PRODUCT_NAME, font=('arial', 18), width=15)
    productname.grid(row=1, column=1)

    productqty = Entry(MidAddNew, textvariable=PRODUCT_QTY, font=('arial', 18), width=15)
    productqty.grid(row=2, column=1)

    productprice = Entry(MidAddNew, textvariable=PRODUCT_PRICE, font=('arial', 18), width=15)
    productprice.grid(row=3, column=1)

    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNew)
    btn_add.grid(row=4, columnspan=2, pady=20)

#=====================================================================================================

def AddNew():

    #Adding Entered Item To Database

    Database()#Calling database
    cursor.execute("INSERT INTO `product` (product_id,product_name, product_qty, product_price) VALUES(?,?, ?, ?)", (int(PRODUCT_ID.get()), str(PRODUCT_NAME.get()), int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get())))
    conn.commit()

    PRODUCT_ID.set("")
    PRODUCT_NAME.set("")
    PRODUCT_PRICE.set("")
    PRODUCT_QTY.set("")

    cursor.close()
    conn.close()

#=====================================================================================================

def ShowView():

    #Customising ViewForm

    global viewform
    viewform = Toplevel()
    viewform.title("Stock Mangement System/View Product")

    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()

#=====================================================================================================

def ViewForm():

    #Creating A View Item Window

    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)

    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)

    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)

    lbl_text = Label(TopViewForm, text="View Products", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)

    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)

    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)

    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_update = Button(LeftViewForm, text="Update", command=ShowUpdate)
    btn_update.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_print = Button(LeftViewForm, text="Print", command=print)
    btn_print.pack(side=TOP, padx=10, pady=10, fill=X)

    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)

    tree = ttk.Treeview(MidViewForm, columns=("ProductID", "Product Name", "Product Qty", "Product Price"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('ProductID', text="ProductID",anchor=W)
    tree.heading('Product Name', text="Product Name",anchor=W)
    tree.heading('Product Qty', text="Product Qty",anchor=W)
    tree.heading('Product Price', text="Product Price",anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=110)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=130)

    tree.pack()
    DisplayData()

#=====================================================================================================

def DisplayData():

    # To Display Data In View Item Window

    Database()

    c = cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()

    for data in fetch:
        tree.insert('', 'end', values=(data))

    cursor.close()
    conn.close()

#=====================================================================================================

def Search():

    # To Search Something In View Item Window

    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()

        cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()

        for data in fetch:
            tree.insert('', 'end', values=(data))

        cursor.close()
        conn.close()

#=====================================================================================================

def Reset():

    # To Reset Search Window

    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")

#=====================================================================================================

def Delete():

    #To Delete Any Item

    if not tree.selection():
       print("ERROR")

    else:
        result = tkMessageBox.askquestion('Stock Manegement System', 'Are you sure you want to delete this record?', icon="warning")

        if result == 'yes':

            curItem = tree.focus()
            contents =(tree.item(curItem))

            selecteditem = contents['values']
            tree.delete(curItem)

            Database()

            cursor.execute("DELETE FROM `product` WHERE `product_id` = %d" % selecteditem[0])

            conn.commit()
            cursor.close()
            conn.close()

#=====================================================================================================

def print():

    # To print the stock details
    Database()

    cr = cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    filename = tempfile.mktemp (".txt")
    f = open (filename, "w")

    for data in fetch:
        f.write (str(data))

    win32api.ShellExecute (
    0,
    "print",
    filename,
    #
    # If this is None, the default printer will
    # be used anyway.
    #
    '/d:"%s"' % win32print.GetDefaultPrinter (),
    ".",
    0
    )


    cursor.close()
    conn.close()


#=====================================================================================================

def ShowUpdate():

    #Creating Add New Item Wingow

    global updateform

    updateform = Toplevel()
    updateform.title("Stock Manegement System/Add new")

    width = 600
    height = 500

    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    updateform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    updateform.resizable(0, 0)
    UpdateForm()
#=====================================================================================================

def UpdateForm():

    #Costmising Update Window


    TopUpdate = Frame(updateform, width=600, height=100, bd=1, relief=SOLID)
    TopUpdate.pack(side=TOP, pady=20)

    lbl_text = Label(TopUpdate, text="Update Product", font=('arial', 25), width=600)
    lbl_text.pack(fill=X)

    MidUpdate = Frame(updateform, width=600)

    MidUpdate.pack(side=TOP, pady=50)

    lbl_productid = Label(MidUpdate, text="Product ID:", font=('arial', 18), bd=10)
    lbl_productid.grid(row=0, sticky=W)

    lbl_productname = Label(MidUpdate, text="Product Name:", font=('arial', 18), bd=10)
    lbl_productname.grid(row=1, sticky=W)

    lbl_qty = Label(MidUpdate, text="Product Quantity:", font=('arial', 18), bd=10)
    lbl_qty.grid(row=2, sticky=W)

    lbl_price = Label(MidUpdate, text="Product Price:", font=('arial', 18), bd=10)
    lbl_price.grid(row=3, sticky=W)

    productid = Entry(MidUpdate, textvariable=PRODUCT_ID1, font=('arial', 18), width=15)
    productid.grid(row=0, column=1)

    productname = Entry(MidUpdate, textvariable=PRODUCT_NAME1, font=('arial', 18), width=15)
    productname.grid(row=1, column=1)

    productqty = Entry(MidUpdate, textvariable=PRODUCT_QTY1, font=('arial', 18), width=15)
    productqty.grid(row=2, column=1)

    productprice = Entry(MidUpdate, textvariable=PRODUCT_PRICE1, font=('arial', 18), width=15)
    productprice.grid(row=3, column=1)

    btn_add = Button(MidUpdate, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=Update)
    btn_add.grid(row=4, columnspan=2, pady=20)

#=====================================================================================================

def Update():

    #Adding Entered Item To Database

    Database()#Calling database

    cursor.execute('UPDATE  product SET PRODUCT_QTY=?,PRODUCT_PRICE=? WHERE PRODUCT_ID=? AND PRODUCT_NAME=?', (int(PRODUCT_QTY1.get()), int(PRODUCT_PRICE1.get()), str(PRODUCT_ID1.get()), str(PRODUCT_NAME1.get())))
    conn.commit()

    PRODUCT_ID1.set("")
    PRODUCT_NAME1.set("")
    PRODUCT_PRICE1.set("")
    PRODUCT_QTY1.set("")

    cursor.close()
    conn.close()
#=====================================================================================================

def Logout():

    #To Logout from the window

    result = tkMessageBox.askquestion('Stock Mangement System', 'Are you sure you want to logout?', icon="warning")

    if result == 'yes':
        admin_id = ""
        root.deiconify()
        Home.destroy()

#=====================================================================================================

def Login(event=None):

    #To login to the window

    global admin_id
    Database()

    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")

    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))

        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()

            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")

            lbl_result.config(text="Logged In",fg = "Green")
            ShowHome()

        else:
            lbl_result.config(text="Invalid Usename or password",fg = 'red')
            USERNAME.set("")
            PASSWORD.set("")

    cursor.close()
    conn.close()

#=====================================================================================================

def Signin(event=None):

    #To Register to window

    global admin_id
    Database()

    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")

    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",(USERNAME.get(), PASSWORD.get()))

        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `admin` (username, password) VALUES( ?, ?)",(USERNAME.get(), PASSWORD.get()))


            conn.commit()
            data = cursor.fetchone()
            lbl_result.config(text="Signed in", fg = 'green')
            Showlog()

        else:
            lbl_result.config(text="User Already Exist",fg = 'red')
            USERNAME.set("")
            PASSWORD.set("")

    cursor.close()
    conn.close()

#=====================================================================================================

def ShowHome():

    # To Directly Switch to home if logged in

    root.withdraw()
    Home()
    loginform.destroy()

#=====================================================================================================

def Showlog():

    # To Directly Switch to login if signed in

    root.withdraw()
    ShowLoginForm()
    logform.destroy()

#=====================================================================================================

def About():

    #To show About window

    root = Tk()
    root.title("About")

    text1 = Text(root, height = 24, width = 90)
    text1.config(state="normal")
    text1.insert(INSERT,'''
•Technologies used    - Python 3.6.
			Python SQLite3 Database
            Python Tkinter GUI

•Language used – Python

•Applications Of The Software –
    o	Following Software can be use to manage stock, print the stock details.
•Features :-
    o	This software provides many features like
        i.	Adding The Items
        ii.	Searching For A Item
        iii.	Deleting any item from stock.
        iv.	Updating the items
        v.	Printing the stock details

•Hardware specifications :-
    o	Windows- 7/8/8.1/10 (32/64 bit)
    o	Minimum ram required – 2 GB
''')
    text1.config(state='disabled')
    text1.pack()

    root.mainloop()

#===============================MENUBAR WIDGETS==================================

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Login", command=ShowLoginForm)
filemenu.add_command(label="Sign Up", command=ShowLogForm)
filemenu.add_command(label="About", command=About)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="Menu", menu=filemenu)
root.config(menu=menubar)

#=======================================Buttons============================

b1 = Button(root,text = 'Login',font=('Arial', 16),fg = 'DarkBlue', bg = 'AliceBlue', height = 3, width = 12, command=ShowLoginForm)
b1.pack(side = LEFT, padx=65, pady=65)
b2 = Button(root,text = 'Register',font=('Arial', 16),fg = 'DarkBlue', bg = 'AliceBlue', height = 3, width = 12, command=ShowLogForm)
b2.pack(side = RIGHT, padx=65, pady=65)
b4 = Button(root,text = 'Exit',font=('Arial', 16),fg = 'DarkBlue', bg = 'AliceBlue', height = 3, width = 12, command=Exit)
b4.pack(side = BOTTOM)
b3 = Button(root,text = 'About',font=('Arial', 16),fg = 'DarkBlue', bg = 'AliceBlue', height = 3, width = 12, command=About)
b3.pack(side = BOTTOM)


#========================================FRAME============================================

Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

#========================================LABEL WIDGET=====================================

lbl_display = Label(Title, text='''STOCK MANEGEMENT
SYSTEM''', font=('Impact', 40),fg = 'DarkBlue', bg = 'AliceBlue')
lbl_display.pack()

#========================================INITIALIZATION===================================

if __name__ == '__main__':
    root.mainloop()

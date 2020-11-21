from tkinter import *
from GetData import *
from tkinter import messagebox

def call_func():
    try:
        get_data(stock_name.get(),file_name.get())
        start(file_name.get())
    except:
        messagebox.showerror("Error","Invalid Stock Name")
        root1.destroy()
        menu()
        return
    root1.destroy()
    menu()

#urls = ["YESBANK.NS","HDFCBANK.BO","SBIN.NS","BANDHANBNK.NS","ICICIBANK.NS","AXISBANK.NS"]

def adjustWindow(window):
    w = 600  # width for the window size
    h = 600  # height for the window size
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)  # calculate x and y coordinates for the Tk window
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    window.resizable(False, False)  # disabling the resize option for the window
    # window.configure(background='#174873') # making the background white of the window


# validate the entry data and makes a new entry into the database


def menu():
    global root1
    # global s
    root1 = Tk()
    adjustWindow(root1)
    Label(root1, text="Stock Screener", width="500", height="2", font=("Calibri", 22, 'bold'), fg='white',
          bg='green').pack()
    global stock_name
    global file_name
    stock_name = StringVar()
    file_name = StringVar()

    Label(root1, text='Enter Stock Name : ').place(x=100, y=150)
    Entry(root1, textvariable=stock_name).place(x=250, y=150)

    Label(root1, text='Enter File Name : ').place(x=100, y=250)
    Entry(root1, textvariable=file_name).place(x=250, y=250)


    Button(root1, text='Fetch', fg="blue",command = call_func).place(x=250, y=350)

    root1.bind('<Return>', lambda event=None: call_func())
    root1.bind('<Escape>', lambda event=None: root1.destroy())
    root1.mainloop()


menu()
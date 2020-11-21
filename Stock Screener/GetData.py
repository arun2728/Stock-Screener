import requests
import urllib.request
from bs4 import BeautifulSoup
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)  # Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np


def _quit():
    root.quit()  # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


def start(name):
    global root
    root = Tk()
    root.wm_title("Embedding in Tk")
    file = name+".csv"
    df = pd.read_csv(file)
    l = df['Adj Close**']
    fig = Figure(figsize=(5, 4), dpi=100)
    print(l)
    # t = np.arange(0, 3, .01)
    fig.add_subplot(111).plot(l)

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack()

    # canvas.mpl_connect("key_press_event", on_key_press)

    button = Button(master=root, text="Quit", command=root.destroy)
    button.pack()
    root.bind('<Return>', lambda event=None: root.destroy())

    root.mainloop()
    # If you put root.destroy() here, it will cause an error if the window is
    # closed with the window manager.




def get_data(url, name):
    url = "https://finance.yahoo.com/quote/" + url + "/history?period1=1514764800&period2=1585353600&interval=1wk&filter=history&frequency=1wk"
    response = requests.get(url)
    print(name + " Stock")
    soup = BeautifulSoup(response.text, 'html.parser')
    heading = soup.findAll('tr', {'class': "C($tertiaryColor) Fz(xs) Ta(end)"})
    heading = heading[0]
    heading = heading.findAll('th')
    heads = []
    for i in heading:
        heads.append(i.text)
    stock = []
    stock_data = soup.find_all('tr', {'class': "BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"})
    for tr in stock_data:
        stocks = []
        for td in tr:
            for j in td:
                for k in j:
                    a = k
                    k = str(k)
                    lists = [" ", "-", ":", '/']
                    if k in lists or ':' in k:
                        continue
                    if k[0].isalpha():
                        stocks.append(k)
                    else:
                        try:
                            index = k.index('.')
                            k = k[0:index]
                        except:
                            print("", end="")
                        k = k.split(',')
                        s = ""
                        for m in k:
                            s += m
                        k = s
                        if int(k) < 10:
                            continue
                        stocks.append(int(k))

        if len(stocks) != 7:
            continue
        stock.append(stocks)

    stock = stock[::-1]
    file = name + ".csv"
    with open(file, 'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(heads)
        for i in stock:
            writer.writerow(i)



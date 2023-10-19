import sys
from tkinter import *
import threading
import time
from PIL import Image, ImageTk

auto1 = False
auto2 = False
auto3 = False
auto4 = False
auto5 = False
buy_auto = False
buy_auto2 = False
buy_auto3 = False
buy_auto4 = False
buy_auto5 = False
cookies = 0
mulitipler = 1
oldlady = 0
farming = 0
mineing = 0
working = 0
banking = 0
window = Tk()
window.title('cookie')
window.geometry("1920x1080")
sys.setrecursionlimit(1000000)


def thing():
    global cookies, my_button, mulitipler
    
   
    print("cookies =",cookies)
    cookies = cookies + 1 * mulitipler  
    my_button.config(text=(f'your cookies: {cookies:,}'))

def close_tri():
    global tri
    tri.destroy()

def close_new():
    global new, my_button, amount_multilper
    new.destroy()
    my_button.config(text=(f'your cookies: {cookies:,}'))
    amount_multilper.config(text=(f'cookie mulitipler: {mulitipler:,}'))
    
def close_win():
    window.destroy()

def gran():
    global  cookies, mulitipler, my_button5, oldlady
    if cookies >= 100:
        oldlady = oldlady + 1
        cookies = cookies - 100
        mulitipler = mulitipler + 1
        my_button5.config(text=(f'old ladys: {oldlady}'))
    else:
        my_button5.config(text=(f'old ladys: {oldlady}'))

def farmer():
    global  cookies, mulitipler, my_button7, farming
    if cookies >= 10000:
        farming = farming + 1
        cookies = cookies - 10000
        mulitipler = mulitipler + 100
        my_button7.config(text=(f'farmers: {farming}'))
    else:
        my_button7.config(text=(f'farmers: {farming}'))

def miner():
    global  cookies, mulitipler, my_button8, mineing

    if cookies >= 1000000:
        mineing = mineing + 1
        cookies = cookies - 1000000
        mulitipler = mulitipler + 10000
        my_button8.config(text=(f'miners: {mineing}'))
    else:
        my_button8.config(text=(f'miners: {mineing}'))

def worker():
    global cookies, mulitipler, my_button9, working

    if cookies >= 100000000:
        working = working + 1
        cookies = cookies - 100000000
        mulitipler = mulitipler + 1000000
        my_button9.config(text=(f'workers: {working}'))
    else:
        my_button9.config(text=(f'workers: {working}'))

def banker():
    global cookies, mulitipler, my_button16, banking

    if cookies >= 10000000000:
        banking = banking + 1
        cookies = cookies - 10000000000
        mulitipler = mulitipler + 100000000
        my_button16.config(text=(f'bankers: {banking}'))
    else:
        my_button16.config(text=(f'bankers: {banking}'))



def setting():
    global tri
    tri = Toplevel(window)
    tri.title('setting')
    tri.geometry("1920x1080")

    list_prices = Label(tri, font=('rockwell',50))
    list_prices.config(text=(f'''
      old ladys = 100 cookies + 1 mulitipler
              farmers = 10,000 cookies +  100 mulitipler
                      miners = 1,000,000 cookies + 10,000 mulitipler
                                 workers = 100,000,000 cookies + 1,000,000 mulitipler
                                    bankers = 10,000,000 cookies + 100,000,000 mulitipler

auto clicker 1 = 1000 cookies + 2s
     auto clicker 2 = 100,000 cookies + 1s
                                    auto clicker 3 = 10,000,000 cookies + 0.5s                      
                     auto clicker 4 = 1,000,000,000 cookies + 0.25s
                                        auto clicker 5 = 100,000,000,000 cookies + 0.125s             
    '''))
    # list_prices.pack(pady=20)
    list_prices.place(x=-640, y=0)

    clicker11 = PhotoImage(file='N:\\Custom Office Templates\\first year\\html\\cross.png')
    img_label = Label(image=clicker11)
    my_button11 = Button(tri, image=clicker11, borderwidth=0, command=close_tri)
    my_button11.pack(pady=20)
    my_button11.place(x=1650, y=0)

    mainloop()


def shop():
    global new, my_button5, my_button6, my_button7, my_button8, my_button9, my_button12, my_button13, my_button14, my_button15, my_button16, oldlady
    new = Toplevel(window)
    new.title('shop')
    new.geometry("1920x1080")


    clicker3 = PhotoImage(file='N:\\Custom Office Templates\\first year\\html\\cross.png')
    img_label = Label(image=clicker3)
    my_button3 = Button(new, image=clicker3, borderwidth=0, command=close_new, compound='top')
    my_button3.pack(pady=20)
    
    im3 = Image.open("N:\\Custom Office Templates\\first year\\html\\granny.png")
    im3 = im3.resize((100, 100))
    clicker4 = ImageTk.PhotoImage(im3)
    img_label = Label(image=clicker4)
    my_button5 = Button(new, image=clicker4, font=('rockwell',50), borderwidth=0, command=gran, compound='left')
    my_button5.pack(pady=20)
    my_button5.place(x=50, y=0)
    my_button5.config(text=(f'old ladys: {oldlady}'))
    
    im6 = Image.open("N:\\Custom Office Templates\\first year\\html\\mouse.png")
    im6 = im6.resize((100, 100))
    clicker6 = ImageTk.PhotoImage(im6)
    img_label = Label(image=clicker6)
    my_button6 = Button(new, image=clicker6, font=('rockwell',30), borderwidth=0, command=start_clicker, compound='left')
    my_button6.pack(pady=20)
    my_button6.place(x=1200, y=0)

    im7 = Image.open("N:\\Custom Office Templates\\first year\\html\\farm.png")
    im7 = im7.resize((100, 100))
    clicker7 = ImageTk.PhotoImage(im7)
    img_label = Label(image=clicker7)
    my_button7 = Button(new, image=clicker7, font=('rockwell',50), borderwidth=0, command=farmer, compound='left')
    my_button7.pack(pady=20)
    my_button7.place(x=50, y=200)
    my_button7.config(text=(f'farmers: {farming}'))

    im8 = Image.open("N:\\Custom Office Templates\\first year\\html\\mine.png")
    im8 = im8.resize((100, 100))
    clicker8 = ImageTk.PhotoImage(im8)
    img_label = Label(image=clicker8)
    my_button8 = Button(new, image=clicker8, font=('rockwell',50), borderwidth=0, command=miner, compound='left')
    my_button8.pack(pady=20)
    my_button8.place(x=50, y=400)
    my_button8.config(text=(f'miners: {mineing}'))
    
    im9 = Image.open("N:\\Custom Office Templates\\first year\\html\\factory.png")
    im9 = im9.resize((100, 100))
    clicker9 = ImageTk.PhotoImage(im9)
    img_label = Label(image=clicker9)
    my_button9 = Button(new, image=clicker9, font=('rockwell',50), borderwidth=0, command=worker, compound='left')
    my_button9.pack(pady=20)
    my_button9.place(x=50, y=600)
    my_button9.config(text=(f'workers: {working}'))
    
    im12 = Image.open("N:\\Custom Office Templates\\first year\\html\\mouse2.png")
    im12 = im12.resize((100, 100))
    clicker12 = ImageTk.PhotoImage(im12)
    img_label = Label(image=clicker12)
    my_button12 = Button(new, image=clicker12, font=('rockwell',30), borderwidth=0, command=start_clicker2, compound='left')
    my_button12.pack(pady=20)
    my_button12.place(x=1200, y=200)

    im13 = Image.open("N:\\Custom Office Templates\\first year\\html\\mouse3.png")
    im13 = im13.resize((100, 100))
    clicker13 = ImageTk.PhotoImage(im13)
    img_label = Label(image=clicker13)
    my_button13 = Button(new, image=clicker13, font=('rockwell',30), borderwidth=0, command=start_clicker3, compound='left')
    my_button13.pack(pady=20)
    my_button13.place(x=1200, y=400)

    im14 = Image.open("N:\\Custom Office Templates\\first year\\html\\mouse4.png")
    im14 = im14.resize((100, 100))
    clicker14 = ImageTk.PhotoImage(im14)
    img_label = Label(image=clicker14)
    my_button14 = Button(new, image=clicker14, font=('rockwell',30), borderwidth=0, command=start_clicker4, compound='left')
    my_button14.pack(pady=20)
    my_button14.place(x=1200, y=600)

    im15 = Image.open("N:\\Custom Office Templates\\first year\\html\\mouse5.png")
    im15 = im15.resize((100, 100))
    clicker15 = ImageTk.PhotoImage(im15)
    img_label = Label(image=clicker15)
    my_button15 = Button(new, image=clicker15, font=('rockwell',30), borderwidth=0, command=start_clicker5, compound='left')
    my_button15.pack(pady=20)
    my_button15.place(x=1200, y=800)

    im16 = Image.open("N:\\Custom Office Templates\\first year\\html\\bank.png")
    im16 = im16.resize((100, 100))
    clicker16 = ImageTk.PhotoImage(im16)
    img_label = Label(image=clicker16)
    my_button16 = Button(new, image=clicker16, font=('rockwell',50), borderwidth=0, command=banker, compound='left')
    my_button16.pack(pady=20)
    my_button16.place(x=50, y=800)
    my_button16.config(text=(f'bankers: {banking}'))

    mainloop()
  


def the_button():
    global cookies, my_button, amount_multilper
    clicker = PhotoImage(file='N:\\Custom Office Templates\\first year\\html\\cookie.png') 
    img_label = Label(image=clicker)
    #img_label.pack(pady=20)

    my_button = Button(window, image=clicker, font=('rockwell',50), command=thing, borderwidth=0, compound='left')
    my_button.pack(pady=20)
    my_button.place(x=100, y=100)

    #my_label = Label(window, text='')
    #my_button.config(text=cookies)
    #my_label.pack(pady=20)

    im2 = Image.open("N:\\Custom Office Templates\\first year\\html\\shop.png")
    im2 = im2.resize((450, 450))
    clicker2 = ImageTk.PhotoImage(im2)
    img_label = Label(image=clicker2)
    my_button2 = Button(window, image=clicker2, borderwidth=0, command=shop, compound='right')
    my_button2.pack(pady=20)
    my_button2.place(x=50, y=550)
    
    clicker4 = PhotoImage(file='N:\\Custom Office Templates\\first year\\html\\cross.png')
    img_label = Label(image=clicker4)
    my_button4 = Button(window, image=clicker4, borderwidth=0, command=close_win)
    my_button4.pack(pady=20)
    my_button4.place(x=1650, y=0)

    im10 = Image.open("N:\\Custom Office Templates\\first year\\html\\cog.png")
    im10 = im10.resize((300, 300))
    clicker10 = ImageTk.PhotoImage(im10)
    img_label = Label(image=clicker10)
    my_button10 = Button(window, image=clicker10, borderwidth=0, command=setting)
    my_button10.pack(pady=20)
    my_button10.place(x=1600, y=700)

    amount_multilper = Label(window, font=('rockwell',50))
    amount_multilper.config(text=(f'cookie mulitipler: {mulitipler:,}'))
    amount_multilper.pack(pady=20)
    amount_multilper.place(x=0, y=0)


    mainloop()


def auto_clicker():
    global cookies, my_button, mulitipler, auto1, auto2, auto3, auto4, auto5
    while True:
        try:
            my_button
            break
        except NameError:
            pass

    while True:
        if auto1 == True and auto2 == False and auto3 == False and auto4 == False and auto5 == False:
            cookies = cookies + 1 * mulitipler
            my_button.config(text=(f'your cookies: {cookies:,}'))
            time.sleep(2)
        elif auto1 == True and auto2 == True and auto3 == False and auto4 == False and auto5 == False:
            cookies = cookies + 1 * mulitipler
            my_button.config(text=(f'your cookies: {cookies:,}'))
            time.sleep(1)
        elif auto1 == True and auto2 == True and auto3 == True and auto4 == False and auto5 == False:
            cookies = cookies + 1 * mulitipler
            my_button.config(text=(f'your cookies: {cookies:,}'))
            time.sleep(0.5)
        elif auto1 == True and auto2 == True and auto3 == True and auto4 == True and auto5 == False:
            cookies = cookies + 1 * mulitipler
            my_button.config(text=(f'your cookies: {cookies:,}'))
            time.sleep(0.25)
        elif auto1 == True and auto2 == True and auto3 == True and auto4 == True and auto5 == True:
            cookies = cookies + 1 * mulitipler
            my_button.config(text=(f'your cookies: {cookies:,}'))
            time.sleep(0.125)

        



def start_clicker():
    global buy_auto, my_button6, cookies, auto1, auto2
    if cookies >= 1000 and buy_auto == False:
        cookies = cookies - 1000
        my_button6.config(text=(f'you have bought auto clicker'))
        buy_auto = True
        auto1 = True
        t1 = threading.Thread(target=auto_clicker)
        t1.start()
    elif cookies >= 1000 and buy_auto == True:
        my_button6.config(text=(f'you already have auto clicker'))
    elif cookies <= 1000 and buy_auto == True:
        my_button6.config(text=(f'you already have auto clicker'))
    
    else:
        my_button6.config(text=(f'you cant afford auto clicker'))

def start_clicker2():
    global buy_auto2, my_button12, cookies, auto2
    if cookies >= 100000 and buy_auto2 == False:
        cookies = cookies - 100000
        my_button12.config(text=(f'you have bought auto clicker'))
        buy_auto2 = True
        auto2 = True
        t1 = threading.Thread(target=auto_clicker)
        t1.start()
    elif cookies >= 100000 and buy_auto2 == True:
        my_button12.config(text=(f'you already have auto clicker'))
    elif cookies <= 100000 and buy_auto2 == True:
        my_button12.config(text=(f'you already have auto clicker'))
    
    else:
        my_button12.config(text=(f'you cant afford auto clicker'))

def start_clicker3():
    global buy_auto3, my_button13, cookies, auto3
    if cookies >= 10000000 and buy_auto3 == False:
        cookies = cookies - 10000000
        my_button13.config(text=(f'you have bought auto clicker'))
        buy_auto3 = True
        auto3 = True
        t1 = threading.Thread(target=auto_clicker)
        t1.start()
    elif cookies >= 10000000 and buy_auto3 == True:
        my_button13.config(text=(f'you already have auto clicker'))
    elif cookies <= 10000000 and buy_auto3 == True:
        my_button13.config(text=(f'you already have auto clicker'))
    
    else:
        my_button13.config(text=(f'you cant afford auto clicker'))

def start_clicker4():
    global buy_auto4, my_button14, cookies, auto4
    if cookies >= 1000000000 and buy_auto4 == False:
        cookies = cookies - 1000000000
        my_button14.config(text=(f'you have bought auto clicker'))
        buy_auto4 = True
        auto4 = True
        t1 = threading.Thread(target=auto_clicker)
        t1.start()
    elif cookies >= 1000000000 and buy_auto4 == True:
        my_button14.config(text=(f'you already have auto clicker'))
    elif cookies <= 1000000000 and buy_auto4 == True:
        my_button14.config(text=(f'you already have auto clicker'))
    
    else:
        my_button14.config(text=(f'you cant afford auto clicker'))

def start_clicker5():
    global buy_auto5, my_button15, cookies, auto5
    if cookies >= 100000000000 and buy_auto5 == False:
        cookies = cookies - 100000000000
        my_button15.config(text=(f'you have bought auto clicker'))
        buy_auto5 = True
        auto5 = True
        t1 = threading.Thread(target=auto_clicker)
        t1.start()
    elif cookies >= 100000000000 and buy_auto5 == True:
        my_button15.config(text=(f'you already have auto clicker'))
    elif cookies <= 100000000000 and buy_auto5 == True:
        my_button15.config(text=(f'you already have auto clicker'))
    
    else:
        my_button15.config(text=(f'you cant afford auto clicker'))
the_button()
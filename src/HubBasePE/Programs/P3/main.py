from turtle import *
import tkinter as tkr
import time


def run():
    window = tkr.Tk()
    button1 = tkr.Button(window, text="Do not press this button", width=40)
    button1.pack(padx=50, pady=20)
    global clicks1
    clicks1 = 0
    print("Please do not close the window before the turtle finishes!")
    print("It may cause bugs.")

    def VShape(size):
        right(25)
        forward(size)
        backward(size)
        left(50)
        forward(size)
        backward(size)
        right(25)

    def SnowflakeArm(size):
        for Cyc8 in range(4):
            forward(size)
            VShape(size)
        backward(size * 4)

    def Snowflake(size):
        color('white')
        for Cyc7 in range(4):
            SnowflakeArm(size)
            right(90)

    def onClick(event):
        global clicks1
        clicks1 = clicks1 + 1
        shape("turtle")
        speed(10)
        pensize(6)
        Screen().bgcolor("turquoise")
        if clicks1 < 20:
            Snowflake(20)
            if clicks1 < 20:
                button1.pack_forget()
                print("Fail")
                Terminator()
        else:
            button1.configure(text="You outsmarted me!")
            print("Success")
            speed(100000)
            Terminator()
            time.sleep(1)
            button1.pack_forget()
            Terminator()

    button1.bind("<ButtonRelease-1>", onClick)
    window.mainloop()

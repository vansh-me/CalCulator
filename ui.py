import tkinter as tk
import math
expression = ""
window = tk.Tk()
window.title("CALCULATOR")
window.geometry("360x500")
display = tk.Entry(window, font=("Arial", 25), justify="right")
display.pack(fill="x",
             padx=10,
             pady=10)
button_frame = tk.Frame(window)
button_frame.pack(padx=10, pady=10)

buttons = [
    ["C", "√", "÷", "⌫"],
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "%"],
    [".", "0", "x", "="],
]


def button_click(value):
    global expression

    if value == "C":
        expression = ""
        display.delete(0, "end")
    elif value == "=":
        try:
            result = eval(expression)
            display.delete(0, "end")
            display.insert("end", result)
            expression = str(result)
        except:
            display.delete(0, "end")
            display.insert("end", "Error")
            expression = ""
    elif value == "√":
        try:
            expression = str(math.sqrt(float(expression)))

            display.delete(0, "end")
            display.insert("end",
                           expression
                           )
        except:
            expression = ""
            display.delete(0, "end")
            display.insert("end", "Error")

    elif value == "⌫":
        expression = expression[:-1]

        display.delete(0, "end")
        display.insert("end",
                       expression.replace("*", "x").replace("/", "÷")
                       )
    elif value == "%":
        expression = str(float(expression)/100)
        display.delete(0, "end")
        display.insert("end",
                       expression)
    else:
        if value == "x":
            value = "*"
        elif value == "÷":
            value = "/"
        expression += value

        display.delete(0, "end")
        display.insert("end",
                       expression.replace("*", "x").replace("/", "÷")
                       )


for row_index, row in enumerate(buttons):
    for column_index, text in enumerate(row):
        tk.Button(
            button_frame, text=text, width=6, height=4,
            command=lambda value=text:
            button_click(value)
        ).grid(row=row_index,
               column=column_index, padx=3, pady=3)


def key_press(event):
    key = event.char
    if key in "0123456789.+-*/":
        button_click(key)
    elif key == "/":
        button_click("÷")
    elif key == "*":
        button_click("x")
    elif key == "\r":
        button_click("=")
    elif key == "%":
        button_click("%")
    elif key == "\x08":
        button_click("⌫")
    elif key.lower() == "c":
        button_click("c")


window.bind("<Key>", key_press)
window.bind("<Return>", lambda event: button_click("="))
window.bind("<BackSpace>", lambda event: button_click("⌫"))
window.bind("<Escape>", lambda event: button_click("C"))
window.mainloop()

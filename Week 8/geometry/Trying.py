from operator import sub, add, mul, truediv, pow
from tkinter import *
from tkinter import ttk

#Create tkinter GUI:
root = Tk()
root.title("Calculator")

# Creating Entry screen

e = Entry(root, width=35, borderwidt=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Calculating what is in the box
def calculate(s):
    operations = {
        "+": add,
        "-": sub,
        "/": truediv,
        "^": pow,
        "*": mul
    }

    if s.isdigit():
        return float(s)
    for i in operations.keys():
        left, operator, right = s.partition(i)
        if operator in operations:
            if operations[operator](calculate(left), calculate(right))%1 > 0:
                return round(float(operations[operator](calculate(left), calculate(right))), 3)
            else:
                return int(operations[operator](calculate(left), calculate(right)))


# Clicking a button
def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return


# Clear button (deletes all in entry)
def button_clear():
    e.delete(0, END)
    return


# Equal button calculates the entry
def button_calculate():
    global calculation
    calculation = e.get()
    answer = calculate(calculation)
    e.delete(0, END)
    e.insert(0, str(answer))
    return answer


# Delete button deletes the last entry
def button_dell():
    input = str(e.get())
    delete = input[0:-1]
    e.delete(0, END)
    e.insert(0, str(delete))


# Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_click("+"))
button_sub = Button(root, text="-", padx=39, pady=20, command=lambda: button_click("-"))
button_div = Button(root, text="/", padx=39, pady=20, command=lambda: button_click("/"))
button_mul = Button(root, text="*", padx=39, pady=20, command=lambda: button_click("*"))
button_pow = Button(root, text="^", padx=39, pady=20, command=lambda: button_click("^"))
button_parl = Button(root, text="(", padx=39, pady=20, command=lambda: button_click("("))
button_parr = Button(root, text=")", padx=39, pady=20, command=lambda: button_click(")"))
button_del = Button(root, text="DEL", padx=39, pady=20, command=button_dell)
button_equal = Button(root, text="=", padx=39, pady=20, command=button_calculate)
button_clear = Button(root, text="Clear", padx=39, pady=20, command=button_clear)


# Put the buttons on the screen
button_parl.grid(row=1, column=0)
button_parr.grid(row=1, column=1)
button_del.grid(row=1, column=2)
button_clear.grid(row= 1, column=3)

button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)
button_div.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_pow.grid(row=4, column=3)

button_0.grid(row=5, column=1)
button_equal.grid(row=5, column=3)
button_add.grid(row=5, column=2)
button_sub.grid(row=5, column=0)

# Mainloop of the program
root.mainloop()






from tkinter import *

root = Tk()
root.title("Calculator")

ent = Entry(root, width=40, bd=4)
ent.grid(row=0, column=0, columnspan=4)

operand = 0
operator = "+"
buffer = ""
pressedEql = False


def buttonPressed(inp):
    
    if isinstance(inp, int):
        numPressed(inp)
    elif inp == "Clear":
        pressClear()
    elif inp == "=": 
        eqlPressed()
    else:
        opPressed(inp)


def numPressed(num):
    global buffer
    buffer += str(num)
    ent.delete(0, END)
    ent.insert(0, buffer)


def eqlPressed():
    eval()
    global pressedEql
    pressedEql = True


def eval():
    global buffer
    if len(buffer) == 0:
        current = 0
    else: 
        current = int(buffer)
    global operand
    global operator
    try: 
        if (operator == "+"):
            operand += current
        elif (operator == "-"):
            operand -= current
        elif (operator == "*"):
            operand = operand * current
        elif (operator == "/"):
            operand = operand / current
        ent.delete(0, END)
        ent.insert(0, str(operand))
        buffer = ""
        operator = "+"
    except Exception as err:
        ent.delete(0, END)
        ent.insert(0, err)
        pressClear()


def opPressed(op):
    global pressedEql
    global operand
    print("buffer", buffer)
    print("operand", operand)
    print(pressedEql)
    if pressedEql and (buffer):
        print("hello")
        #global operand
        operand = 0
    pressedEql = False
    eval()
    global operator
    operator = op


def pressClear():
    global operand
    global operator
    global buffer
    operand = 0
    operator = "+"
    buffer = ""
    ent.delete(0, END)



#Added all the buttons
buttonx = 40
buttony = 10

button1 = Button(root, text="1", padx=buttonx, pady=buttony, command=lambda: buttonPressed(1))
button2 = Button(root, text="2", padx=buttonx, pady=buttony, command=lambda: buttonPressed(2))
button3 = Button(root, text="3", padx=buttonx, pady=buttony, command=lambda: buttonPressed(3))

button4 = Button(root, text="4", padx=buttonx, pady=buttony, command=lambda: buttonPressed(4))
button5 = Button(root, text="5", padx=buttonx, pady=buttony, command=lambda: buttonPressed(5))
button6 = Button(root, text="6", padx=buttonx, pady=buttony, command=lambda: buttonPressed(6))

button7 = Button(root, text="7", padx=buttonx, pady=buttony, command=lambda: buttonPressed(7))
button8 = Button(root, text="8", padx=buttonx, pady=buttony, command=lambda: buttonPressed(8))
button9 = Button(root, text="9", padx=buttonx, pady=buttony, command=lambda: buttonPressed(9))
button0 = Button(root, text="0", padx=buttonx, pady=buttony, command=lambda: buttonPressed(0))

buttonPlu = Button(root, text="+", padx=buttonx-1, pady=buttony, command=lambda: buttonPressed("+"))
buttonSub = Button(root, text="-", padx=buttonx+1, pady=buttony, command=lambda: buttonPressed("-"))
buttonMul = Button(root, text="*", padx=buttonx+1, pady=buttony, command=lambda: buttonPressed("*"))
buttonDiv = Button(root, text="/", padx=buttonx+1, pady=buttony, command=lambda: buttonPressed("/"))

buttonEql = Button(root, text="=", padx=buttonx-1, pady=buttony, command=lambda: buttonPressed("="))
buttonDot = Button(root, text=".", padx=buttonx+2, pady=buttony)
buttonSign = Button(root, text="+/-", padx=buttonx-6, pady=buttony)

buttonClear = Button(root, text="Clear", padx=buttonx-12, pady=buttony, command=lambda: buttonPressed("Clear"))
buttonCE = Button(root, text="CE", padx=buttonx-4, pady=buttony)
buttonDel = Button(root, text="<-", padx=buttonx-4, pady=buttony)

buttonPer = Button(root, text="%", padx=buttonx-2, pady=buttony)
buttonOneOver = Button(root, text="1/x", padx=buttonx-6, pady=buttony)
buttonSqr = Button(root, text="x^2", padx=buttonx-7, pady=buttony)
buttonSqrt = Button(root, text="sqrt", padx=buttonx-8, pady=buttony)

#Position all the buttons

#first row
buttonPer.grid(row=1, column=0)
buttonCE.grid(row=1, column=1)
buttonClear.grid(row=1, column=2)
buttonDel.grid(row=1, column=3)

#second row
buttonOneOver.grid(row=2, column=0)
buttonSqr.grid(row=2, column=1)
buttonSqrt.grid(row=2, column=2)
buttonDiv.grid(row=2, column=3)

#third row
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
buttonMul.grid(row=3, column=3)

#fourth row
button4.grid(row=4, column=0)
button5.grid(row=4, column=1)
button6.grid(row=4, column=2)
buttonSub.grid(row=4, column=3)

#fifth row
button1.grid(row=5, column=0)
button2.grid(row=5, column=1)
button3.grid(row=5, column=2)
buttonPlu.grid(row=5, column=3)

#sixth row
buttonSign.grid(row=6, column=0)
button0.grid(row=6, column=1)
buttonDot.grid(row=6, column=2)
buttonEql.grid(row=6, column=3)

root.mainloop()

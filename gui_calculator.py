from tkinter import *

#the value in the calculation field, in string format.
expression = "" 

#function that takes as input the value of the pressed button, updates the expression variable with the pressed button, then sets the calculation variable to this expression.
#Bear in mind that expresspion is a string, calculation is a string variable, which is turned to a mathemamatic calculation using eval
def press(num): 
	global expression 

	expression = expression + str(num)
 
	calculation.set(expression) 

#function that evaluates the expression that has been formed, sets the calculation variable to the calculated value, then clears the expression variable
def equalpress(): 

    try: 

        global expression

        total = str(eval(expression))

        calculation.set(total)

        #This makes sure the calculated value stays in the calculator display, and when calculation is set it takes in the calculation 
        expression = str(total) 

    #except clause triggered when expression does not make mathemical sense, and cannot be evaluated with eval
    except: 

        calculation.set(" error ") 
        expression = "" 

#clears both the expression string and the calculation variable
def clear(): 
	global expression 
	expression = "" 
	calculation.set("") 
	

if __name__=='__main__':

    calculator = Tk()

    #sets calculator background to white and changes the window title
    calculator.configure(background='white')
    calculator.title("Calculator v1")
	
    #instantiates the Calculation variable, the value of this variable is calculated with eval, and every time a button is pressed this variable is set to whatever is in the calculator display (the value of the expression variable)
    calculation = StringVar() 

    # By using a PhotoImage, I can set the dimensions of the buttons in pixels instead of text units, by setting the dimensions of pixelVirtual to a 1px square, and the specifying in the Buttons' options how many pixelVirtuals the buttton should be
    pixelVirtual = PhotoImage(width=1, height=1)

    # Grid placement allows me to place the buttons in a 4x5 grid
    # Row values range from 0 to 5
	
    #the text in calculation_field is whatever the textvariable calculation is equal to. We can change the textvariable with calculation.set()
    calculation_field = Entry(calculator, textvariable=calculation)
    calculation_field.grid(row=0, column=0, columnspan=4, ipadx=103, ipady=15)
	
    #button text is silver, button body is black, text font is Helvetica and font size is 20 pixels. compund='c' centres text, command is what is to be executed when button is clicked
    button0 = Button(calculator, text='0', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press(0))
    button0.grid(row=1, column=0)

    button1 = Button(calculator, text='1', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press(1))
    button1.grid(row=1, column=1)

    button2 = Button(calculator, text='2', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press(2))
    button2.grid(row=1, column=2)

    buttonplus = Button(calculator, text='+', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press("+"))
    buttonplus.grid(row=1, column=3)

    button3 = Button(calculator, text='3', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press(3))
    button3.grid(row=2, column=0)

    button4 = Button(calculator, text='4', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press(4))
    button4.grid(row=2, column=1)

    button5 = Button(calculator, text='5', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press(5))
    button5.grid(row=2, column=2)

    buttonminus = Button(calculator, text='-', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press("-"))
    buttonminus.grid(row=2, column=3)

    button6 = Button(calculator, text='6', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press(6))
    button6.grid(row=3, column=0)

    button7 = Button(calculator, text='7', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press(7))
    button7.grid(row=3, column=1)

    button8 = Button(calculator, text='8', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press(8))
    button8.grid(row=3, column=2)

    buttonmult = Button(calculator, text='x', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press("*"))
    buttonmult.grid(row=3, column=3)

    button9 = Button(calculator, text='9', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press(9))
    button9.grid(row=4, column=0)

    buttondp = Button(calculator, text='.', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press("."))
    buttondp.grid(row=4, column=1)

    buttonclr = Button(calculator, text='CLR', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: clear())
    buttonclr.grid(row=4, column=2)

    buttondiv = Button(calculator, text='÷', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=75, image=pixelVirtual, compound="c", command=lambda: press("/"))
    buttondiv.grid(row=4, column=3)

    buttoneq = Button(calculator, text='=', fg='silver', bg='black', font=('Helvetica', -20), height=60, width=325, image=pixelVirtual, compound="c", command=lambda: equalpress())
    buttoneq.grid(row=5, column=0, columnspan=4)


    calculator.mainloop()

from tkinter import *

expression = "" 

def press(num): 
	global expression 

	expression = expression + str(num) 
 
	calculation.set(expression) 


def equalpress(): 

	try: 

		global expression

		total = str(eval(expression)) 

		calculation.set(total) 

		expression = "" 

	except: 

		calculation.set(" error ") 
		expression = "" 


def clear(): 
	global expression 
	expression = "" 
	calculation.set("") 
	

if __name__=='__main__':

    calculator = Tk()

    calculator.configure(background='white')
    calculator.title("Calculator v1")
	
    calculation = StringVar() 

    pixelVirtual = PhotoImage(width=1, height=1)

    calculation_field = Entry(calculator, textvariable=calculation)
    calculation_field.grid(row=0, column=0, columnspan=4, ipadx=103, ipady=15)

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
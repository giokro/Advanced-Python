import tkinter as tk
from quadratic_equation import Quad
	
def compute():
	try:
		a = float(ea.get())
		b = float(eb.get())
		c = float(ec.get())
	except:
		output['text']="Input must be a number"
		return

	func = ""
	func+=str(a)+"x^2 + "+str(b)+"x + "+str(c)
	lfunc['text']=func

	roots = Quad.Quad(a,b,c)

	if(len(roots)==0):
		output['text']="Threre are no roots"
	elif(len(roots)==1):
		output['text']="X = " + str(roots[0])
	else:
		output['text']="X1 = " + str(roots[0]) + ",  X2 = " + str(roots[1])

	

window = tk.Tk()
window.title("Quadratic Equation")
window.geometry('400x400')
window.configure(background="white")


# spc
spc = tk.Label(window, background="white")
spc.pack()


# function label
lfunc = tk.Label(window, background="white", text="ax^2 + bx + c")
lfunc.pack()


# a 	
la = tk.Label(window, background="white", text="a: ")
la.pack()

ea = tk.Entry(window)
ea.pack()


# b
lb = tk.Label(window, background="white", text="b: ")
lb.pack()

eb = tk.Entry(window)
eb.pack()


# c
lc = tk.Label(window, background="white", text="c: ")
lc.pack()

ec = tk.Entry(window)
ec.pack()


# spc
spc = tk.Label(window, background="white")
spc.pack()


# compute btn
compute = tk.Button(window, text="Compute", command=compute)
compute.pack()


# spc
spc = tk.Label(window, background="white")
spc.pack()


# output
output = tk.Label(window, height=100, width=200, background="lightgray")
output.pack()


# this runs the gui or main loop
window.mainloop()




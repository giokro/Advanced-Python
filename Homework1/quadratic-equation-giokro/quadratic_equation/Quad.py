from math import sqrt

def Quad(a, b, c):
	roots = []	

	D = (b*b)-(4*a*c)
	print("D = ", D)
	
	if D>0:
		x1 = (-b + sqrt(D))/(2*a)
		x2 = (-b - sqrt(D))/(2*a)
		print("x1 =", x1, " x2 =", x2)

		roots.append(x1)
		roots.append(x2)
		return roots
		
	elif D==0:
		x = -b/(2*a)
		print("x =", x)

		roots.append(x)
		return roots
	else:
		print("There are no roots")
		return roots


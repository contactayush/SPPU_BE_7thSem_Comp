n=int(input("Enter number of terms to be shown"))

def Fib(n,a,b):
	if(n==1):
		return
	else:
		c=a+b
		print(c)
		Fib(n-1,b,c)

if(n==0):
	print("no series for 0 input")
else:	
	print(0)	
	Fib(n,0,1)


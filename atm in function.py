print("welcome")
print("swipe your card")
def amt(n):
	pin=int(input("enter your pin"))
	if pin ==1234:
		trans = input('Balance enquiry, withdrawal,deposit,quit')
		if trans=="Balance enquiry" :
			print(n)
		elif trans=="withdrawal":
			a=int(input("enter the your amount"))
			n=n-a
			print('take your cash')
			print("Reamaining Balance=",n)
		elif trans=="deposit":
		  	b=int(input("enter the amount"))
		  	n=n+b
		  	print("your total amount=",n)
		elif trans=="quit":
			print("exit")
	else:
		print("pin is wrong")	
n=int(input("enter amount"))
amt(n)
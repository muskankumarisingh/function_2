def password(a):
	i=0
	while len(a)>=6:
		if len(a)<=16:
			if a[i]=="$":
				if a[i]=="2" or a[i]=="8":
					if a[i]=="A" or a[i]=="Z":
						return "strong password hai"
					else:
						return "weak password"
				else:
					return "weak password"
		else:
			return "weak password"
		i+=1
			
a=input("enter strong password")
print(password(a))
#strong password error2345ABCD$
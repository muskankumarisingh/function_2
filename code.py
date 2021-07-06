def max(list):
	j=0
	max=0
	while j<len(list):
		if list[j]>max:
			max=list[j]
		j=j+1
	return max			
def var(e,b):
    c=e+b
    d=max(c)
    return d
def maximum(ele):
	i=0
	e=[ ]
	b=[ ]
	while i<len(ele):
		if ele[i]%2==0:
			e.append(ele[i])
		else:
			b.append(ele[i])
		i=i+1
	print(e)
	print(b)
	final=var(e,b)
	print(final)
ele=[1,12,3,44,3,67,5,78,18,19,22,34,24]
maximum(ele)
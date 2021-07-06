def max(list):
	j=0
	while j<len(list):
		if list[j]>max:
			max=list[j]
			j=j+1
			
def var(l,m):
    c=l+m
    d=max(c)
    return d
def maximum(ele):
    i=0
    l=[]
    m=[]
    while i<len(ele):
        if ele[i]%2==0:
            l.append(ele[i])
        else:
            m.append(ele[i])
        i=i+1
    print(l)
    print(m)
ele=[1,12,3,44,3,67,5,78,18,19,22,34,24]
maximum(ele)

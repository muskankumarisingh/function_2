a=open("my_function.text","w")
list=["muskan","sindhu","shabeera","tanjum","sirisha"]
i=0
while i<len(list):
    a.write(list[i])
    a.write("\n")
    i=i+1
a.close()


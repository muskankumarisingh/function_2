def function(list):
    list=[8,6,4,8,4,50,2,7]
    i=0
    x=list[i]
    while i<len(list):
        if x>list[i]:
            x=list[i]
        i=i+1
    print(x)
function(list)
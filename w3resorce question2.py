# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8, 2, 3, 0, 7)))
def sum(numbers):
    total_sum=0
    i=0
    while i<len(numbers):
        total_sum=total_sum+numbers[i]
        i+=1
    return total_sum
print(sum((8,2,3,0,7)))
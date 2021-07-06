def numbers_less_than_twenty(list):
  counter = 0
  while counter < len(num_list):
    item =num_list[counter]
    if item < 0:
      list.remove(item)
    else:
      counter += 1
  return num_list

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num_list_sub_20 = numbers_less_than_twenty(num_list)
print(num_list_sub_20) 
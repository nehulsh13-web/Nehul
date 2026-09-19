import array as arr
array_num = arr.array('i',[2,5,7,3,4,8,3])
print("Original Array :", array_num)
print("Number of occurance of the number 3 in the given array :" +str(array_num.count(3)))
array_num.reverse()
print("Reverse the order of the items :", array_num)

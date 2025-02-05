import array

arr=array.array('i',[1,2,3])

for i in range(0,3):
    print(arr[i])

#accessing single element
print(arr[1])
#accessing  from  index 1 to 2
print(arr[1:3])
#accessing total 
print(arr[:])
#accessing  total in reverse
print(arr[::-1])
#skiping 2 no in b\w
print(arr[::2])
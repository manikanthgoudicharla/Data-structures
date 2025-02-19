def insertionsort(array):
     for i in range(1,len(array)):
          temp=array[i]
          j=i-1
          while j>=0 and array[j]>temp:
               array[j+1]=array[j]
               j=j-1
          array[j+1]=temp


def printarray(size,array):
     for i in range(0,size):
          print(f"The {i+1} element of the Array:{array[i]}")


size=int(input("Enter the Size of the Array:"))
array=[]

for i in range(0,size):
     element=list(input(f"Enter the {i+1} Element of the Array:"))
     array.append(element)

print("Array Before insertion sort:")
printarray(size,array)

insertionsort(array)

print("Array After insertion sort:")
printarray(size,array)
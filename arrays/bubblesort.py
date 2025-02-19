
def bubblesort(size,array):
     for i in range(0,size):
          for j in range(0,(size-i)-1):
               if(array[j]>array[j+1]):
                    temp=array[j]
                    array[j]=array[j+1]
                    array[j+1]=temp
          

def printarray(size,array):
     for i in range(0,size):
          print(f"The {i+1} element of the Array:{array[i]}")


size=int(input("Enter the Size of the Array:"))
array=[]

for i in range(0,size):
     element=int(input(f"Enter the {i+1} Element of the Array:"))
     array.append(element)

print("Array Before Bubble sort:")
printarray(size,array)

bubblesort(size,array)

print("Array After Bubble sort:")

printarray(size,array)

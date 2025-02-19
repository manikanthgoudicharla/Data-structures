
def selectionsort(array):
    for i in range(len(array)-1):
        minindex=i
        for j in range(i+1,len(array)):
            if array[j] < array[minindex]:
                minindex=j
        if i!=minindex:
            array[i], array[minindex] = array[minindex], array[i]

def printarray(size,array):
     for i in range(0,size):
          print(f"The {i+1} element of the Array:{array[i]}")

size=int(input("Enter the Size of the Array:"))
array=[]

for i in range(0,size):
     element=list(input(f"Enter the {i+1} Element of the Array:"))
     array.append(element)

print("Array Before selection sort:")
printarray(size,array)

selectionsort(array)

print("Array After selection sort:")

printarray(size,array)


 

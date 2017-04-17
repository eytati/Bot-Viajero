def quickSort(lista):
   quickSortHelper(lista, 0, len(lista) - 1)

def quickSortHelper(lista, primero, utlimo):
   if primero<utlimo:

        splitpoint = partition(lista, primero, utlimo)

        quickSortHelper(lista, primero, splitpoint - 1)


        quickSortHelper(lista, splitpoint + 1, utlimo)


def partition(lista, primero, ultimo):
   pivotvalue = lista[primero]

   leftmark = primero + 1
   rightmark = ultimo

   done = False
   while not done:

       while leftmark <= rightmark and lista[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while lista[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = lista[leftmark]
           lista[leftmark] = lista[rightmark]
           lista[rightmark] = temp

   temp = lista[primero]
   lista[primero] = lista[rightmark]
   lista[rightmark] = temp


   return rightmark

lista = [14, 17, 13, 15, 19, 10, 3, 16, 9, 12]
quickSort(lista)
print(lista)
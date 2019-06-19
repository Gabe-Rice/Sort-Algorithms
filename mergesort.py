def mergeSort(my_list):

   if len(my_list) > 1:
       mid = len(my_list) // 2
       leftHalf = my_list[:mid]
       rightHalf = my_list[mid:]

       #recursion
       mergeSort(leftHalf)
       mergeSort(rightHalf)

       i=0
       j=0
       k=0

       while i < len(leftHalf) and j < len(rightHalf):
           if leftHalf[i] < rightHalf[j]:
               my_list[k] = leftHalf[i]
               i=i+1
           else:
               my_list[k] = rightHalf[j]
               j=j+1
           k=k+1

       while i < len(leftHalf):
           my_list[k] = leftHalf[i]
           i=i+1
           k=k+1

       while j < len(rightHalf):
           my_list[k]=rightHalf[j]
           j=j+1
           k=k+1

fOut = open('merge.txt', 'w')
with open('data.txt', 'r') as fIn:
    for line in fIn:
        my_list = [int(num) for num in line.split()]
        size = my_list[0]
        my_list.pop(0)
        mergeSort(my_list)
        refineList = ' '.join(map(str, my_list))
        #print(refineList)
        fOut.write('%s\n' % refineList)

fIn.close()
fOut.close()
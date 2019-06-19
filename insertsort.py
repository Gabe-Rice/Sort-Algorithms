def insertionSort(my_list):
    # for every element in our array
    for i in range(1, len(my_list)):
        current = my_list[i]
    
        while i > 0 and my_list[i-1] > current:
            my_list[i] = my_list[i-1]
            i -= 1

        my_list[i] = current

    return my_list


fOut = open('insert.txt', 'w')
with open('data.txt', 'r') as fIn:
    for line in fIn:
        data = [int(num) for num in line.split()]
        size = data[0]
        data.pop(0)
        sortedData = insertionSort(data)
        refineList = ' '.join(map(str, sortedData))
        #print(refineList)
        fOut.write('%s\n' % refineList)

fIn.close()
fOut.close()
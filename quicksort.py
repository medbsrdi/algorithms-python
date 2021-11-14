#devide-and-concer algorithm, like the merge sort
#Also uses recursion to perform sorting
#Generally performs better than merge sort , O(n log(n))
#doesn't need extra memory
#worst case O(n^2)

items = [20,6,8,53,56,23,87,41,49,19]

def quicksort(dataset,first,last):
    if first < last:
        #calculate the splite point
        pivotIdx = partition(dataset,first,last)

        #now sort the two parition 
        quicksort(dataset,first,pivotIdx-1)
        quicksort(dataset,pivotIdx+1,last)

def partition(datavalues,first,last):
    #chose the first items as the pivot value
    pivotvalue = datavalues[first]
    #establish the upper and lower indexes
    lower = first + 1
    upper = last  

    #start searching for the crossing point 
    done = False
    while not done:
        #TODO : Advance the lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower+=1
        #TODO : advance the upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper-=1
        #TODO : if the two indexes cross, we have found the split point
        if upper<lower:
            done = True
        else:
            tmp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = tmp

    #when the split point is found , exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    #return the split index
    return upper


print(items)
quicksort(items,0,len(items)-1)
print(items)
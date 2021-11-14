#merge sort algorithm 
# devide-and-concer algorithm
#break a dataset into individual pieces and merges them
#uses recursion to operate on datasets
#perform well on big dataset --> O(n.log(n))

#Implement a merge sort with recursion

items = [6,23,21,34,69,9,5,6,0,103,34]

def mergesort(dataset):
    if len(dataset)>1:
        mid = len(dataset)//2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]
        #TODO: recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)
        #TODO: now perform the merging
        i = 0 #index info left array
        j = 0 #index info right array
        k = 0 #index into merged array
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i+=1
            else:
                dataset[k] = rightarr[j]
                j+=1
            k+=1 
        #TODO:while both array have content
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i+=1
            k+=1

        #TODO: if the left array still has values,add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j+=1
            k+=1

print(items)
mergesort(items)
print(items)
#searching for an item in an ordered list 
#this techniques uses a binary search


items = [6,8,19,20,23,41,49,53,56,87]

def binarysearch(items,itemlist):
    #get the list size
    listsize = len(itemlist) - 1
    #start at two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        #TODO:calculate the middle
        mid = (lowerIdx+upperIdx)//2
        #TODO:if item is found,return index
        if items == itemlist[mid]:
            return mid
        #TODO: if the item is not found,get the next mid
        if items>itemlist[mid]:
            lowerIdx = mid+1
        else:
            upperIdx = mid-1
    
    if lowerIdx>upperIdx:
        return -1
    
        


print(binarysearch(0,items))
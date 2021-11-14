#Bubble sort Algorithm

def bubbleSort(dataset):
    #start with the array length and drecreameant each time
    for i in range(len(dataset)-1,0,-1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                tmp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = tmp
        print("Current status ",dataset)
    

def main():
    list1 = [6,23,34,21,8,0,10]
    bubbleSort(list1)
    print("Result ",list1)

if __name__ == '__main__':
    main()
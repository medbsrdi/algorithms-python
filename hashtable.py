#use a hashtable to filter out duplicate items

#define a set of items that we want to reduce duplicates
items = ["apple","pear","orange","banana","apple",
        "orange","apple","pear","banana","orange",
        "apple","kiwi","pear","apple","orange"]

#create filter 
filter = dict()

#loop over each item 
for key in items:
    filter[key] = 0


#create a set from resulting keys in the hashtable
result = set(filter.keys())
print(result)


#counting the element 
count = dict()

for itm in items:
    if itm in count.keys():
        count[itm]+=1
    else:
        count[itm] = 1

print(count)
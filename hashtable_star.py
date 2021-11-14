#hash table usage

# create a hash table all at once
itmes1 = dict({"key1":1,"key2":2,"key3":"three"})
print(itmes1)

#create hash table progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
items2["key4"] = 4
print(items2)

#iterate the key and values in the dictionary
for key,value in items2.items():
    print("key :",key," value :",value)
eids=[101,102,103,106]
eids.pop() #remove last element from list

print(eids)

eids.remove(102) #remove specified eleement from list
print(eids) #[101,103]
eids.clear()
print(eids)

del eids  
print(eids)  #name error
""" eids={101,102,103,104}
#create
uids=eids.copy()
print(uids) """

""" #update
eids={101,102,103}
eids.add(104)
print(eids)
 """

""" eids={102,102,103}
new_eids={101,104,105}
eids.update(new_eids)
print(eids) """

""" #delete
eids={101,102,103}
eids.pop()   #remove aerbitary element from set
print(eids)
 """

""" #remove
eids={101,102,103}
eids.remove(104)  #remove specified element fromm set
#if element is not present,it return key error
print(eids) """

#discard
eids={101,102,103}
eids.discard(104)
#remove specified element from set
#if element is not present,it return any error
print(eids)

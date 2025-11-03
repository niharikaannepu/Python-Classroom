emp={
    'eid':101,
    'ename':"rahul",
    'esal':45000
}
#dict.get(key) #return value of specified key
print(emp.get('eid'))#101
print(emp.get('loc')) #none



for key in emp.keys():
    print(key,":",emp.get(key))

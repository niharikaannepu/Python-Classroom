#WAP to read data.txt file and print data file

fp=open('data.txt','r')
data=fp.read()
print(data)


fp.close()
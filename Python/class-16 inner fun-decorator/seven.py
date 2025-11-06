def add(a,b):
    def inner():
        print("inner")
    return a+b,"Niharika",inner
result=add(10,20)
print(result)

result[2]()
result[2]()
result[2]()

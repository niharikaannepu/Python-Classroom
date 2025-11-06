#how to invoke inner function from outside?
def outer():
    print('Outer Function')
    
    def inner():
        print('Inner Function')
    return inner
    
inn=outer()
print(inn)
print(type(inn))
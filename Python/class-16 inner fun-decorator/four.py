def calc():
    print('Outer Function')
    def add():
        print('Addition')
        
    def multi():
        print("Multiplication")
    return add  
inner=calc()

inner()
inner()
        
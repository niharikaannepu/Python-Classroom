try:
    a=int(input("Enter FN"))
    b=int(input("Enter SN"))
    print(a/b)
except ValueError as err:
    print("Enter Integer only")
except ZeroDivisionError as err:
    print("Can't Divide by Zero ")
    
print("GE")
print('''
+ Add
- Subtract
* Mulltiply  
/ Division              

'''

)
a=int(input("Enter the a: "))
b=int(input("Enter the b: "))
opr=input("Enter the operation: ")
if opr=="+":
    print(a+b)
elif opr=="-":
    print(a-b)
elif opr=="/":
    print(a/b)
elif opr=="*":
    print(a*b)
else:
    print("Invalid Operation")
 
def add(x,y):
    return x + y
def mult(x,y):
    return x * y
def sub(x,y):
    return x - y
def div(x,y):
  if  y == 0: 
    return "error! divide by zero"
  return x/y
while True:
    print("\nsimple calculator")
    print("1.addition(+)")
    print("2.multiplication(*)")
    print("3.subtraction(-)")
    print("4.division(/)")
    print("5.exit")
    choice = input("enter choice(1/2/3/4/5): ")
    if  choice == '5':
       print("exit")
       break
    if choice in ('1','2','3','4'):
     num1 = float(input("enter first number"))
     num2 = float(input("enter second number"))
    if choice == '1':
       print("Result:",add(num1,num2))
    if choice == '2':
        print("Result:",mult(num1,num2))
    elif choice == '3':
         print("Result:",sub(num1,num2))
    elif choice == '4':
         print("Result:",div(num1,num2))
    else:
        print("invalid choice")



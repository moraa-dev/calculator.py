a = float (input("enter the first number"))
b = float (input("enter the second number"))
op = input ("enter your operation (+,-,*,/)")

if op == '+':
    answer = a+b

    print (f"{a}+{b} = {answer}")

elif op == '-':
  answer = a-b
  print (f"{a}-{b} = {answer}")

elif op == '*':
  answer = a*b
  print (f"{a}*{b} = {answer}")

elif op == '/':
  if b!= 0:
   answer = a/b
   print (f"{a}/{b} = {answer}")

  else:
   print ("Error")

else:
 print ("Operator Not Allowed")

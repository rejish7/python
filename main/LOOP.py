# WAP enter numberr of values and cALCULATE SUM OF ALL VALUES

values=[]
num=int(input("Enter the value"))

for i in range(num):
 number = int(input("Enter number"))
values.append(number)

total= 0
for i in values:
  total+=i

print("total:",total)
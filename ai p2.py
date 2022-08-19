num=int(input("enter a number:"))
 flag = false
if num>1:
    for i in range (2,num):
        if(num%i)==0:
            flag=true
            break
if flag:
    print(num,"is not aprime number")
else:
    print(num,"is a prime number")

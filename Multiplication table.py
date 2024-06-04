#printing multiplication tables
n=int(input("Enter the number of table: "))
e=int(input("Enter till which you want the tables: "))
print("***Multiplication table of",n,"from 1 to",e,"***")
for i in range(1,e+1):
    print(n,"x",i,"=",i*n)
    

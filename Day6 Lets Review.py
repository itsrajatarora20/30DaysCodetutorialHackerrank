# Enter your code here. Read input from STDIN. Print output to STDOUT
noofwords=int(input())
x=[]
for p in range(noofwords):
    x.append(input())
for i in range(len(x)):
    p=x[i]
    print(p[0:len(p):2],end=" ")
    print(p[1:len(p):2])

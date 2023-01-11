x=0
y=1

limit= int(input("How many fibonac you want: "))

while limit>0:
    print(x)
    nextTerm=x+y
    x=y
    y=nextTerm
    limit-=1



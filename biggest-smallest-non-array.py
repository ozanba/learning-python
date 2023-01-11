#program prints biggest and smallest number not using array


i=1
biggest=-1
smallest= 9999999
while True:
    num=int(input("Enter %d. integer: " %i ))
    if num==0:
        break
    if num>biggest :
        biggest=num
    if num<smallest:
        smallest=num
    i +=1
   

print("Biggest number is ",biggest)
print("Smalles number is ",smallest)
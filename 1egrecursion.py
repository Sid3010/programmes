def square(n):
    if n==0:
        return 1
    return n*square(n**2)   
num=square(5)     
print(num)






def fact(n):
    if n==0:
                return 1
    return n*fact(n-1)   

num=fact(10)     
print(num)




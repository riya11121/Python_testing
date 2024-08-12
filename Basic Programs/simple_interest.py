def simpleint(p,r,t):
    si=(p*r*t)/100
    print(f"simple interest is {si}")
    return si

p=int(input("Enter principle amount: "))
r=int(input("Enter rate of interest: "))
t=int(input("Enter time of period: "))

simpleint(p,r,t)
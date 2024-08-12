#A=P(1+R/100)^t

def compound_interest(p,r,t):
    a=p*(1+(r/100))**t
    print(f"compound interest is {a}")
    return a

p=int(input("Enter principle amount: "))
r=float(input("Enter rate of interest: "))
t=int(input("Enter time of period: "))

compound_interest(p,r,t)




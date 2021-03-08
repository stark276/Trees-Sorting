def raise_power(base,power):
    if(power==1):
       return(base)
    else:
       return(base*raise_power(base,power-1))
base=10
power=3
print(raise_power(base,power))

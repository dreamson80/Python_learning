def cel_to_fahr(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c * 9/5 + 32
        return f
        
c =  float(input("Enter your Celsius: "))
print(cel_to_fahr(c))

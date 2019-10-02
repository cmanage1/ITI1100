def convert (x):
    ans= x * (9/5) + 32
    return(ans)

temp_c=int(input("Enter a temperature in Celcius"))
temp_f=convert(temp_c)
print("The temperature in Fahrenheit is", temp_f)

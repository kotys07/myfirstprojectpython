print("Сума натуральних чисел")
n = 500

text = "1+2+...+"+str(n)+" ="
i = 1
s = 0
while True:
    s+=i
    i+=1
    if i>n:
        break
print(text,s)

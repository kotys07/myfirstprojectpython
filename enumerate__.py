date = [2,3,8,9,6,4,7,8,5,41,2,3]

for num, val in enumerate(date, 1):
    print(str(num) + '-e значення рівне ' + str(val))

#без функції enumerate

date1 = [5,6,8,9,4,5,22,66,44,56,88,952,1,2,3]
ind = 1
for datee in date1:
    print(str(ind) + '-e значення рівне ' + str(datee))
    ind += 1

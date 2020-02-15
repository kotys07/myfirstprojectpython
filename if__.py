res = eval(input("Введіть що-небуть: "))
resType = type(res)
if resType == int:
    print("Ви ввели ціле число!")
elif resType == float:
    print("Ви ввели дійсне число")
else:
    print("Ви ввели напевно текст!")
print("Роботу закінчено!!!")

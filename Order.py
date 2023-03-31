print("-------------")
print("-----Our Menu------")
print("1.) ADOBO @ 20")
print("2.) RICE @ 10")
print("3.) LINAGA @ 40")
print("4.) PORKCHOP @ 30")

x = int(input("Enter the number of your order:"))
if(x == 1):
    c = int(input("Enter the amount of your money"))
    change = c - 20
    print("Your Change:", change)
elif(x == 2):
    c = int(input("Enter the amount of your money"))
    change = c - 10
    print("Your Change:", change)
elif(x == 3):
    c = int(input("Enter the amount of your money"))
    change = c - 40
    print("Your Change:", change)
elif(x == 4):
    c = int(input("Enter the amount of your money"))
    change = c - 30
    print("Your Change:", change)
else:
    print("Input is not in the choices")

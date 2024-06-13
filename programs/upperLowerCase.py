def checkUpperLower(alpha):
    # for checking upperCase
    if "A"<=alpha[0]<="Z":
        print("is captital")
    # for checking lowerCase
    else:
        print(alpha,"is small")


while (1>0):
    alpha = input("enter a character:")
    checkUpperLower(alpha)
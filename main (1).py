#
year= int(input("Enter the year to be checked:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("The year",year,"is a leap year")
        else:
            print("The year",year,"is not a leap year")
    else:
        print("The year",year,"is a leap year")
else:
    print("The year",year,"is not a leap year")
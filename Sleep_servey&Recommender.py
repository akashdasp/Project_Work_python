CarryOn="y"
agelist=[]
namelist=[]
hourslist=[]
zipped=[]
total_hours=0
number_student=0
while CarryOn=='y':
    name=input("Enter your Name")
    namelist.append(name)
    age=int(input("Enter your Age"))
    agelist.append(age)
    hours=int(input("Enter the Number Hours You Sleep"))
    hourslist.append(hours)
    #this block of Code is to give the Recomendation
    if 6<=age<=13:
        if 9<=hours<=11:
            print("Recomended")
        elif hours<9:
            print("Under Sleep")
        elif hours>11:
            print("over Sleep")
    elif 14<=age<=17:
        if 8<=hours<=10:
            print("Recomended")
        elif hours<8:
            print("Under Sleep")
        elif hours>10:
            print("over Sleep")
    elif 18<=age<=25 or age >25 :
        if 7<=hours<=9:
            print("Recomended")
        elif hours<7:
            print("Under Sleep")
        elif hours>9:
            print("over Sleep")
    else:
        print("You have enter A wrong Number! Try again ")
    total_hours=total_hours+hours
    number_student=number_student+1
    avg=total_hours/number_student
    if number_student==10:
        print(avg)
    CarryOn=input("Press Y to Continue or press N").lower()
zipped=zip(namelist,agelist,hourslist)
print(list(zipped))

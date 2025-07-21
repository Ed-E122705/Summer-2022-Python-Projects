# AD1 Systems - Unit Converter

# This was the first project I created in Python which explains why it's significantly long for such a simple project

print("Which Conversion feature would you like to use? \n")
print("1. Speed")
print("2. Distance")
print("3. Currency")
print("4. Weight")
print("5. Length")
print("6. Temperature")

pick = input()

if (pick=="1") or (pick=="1 "):
    print("Which Speed Conversion would you like to use? \n")
    print("1. m/s to km/hr")
    print("2. km/h to m/s")
    print("3. km/hr to mi/hr")
    print("4. mi/hr to km/hr")
    print("5. m/s to mi/hr")
    print("6. mi/hr to m/s")
    num=input()
    if (num=="1") or (num=="1 "):
        ms=float(input("Input Speed"))
        print(ms*3.6)
    elif (num=="2") or (num=="2 "):
        kmh=float(input("Input Speed"))
        print(kmh*1/3.6)
    elif (num=="3") or (num=="3 "):
        kmhr=float(input("Input Speed"))
        print(kmhr*0.6213711922)
    elif (num=="4") or (num=="4 "):
        mihr=float(input("Input Speed"))
        print(mihr*1.609344)
    elif (num=="5") or (num=="5 "):
        msec=float(input("Input Speed"))
        print(msec*2.23694)
    elif (num=="6") or (num=="6 "):
        mih=float(input("Input Speed"))
        print(mih*0.44704)

elif (pick=="2") or (pick=="2 "):
    print("Which Distance Conversion would you like to use? \n")
    print("1. m to ft")
    print("2. ft to m")
    print("3. m to mi")
    print("4. mi to m")
    print("5. km to mi")
    print("6. mi to km")
    print("7. km to ft")
    print("8. ft to km")
    print("9. m to in")
    print("10. in to m")
    print("11. mi to ft")
    print("12. ft to mi")
    nu = input()
    if (nu=="1") or (nu=="1 "):
        m=float(input("Input Distance"))
        print(m*3.28084)
    elif (nu=="2") or (nu=="2 "):
        ft=float(input("Input Distance"))
        print(ft*0.3048)
    elif (nu=="3") or (nu=="3 "):
        me=float(input("Input Distance"))
        print(me*1/1609.34)
    elif (nu=="4") or (nu=="4 "):
        mi=float(input("Input Distance"))
        print(mi*1609.34)
    elif (nu=="5") or (nu=="5 "):
        km=float(input("Input Distance"))
        print(km*1/1.60934)
    elif (nu=="6") or (nu=="6 "):
        mil=float(input("Input Distance"))
        print(mil*1.60934)
    elif (nu=="7") or (nu=="7 "):
        kilom=float(input("Input Distance"))
        print(kilom*3280.84)
    elif (nu=="8") or (nu=="8 "):
        fet=float(input("Input Distance"))
        print(fet*1/3280.84)
    elif (nu=="9") or (nu=="9 "):
        met=float(input("Input Distance"))
        print(met*39.3701)
    elif (nu=="10") or (nu=="10 "):
        inc=float(input("Input Distance"))
        print(inc*1/39.3701)
    elif (nu=="11") or (nu=="11 "):
        miles=float(input("Input Distance"))
        print(miles*5280)
    elif (nu=="12") or (nu=="12 "):
        feet=float(input("Input Distance"))
        print(feet*1/5280)

elif (pick=="3") or (pick=="3 "):
    print("Which Currency Conversion would you like to use? \n")
    print("1. USD to INR")
    print("2. INR to USD")
    print("3. GBP to USD")
    print("4. USD to GBP")
    print("5. GBP to INR")
    print("6. INR to GBP")
    numb = input()
    if (numb=="1") or (numb=="1 "):
        usd=float(input("Input Currency"))
        print(usd*77.49)
    elif (numb=="2") or (numb=="2 "):
        inr=float(input("Input Currency"))
        print(inr*1/77.49)
    elif (numb=="3") or (numb=="3 "):
        gbp=float(input("Input Currecy"))
        print(gbp*1.22)
    elif (numb=="4") or (numb=="4 "):
        usdol=float(input("Input Currency"))
        print(usdol*1/1.22)
    elif (numb=="5") or (numb=="5 "):
        PS=float(input("Input Currency"))
        print(PS*94.86)
    elif (numb=="6") or (numb=="6 "):
        Rup=float(input("Input Currency"))
        print(Rup*1/94.86)

elif (pick=="4") or (pick=="4 "):
    print("Which Weight Conversion would you like to use? \n")
    print("1. kg to lbs")
    print("2. lbs to kg")
    print("3. lbs to oz")
    print("4. oz to lbs")
    print("5. g to oz")
    print("6. oz to g")
    numbe = input()
    if (numbe=="1") or (numbe=="1 "):
        kg=float(input("Input Weight"))
        print(kg*2.20462)
    elif (numbe=="2") or (numbe=="2 "):
        lbs=float(input("Input Weight"))
        print(lbs*1/2.20462)
    elif (numbe=="3") or (numbe=="3 "):
        lb=float(input("Input Weight"))
        print(lb*16)
    elif (numbe=="4") or (numbe=="4 "):
        oz=float(input("Input Weight"))
        print(oz*1/16)
    elif (numbe=="5") or (numbe=="5 "):
        g=float(input("Input Weight"))
        print(g*0.035274)
    elif (numbe=="6") or (numbe=="6 "):
        ozs=float(input("Input Weight"))
        print(ozs*1/0.035274)

elif (pick=="5") or (pick=="5 "):
    print("Which Length Conversion would you like to use? \n")
    print("1. ft to in")
    print("2. in to ft")
    print("3. cm to in")
    print("4. in to cm")
    print("5. ft to yds")
    print("6. yds to ft")
    n = input()
    if (n=="1") or (n=="1 "):
        fts=float(input("Input Length"))
        print(fts*12)
    elif (n=="2") or (n=="2 "):
        ins=float(input("Input Length"))
        print(ins*1/12)
    elif (n=="3") or (n=="3 "):
        cms=float(input("Input Length"))
        print(cms*0.393701)
    elif (n=="4") or (n=="4 "):
        inches=float(input("Input Length"))
        print(inches*1/0.393701)
    elif (n=="5") or (n=="5 "):
        feets=float(input("Input Length"))
        print(feets*1/3)
    elif (n=="6") or (n=="6 "):
        yds=float(input("Input Length"))
        print(yds*3)
elif (pick=="6") or (pick=="6 "):
    print("Which Temperature Conversion would you like to use? \n")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    numberozo = input()
    if (numberozo=="1") or (numberozo=="1 "):
        cel=float(input("Input Temperature"))
        print((cel*9/5)+32)
    elif (numberozo=="2") or (numberozo=="2 "):
        fht=float(input("Input Temperature"))
        print((fht-32)*5/9)

else:
    print("Error.")
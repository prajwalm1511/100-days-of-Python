# code for roller coaster
height = int(input("what's ur height "))


if height<120:
    print("cant ride")
elif height>120:
    print("can ride")

    age=int(input("whats you age "))
    if age <12:
        bill = 5

    elif age >=12 and age <=18:
        bill=7

    elif age >18:
        bill=12
        
    print(f"your current bill is:{bill}")
    ph = str(input("do you want photos? "))
    
    if ph== 'yes':
        bill += 3
        print(f"total bill :{bill}")
    if ph=='no':
        print(f"total bill :{bill}")


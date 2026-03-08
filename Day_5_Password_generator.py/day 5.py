# LOOP
fruits=["Aaple","peach","pear"]
for fruit in fruits:
# here we are declaring a variable fruit that we want to use in a specific task
# we start with for , link the variable and the function with 'in' operator
    print(fruit)
# here fruit takes aaple as value in intially
# after the loop runs , its value changes to peach
# again the loop runs,its value changes to pear
st_sc=[180,150,30,40,56,66]
i=0
for sc in st_sc:
    i+=sc
print(i)

print(max(st_sc))
max=0
for sc in st_sc:
    if sc>max:
        max=sc
print(max)

# RANGE FUNCTION
# syntax :
# For i in range(a,b):
#   print(i)
# range always comes with a function
print(range(1,10)) # it prints - range(1,10)
for t in range(1,10):
    print(t)
    # it prints number from 1 to 9.....not the last digit
     
total=0
for i in range (1,101):
    total += i

print(total)


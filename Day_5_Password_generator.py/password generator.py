import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','(',')','*']

print("welcome to the password generator")
nr_letter=int(input("How many letters would you like to have in your password:"))
nr_number=int(input("How many numbers would you like to have in your password:"))
nr_symbolr=int(input("How many symbols would you like to have in your password:"))

password=""
for i in range(1, nr_letter + 1):
    password += random.choice(letters)
for i in range(1,nr_number + 1):
    password += random.choice(number)
for i in range(1,nr_number + 1):
    password += random.choice(symbols) 

print(password)

a=list(password)#here first we convert it into an array
random.shuffle(a)#then shuffle it
new_pass="".join(a)# that that array/list into a string by join(a)
print(new_pass)
print("")

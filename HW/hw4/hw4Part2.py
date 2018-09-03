#ask for input of a password
password = input("Enter a password => ")
print(password)
#use list to collect results for five rules
list=[]

#Rule 1
#the length of the password should between 10 and 25
is_long_enough = len(str(password))>=10 and len(str(password))<=25
#first letter of the password can't be number or other characters 
lower_or_upper = password[0].islower() or password[0].isupper()
if is_long_enough and lower_or_upper:
    print("Rule 1 is satisfied")
    list.append('1')
else:
    print("Rule 1 is not satisfied")

#Rule 2
#password should contain at least one either '@' or '$' but can't contain any '%'
character = (password.count('@')>0 or\
    password.count('$')>0)\
    and password.count('%')==0
if character:
    print("Rule 2 is satisfied")
    list.append('2')
elif not character:
    print("Rule 2 is not satisfied")

#Rule 3
#the password should contain at least one number of either 1,2,3 or 4
upper_lower = password.islower() or password.isupper()
count_number = password.count('1')>0 or\
    password.count('2')>0 or\
    password.count('3')>0 or\
    password.count('4')>0
if not upper_lower or count_number:
    print("Rule 3 is satisfied")
    list.append('3')
elif not (not upper_lower or count_number):
    print("Rule 3 is not satisfied")
    
#Rule 4
#after a capital letter, there must be a '_' followed
upper_case = password.isupper()
for n in range(len(password)-1): 
    #the last letter can't be capital, else it doesn't fllow the rule
    if password[len(password)-1].isupper():
        print("Rule 4 is not satisfied")
        break
    if password[n].isupper() and password[n+1] != '_':
        print("Rule 4 is not satisfied")
        break
    else:
        print("Rule 4 is satisfied")
        list.append('4')
        break
        
#Rule 5
#for number in the password, it can only smller than 4
upper_lower = password.islower() or password.isupper() 
if password.count('1')+password.count('2')+password.count('3')+password.count('4')>=0 and\
   password.count('5')+password.count('6')+password.count('7')+password.count('8')+password.count('9')==0:
    print("Rule 5 is satisfied")  
    list.append('5')
else:
    print("Rule 5 is not satisfied")  
    
#suggestion
if len(list)==5:
    print("The password is valid")
elif list[0] == '1':
    print("A suggested password is "+str(password[:8])+'42'+str(password[len(password)-8:]))
    
        

    
